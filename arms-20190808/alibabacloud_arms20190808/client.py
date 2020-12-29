# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20190808 import models as arms20190808_models
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
            'ap-northeast-1': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'arms.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'arms.aliyuncs.com',
            'cn-huhehaote': 'arms.aliyuncs.com',
            'eu-central-1': 'arms.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'arms.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'arms.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'arms.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'arms.aliyuncs.com',
            'cn-shenzhen-finance-1': 'arms.aliyuncs.com',
            'cn-shanghai-finance-1': 'arms.aliyuncs.com',
            'cn-north-2-gov-1': 'arms.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('arms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_grafana_with_options(
        self,
        request: arms20190808_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.AddGrafanaResponse().from_map(
            self.do_rpcrequest('AddGrafana', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_grafana_with_options_async(
        self,
        request: arms20190808_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.AddGrafanaResponse().from_map(
            await self.do_rpcrequest_async('AddGrafana', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_grafana(
        self,
        request: arms20190808_models.AddGrafanaRequest,
    ) -> arms20190808_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    async def add_grafana_async(
        self,
        request: arms20190808_models.AddGrafanaRequest,
    ) -> arms20190808_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_grafana_with_options_async(request, runtime)

    def add_integration_with_options(
        self,
        request: arms20190808_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.AddIntegrationResponse().from_map(
            self.do_rpcrequest('AddIntegration', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_integration_with_options_async(
        self,
        request: arms20190808_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.AddIntegrationResponse().from_map(
            await self.do_rpcrequest_async('AddIntegration', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_integration(
        self,
        request: arms20190808_models.AddIntegrationRequest,
    ) -> arms20190808_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: arms20190808_models.AddIntegrationRequest,
    ) -> arms20190808_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_integration_with_options_async(request, runtime)

    def apply_scenario_with_options(
        self,
        tmp_req: arms20190808_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ApplyScenarioResponse().from_map(
            self.do_rpcrequest('ApplyScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_scenario_with_options_async(
        self,
        tmp_req: arms20190808_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ApplyScenarioResponse().from_map(
            await self.do_rpcrequest_async('ApplyScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_scenario(
        self,
        request: arms20190808_models.ApplyScenarioRequest,
    ) -> arms20190808_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    async def apply_scenario_async(
        self,
        request: arms20190808_models.ApplyScenarioRequest,
    ) -> arms20190808_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_scenario_with_options_async(request, runtime)

    def check_data_consistency_with_options(
        self,
        request: arms20190808_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CheckDataConsistencyResponse().from_map(
            self.do_rpcrequest('CheckDataConsistency', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_data_consistency_with_options_async(
        self,
        request: arms20190808_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CheckDataConsistencyResponse().from_map(
            await self.do_rpcrequest_async('CheckDataConsistency', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_data_consistency(
        self,
        request: arms20190808_models.CheckDataConsistencyRequest,
    ) -> arms20190808_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_data_consistency_with_options(request, runtime)

    async def check_data_consistency_async(
        self,
        request: arms20190808_models.CheckDataConsistencyRequest,
    ) -> arms20190808_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_data_consistency_with_options_async(request, runtime)

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: arms20190808_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CheckServiceLinkedRoleForDeletingResponse().from_map(
            self.do_rpcrequest('CheckServiceLinkedRoleForDeleting', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: arms20190808_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CheckServiceLinkedRoleForDeletingResponse().from_map(
            await self.do_rpcrequest_async('CheckServiceLinkedRoleForDeleting', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: arms20190808_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20190808_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: arms20190808_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20190808_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: arms20190808_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ConfigAppResponse().from_map(
            self.do_rpcrequest('ConfigApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_app_with_options_async(
        self,
        request: arms20190808_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ConfigAppResponse().from_map(
            await self.do_rpcrequest_async('ConfigApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_app(
        self,
        request: arms20190808_models.ConfigAppRequest,
    ) -> arms20190808_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: arms20190808_models.ConfigAppRequest,
    ) -> arms20190808_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateAlertContactResponse().from_map(
            self.do_rpcrequest('CreateAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateAlertContactResponse().from_map(
            await self.do_rpcrequest_async('CreateAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alert_contact(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
    ) -> arms20190808_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
    ) -> arms20190808_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateAlertContactGroupResponse().from_map(
            self.do_rpcrequest('CreateAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateAlertContactGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateRetcodeAppResponse().from_map(
            self.do_rpcrequest('CreateRetcodeApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_retcode_app_with_options_async(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateRetcodeAppResponse().from_map(
            await self.do_rpcrequest_async('CreateRetcodeApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_retcode_app(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    async def create_retcode_app_async(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_retcode_app_with_options_async(request, runtime)

    def create_wehook_with_options(
        self,
        request: arms20190808_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateWehookResponse().from_map(
            self.do_rpcrequest('CreateWehook', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_wehook_with_options_async(
        self,
        request: arms20190808_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.CreateWehookResponse().from_map(
            await self.do_rpcrequest_async('CreateWehook', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_wehook(
        self,
        request: arms20190808_models.CreateWehookRequest,
    ) -> arms20190808_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_wehook_with_options(request, runtime)

    async def create_wehook_async(
        self,
        request: arms20190808_models.CreateWehookRequest,
    ) -> arms20190808_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_wehook_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertContactResponse().from_map(
            self.do_rpcrequest('DeleteAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertContactResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_contact(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertContactGroupResponse().from_map(
            self.do_rpcrequest('DeleteAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertContactGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def delete_alert_rules_with_options(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertRulesResponse().from_map(
            self.do_rpcrequest('DeleteAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_rules_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteAlertRulesResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_rules(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    async def delete_alert_rules_async(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rules_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteRetcodeAppResponse().from_map(
            self.do_rpcrequest('DeleteRetcodeApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_retcode_app_with_options_async(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteRetcodeAppResponse().from_map(
            await self.do_rpcrequest_async('DeleteRetcodeApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_retcode_app(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    async def delete_retcode_app_async(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_retcode_app_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteScenarioResponse().from_map(
            self.do_rpcrequest('DeleteScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteScenarioResponse().from_map(
            await self.do_rpcrequest_async('DeleteScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scenario(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
    ) -> arms20190808_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
    ) -> arms20190808_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteTraceAppResponse().from_map(
            self.do_rpcrequest('DeleteTraceApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_trace_app_with_options_async(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DeleteTraceAppResponse().from_map(
            await self.do_rpcrequest_async('DeleteTraceApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trace_app(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    async def delete_trace_app_async(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trace_app_with_options_async(request, runtime)

    def describe_dispatch_rule_with_options(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeDispatchRuleResponse().from_map(
            self.do_rpcrequest('DescribeDispatchRule', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeDispatchRuleResponse().from_map(
            await self.do_rpcrequest_async('DescribeDispatchRule', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dispatch_rule(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    async def describe_dispatch_rule_async(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispatch_rule_with_options_async(request, runtime)

    def describe_trace_license_key_with_options(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeTraceLicenseKeyResponse().from_map(
            self.do_rpcrequest('DescribeTraceLicenseKey', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_trace_license_key_with_options_async(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeTraceLicenseKeyResponse().from_map(
            await self.do_rpcrequest_async('DescribeTraceLicenseKey', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_trace_license_key(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    async def describe_trace_license_key_async(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_license_key_with_options_async(request, runtime)

    def describe_trace_location_with_options(
        self,
        request: arms20190808_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeTraceLocationResponse().from_map(
            self.do_rpcrequest('DescribeTraceLocation', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_trace_location_with_options_async(
        self,
        request: arms20190808_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.DescribeTraceLocationResponse().from_map(
            await self.do_rpcrequest_async('DescribeTraceLocation', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_trace_location(
        self,
        request: arms20190808_models.DescribeTraceLocationRequest,
    ) -> arms20190808_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_location_with_options(request, runtime)

    async def describe_trace_location_async(
        self,
        request: arms20190808_models.DescribeTraceLocationRequest,
    ) -> arms20190808_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_location_with_options_async(request, runtime)

    def export_prometheus_rules_with_options(
        self,
        request: arms20190808_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ExportPrometheusRulesResponse().from_map(
            self.do_rpcrequest('ExportPrometheusRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_prometheus_rules_with_options_async(
        self,
        request: arms20190808_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ExportPrometheusRulesResponse().from_map(
            await self.do_rpcrequest_async('ExportPrometheusRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_prometheus_rules(
        self,
        request: arms20190808_models.ExportPrometheusRulesRequest,
    ) -> arms20190808_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_prometheus_rules_with_options(request, runtime)

    async def export_prometheus_rules_async(
        self,
        request: arms20190808_models.ExportPrometheusRulesRequest,
    ) -> arms20190808_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_prometheus_rules_with_options_async(request, runtime)

    def get_agent_download_url_with_options(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return arms20190808_models.GetAgentDownloadUrlResponse().from_map(
            self.do_rpcrequest('GetAgentDownloadUrl', '2019-08-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_download_url_with_options_async(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return arms20190808_models.GetAgentDownloadUrlResponse().from_map(
            await self.do_rpcrequest_async('GetAgentDownloadUrl', '2019-08-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_download_url(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    async def get_agent_download_url_async(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_download_url_with_options_async(request, runtime)

    def get_app_api_by_page_with_options(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetAppApiByPageResponse().from_map(
            self.do_rpcrequest('GetAppApiByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_api_by_page_with_options_async(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetAppApiByPageResponse().from_map(
            await self.do_rpcrequest_async('GetAppApiByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_api_by_page(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    async def get_app_api_by_page_async(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_api_by_page_with_options_async(request, runtime)

    def get_consistency_snapshot_with_options(
        self,
        request: arms20190808_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetConsistencySnapshotResponse().from_map(
            self.do_rpcrequest('GetConsistencySnapshot', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consistency_snapshot_with_options_async(
        self,
        request: arms20190808_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetConsistencySnapshotResponse().from_map(
            await self.do_rpcrequest_async('GetConsistencySnapshot', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consistency_snapshot(
        self,
        request: arms20190808_models.GetConsistencySnapshotRequest,
    ) -> arms20190808_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consistency_snapshot_with_options(request, runtime)

    async def get_consistency_snapshot_async(
        self,
        request: arms20190808_models.GetConsistencySnapshotRequest,
    ) -> arms20190808_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consistency_snapshot_with_options_async(request, runtime)

    def get_integration_token_with_options(
        self,
        request: arms20190808_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetIntegrationTokenResponse().from_map(
            self.do_rpcrequest('GetIntegrationToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_integration_token_with_options_async(
        self,
        request: arms20190808_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetIntegrationTokenResponse().from_map(
            await self.do_rpcrequest_async('GetIntegrationToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_integration_token(
        self,
        request: arms20190808_models.GetIntegrationTokenRequest,
    ) -> arms20190808_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_integration_token_with_options(request, runtime)

    async def get_integration_token_async(
        self,
        request: arms20190808_models.GetIntegrationTokenRequest,
    ) -> arms20190808_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_integration_token_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetMultipleTraceResponse().from_map(
            self.do_rpcrequest('GetMultipleTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multiple_trace_with_options_async(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetMultipleTraceResponse().from_map(
            await self.do_rpcrequest_async('GetMultipleTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_multiple_trace(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    async def get_multiple_trace_async(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multiple_trace_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetPrometheusApiTokenResponse().from_map(
            self.do_rpcrequest('GetPrometheusApiToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_prometheus_api_token_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetPrometheusApiTokenResponse().from_map(
            await self.do_rpcrequest_async('GetPrometheusApiToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_prometheus_api_token(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_api_token_with_options_async(request, runtime)

    def get_retcode_share_url_with_options(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetRetcodeShareUrlResponse().from_map(
            self.do_rpcrequest('GetRetcodeShareUrl', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_retcode_share_url_with_options_async(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetRetcodeShareUrlResponse().from_map(
            await self.do_rpcrequest_async('GetRetcodeShareUrl', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_retcode_share_url(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    async def get_retcode_share_url_async(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_share_url_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: arms20190808_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetStackResponse().from_map(
            self.do_rpcrequest('GetStack', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: arms20190808_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetStackResponse().from_map(
            await self.do_rpcrequest_async('GetStack', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack(
        self,
        request: arms20190808_models.GetStackRequest,
    ) -> arms20190808_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: arms20190808_models.GetStackRequest,
    ) -> arms20190808_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: arms20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetTraceResponse().from_map(
            self.do_rpcrequest('GetTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: arms20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetTraceResponse().from_map(
            await self.do_rpcrequest_async('GetTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trace(
        self,
        request: arms20190808_models.GetTraceRequest,
    ) -> arms20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: arms20190808_models.GetTraceRequest,
    ) -> arms20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def get_trace_app_with_options(
        self,
        request: arms20190808_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetTraceAppResponse().from_map(
            self.do_rpcrequest('GetTraceApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_app_with_options_async(
        self,
        request: arms20190808_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.GetTraceAppResponse().from_map(
            await self.do_rpcrequest_async('GetTraceApp', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trace_app(
        self,
        request: arms20190808_models.GetTraceAppRequest,
    ) -> arms20190808_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    async def get_trace_app_async(
        self,
        request: arms20190808_models.GetTraceAppRequest,
    ) -> arms20190808_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_app_with_options_async(request, runtime)

    def import_app_alert_rules_with_options(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportAppAlertRulesResponse().from_map(
            self.do_rpcrequest('ImportAppAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_app_alert_rules_with_options_async(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportAppAlertRulesResponse().from_map(
            await self.do_rpcrequest_async('ImportAppAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_app_alert_rules(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def import_custom_alert_rules_with_options(
        self,
        request: arms20190808_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportCustomAlertRulesResponse().from_map(
            self.do_rpcrequest('ImportCustomAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_custom_alert_rules_with_options_async(
        self,
        request: arms20190808_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportCustomAlertRulesResponse().from_map(
            await self.do_rpcrequest_async('ImportCustomAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_custom_alert_rules(
        self,
        request: arms20190808_models.ImportCustomAlertRulesRequest,
    ) -> arms20190808_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_custom_alert_rules_with_options(request, runtime)

    async def import_custom_alert_rules_async(
        self,
        request: arms20190808_models.ImportCustomAlertRulesRequest,
    ) -> arms20190808_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_custom_alert_rules_with_options_async(request, runtime)

    def import_prometheus_rules_with_options(
        self,
        request: arms20190808_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportPrometheusRulesResponse().from_map(
            self.do_rpcrequest('ImportPrometheusRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_prometheus_rules_with_options_async(
        self,
        request: arms20190808_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ImportPrometheusRulesResponse().from_map(
            await self.do_rpcrequest_async('ImportPrometheusRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_prometheus_rules(
        self,
        request: arms20190808_models.ImportPrometheusRulesRequest,
    ) -> arms20190808_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_prometheus_rules_with_options(request, runtime)

    async def import_prometheus_rules_async(
        self,
        request: arms20190808_models.ImportPrometheusRulesRequest,
    ) -> arms20190808_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_prometheus_rules_with_options_async(request, runtime)

    def list_cluster_from_grafana_with_options(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListClusterFromGrafanaResponse().from_map(
            self.do_rpcrequest('ListClusterFromGrafana', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_from_grafana_with_options_async(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListClusterFromGrafanaResponse().from_map(
            await self.do_rpcrequest_async('ListClusterFromGrafana', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_from_grafana(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    async def list_cluster_from_grafana_async(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_from_grafana_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: arms20190808_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListDashboardsResponse().from_map(
            self.do_rpcrequest('ListDashboards', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dashboards_with_options_async(
        self,
        request: arms20190808_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListDashboardsResponse().from_map(
            await self.do_rpcrequest_async('ListDashboards', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dashboards(
        self,
        request: arms20190808_models.ListDashboardsRequest,
    ) -> arms20190808_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: arms20190808_models.ListDashboardsRequest,
    ) -> arms20190808_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_prom_clusters_with_options(
        self,
        request: arms20190808_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListPromClustersResponse().from_map(
            self.do_rpcrequest('ListPromClusters', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_prom_clusters_with_options_async(
        self,
        request: arms20190808_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListPromClustersResponse().from_map(
            await self.do_rpcrequest_async('ListPromClusters', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_prom_clusters(
        self,
        request: arms20190808_models.ListPromClustersRequest,
    ) -> arms20190808_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prom_clusters_with_options(request, runtime)

    async def list_prom_clusters_async(
        self,
        request: arms20190808_models.ListPromClustersRequest,
    ) -> arms20190808_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prom_clusters_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListRetcodeAppsResponse().from_map(
            self.do_rpcrequest('ListRetcodeApps', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_retcode_apps_with_options_async(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListRetcodeAppsResponse().from_map(
            await self.do_rpcrequest_async('ListRetcodeApps', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_retcode_apps(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_retcode_apps_with_options_async(request, runtime)

    def list_scenario_with_options(
        self,
        request: arms20190808_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListScenarioResponse().from_map(
            self.do_rpcrequest('ListScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenario_with_options_async(
        self,
        request: arms20190808_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListScenarioResponse().from_map(
            await self.do_rpcrequest_async('ListScenario', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenario(
        self,
        request: arms20190808_models.ListScenarioRequest,
    ) -> arms20190808_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    async def list_scenario_async(
        self,
        request: arms20190808_models.ListScenarioRequest,
    ) -> arms20190808_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListTraceAppsResponse().from_map(
            self.do_rpcrequest('ListTraceApps', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_trace_apps_with_options_async(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.ListTraceAppsResponse().from_map(
            await self.do_rpcrequest_async('ListTraceApps', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trace_apps(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
    ) -> arms20190808_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    async def list_trace_apps_async(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
    ) -> arms20190808_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trace_apps_with_options_async(request, runtime)

    def open_arms_service_with_options(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.OpenArmsServiceResponse().from_map(
            self.do_rpcrequest('OpenArmsService', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_arms_service_with_options_async(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.OpenArmsServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenArmsService', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_arms_service(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

    async def open_arms_service_async(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_with_options_async(request, runtime)

    def query_dataset_with_options(
        self,
        request: arms20190808_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryDatasetResponse().from_map(
            self.do_rpcrequest('QueryDataset', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dataset_with_options_async(
        self,
        request: arms20190808_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryDatasetResponse().from_map(
            await self.do_rpcrequest_async('QueryDataset', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dataset(
        self,
        request: arms20190808_models.QueryDatasetRequest,
    ) -> arms20190808_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    async def query_dataset_async(
        self,
        request: arms20190808_models.QueryDatasetRequest,
    ) -> arms20190808_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: arms20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryMetricResponse().from_map(
            self.do_rpcrequest('QueryMetric', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: arms20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryMetricResponse().from_map(
            await self.do_rpcrequest_async('QueryMetric', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_metric(
        self,
        request: arms20190808_models.QueryMetricRequest,
    ) -> arms20190808_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: arms20190808_models.QueryMetricRequest,
    ) -> arms20190808_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def query_metric_by_page_with_options(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryMetricByPageResponse().from_map(
            self.do_rpcrequest('QueryMetricByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_metric_by_page_with_options_async(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.QueryMetricByPageResponse().from_map(
            await self.do_rpcrequest_async('QueryMetricByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_metric_by_page(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    async def query_metric_by_page_async(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_by_page_with_options_async(request, runtime)

    def save_trace_app_config_with_options(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SaveTraceAppConfigResponse().from_map(
            self.do_rpcrequest('SaveTraceAppConfig', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_trace_app_config_with_options_async(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SaveTraceAppConfigResponse().from_map(
            await self.do_rpcrequest_async('SaveTraceAppConfig', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_trace_app_config(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    async def save_trace_app_config_async(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_trace_app_config_with_options_async(request, runtime)

    def search_alert_contact_with_options(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertContactResponse().from_map(
            self.do_rpcrequest('SearchAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_contact_with_options_async(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertContactResponse().from_map(
            await self.do_rpcrequest_async('SearchAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_contact(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
    ) -> arms20190808_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
    ) -> arms20190808_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertContactGroupResponse().from_map(
            self.do_rpcrequest('SearchAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertContactGroupResponse().from_map(
            await self.do_rpcrequest_async('SearchAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_contact_group(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertHistoriesResponse().from_map(
            self.do_rpcrequest('SearchAlertHistories', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_histories_with_options_async(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertHistoriesResponse().from_map(
            await self.do_rpcrequest_async('SearchAlertHistories', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_histories(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertRulesResponse().from_map(
            self.do_rpcrequest('SearchAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_rules_with_options_async(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchAlertRulesResponse().from_map(
            await self.do_rpcrequest_async('SearchAlertRules', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_rules(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: arms20190808_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchEventsResponse().from_map(
            self.do_rpcrequest('SearchEvents', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_events_with_options_async(
        self,
        request: arms20190808_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchEventsResponse().from_map(
            await self.do_rpcrequest_async('SearchEvents', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_events(
        self,
        request: arms20190808_models.SearchEventsRequest,
    ) -> arms20190808_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: arms20190808_models.SearchEventsRequest,
    ) -> arms20190808_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_events_with_options_async(request, runtime)

    def search_retcode_app_by_page_with_options(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchRetcodeAppByPageResponse().from_map(
            self.do_rpcrequest('SearchRetcodeAppByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_retcode_app_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchRetcodeAppByPageResponse().from_map(
            await self.do_rpcrequest_async('SearchRetcodeAppByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_retcode_app_by_page(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    async def search_retcode_app_by_page_async(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_retcode_app_by_page_with_options_async(request, runtime)

    def search_trace_app_by_name_with_options(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTraceAppByNameResponse().from_map(
            self.do_rpcrequest('SearchTraceAppByName', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_trace_app_by_name_with_options_async(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTraceAppByNameResponse().from_map(
            await self.do_rpcrequest_async('SearchTraceAppByName', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_trace_app_by_name(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    async def search_trace_app_by_name_async(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_name_with_options_async(request, runtime)

    def search_trace_app_by_page_with_options(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTraceAppByPageResponse().from_map(
            self.do_rpcrequest('SearchTraceAppByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_trace_app_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTraceAppByPageResponse().from_map(
            await self.do_rpcrequest_async('SearchTraceAppByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_trace_app_by_page(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    async def search_trace_app_by_page_async(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_page_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: arms20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTracesResponse().from_map(
            self.do_rpcrequest('SearchTraces', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: arms20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTracesResponse().from_map(
            await self.do_rpcrequest_async('SearchTraces', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_traces(
        self,
        request: arms20190808_models.SearchTracesRequest,
    ) -> arms20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: arms20190808_models.SearchTracesRequest,
    ) -> arms20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)

    def search_traces_by_page_with_options(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTracesByPageResponse().from_map(
            self.do_rpcrequest('SearchTracesByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SearchTracesByPageResponse().from_map(
            await self.do_rpcrequest_async('SearchTracesByPage', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_traces_by_page(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    async def search_traces_by_page_async(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_by_page_with_options_async(request, runtime)

    def send_custom_incidents_with_options(
        self,
        request: arms20190808_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SendCustomIncidentsResponse().from_map(
            self.do_rpcrequest('SendCustomIncidents', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_custom_incidents_with_options_async(
        self,
        request: arms20190808_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SendCustomIncidentsResponse().from_map(
            await self.do_rpcrequest_async('SendCustomIncidents', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_incidents(
        self,
        request: arms20190808_models.SendCustomIncidentsRequest,
    ) -> arms20190808_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_incidents_with_options(request, runtime)

    async def send_custom_incidents_async(
        self,
        request: arms20190808_models.SendCustomIncidentsRequest,
    ) -> arms20190808_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_incidents_with_options_async(request, runtime)

    def send_mse_incident_with_options(
        self,
        request: arms20190808_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SendMseIncidentResponse().from_map(
            self.do_rpcrequest('SendMseIncident', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_mse_incident_with_options_async(
        self,
        request: arms20190808_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SendMseIncidentResponse().from_map(
            await self.do_rpcrequest_async('SendMseIncident', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_mse_incident(
        self,
        request: arms20190808_models.SendMseIncidentRequest,
    ) -> arms20190808_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_mse_incident_with_options(request, runtime)

    async def send_mse_incident_async(
        self,
        request: arms20190808_models.SendMseIncidentRequest,
    ) -> arms20190808_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_mse_incident_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SetRetcodeShareStatusResponse().from_map(
            self.do_rpcrequest('SetRetcodeShareStatus', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_retcode_share_status_with_options_async(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.SetRetcodeShareStatusResponse().from_map(
            await self.do_rpcrequest_async('SetRetcodeShareStatus', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_retcode_share_status(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    async def set_retcode_share_status_async(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_retcode_share_status_with_options_async(request, runtime)

    def start_alert_with_options(
        self,
        request: arms20190808_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.StartAlertResponse().from_map(
            self.do_rpcrequest('StartAlert', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        request: arms20190808_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.StartAlertResponse().from_map(
            await self.do_rpcrequest_async('StartAlert', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_alert(
        self,
        request: arms20190808_models.StartAlertRequest,
    ) -> arms20190808_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    async def start_alert_async(
        self,
        request: arms20190808_models.StartAlertRequest,
    ) -> arms20190808_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_alert_with_options_async(request, runtime)

    def stop_alert_with_options(
        self,
        request: arms20190808_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.StopAlertResponse().from_map(
            self.do_rpcrequest('StopAlert', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        request: arms20190808_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.StopAlertResponse().from_map(
            await self.do_rpcrequest_async('StopAlert', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_alert(
        self,
        request: arms20190808_models.StopAlertRequest,
    ) -> arms20190808_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    async def stop_alert_async(
        self,
        request: arms20190808_models.StopAlertRequest,
    ) -> arms20190808_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_alert_with_options_async(request, runtime)

    def update_alert_contact_with_options(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertContactResponse().from_map(
            self.do_rpcrequest('UpdateAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_contact_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertContactResponse().from_map(
            await self.do_rpcrequest_async('UpdateAlertContact', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_contact(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_with_options_async(request, runtime)

    def update_alert_contact_group_with_options(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertContactGroupResponse().from_map(
            self.do_rpcrequest('UpdateAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertContactGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateAlertContactGroup', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_contact_group(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    async def update_alert_contact_group_async(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_group_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertRuleResponse().from_map(
            self.do_rpcrequest('UpdateAlertRule', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateAlertRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateAlertRule', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_rule(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateWebhookResponse().from_map(
            self.do_rpcrequest('UpdateWebhook', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return arms20190808_models.UpdateWebhookResponse().from_map(
            await self.do_rpcrequest_async('UpdateWebhook', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_webhook(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
    ) -> arms20190808_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
    ) -> arms20190808_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)
