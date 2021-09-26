# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20180320 import models as yundun_dbaudit_20180320_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_log_mask_config_with_options(
        self,
        request: yundun_dbaudit_20180320_models.AddLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AddLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AddLogMaskConfigResponse(),
            self.do_rpcrequest('AddLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_log_mask_config_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.AddLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AddLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AddLogMaskConfigResponse(),
            await self.do_rpcrequest_async('AddLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_log_mask_config(
        self,
        request: yundun_dbaudit_20180320_models.AddLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.AddLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_log_mask_config_with_options(request, runtime)

    async def add_log_mask_config_async(
        self,
        request: yundun_dbaudit_20180320_models.AddLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.AddLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_log_mask_config_with_options_async(request, runtime)

    def associate_db_to_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.AssociateDbToRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AssociateDbToRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateDbToRuleResponse(),
            self.do_rpcrequest('AssociateDbToRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_db_to_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.AssociateDbToRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AssociateDbToRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateDbToRuleResponse(),
            await self.do_rpcrequest_async('AssociateDbToRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_db_to_rule(
        self,
        request: yundun_dbaudit_20180320_models.AssociateDbToRuleRequest,
    ) -> yundun_dbaudit_20180320_models.AssociateDbToRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_db_to_rule_with_options(request, runtime)

    async def associate_db_to_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.AssociateDbToRuleRequest,
    ) -> yundun_dbaudit_20180320_models.AssociateDbToRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_db_to_rule_with_options_async(request, runtime)

    def associate_rule_to_db_with_options(
        self,
        request: yundun_dbaudit_20180320_models.AssociateRuleToDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AssociateRuleToDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateRuleToDbResponse(),
            self.do_rpcrequest('AssociateRuleToDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_rule_to_db_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.AssociateRuleToDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.AssociateRuleToDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateRuleToDbResponse(),
            await self.do_rpcrequest_async('AssociateRuleToDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_rule_to_db(
        self,
        request: yundun_dbaudit_20180320_models.AssociateRuleToDbRequest,
    ) -> yundun_dbaudit_20180320_models.AssociateRuleToDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_rule_to_db_with_options(request, runtime)

    async def associate_rule_to_db_async(
        self,
        request: yundun_dbaudit_20180320_models.AssociateRuleToDbRequest,
    ) -> yundun_dbaudit_20180320_models.AssociateRuleToDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_rule_to_db_with_options_async(request, runtime)

    def change_agent_status_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ChangeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeAgentStatusResponse(),
            self.do_rpcrequest('ChangeAgentStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_agent_status_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeAgentStatusResponse(),
            await self.do_rpcrequest_async('ChangeAgentStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_agent_status(
        self,
        request: yundun_dbaudit_20180320_models.ChangeAgentStatusRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_agent_status_with_options(request, runtime)

    async def change_agent_status_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeAgentStatusRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_agent_status_with_options_async(request, runtime)

    def change_log_mask_config_state_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse(),
            self.do_rpcrequest('ChangeLogMaskConfigState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_log_mask_config_state_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse(),
            await self.do_rpcrequest_async('ChangeLogMaskConfigState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_log_mask_config_state(
        self,
        request: yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_log_mask_config_state_with_options(request, runtime)

    async def change_log_mask_config_state_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_log_mask_config_state_with_options_async(request, runtime)

    def change_rule_priority_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRulePriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeRulePriorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRulePriorityResponse(),
            self.do_rpcrequest('ChangeRulePriority', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_rule_priority_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRulePriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeRulePriorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRulePriorityResponse(),
            await self.do_rpcrequest_async('ChangeRulePriority', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_rule_priority(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRulePriorityRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeRulePriorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_rule_priority_with_options(request, runtime)

    async def change_rule_priority_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRulePriorityRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeRulePriorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_rule_priority_with_options_async(request, runtime)

    def change_rule_status_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRuleStatusResponse(),
            self.do_rpcrequest('ChangeRuleStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_rule_status_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ChangeRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRuleStatusResponse(),
            await self.do_rpcrequest_async('ChangeRuleStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_rule_status(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRuleStatusRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_rule_status_with_options(request, runtime)

    async def change_rule_status_async(
        self,
        request: yundun_dbaudit_20180320_models.ChangeRuleStatusRequest,
    ) -> yundun_dbaudit_20180320_models.ChangeRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_rule_status_with_options_async(request, runtime)

    def check_mail_registered_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CheckMailRegisteredRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CheckMailRegisteredResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CheckMailRegisteredResponse(),
            self.do_rpcrequest('CheckMailRegistered', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_mail_registered_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CheckMailRegisteredRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CheckMailRegisteredResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CheckMailRegisteredResponse(),
            await self.do_rpcrequest_async('CheckMailRegistered', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_mail_registered(
        self,
        request: yundun_dbaudit_20180320_models.CheckMailRegisteredRequest,
    ) -> yundun_dbaudit_20180320_models.CheckMailRegisteredResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_mail_registered_with_options(request, runtime)

    async def check_mail_registered_async(
        self,
        request: yundun_dbaudit_20180320_models.CheckMailRegisteredRequest,
    ) -> yundun_dbaudit_20180320_models.CheckMailRegisteredResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_mail_registered_with_options_async(request, runtime)

    def clear_agent_records_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ClearAgentRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ClearAgentRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ClearAgentRecordsResponse(),
            self.do_rpcrequest('ClearAgentRecords', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_agent_records_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ClearAgentRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ClearAgentRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ClearAgentRecordsResponse(),
            await self.do_rpcrequest_async('ClearAgentRecords', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_agent_records(
        self,
        request: yundun_dbaudit_20180320_models.ClearAgentRecordsRequest,
    ) -> yundun_dbaudit_20180320_models.ClearAgentRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_agent_records_with_options(request, runtime)

    async def clear_agent_records_async(
        self,
        request: yundun_dbaudit_20180320_models.ClearAgentRecordsRequest,
    ) -> yundun_dbaudit_20180320_models.ClearAgentRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_agent_records_with_options_async(request, runtime)

    def config_instance_network_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ConfigInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse(),
            self.do_rpcrequest('ConfigInstanceNetwork', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_network_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ConfigInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse(),
            await self.do_rpcrequest_async('ConfigInstanceNetwork', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_network(
        self,
        request: yundun_dbaudit_20180320_models.ConfigInstanceNetworkRequest,
    ) -> yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_network_with_options(request, runtime)

    async def config_instance_network_async(
        self,
        request: yundun_dbaudit_20180320_models.ConfigInstanceNetworkRequest,
    ) -> yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_network_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateDataSourceResponse(),
            self.do_rpcrequest('CreateDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateDataSourceResponse(),
            await self.do_rpcrequest_async('CreateDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_source(
        self,
        request: yundun_dbaudit_20180320_models.CreateDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_grade_protection_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateGradeProtectionReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse(),
            self.do_rpcrequest('CreateGradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_grade_protection_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateGradeProtectionReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse(),
            await self.do_rpcrequest_async('CreateGradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_grade_protection_report(
        self,
        request: yundun_dbaudit_20180320_models.CreateGradeProtectionReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_grade_protection_report_with_options(request, runtime)

    async def create_grade_protection_report_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateGradeProtectionReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_grade_protection_report_with_options_async(request, runtime)

    def create_integrated_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateIntegratedReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateIntegratedReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateIntegratedReportResponse(),
            self.do_rpcrequest('CreateIntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_integrated_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateIntegratedReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateIntegratedReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateIntegratedReportResponse(),
            await self.do_rpcrequest_async('CreateIntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_integrated_report(
        self,
        request: yundun_dbaudit_20180320_models.CreateIntegratedReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateIntegratedReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_integrated_report_with_options(request, runtime)

    async def create_integrated_report_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateIntegratedReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateIntegratedReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_integrated_report_with_options_async(request, runtime)

    def create_log_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateLogAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse(),
            self.do_rpcrequest('CreateLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_log_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateLogAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse(),
            await self.do_rpcrequest_async('CreateLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_log_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.CreateLogAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_log_alarm_task_with_options(request, runtime)

    async def create_log_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateLogAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_log_alarm_task_with_options_async(request, runtime)

    def create_pcireport_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreatePCIReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreatePCIReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreatePCIReportResponse(),
            self.do_rpcrequest('CreatePCIReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pcireport_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreatePCIReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreatePCIReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreatePCIReportResponse(),
            await self.do_rpcrequest_async('CreatePCIReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pcireport(
        self,
        request: yundun_dbaudit_20180320_models.CreatePCIReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreatePCIReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pcireport_with_options(request, runtime)

    async def create_pcireport_async(
        self,
        request: yundun_dbaudit_20180320_models.CreatePCIReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreatePCIReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pcireport_with_options_async(request, runtime)

    def create_report_push_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateReportPushTaskResponse(),
            self.do_rpcrequest('CreateReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_report_push_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateReportPushTaskResponse(),
            await self.do_rpcrequest_async('CreateReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_report_push_task(
        self,
        request: yundun_dbaudit_20180320_models.CreateReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_report_push_task_with_options(request, runtime)

    async def create_report_push_task_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_report_push_task_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleResponse(),
            await self.do_rpcrequest_async('CreateRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleRequest,
    ) -> yundun_dbaudit_20180320_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleRequest,
    ) -> yundun_dbaudit_20180320_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rule_group_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleGroupResponse(),
            self.do_rpcrequest('CreateRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_group_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleGroupResponse(),
            await self.do_rpcrequest_async('CreateRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule_group(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.CreateRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_group_with_options(request, runtime)

    async def create_rule_group_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.CreateRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_group_with_options_async(request, runtime)

    def create_soxreport_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateSOXReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSOXReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSOXReportResponse(),
            self.do_rpcrequest('CreateSOXReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_soxreport_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSOXReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSOXReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSOXReportResponse(),
            await self.do_rpcrequest_async('CreateSOXReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_soxreport(
        self,
        request: yundun_dbaudit_20180320_models.CreateSOXReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSOXReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_soxreport_with_options(request, runtime)

    async def create_soxreport_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSOXReportRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSOXReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_soxreport_with_options_async(request, runtime)

    def create_sql_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateSqlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSqlRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSqlRuleResponse(),
            self.do_rpcrequest('CreateSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sql_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSqlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSqlRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSqlRuleResponse(),
            await self.do_rpcrequest_async('CreateSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sql_rule(
        self,
        request: yundun_dbaudit_20180320_models.CreateSqlRuleRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSqlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sql_rule_with_options(request, runtime)

    async def create_sql_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSqlRuleRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSqlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sql_rule_with_options_async(request, runtime)

    def create_system_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.CreateSystemAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse(),
            self.do_rpcrequest('CreateSystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_system_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSystemAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse(),
            await self.do_rpcrequest_async('CreateSystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_system_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.CreateSystemAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_system_alarm_task_with_options(request, runtime)

    async def create_system_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.CreateSystemAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_system_alarm_task_with_options_async(request, runtime)

    def delete_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeleteAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse(),
            self.do_rpcrequest('DeleteAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse(),
            await self.do_rpcrequest_async('DeleteAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.DeleteAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_task_with_options(request, runtime)

    async def delete_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_task_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteDataSourceResponse(),
            self.do_rpcrequest('DeleteDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteDataSourceResponse(),
            await self.do_rpcrequest_async('DeleteDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_source(
        self,
        request: yundun_dbaudit_20180320_models.DeleteDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_report_push_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeleteReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse(),
            self.do_rpcrequest('DeleteReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_report_push_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse(),
            await self.do_rpcrequest_async('DeleteReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_report_push_task(
        self,
        request: yundun_dbaudit_20180320_models.DeleteReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_report_push_task_with_options(request, runtime)

    async def delete_report_push_task_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_report_push_task_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleResponse(),
            await self.do_rpcrequest_async('DeleteRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rule_group_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleGroupResponse(),
            self.do_rpcrequest('DeleteRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_group_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleGroupResponse(),
            await self.do_rpcrequest_async('DeleteRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule_group(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_group_with_options(request, runtime)

    async def delete_rule_group_async(
        self,
        request: yundun_dbaudit_20180320_models.DeleteRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.DeleteRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_group_with_options_async(request, runtime)

    def deregister_templates_from_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse(),
            self.do_rpcrequest('DeregisterTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deregister_templates_from_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse(),
            await self.do_rpcrequest_async('DeregisterTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_templates_from_rule(
        self,
        request: yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_templates_from_rule_with_options(request, runtime)

    async def deregister_templates_from_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_templates_from_rule_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_login_ticket_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DescribeLoginTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeLoginTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeLoginTicketResponse(),
            self.do_rpcrequest('DescribeLoginTicket', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_login_ticket_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeLoginTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeLoginTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeLoginTicketResponse(),
            await self.do_rpcrequest_async('DescribeLoginTicket', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_login_ticket(
        self,
        request: yundun_dbaudit_20180320_models.DescribeLoginTicketRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeLoginTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_login_ticket_with_options(request, runtime)

    async def describe_login_ticket_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeLoginTicketRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeLoginTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_login_ticket_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: yundun_dbaudit_20180320_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_sync_info_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DescribeSyncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeSyncInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeSyncInfoResponse(),
            self.do_rpcrequest('DescribeSyncInfo', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sync_info_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeSyncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DescribeSyncInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeSyncInfoResponse(),
            await self.do_rpcrequest_async('DescribeSyncInfo', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sync_info(
        self,
        request: yundun_dbaudit_20180320_models.DescribeSyncInfoRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeSyncInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_info_with_options(request, runtime)

    async def describe_sync_info_async(
        self,
        request: yundun_dbaudit_20180320_models.DescribeSyncInfoRequest,
    ) -> yundun_dbaudit_20180320_models.DescribeSyncInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sync_info_with_options_async(request, runtime)

    def disable_log_mask_configs_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DisableLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse(),
            self.do_rpcrequest('DisableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_log_mask_configs_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DisableLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse(),
            await self.do_rpcrequest_async('DisableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_log_mask_configs(
        self,
        request: yundun_dbaudit_20180320_models.DisableLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_log_mask_configs_with_options(request, runtime)

    async def disable_log_mask_configs_async(
        self,
        request: yundun_dbaudit_20180320_models.DisableLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_log_mask_configs_with_options_async(request, runtime)

    def dissociate_rules_from_db_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DissociateRulesFromDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse(),
            self.do_rpcrequest('DissociateRulesFromDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_rules_from_db_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DissociateRulesFromDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse(),
            await self.do_rpcrequest_async('DissociateRulesFromDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_rules_from_db(
        self,
        request: yundun_dbaudit_20180320_models.DissociateRulesFromDbRequest,
    ) -> yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_rules_from_db_with_options(request, runtime)

    async def dissociate_rules_from_db_async(
        self,
        request: yundun_dbaudit_20180320_models.DissociateRulesFromDbRequest,
    ) -> yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_rules_from_db_with_options_async(request, runtime)

    def dissociate_templates_from_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse(),
            self.do_rpcrequest('DissociateTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_templates_from_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse(),
            await self.do_rpcrequest_async('DissociateTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_templates_from_rule(
        self,
        request: yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_templates_from_rule_with_options(request, runtime)

    async def dissociate_templates_from_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleRequest,
    ) -> yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_templates_from_rule_with_options_async(request, runtime)

    def edit_log_mask_config_with_options(
        self,
        request: yundun_dbaudit_20180320_models.EditLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.EditLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EditLogMaskConfigResponse(),
            self.do_rpcrequest('EditLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_log_mask_config_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.EditLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.EditLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EditLogMaskConfigResponse(),
            await self.do_rpcrequest_async('EditLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_log_mask_config(
        self,
        request: yundun_dbaudit_20180320_models.EditLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.EditLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_log_mask_config_with_options(request, runtime)

    async def edit_log_mask_config_async(
        self,
        request: yundun_dbaudit_20180320_models.EditLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.EditLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_log_mask_config_with_options_async(request, runtime)

    def enable_log_mask_configs_with_options(
        self,
        request: yundun_dbaudit_20180320_models.EnableLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse(),
            self.do_rpcrequest('EnableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_log_mask_configs_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.EnableLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse(),
            await self.do_rpcrequest_async('EnableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_log_mask_configs(
        self,
        request: yundun_dbaudit_20180320_models.EnableLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_log_mask_configs_with_options(request, runtime)

    async def enable_log_mask_configs_async(
        self,
        request: yundun_dbaudit_20180320_models.EnableLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_log_mask_configs_with_options_async(request, runtime)

    def get_agent_file_url_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAgentFileUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentFileUrlResponse(),
            self.do_rpcrequest('GetAgentFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_agent_file_url_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAgentFileUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentFileUrlResponse(),
            await self.do_rpcrequest_async('GetAgentFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_file_url(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentFileUrlRequest,
    ) -> yundun_dbaudit_20180320_models.GetAgentFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_file_url_with_options(request, runtime)

    async def get_agent_file_url_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentFileUrlRequest,
    ) -> yundun_dbaudit_20180320_models.GetAgentFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_file_url_with_options_async(request, runtime)

    def get_agent_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAgentListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentListResponse(),
            self.do_rpcrequest('GetAgentList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_agent_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAgentListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentListResponse(),
            await self.do_rpcrequest_async('GetAgentList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_list(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentListRequest,
    ) -> yundun_dbaudit_20180320_models.GetAgentListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_list_with_options(request, runtime)

    async def get_agent_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAgentListRequest,
    ) -> yundun_dbaudit_20180320_models.GetAgentListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_list_with_options_async(request, runtime)

    def get_appoint_operation_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetAppointOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAppointOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAppointOperationResponse(),
            self.do_rpcrequest('GetAppointOperation', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_appoint_operation_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAppointOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAppointOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAppointOperationResponse(),
            await self.do_rpcrequest_async('GetAppointOperation', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_appoint_operation(
        self,
        request: yundun_dbaudit_20180320_models.GetAppointOperationRequest,
    ) -> yundun_dbaudit_20180320_models.GetAppointOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_appoint_operation_with_options(request, runtime)

    async def get_appoint_operation_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAppointOperationRequest,
    ) -> yundun_dbaudit_20180320_models.GetAppointOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_appoint_operation_with_options_async(request, runtime)

    def get_audit_count_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountResponse(),
            self.do_rpcrequest('GetAuditCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audit_count_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountResponse(),
            await self.do_rpcrequest_async('GetAuditCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_count(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountRequest,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_count_with_options(request, runtime)

    async def get_audit_count_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountRequest,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_count_with_options_async(request, runtime)

    def get_audit_count_distribution_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse(),
            self.do_rpcrequest('GetAuditCountDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audit_count_distribution_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse(),
            await self.do_rpcrequest_async('GetAuditCountDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_count_distribution(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_count_distribution_with_options(request, runtime)

    async def get_audit_count_distribution_async(
        self,
        request: yundun_dbaudit_20180320_models.GetAuditCountDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_count_distribution_with_options_async(request, runtime)

    def get_base_template_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetBaseTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetBaseTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetBaseTemplateListResponse(),
            self.do_rpcrequest('GetBaseTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_base_template_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetBaseTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetBaseTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetBaseTemplateListResponse(),
            await self.do_rpcrequest_async('GetBaseTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_base_template_list(
        self,
        request: yundun_dbaudit_20180320_models.GetBaseTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetBaseTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_base_template_list_with_options(request, runtime)

    async def get_base_template_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetBaseTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetBaseTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_base_template_list_with_options_async(request, runtime)

    def get_das_usage_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetDasUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetDasUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDasUsageResponse(),
            self.do_rpcrequest('GetDasUsage', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_das_usage_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetDasUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetDasUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDasUsageResponse(),
            await self.do_rpcrequest_async('GetDasUsage', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_das_usage(
        self,
        request: yundun_dbaudit_20180320_models.GetDasUsageRequest,
    ) -> yundun_dbaudit_20180320_models.GetDasUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_das_usage_with_options(request, runtime)

    async def get_das_usage_async(
        self,
        request: yundun_dbaudit_20180320_models.GetDasUsageRequest,
    ) -> yundun_dbaudit_20180320_models.GetDasUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_das_usage_with_options_async(request, runtime)

    def get_dbaudit_count_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetDBAuditCountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetDBAuditCountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDBAuditCountListResponse(),
            self.do_rpcrequest('GetDBAuditCountList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dbaudit_count_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetDBAuditCountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetDBAuditCountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDBAuditCountListResponse(),
            await self.do_rpcrequest_async('GetDBAuditCountList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dbaudit_count_list(
        self,
        request: yundun_dbaudit_20180320_models.GetDBAuditCountListRequest,
    ) -> yundun_dbaudit_20180320_models.GetDBAuditCountListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbaudit_count_list_with_options(request, runtime)

    async def get_dbaudit_count_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetDBAuditCountListRequest,
    ) -> yundun_dbaudit_20180320_models.GetDBAuditCountListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbaudit_count_list_with_options_async(request, runtime)

    def get_group_detail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetGroupDetailResponse(),
            self.do_rpcrequest('GetGroupDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_group_detail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetGroupDetailResponse(),
            await self.do_rpcrequest_async('GetGroupDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_detail(
        self,
        request: yundun_dbaudit_20180320_models.GetGroupDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_detail_with_options(request, runtime)

    async def get_group_detail_async(
        self,
        request: yundun_dbaudit_20180320_models.GetGroupDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_detail_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLicenseResponse(),
            self.do_rpcrequest('GetLicense', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_license_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLicenseResponse(),
            await self.do_rpcrequest_async('GetLicense', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_license(
        self,
        request: yundun_dbaudit_20180320_models.GetLicenseRequest,
    ) -> yundun_dbaudit_20180320_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    async def get_license_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLicenseRequest,
    ) -> yundun_dbaudit_20180320_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_license_with_options_async(request, runtime)

    def get_log_detail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogDetailResponse(),
            self.do_rpcrequest('GetLogDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_detail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogDetailResponse(),
            await self.do_rpcrequest_async('GetLogDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_detail(
        self,
        request: yundun_dbaudit_20180320_models.GetLogDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_detail_with_options(request, runtime)

    async def get_log_detail_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_detail_with_options_async(request, runtime)

    def get_log_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogListResponse(),
            self.do_rpcrequest('GetLogList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogListResponse(),
            await self.do_rpcrequest_async('GetLogList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_list(
        self,
        request: yundun_dbaudit_20180320_models.GetLogListRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_list_with_options(request, runtime)

    async def get_log_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogListRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_list_with_options_async(request, runtime)

    def get_log_mask_configs_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse(),
            self.do_rpcrequest('GetLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_mask_configs_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogMaskConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse(),
            await self.do_rpcrequest_async('GetLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_mask_configs(
        self,
        request: yundun_dbaudit_20180320_models.GetLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_mask_configs_with_options(request, runtime)

    async def get_log_mask_configs_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogMaskConfigsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_mask_configs_with_options_async(request, runtime)

    def get_log_query_condition_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogQueryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogQueryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogQueryConditionResponse(),
            self.do_rpcrequest('GetLogQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_query_condition_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogQueryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogQueryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogQueryConditionResponse(),
            await self.do_rpcrequest_async('GetLogQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_query_condition(
        self,
        request: yundun_dbaudit_20180320_models.GetLogQueryConditionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogQueryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_query_condition_with_options(request, runtime)

    async def get_log_query_condition_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogQueryConditionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogQueryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_query_condition_with_options_async(request, runtime)

    def get_log_statistics_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogStatisticsResponse(),
            self.do_rpcrequest('GetLogStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_statistics_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogStatisticsResponse(),
            await self.do_rpcrequest_async('GetLogStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_statistics(
        self,
        request: yundun_dbaudit_20180320_models.GetLogStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_statistics_with_options(request, runtime)

    async def get_log_statistics_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_statistics_with_options_async(request, runtime)

    def get_log_top_distribution_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTopDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopDistributionResponse(),
            self.do_rpcrequest('GetLogTopDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_top_distribution_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTopDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopDistributionResponse(),
            await self.do_rpcrequest_async('GetLogTopDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_top_distribution(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTopDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_top_distribution_with_options(request, runtime)

    async def get_log_top_distribution_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTopDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_top_distribution_with_options_async(request, runtime)

    def get_log_top_statistics_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse(),
            self.do_rpcrequest('GetLogTopStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_top_statistics_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse(),
            await self.do_rpcrequest_async('GetLogTopStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_top_statistics(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_top_statistics_with_options(request, runtime)

    async def get_log_top_statistics_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTopStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_top_statistics_with_options_async(request, runtime)

    def get_log_type_distribution_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTypeDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse(),
            self.do_rpcrequest('GetLogTypeDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_log_type_distribution_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTypeDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse(),
            await self.do_rpcrequest_async('GetLogTypeDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_type_distribution(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTypeDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_type_distribution_with_options(request, runtime)

    async def get_log_type_distribution_async(
        self,
        request: yundun_dbaudit_20180320_models.GetLogTypeDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_type_distribution_with_options_async(request, runtime)

    def get_new_sql_template_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetNewSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse(),
            self.do_rpcrequest('GetNewSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_new_sql_template_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetNewSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse(),
            await self.do_rpcrequest_async('GetNewSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_new_sql_template_list(
        self,
        request: yundun_dbaudit_20180320_models.GetNewSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_new_sql_template_list_with_options(request, runtime)

    async def get_new_sql_template_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetNewSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_new_sql_template_list_with_options_async(request, runtime)

    def get_report_file_url_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetReportFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetReportFileUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetReportFileUrlResponse(),
            self.do_rpcrequest('GetReportFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_report_file_url_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetReportFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetReportFileUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetReportFileUrlResponse(),
            await self.do_rpcrequest_async('GetReportFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_report_file_url(
        self,
        request: yundun_dbaudit_20180320_models.GetReportFileUrlRequest,
    ) -> yundun_dbaudit_20180320_models.GetReportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_report_file_url_with_options(request, runtime)

    async def get_report_file_url_async(
        self,
        request: yundun_dbaudit_20180320_models.GetReportFileUrlRequest,
    ) -> yundun_dbaudit_20180320_models.GetReportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_report_file_url_with_options_async(request, runtime)

    def get_risk_level_distribution_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskLevelDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse(),
            self.do_rpcrequest('GetRiskLevelDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_risk_level_distribution_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskLevelDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse(),
            await self.do_rpcrequest_async('GetRiskLevelDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_risk_level_distribution(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskLevelDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_level_distribution_with_options(request, runtime)

    async def get_risk_level_distribution_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskLevelDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_level_distribution_with_options_async(request, runtime)

    def get_risk_statistics_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRiskStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskStatisticsResponse(),
            self.do_rpcrequest('GetRiskStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_risk_statistics_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRiskStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskStatisticsResponse(),
            await self.do_rpcrequest_async('GetRiskStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_risk_statistics(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetRiskStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_statistics_with_options(request, runtime)

    async def get_risk_statistics_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRiskStatisticsRequest,
    ) -> yundun_dbaudit_20180320_models.GetRiskStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_statistics_with_options_async(request, runtime)

    def get_rule_detail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRuleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleDetailResponse(),
            self.do_rpcrequest('GetRuleDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_detail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRuleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleDetailResponse(),
            await self.do_rpcrequest_async('GetRuleDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_detail(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    async def get_rule_detail_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_detail_with_options_async(request, runtime)

    def get_rule_group_name_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRuleGroupNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleGroupNameResponse(),
            self.do_rpcrequest('GetRuleGroupName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_group_name_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetRuleGroupNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleGroupNameResponse(),
            await self.do_rpcrequest_async('GetRuleGroupName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_group_name(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleGroupNameRequest,
    ) -> yundun_dbaudit_20180320_models.GetRuleGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_group_name_with_options(request, runtime)

    async def get_rule_group_name_async(
        self,
        request: yundun_dbaudit_20180320_models.GetRuleGroupNameRequest,
    ) -> yundun_dbaudit_20180320_models.GetRuleGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_group_name_with_options_async(request, runtime)

    def get_session_detail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDetailResponse(),
            self.do_rpcrequest('GetSessionDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_session_detail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDetailResponse(),
            await self.do_rpcrequest_async('GetSessionDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_detail(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_session_detail_with_options(request, runtime)

    async def get_session_detail_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDetailRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_session_detail_with_options_async(request, runtime)

    def get_session_distribution_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDistributionResponse(),
            self.do_rpcrequest('GetSessionDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_session_distribution_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDistributionResponse(),
            await self.do_rpcrequest_async('GetSessionDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_distribution(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_session_distribution_with_options(request, runtime)

    async def get_session_distribution_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionDistributionRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_session_distribution_with_options_async(request, runtime)

    def get_session_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionListResponse(),
            self.do_rpcrequest('GetSessionList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_session_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionListResponse(),
            await self.do_rpcrequest_async('GetSessionList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_list(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionListRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_session_list_with_options(request, runtime)

    async def get_session_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionListRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_session_list_with_options_async(request, runtime)

    def get_session_query_condition_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionQueryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse(),
            self.do_rpcrequest('GetSessionQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_session_query_condition_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionQueryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse(),
            await self.do_rpcrequest_async('GetSessionQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_query_condition(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionQueryConditionRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_session_query_condition_with_options(request, runtime)

    async def get_session_query_condition_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSessionQueryConditionRequest,
    ) -> yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_session_query_condition_with_options_async(request, runtime)

    def get_sql_template_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSqlTemplateListResponse(),
            self.do_rpcrequest('GetSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sql_template_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSqlTemplateListResponse(),
            await self.do_rpcrequest_async('GetSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_template_list(
        self,
        request: yundun_dbaudit_20180320_models.GetSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sql_template_list_with_options(request, runtime)

    async def get_sql_template_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_template_list_with_options_async(request, runtime)

    def get_top_sql_template_list_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GetTopSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse(),
            self.do_rpcrequest('GetTopSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_top_sql_template_list_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GetTopSqlTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse(),
            await self.do_rpcrequest_async('GetTopSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_top_sql_template_list(
        self,
        request: yundun_dbaudit_20180320_models.GetTopSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_top_sql_template_list_with_options(request, runtime)

    async def get_top_sql_template_list_async(
        self,
        request: yundun_dbaudit_20180320_models.GetTopSqlTemplateListRequest,
    ) -> yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_top_sql_template_list_with_options_async(request, runtime)

    def grade_protection_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.GradeProtectionReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GradeProtectionReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GradeProtectionReportResponse(),
            self.do_rpcrequest('GradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grade_protection_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.GradeProtectionReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.GradeProtectionReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GradeProtectionReportResponse(),
            await self.do_rpcrequest_async('GradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grade_protection_report(
        self,
        request: yundun_dbaudit_20180320_models.GradeProtectionReportRequest,
    ) -> yundun_dbaudit_20180320_models.GradeProtectionReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.grade_protection_report_with_options(request, runtime)

    async def grade_protection_report_async(
        self,
        request: yundun_dbaudit_20180320_models.GradeProtectionReportRequest,
    ) -> yundun_dbaudit_20180320_models.GradeProtectionReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grade_protection_report_with_options_async(request, runtime)

    def import_data_source_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ImportDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ImportDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ImportDataSourceResponse(),
            self.do_rpcrequest('ImportDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_data_source_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ImportDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ImportDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ImportDataSourceResponse(),
            await self.do_rpcrequest_async('ImportDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_data_source(
        self,
        request: yundun_dbaudit_20180320_models.ImportDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.ImportDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_data_source_with_options(request, runtime)

    async def import_data_source_async(
        self,
        request: yundun_dbaudit_20180320_models.ImportDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.ImportDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_data_source_with_options_async(request, runtime)

    def integrated_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.IntegratedReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.IntegratedReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.IntegratedReportResponse(),
            self.do_rpcrequest('IntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def integrated_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.IntegratedReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.IntegratedReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.IntegratedReportResponse(),
            await self.do_rpcrequest_async('IntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def integrated_report(
        self,
        request: yundun_dbaudit_20180320_models.IntegratedReportRequest,
    ) -> yundun_dbaudit_20180320_models.IntegratedReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.integrated_report_with_options(request, runtime)

    async def integrated_report_async(
        self,
        request: yundun_dbaudit_20180320_models.IntegratedReportRequest,
    ) -> yundun_dbaudit_20180320_models.IntegratedReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.integrated_report_with_options_async(request, runtime)

    def list_associated_rules_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListAssociatedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListAssociatedRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListAssociatedRulesResponse(),
            self.do_rpcrequest('ListAssociatedRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_associated_rules_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListAssociatedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListAssociatedRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListAssociatedRulesResponse(),
            await self.do_rpcrequest_async('ListAssociatedRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_associated_rules(
        self,
        request: yundun_dbaudit_20180320_models.ListAssociatedRulesRequest,
    ) -> yundun_dbaudit_20180320_models.ListAssociatedRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_associated_rules_with_options(request, runtime)

    async def list_associated_rules_async(
        self,
        request: yundun_dbaudit_20180320_models.ListAssociatedRulesRequest,
    ) -> yundun_dbaudit_20180320_models.ListAssociatedRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_associated_rules_with_options_async(request, runtime)

    def list_data_source_attribute_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse(),
            self.do_rpcrequest('ListDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_source_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse(),
            await self.do_rpcrequest_async('ListDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_source_attribute(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_attribute_with_options(request, runtime)

    async def list_data_source_attribute_async(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_attribute_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourcesResponse(),
            self.do_rpcrequest('ListDataSources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourcesResponse(),
            await self.do_rpcrequest_async('ListDataSources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_sources(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourcesRequest,
    ) -> yundun_dbaudit_20180320_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: yundun_dbaudit_20180320_models.ListDataSourcesRequest,
    ) -> yundun_dbaudit_20180320_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_log_alarm_tasks_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListLogAlarmTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse(),
            self.do_rpcrequest('ListLogAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_log_alarm_tasks_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListLogAlarmTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse(),
            await self.do_rpcrequest_async('ListLogAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_log_alarm_tasks(
        self,
        request: yundun_dbaudit_20180320_models.ListLogAlarmTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_log_alarm_tasks_with_options(request, runtime)

    async def list_log_alarm_tasks_async(
        self,
        request: yundun_dbaudit_20180320_models.ListLogAlarmTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_log_alarm_tasks_with_options_async(request, runtime)

    def list_report_push_tasks_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListReportPushTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListReportPushTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListReportPushTasksResponse(),
            self.do_rpcrequest('ListReportPushTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_report_push_tasks_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListReportPushTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListReportPushTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListReportPushTasksResponse(),
            await self.do_rpcrequest_async('ListReportPushTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_report_push_tasks(
        self,
        request: yundun_dbaudit_20180320_models.ListReportPushTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListReportPushTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_report_push_tasks_with_options(request, runtime)

    async def list_report_push_tasks_async(
        self,
        request: yundun_dbaudit_20180320_models.ListReportPushTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListReportPushTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_report_push_tasks_with_options_async(request, runtime)

    def list_rule_groups_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListRuleGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRuleGroupsResponse(),
            self.do_rpcrequest('ListRuleGroups', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rule_groups_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListRuleGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRuleGroupsResponse(),
            await self.do_rpcrequest_async('ListRuleGroups', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rule_groups(
        self,
        request: yundun_dbaudit_20180320_models.ListRuleGroupsRequest,
    ) -> yundun_dbaudit_20180320_models.ListRuleGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rule_groups_with_options(request, runtime)

    async def list_rule_groups_async(
        self,
        request: yundun_dbaudit_20180320_models.ListRuleGroupsRequest,
    ) -> yundun_dbaudit_20180320_models.ListRuleGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rule_groups_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRulesResponse(),
            self.do_rpcrequest('ListRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRulesResponse(),
            await self.do_rpcrequest_async('ListRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rules(
        self,
        request: yundun_dbaudit_20180320_models.ListRulesRequest,
    ) -> yundun_dbaudit_20180320_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: yundun_dbaudit_20180320_models.ListRulesRequest,
    ) -> yundun_dbaudit_20180320_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_sql_type_keys_for_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse(),
            self.do_rpcrequest('ListSqlTypeKeysForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sql_type_keys_for_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse(),
            await self.do_rpcrequest_async('ListSqlTypeKeysForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sql_type_keys_for_rule(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sql_type_keys_for_rule_with_options(request, runtime)

    async def list_sql_type_keys_for_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sql_type_keys_for_rule_with_options_async(request, runtime)

    def list_sql_types_for_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypesForRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse(),
            self.do_rpcrequest('ListSqlTypesForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sql_types_for_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypesForRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse(),
            await self.do_rpcrequest_async('ListSqlTypesForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sql_types_for_rule(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypesForRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sql_types_for_rule_with_options(request, runtime)

    async def list_sql_types_for_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSqlTypesForRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sql_types_for_rule_with_options_async(request, runtime)

    def list_support_db_types_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListSupportDbTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSupportDbTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSupportDbTypesResponse(),
            self.do_rpcrequest('ListSupportDbTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_support_db_types_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSupportDbTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSupportDbTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSupportDbTypesResponse(),
            await self.do_rpcrequest_async('ListSupportDbTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_support_db_types(
        self,
        request: yundun_dbaudit_20180320_models.ListSupportDbTypesRequest,
    ) -> yundun_dbaudit_20180320_models.ListSupportDbTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_support_db_types_with_options(request, runtime)

    async def list_support_db_types_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSupportDbTypesRequest,
    ) -> yundun_dbaudit_20180320_models.ListSupportDbTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_support_db_types_with_options_async(request, runtime)

    def list_system_alarms_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmsResponse(),
            self.do_rpcrequest('ListSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_system_alarms_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmsResponse(),
            await self.do_rpcrequest_async('ListSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_alarms(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmsRequest,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_alarms_with_options(request, runtime)

    async def list_system_alarms_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmsRequest,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_alarms_with_options_async(request, runtime)

    def list_system_alarm_tasks_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse(),
            self.do_rpcrequest('ListSystemAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_system_alarm_tasks_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse(),
            await self.do_rpcrequest_async('ListSystemAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_alarm_tasks(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_alarm_tasks_with_options(request, runtime)

    async def list_system_alarm_tasks_async(
        self,
        request: yundun_dbaudit_20180320_models.ListSystemAlarmTasksRequest,
    ) -> yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_alarm_tasks_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: yundun_dbaudit_20180320_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20180320_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20180320_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: yundun_dbaudit_20180320_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_templates_for_sql_rule_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse(),
            self.do_rpcrequest('ListTemplatesForSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_for_sql_rule_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse(),
            await self.do_rpcrequest_async('ListTemplatesForSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates_for_sql_rule(
        self,
        request: yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_for_sql_rule_with_options(request, runtime)

    async def list_templates_for_sql_rule_async(
        self,
        request: yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleRequest,
    ) -> yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_for_sql_rule_with_options_async(request, runtime)

    def list_used_sql_types_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ListUsedSqlTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse(),
            self.do_rpcrequest('ListUsedSqlTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_used_sql_types_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ListUsedSqlTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse(),
            await self.do_rpcrequest_async('ListUsedSqlTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_used_sql_types(
        self,
        request: yundun_dbaudit_20180320_models.ListUsedSqlTypesRequest,
    ) -> yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_used_sql_types_with_options(request, runtime)

    async def list_used_sql_types_async(
        self,
        request: yundun_dbaudit_20180320_models.ListUsedSqlTypesRequest,
    ) -> yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_used_sql_types_with_options_async(request, runtime)

    def modify_base_template_state_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyBaseTemplateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse(),
            self.do_rpcrequest('ModifyBaseTemplateState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_base_template_state_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyBaseTemplateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse(),
            await self.do_rpcrequest_async('ModifyBaseTemplateState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_base_template_state(
        self,
        request: yundun_dbaudit_20180320_models.ModifyBaseTemplateStateRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_base_template_state_with_options(request, runtime)

    async def modify_base_template_state_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyBaseTemplateStateRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_base_template_state_with_options_async(request, runtime)

    def modify_custom_name_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyCustomNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyCustomNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyCustomNameResponse(),
            self.do_rpcrequest('ModifyCustomName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_custom_name_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyCustomNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyCustomNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyCustomNameResponse(),
            await self.do_rpcrequest_async('ModifyCustomName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_custom_name(
        self,
        request: yundun_dbaudit_20180320_models.ModifyCustomNameRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyCustomNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_name_with_options(request, runtime)

    async def modify_custom_name_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyCustomNameRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyCustomNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_custom_name_with_options_async(request, runtime)

    def modify_data_source_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceResponse(),
            self.do_rpcrequest('ModifyDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceResponse(),
            await self.do_rpcrequest_async('ModifyDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_source(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_with_options(request, runtime)

    async def modify_data_source_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_with_options_async(request, runtime)

    def modify_data_source_attribute_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse(),
            self.do_rpcrequest('ModifyDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_data_source_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse(),
            await self.do_rpcrequest_async('ModifyDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_source_attribute(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_attribute_with_options(request, runtime)

    async def modify_data_source_attribute_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyDataSourceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_attribute_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: yundun_dbaudit_20180320_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_log_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyLogAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse(),
            self.do_rpcrequest('ModifyLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_log_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyLogAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse(),
            await self.do_rpcrequest_async('ModifyLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.ModifyLogAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_alarm_task_with_options(request, runtime)

    async def modify_log_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyLogAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_alarm_task_with_options_async(request, runtime)

    def modify_plan_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyPlanResponse(),
            self.do_rpcrequest('ModifyPlan', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_plan_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyPlanResponse(),
            await self.do_rpcrequest_async('ModifyPlan', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_plan(
        self,
        request: yundun_dbaudit_20180320_models.ModifyPlanRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_plan_with_options(request, runtime)

    async def modify_plan_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyPlanRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_plan_with_options_async(request, runtime)

    def modify_report_push_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse(),
            self.do_rpcrequest('ModifyReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_report_push_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyReportPushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse(),
            await self.do_rpcrequest_async('ModifyReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_report_push_task(
        self,
        request: yundun_dbaudit_20180320_models.ModifyReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_report_push_task_with_options(request, runtime)

    async def modify_report_push_task_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyReportPushTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_report_push_task_with_options_async(request, runtime)

    def modify_rule_group_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifyRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyRuleGroupResponse(),
            self.do_rpcrequest('ModifyRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_rule_group_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifyRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyRuleGroupResponse(),
            await self.do_rpcrequest_async('ModifyRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rule_group(
        self,
        request: yundun_dbaudit_20180320_models.ModifyRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_group_with_options(request, runtime)

    async def modify_rule_group_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifyRuleGroupRequest,
    ) -> yundun_dbaudit_20180320_models.ModifyRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rule_group_with_options_async(request, runtime)

    def modify_system_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ModifySystemAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse(),
            self.do_rpcrequest('ModifySystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_system_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifySystemAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse(),
            await self.do_rpcrequest_async('ModifySystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_system_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.ModifySystemAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_system_alarm_task_with_options(request, runtime)

    async def modify_system_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.ModifySystemAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_system_alarm_task_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_dbaudit_20180320_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.MoveResourceGroupResponse(),
            await self.do_rpcrequest_async('MoveResourceGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: yundun_dbaudit_20180320_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20180320_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_dbaudit_20180320_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20180320_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def pci_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.PciReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.PciReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PciReportResponse(),
            self.do_rpcrequest('PciReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pci_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.PciReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.PciReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PciReportResponse(),
            await self.do_rpcrequest_async('PciReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pci_report(
        self,
        request: yundun_dbaudit_20180320_models.PciReportRequest,
    ) -> yundun_dbaudit_20180320_models.PciReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.pci_report_with_options(request, runtime)

    async def pci_report_async(
        self,
        request: yundun_dbaudit_20180320_models.PciReportRequest,
    ) -> yundun_dbaudit_20180320_models.PciReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pci_report_with_options_async(request, runtime)

    def put_login_count_with_options(
        self,
        request: yundun_dbaudit_20180320_models.PutLoginCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.PutLoginCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PutLoginCountResponse(),
            self.do_rpcrequest('PutLoginCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_login_count_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.PutLoginCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.PutLoginCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PutLoginCountResponse(),
            await self.do_rpcrequest_async('PutLoginCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_login_count(
        self,
        request: yundun_dbaudit_20180320_models.PutLoginCountRequest,
    ) -> yundun_dbaudit_20180320_models.PutLoginCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_login_count_with_options(request, runtime)

    async def put_login_count_async(
        self,
        request: yundun_dbaudit_20180320_models.PutLoginCountRequest,
    ) -> yundun_dbaudit_20180320_models.PutLoginCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_login_count_with_options_async(request, runtime)

    def read_mark_system_alarms_with_options(
        self,
        request: yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse(),
            self.do_rpcrequest('ReadMarkSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def read_mark_system_alarms_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse(),
            await self.do_rpcrequest_async('ReadMarkSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def read_mark_system_alarms(
        self,
        request: yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsRequest,
    ) -> yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.read_mark_system_alarms_with_options(request, runtime)

    async def read_mark_system_alarms_async(
        self,
        request: yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsRequest,
    ) -> yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.read_mark_system_alarms_with_options_async(request, runtime)

    def refund_instance_with_options(
        self,
        request: yundun_dbaudit_20180320_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RefundInstanceResponse(),
            self.do_rpcrequest('RefundInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_instance_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RefundInstanceResponse(),
            await self.do_rpcrequest_async('RefundInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_instance(
        self,
        request: yundun_dbaudit_20180320_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20180320_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    async def refund_instance_async(
        self,
        request: yundun_dbaudit_20180320_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20180320_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_instance_with_options_async(request, runtime)

    def register_notice_mail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.RegisterNoticeMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RegisterNoticeMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RegisterNoticeMailResponse(),
            self.do_rpcrequest('RegisterNoticeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_notice_mail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.RegisterNoticeMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RegisterNoticeMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RegisterNoticeMailResponse(),
            await self.do_rpcrequest_async('RegisterNoticeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_notice_mail(
        self,
        request: yundun_dbaudit_20180320_models.RegisterNoticeMailRequest,
    ) -> yundun_dbaudit_20180320_models.RegisterNoticeMailResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_notice_mail_with_options(request, runtime)

    async def register_notice_mail_async(
        self,
        request: yundun_dbaudit_20180320_models.RegisterNoticeMailRequest,
    ) -> yundun_dbaudit_20180320_models.RegisterNoticeMailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_notice_mail_with_options_async(request, runtime)

    def remove_log_mask_config_with_options(
        self,
        request: yundun_dbaudit_20180320_models.RemoveLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse(),
            self.do_rpcrequest('RemoveLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_log_mask_config_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.RemoveLogMaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse(),
            await self.do_rpcrequest_async('RemoveLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_log_mask_config(
        self,
        request: yundun_dbaudit_20180320_models.RemoveLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_log_mask_config_with_options(request, runtime)

    async def remove_log_mask_config_async(
        self,
        request: yundun_dbaudit_20180320_models.RemoveLogMaskConfigRequest,
    ) -> yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_log_mask_config_with_options_async(request, runtime)

    def send_verify_code_mail_with_options(
        self,
        request: yundun_dbaudit_20180320_models.SendVerifyCodeMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse(),
            self.do_rpcrequest('SendVerifyCodeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_verify_code_mail_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.SendVerifyCodeMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse(),
            await self.do_rpcrequest_async('SendVerifyCodeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_verify_code_mail(
        self,
        request: yundun_dbaudit_20180320_models.SendVerifyCodeMailRequest,
    ) -> yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_mail_with_options(request, runtime)

    async def send_verify_code_mail_async(
        self,
        request: yundun_dbaudit_20180320_models.SendVerifyCodeMailRequest,
    ) -> yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_mail_with_options_async(request, runtime)

    def sox_report_with_options(
        self,
        request: yundun_dbaudit_20180320_models.SoxReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.SoxReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SoxReportResponse(),
            self.do_rpcrequest('SoxReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sox_report_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.SoxReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.SoxReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SoxReportResponse(),
            await self.do_rpcrequest_async('SoxReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sox_report(
        self,
        request: yundun_dbaudit_20180320_models.SoxReportRequest,
    ) -> yundun_dbaudit_20180320_models.SoxReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.sox_report_with_options(request, runtime)

    async def sox_report_async(
        self,
        request: yundun_dbaudit_20180320_models.SoxReportRequest,
    ) -> yundun_dbaudit_20180320_models.SoxReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sox_report_with_options_async(request, runtime)

    def start_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.StartAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StartAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartAlarmTaskResponse(),
            self.do_rpcrequest('StartAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.StartAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StartAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartAlarmTaskResponse(),
            await self.do_rpcrequest_async('StartAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.StartAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.StartAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_alarm_task_with_options(request, runtime)

    async def start_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.StartAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.StartAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_alarm_task_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_dbaudit_20180320_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartInstanceResponse(),
            await self.do_rpcrequest_async('StartInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: yundun_dbaudit_20180320_models.StartInstanceRequest,
    ) -> yundun_dbaudit_20180320_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: yundun_dbaudit_20180320_models.StartInstanceRequest,
    ) -> yundun_dbaudit_20180320_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_alarm_task_with_options(
        self,
        request: yundun_dbaudit_20180320_models.StopAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StopAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StopAlarmTaskResponse(),
            self.do_rpcrequest('StopAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_alarm_task_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.StopAlarmTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.StopAlarmTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StopAlarmTaskResponse(),
            await self.do_rpcrequest_async('StopAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_alarm_task(
        self,
        request: yundun_dbaudit_20180320_models.StopAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.StopAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_alarm_task_with_options(request, runtime)

    async def stop_alarm_task_async(
        self,
        request: yundun_dbaudit_20180320_models.StopAlarmTaskRequest,
    ) -> yundun_dbaudit_20180320_models.StopAlarmTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_alarm_task_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_dbaudit_20180320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: yundun_dbaudit_20180320_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_dbaudit_20180320_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_dbaudit_20180320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: yundun_dbaudit_20180320_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_dbaudit_20180320_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20180320_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: yundun_dbaudit_20180320_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse(),
            self.do_rpcrequest('UpgradeInstanceVersion', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: yundun_dbaudit_20180320_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse(),
            await self.do_rpcrequest_async('UpgradeInstanceVersion', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: yundun_dbaudit_20180320_models.UpgradeInstanceVersionRequest,
    ) -> yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: yundun_dbaudit_20180320_models.UpgradeInstanceVersionRequest,
    ) -> yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)
