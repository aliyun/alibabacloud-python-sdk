# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ahas_openapi20190901 import models as ahas_openapi_20190901_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'ahas.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'ahas.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'ahas.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'ahas.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'ahas.cn-shenzhen.aliyuncs.com',
            'ap-southeast-1': 'ahas.ap-southeast-1.aliyuncs.com',
            'cn-hongkong': 'ahas.cn-hongkong.aliyuncs.com',
            'eu-central-1': 'ahas.eu-central-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ahas-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_application_emp_id_relation_with_options(
        self,
        request: ahas_openapi_20190901_models.AddApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse().from_map(
            self.do_rpcrequest('AddApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_application_emp_id_relation_with_options_async(
        self,
        request: ahas_openapi_20190901_models.AddApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse().from_map(
            await self.do_rpcrequest_async('AddApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_application_emp_id_relation(
        self,
        request: ahas_openapi_20190901_models.AddApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_application_emp_id_relation_with_options(request, runtime)

    async def add_application_emp_id_relation_async(
        self,
        request: ahas_openapi_20190901_models.AddApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.AddApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_application_emp_id_relation_with_options_async(request, runtime)

    def check_experiment_permission_for_mk_with_options(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentPermissionForMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse().from_map(
            self.do_rpcrequest('CheckExperimentPermissionForMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_experiment_permission_for_mk_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentPermissionForMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse().from_map(
            await self.do_rpcrequest_async('CheckExperimentPermissionForMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_experiment_permission_for_mk(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentPermissionForMkRequest,
    ) -> ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_experiment_permission_for_mk_with_options(request, runtime)

    async def check_experiment_permission_for_mk_async(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentPermissionForMkRequest,
    ) -> ahas_openapi_20190901_models.CheckExperimentPermissionForMkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_experiment_permission_for_mk_with_options_async(request, runtime)

    def check_experiment_runnable_with_options(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentRunnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CheckExperimentRunnableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CheckExperimentRunnableResponse().from_map(
            self.do_rpcrequest('CheckExperimentRunnable', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_experiment_runnable_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentRunnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CheckExperimentRunnableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CheckExperimentRunnableResponse().from_map(
            await self.do_rpcrequest_async('CheckExperimentRunnable', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_experiment_runnable(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentRunnableRequest,
    ) -> ahas_openapi_20190901_models.CheckExperimentRunnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_experiment_runnable_with_options(request, runtime)

    async def check_experiment_runnable_async(
        self,
        request: ahas_openapi_20190901_models.CheckExperimentRunnableRequest,
    ) -> ahas_openapi_20190901_models.CheckExperimentRunnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_experiment_runnable_with_options_async(request, runtime)

    def create_degrade_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateDegradeRuleResponse().from_map(
            self.do_rpcrequest('CreateDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_degrade_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateDegradeRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_degrade_rule(
        self,
        request: ahas_openapi_20190901_models.CreateDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_degrade_rule_with_options(request, runtime)

    async def create_degrade_rule_async(
        self,
        request: ahas_openapi_20190901_models.CreateDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_degrade_rule_with_options_async(request, runtime)

    def create_experiment_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateExperimentResponse().from_map(
            self.do_rpcrequest('CreateExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateExperimentResponse().from_map(
            await self.do_rpcrequest_async('CreateExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_experiment(
        self,
        request: ahas_openapi_20190901_models.CreateExperimentRequest,
    ) -> ahas_openapi_20190901_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_experiment_with_options(request, runtime)

    async def create_experiment_async(
        self,
        request: ahas_openapi_20190901_models.CreateExperimentRequest,
    ) -> ahas_openapi_20190901_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_experiment_with_options_async(request, runtime)

    def create_flow_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateFlowRuleResponse().from_map(
            self.do_rpcrequest('CreateFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateFlowRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_rule(
        self,
        request: ahas_openapi_20190901_models.CreateFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_rule_with_options(request, runtime)

    async def create_flow_rule_async(
        self,
        request: ahas_openapi_20190901_models.CreateFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_rule_with_options_async(request, runtime)

    def create_hot_param_items_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateHotParamItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateHotParamItemsResponse().from_map(
            self.do_rpcrequest('CreateHotParamItems', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_hot_param_items_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateHotParamItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateHotParamItemsResponse().from_map(
            await self.do_rpcrequest_async('CreateHotParamItems', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_hot_param_items(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamItemsRequest,
    ) -> ahas_openapi_20190901_models.CreateHotParamItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hot_param_items_with_options(request, runtime)

    async def create_hot_param_items_async(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamItemsRequest,
    ) -> ahas_openapi_20190901_models.CreateHotParamItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hot_param_items_with_options_async(request, runtime)

    def create_hot_param_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateHotParamRuleResponse().from_map(
            self.do_rpcrequest('CreateHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_hot_param_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateHotParamRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_hot_param_rule(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hot_param_rule_with_options(request, runtime)

    async def create_hot_param_rule_async(
        self,
        request: ahas_openapi_20190901_models.CreateHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hot_param_rule_with_options_async(request, runtime)

    def create_isolation_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateIsolationRuleResponse().from_map(
            self.do_rpcrequest('CreateIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_isolation_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateIsolationRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_isolation_rule(
        self,
        request: ahas_openapi_20190901_models.CreateIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_isolation_rule_with_options(request, runtime)

    async def create_isolation_rule_async(
        self,
        request: ahas_openapi_20190901_models.CreateIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_isolation_rule_with_options_async(request, runtime)

    def create_system_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.CreateSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateSystemRuleResponse().from_map(
            self.do_rpcrequest('CreateSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_system_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.CreateSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.CreateSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.CreateSystemRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_system_rule(
        self,
        request: ahas_openapi_20190901_models.CreateSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_system_rule_with_options(request, runtime)

    async def create_system_rule_async(
        self,
        request: ahas_openapi_20190901_models.CreateSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.CreateSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_system_rule_with_options_async(request, runtime)

    def delete_application_emp_id_relation_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse().from_map(
            self.do_rpcrequest('DeleteApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_application_emp_id_relation_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse().from_map(
            await self.do_rpcrequest_async('DeleteApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_application_emp_id_relation(
        self,
        request: ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_emp_id_relation_with_options(request, runtime)

    async def delete_application_emp_id_relation_async(
        self,
        request: ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.DeleteApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_emp_id_relation_with_options_async(request, runtime)

    def delete_degrade_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteDegradeRuleResponse().from_map(
            self.do_rpcrequest('DeleteDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_degrade_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteDegradeRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_degrade_rule(
        self,
        request: ahas_openapi_20190901_models.DeleteDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_degrade_rule_with_options(request, runtime)

    async def delete_degrade_rule_async(
        self,
        request: ahas_openapi_20190901_models.DeleteDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_degrade_rule_with_options_async(request, runtime)

    def delete_flow_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteFlowRuleResponse().from_map(
            self.do_rpcrequest('DeleteFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteFlowRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_rule(
        self,
        request: ahas_openapi_20190901_models.DeleteFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_rule_with_options(request, runtime)

    async def delete_flow_rule_async(
        self,
        request: ahas_openapi_20190901_models.DeleteFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_rule_with_options_async(request, runtime)

    def delete_hot_param_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteHotParamRuleResponse().from_map(
            self.do_rpcrequest('DeleteHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_hot_param_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteHotParamRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_hot_param_rule(
        self,
        request: ahas_openapi_20190901_models.DeleteHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_hot_param_rule_with_options(request, runtime)

    async def delete_hot_param_rule_async(
        self,
        request: ahas_openapi_20190901_models.DeleteHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_hot_param_rule_with_options_async(request, runtime)

    def delete_isolation_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteIsolationRuleResponse().from_map(
            self.do_rpcrequest('DeleteIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_isolation_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteIsolationRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_isolation_rule(
        self,
        request: ahas_openapi_20190901_models.DeleteIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_isolation_rule_with_options(request, runtime)

    async def delete_isolation_rule_async(
        self,
        request: ahas_openapi_20190901_models.DeleteIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_isolation_rule_with_options_async(request, runtime)

    def delete_system_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DeleteSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteSystemRuleResponse().from_map(
            self.do_rpcrequest('DeleteSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_system_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DeleteSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DeleteSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DeleteSystemRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_system_rule(
        self,
        request: ahas_openapi_20190901_models.DeleteSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_system_rule_with_options(request, runtime)

    async def delete_system_rule_async(
        self,
        request: ahas_openapi_20190901_models.DeleteSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.DeleteSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_system_rule_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ahas_openapi_20190901_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ahas_openapi_20190901_models.DescribeRegionsRequest,
    ) -> ahas_openapi_20190901_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ahas_openapi_20190901_models.DescribeRegionsRequest,
    ) -> ahas_openapi_20190901_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def disable_degrade_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DisableDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableDegradeRuleResponse().from_map(
            self.do_rpcrequest('DisableDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_degrade_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DisableDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableDegradeRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_degrade_rule(
        self,
        request: ahas_openapi_20190901_models.DisableDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_degrade_rule_with_options(request, runtime)

    async def disable_degrade_rule_async(
        self,
        request: ahas_openapi_20190901_models.DisableDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_degrade_rule_with_options_async(request, runtime)

    def disable_flow_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DisableFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableFlowRuleResponse().from_map(
            self.do_rpcrequest('DisableFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_flow_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DisableFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableFlowRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_flow_rule(
        self,
        request: ahas_openapi_20190901_models.DisableFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_flow_rule_with_options(request, runtime)

    async def disable_flow_rule_async(
        self,
        request: ahas_openapi_20190901_models.DisableFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_flow_rule_with_options_async(request, runtime)

    def disable_hot_param_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DisableHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableHotParamRuleResponse().from_map(
            self.do_rpcrequest('DisableHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_hot_param_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DisableHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableHotParamRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_hot_param_rule(
        self,
        request: ahas_openapi_20190901_models.DisableHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_hot_param_rule_with_options(request, runtime)

    async def disable_hot_param_rule_async(
        self,
        request: ahas_openapi_20190901_models.DisableHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_hot_param_rule_with_options_async(request, runtime)

    def disable_isolation_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DisableIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableIsolationRuleResponse().from_map(
            self.do_rpcrequest('DisableIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_isolation_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DisableIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableIsolationRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_isolation_rule(
        self,
        request: ahas_openapi_20190901_models.DisableIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_isolation_rule_with_options(request, runtime)

    async def disable_isolation_rule_async(
        self,
        request: ahas_openapi_20190901_models.DisableIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_isolation_rule_with_options_async(request, runtime)

    def disable_system_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.DisableSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableSystemRuleResponse().from_map(
            self.do_rpcrequest('DisableSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_system_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.DisableSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.DisableSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.DisableSystemRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_system_rule(
        self,
        request: ahas_openapi_20190901_models.DisableSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_system_rule_with_options(request, runtime)

    async def disable_system_rule_async(
        self,
        request: ahas_openapi_20190901_models.DisableSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.DisableSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_system_rule_with_options_async(request, runtime)

    def enable_degrade_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.EnableDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableDegradeRuleResponse().from_map(
            self.do_rpcrequest('EnableDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_degrade_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.EnableDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableDegradeRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_degrade_rule(
        self,
        request: ahas_openapi_20190901_models.EnableDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_degrade_rule_with_options(request, runtime)

    async def enable_degrade_rule_async(
        self,
        request: ahas_openapi_20190901_models.EnableDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_degrade_rule_with_options_async(request, runtime)

    def enable_flow_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.EnableFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableFlowRuleResponse().from_map(
            self.do_rpcrequest('EnableFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_flow_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.EnableFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableFlowRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_flow_rule(
        self,
        request: ahas_openapi_20190901_models.EnableFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_flow_rule_with_options(request, runtime)

    async def enable_flow_rule_async(
        self,
        request: ahas_openapi_20190901_models.EnableFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_flow_rule_with_options_async(request, runtime)

    def enable_hot_param_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.EnableHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableHotParamRuleResponse().from_map(
            self.do_rpcrequest('EnableHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_hot_param_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.EnableHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableHotParamRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_hot_param_rule(
        self,
        request: ahas_openapi_20190901_models.EnableHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_hot_param_rule_with_options(request, runtime)

    async def enable_hot_param_rule_async(
        self,
        request: ahas_openapi_20190901_models.EnableHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_hot_param_rule_with_options_async(request, runtime)

    def enable_isolation_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.EnableIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableIsolationRuleResponse().from_map(
            self.do_rpcrequest('EnableIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_isolation_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.EnableIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableIsolationRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_isolation_rule(
        self,
        request: ahas_openapi_20190901_models.EnableIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_isolation_rule_with_options(request, runtime)

    async def enable_isolation_rule_async(
        self,
        request: ahas_openapi_20190901_models.EnableIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_isolation_rule_with_options_async(request, runtime)

    def enable_system_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.EnableSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableSystemRuleResponse().from_map(
            self.do_rpcrequest('EnableSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_system_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.EnableSystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.EnableSystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.EnableSystemRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableSystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_system_rule(
        self,
        request: ahas_openapi_20190901_models.EnableSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_system_rule_with_options(request, runtime)

    async def enable_system_rule_async(
        self,
        request: ahas_openapi_20190901_models.EnableSystemRuleRequest,
    ) -> ahas_openapi_20190901_models.EnableSystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_system_rule_with_options_async(request, runtime)

    def execute_experiment_with_options(
        self,
        request: ahas_openapi_20190901_models.ExecuteExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ExecuteExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ExecuteExperimentResponse().from_map(
            self.do_rpcrequest('ExecuteExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_experiment_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ExecuteExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ExecuteExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ExecuteExperimentResponse().from_map(
            await self.do_rpcrequest_async('ExecuteExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_experiment(
        self,
        request: ahas_openapi_20190901_models.ExecuteExperimentRequest,
    ) -> ahas_openapi_20190901_models.ExecuteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_experiment_with_options(request, runtime)

    async def execute_experiment_async(
        self,
        request: ahas_openapi_20190901_models.ExecuteExperimentRequest,
    ) -> ahas_openapi_20190901_models.ExecuteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_experiment_with_options_async(request, runtime)

    def finish_experiment_task_with_options(
        self,
        request: ahas_openapi_20190901_models.FinishExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.FinishExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.FinishExperimentTaskResponse().from_map(
            self.do_rpcrequest('FinishExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def finish_experiment_task_with_options_async(
        self,
        request: ahas_openapi_20190901_models.FinishExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.FinishExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.FinishExperimentTaskResponse().from_map(
            await self.do_rpcrequest_async('FinishExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def finish_experiment_task(
        self,
        request: ahas_openapi_20190901_models.FinishExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.FinishExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.finish_experiment_task_with_options(request, runtime)

    async def finish_experiment_task_async(
        self,
        request: ahas_openapi_20190901_models.FinishExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.FinishExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.finish_experiment_task_with_options_async(request, runtime)

    def get_activity_task_with_options(
        self,
        request: ahas_openapi_20190901_models.GetActivityTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetActivityTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetActivityTaskResponse().from_map(
            self.do_rpcrequest('GetActivityTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_activity_task_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetActivityTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetActivityTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetActivityTaskResponse().from_map(
            await self.do_rpcrequest_async('GetActivityTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_activity_task(
        self,
        request: ahas_openapi_20190901_models.GetActivityTaskRequest,
    ) -> ahas_openapi_20190901_models.GetActivityTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_activity_task_with_options(request, runtime)

    async def get_activity_task_async(
        self,
        request: ahas_openapi_20190901_models.GetActivityTaskRequest,
    ) -> ahas_openapi_20190901_models.GetActivityTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_activity_task_with_options_async(request, runtime)

    def get_application_emp_id_relation_with_options(
        self,
        request: ahas_openapi_20190901_models.GetApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse().from_map(
            self.do_rpcrequest('GetApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_application_emp_id_relation_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetApplicationEmpIdRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse().from_map(
            await self.do_rpcrequest_async('GetApplicationEmpIdRelation', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_application_emp_id_relation(
        self,
        request: ahas_openapi_20190901_models.GetApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_emp_id_relation_with_options(request, runtime)

    async def get_application_emp_id_relation_async(
        self,
        request: ahas_openapi_20190901_models.GetApplicationEmpIdRelationRequest,
    ) -> ahas_openapi_20190901_models.GetApplicationEmpIdRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_emp_id_relation_with_options_async(request, runtime)

    def get_experiment_meta_with_options(
        self,
        request: ahas_openapi_20190901_models.GetExperimentMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetExperimentMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetExperimentMetaResponse().from_map(
            self.do_rpcrequest('GetExperimentMeta', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_experiment_meta_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetExperimentMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetExperimentMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetExperimentMetaResponse().from_map(
            await self.do_rpcrequest_async('GetExperimentMeta', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_experiment_meta(
        self,
        request: ahas_openapi_20190901_models.GetExperimentMetaRequest,
    ) -> ahas_openapi_20190901_models.GetExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_meta_with_options(request, runtime)

    async def get_experiment_meta_async(
        self,
        request: ahas_openapi_20190901_models.GetExperimentMetaRequest,
    ) -> ahas_openapi_20190901_models.GetExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_meta_with_options_async(request, runtime)

    def get_experiment_task_with_options(
        self,
        request: ahas_openapi_20190901_models.GetExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetExperimentTaskResponse().from_map(
            self.do_rpcrequest('GetExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_experiment_task_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetExperimentTaskResponse().from_map(
            await self.do_rpcrequest_async('GetExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_experiment_task(
        self,
        request: ahas_openapi_20190901_models.GetExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.GetExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_task_with_options(request, runtime)

    async def get_experiment_task_async(
        self,
        request: ahas_openapi_20190901_models.GetExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.GetExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_task_with_options_async(request, runtime)

    def get_hit_count_with_options(
        self,
        request: ahas_openapi_20190901_models.GetHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetHitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetHitCountResponse().from_map(
            self.do_rpcrequest('GetHitCount', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hit_count_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetHitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetHitCountResponse().from_map(
            await self.do_rpcrequest_async('GetHitCount', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hit_count(
        self,
        request: ahas_openapi_20190901_models.GetHitCountRequest,
    ) -> ahas_openapi_20190901_models.GetHitCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hit_count_with_options(request, runtime)

    async def get_hit_count_async(
        self,
        request: ahas_openapi_20190901_models.GetHitCountRequest,
    ) -> ahas_openapi_20190901_models.GetHitCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hit_count_with_options_async(request, runtime)

    def get_license_key_with_options(
        self,
        request: ahas_openapi_20190901_models.GetLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetLicenseKeyResponse().from_map(
            self.do_rpcrequest('GetLicenseKey', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_license_key_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetLicenseKeyResponse().from_map(
            await self.do_rpcrequest_async('GetLicenseKey', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_license_key(
        self,
        request: ahas_openapi_20190901_models.GetLicenseKeyRequest,
    ) -> ahas_openapi_20190901_models.GetLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_license_key_with_options(request, runtime)

    async def get_license_key_async(
        self,
        request: ahas_openapi_20190901_models.GetLicenseKeyRequest,
    ) -> ahas_openapi_20190901_models.GetLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_license_key_with_options_async(request, runtime)

    def get_metrics_of_app_with_options(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetMetricsOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetMetricsOfAppResponse().from_map(
            self.do_rpcrequest('GetMetricsOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_metrics_of_app_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetMetricsOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetMetricsOfAppResponse().from_map(
            await self.do_rpcrequest_async('GetMetricsOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_metrics_of_app(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfAppRequest,
    ) -> ahas_openapi_20190901_models.GetMetricsOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_metrics_of_app_with_options(request, runtime)

    async def get_metrics_of_app_async(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfAppRequest,
    ) -> ahas_openapi_20190901_models.GetMetricsOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_metrics_of_app_with_options_async(request, runtime)

    def get_metrics_of_resource_with_options(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetMetricsOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetMetricsOfResourceResponse().from_map(
            self.do_rpcrequest('GetMetricsOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_metrics_of_resource_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetMetricsOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetMetricsOfResourceResponse().from_map(
            await self.do_rpcrequest_async('GetMetricsOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_metrics_of_resource(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfResourceRequest,
    ) -> ahas_openapi_20190901_models.GetMetricsOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_metrics_of_resource_with_options(request, runtime)

    async def get_metrics_of_resource_async(
        self,
        request: ahas_openapi_20190901_models.GetMetricsOfResourceRequest,
    ) -> ahas_openapi_20190901_models.GetMetricsOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_metrics_of_resource_with_options_async(request, runtime)

    def get_sentinel_app_sum_metric_with_options(
        self,
        request: ahas_openapi_20190901_models.GetSentinelAppSumMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse().from_map(
            self.do_rpcrequest('GetSentinelAppSumMetric', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sentinel_app_sum_metric_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetSentinelAppSumMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse().from_map(
            await self.do_rpcrequest_async('GetSentinelAppSumMetric', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sentinel_app_sum_metric(
        self,
        request: ahas_openapi_20190901_models.GetSentinelAppSumMetricRequest,
    ) -> ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sentinel_app_sum_metric_with_options(request, runtime)

    async def get_sentinel_app_sum_metric_async(
        self,
        request: ahas_openapi_20190901_models.GetSentinelAppSumMetricRequest,
    ) -> ahas_openapi_20190901_models.GetSentinelAppSumMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sentinel_app_sum_metric_with_options_async(request, runtime)

    def get_user_applications_with_options(
        self,
        request: ahas_openapi_20190901_models.GetUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetUserApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetUserApplicationsResponse().from_map(
            self.do_rpcrequest('GetUserApplications', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_applications_with_options_async(
        self,
        request: ahas_openapi_20190901_models.GetUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.GetUserApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.GetUserApplicationsResponse().from_map(
            await self.do_rpcrequest_async('GetUserApplications', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_applications(
        self,
        request: ahas_openapi_20190901_models.GetUserApplicationsRequest,
    ) -> ahas_openapi_20190901_models.GetUserApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_applications_with_options(request, runtime)

    async def get_user_applications_async(
        self,
        request: ahas_openapi_20190901_models.GetUserApplicationsRequest,
    ) -> ahas_openapi_20190901_models.GetUserApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_applications_with_options_async(request, runtime)

    def import_experiment_from_mk_with_options(
        self,
        request: ahas_openapi_20190901_models.ImportExperimentFromMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ImportExperimentFromMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ImportExperimentFromMkResponse().from_map(
            self.do_rpcrequest('ImportExperimentFromMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_experiment_from_mk_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ImportExperimentFromMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ImportExperimentFromMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ImportExperimentFromMkResponse().from_map(
            await self.do_rpcrequest_async('ImportExperimentFromMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_experiment_from_mk(
        self,
        request: ahas_openapi_20190901_models.ImportExperimentFromMkRequest,
    ) -> ahas_openapi_20190901_models.ImportExperimentFromMkResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_experiment_from_mk_with_options(request, runtime)

    async def import_experiment_from_mk_async(
        self,
        request: ahas_openapi_20190901_models.ImportExperimentFromMkRequest,
    ) -> ahas_openapi_20190901_models.ImportExperimentFromMkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_experiment_from_mk_with_options_async(request, runtime)

    def list_active_apps_with_options(
        self,
        request: ahas_openapi_20190901_models.ListActiveAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListActiveAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListActiveAppsResponse().from_map(
            self.do_rpcrequest('ListActiveApps', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_active_apps_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListActiveAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListActiveAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListActiveAppsResponse().from_map(
            await self.do_rpcrequest_async('ListActiveApps', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_active_apps(
        self,
        request: ahas_openapi_20190901_models.ListActiveAppsRequest,
    ) -> ahas_openapi_20190901_models.ListActiveAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_active_apps_with_options(request, runtime)

    async def list_active_apps_async(
        self,
        request: ahas_openapi_20190901_models.ListActiveAppsRequest,
    ) -> ahas_openapi_20190901_models.ListActiveAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_active_apps_with_options_async(request, runtime)

    def list_degrade_rules_of_app_with_options(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse().from_map(
            self.do_rpcrequest('ListDegradeRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_degrade_rules_of_app_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse().from_map(
            await self.do_rpcrequest_async('ListDegradeRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_degrade_rules_of_app(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_degrade_rules_of_app_with_options(request, runtime)

    async def list_degrade_rules_of_app_async(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_degrade_rules_of_app_with_options_async(request, runtime)

    def list_degrade_rules_of_resource_with_options(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse().from_map(
            self.do_rpcrequest('ListDegradeRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_degrade_rules_of_resource_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse().from_map(
            await self.do_rpcrequest_async('ListDegradeRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_degrade_rules_of_resource(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_degrade_rules_of_resource_with_options(request, runtime)

    async def list_degrade_rules_of_resource_async(
        self,
        request: ahas_openapi_20190901_models.ListDegradeRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListDegradeRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_degrade_rules_of_resource_with_options_async(request, runtime)

    def list_experiment_metas_with_options(
        self,
        request: ahas_openapi_20190901_models.ListExperimentMetasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListExperimentMetasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListExperimentMetasResponse().from_map(
            self.do_rpcrequest('ListExperimentMetas', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_experiment_metas_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListExperimentMetasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListExperimentMetasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListExperimentMetasResponse().from_map(
            await self.do_rpcrequest_async('ListExperimentMetas', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_experiment_metas(
        self,
        request: ahas_openapi_20190901_models.ListExperimentMetasRequest,
    ) -> ahas_openapi_20190901_models.ListExperimentMetasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_experiment_metas_with_options(request, runtime)

    async def list_experiment_metas_async(
        self,
        request: ahas_openapi_20190901_models.ListExperimentMetasRequest,
    ) -> ahas_openapi_20190901_models.ListExperimentMetasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_experiment_metas_with_options_async(request, runtime)

    def list_flow_rules_of_app_with_options(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListFlowRulesOfAppResponse().from_map(
            self.do_rpcrequest('ListFlowRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_rules_of_app_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListFlowRulesOfAppResponse().from_map(
            await self.do_rpcrequest_async('ListFlowRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_rules_of_app(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_rules_of_app_with_options(request, runtime)

    async def list_flow_rules_of_app_async(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_rules_of_app_with_options_async(request, runtime)

    def list_flow_rules_of_resource_with_options(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse().from_map(
            self.do_rpcrequest('ListFlowRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_rules_of_resource_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse().from_map(
            await self.do_rpcrequest_async('ListFlowRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_rules_of_resource(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_rules_of_resource_with_options(request, runtime)

    async def list_flow_rules_of_resource_async(
        self,
        request: ahas_openapi_20190901_models.ListFlowRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListFlowRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_rules_of_resource_with_options_async(request, runtime)

    def list_hot_param_rules_of_app_with_options(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse().from_map(
            self.do_rpcrequest('ListHotParamRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hot_param_rules_of_app_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse().from_map(
            await self.do_rpcrequest_async('ListHotParamRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hot_param_rules_of_app(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hot_param_rules_of_app_with_options(request, runtime)

    async def list_hot_param_rules_of_app_async(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_param_rules_of_app_with_options_async(request, runtime)

    def list_hot_param_rules_of_resource_with_options(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse().from_map(
            self.do_rpcrequest('ListHotParamRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hot_param_rules_of_resource_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse().from_map(
            await self.do_rpcrequest_async('ListHotParamRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hot_param_rules_of_resource(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hot_param_rules_of_resource_with_options(request, runtime)

    async def list_hot_param_rules_of_resource_async(
        self,
        request: ahas_openapi_20190901_models.ListHotParamRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListHotParamRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_param_rules_of_resource_with_options_async(request, runtime)

    def list_isolation_rules_of_app_with_options(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse().from_map(
            self.do_rpcrequest('ListIsolationRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_isolation_rules_of_app_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse().from_map(
            await self.do_rpcrequest_async('ListIsolationRulesOfApp', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_isolation_rules_of_app(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_isolation_rules_of_app_with_options(request, runtime)

    async def list_isolation_rules_of_app_async(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfAppRequest,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_isolation_rules_of_app_with_options_async(request, runtime)

    def list_isolation_rules_of_resource_with_options(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse().from_map(
            self.do_rpcrequest('ListIsolationRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_isolation_rules_of_resource_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse().from_map(
            await self.do_rpcrequest_async('ListIsolationRulesOfResource', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_isolation_rules_of_resource(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_isolation_rules_of_resource_with_options(request, runtime)

    async def list_isolation_rules_of_resource_async(
        self,
        request: ahas_openapi_20190901_models.ListIsolationRulesOfResourceRequest,
    ) -> ahas_openapi_20190901_models.ListIsolationRulesOfResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_isolation_rules_of_resource_with_options_async(request, runtime)

    def list_system_rules_with_options(
        self,
        request: ahas_openapi_20190901_models.ListSystemRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListSystemRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListSystemRulesResponse().from_map(
            self.do_rpcrequest('ListSystemRules', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_system_rules_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ListSystemRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ListSystemRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ListSystemRulesResponse().from_map(
            await self.do_rpcrequest_async('ListSystemRules', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_rules(
        self,
        request: ahas_openapi_20190901_models.ListSystemRulesRequest,
    ) -> ahas_openapi_20190901_models.ListSystemRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_rules_with_options(request, runtime)

    async def list_system_rules_async(
        self,
        request: ahas_openapi_20190901_models.ListSystemRulesRequest,
    ) -> ahas_openapi_20190901_models.ListSystemRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_rules_with_options_async(request, runtime)

    def modify_degrade_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.ModifyDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyDegradeRuleResponse().from_map(
            self.do_rpcrequest('ModifyDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_degrade_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ModifyDegradeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyDegradeRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyDegradeRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyDegradeRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_degrade_rule(
        self,
        request: ahas_openapi_20190901_models.ModifyDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_degrade_rule_with_options(request, runtime)

    async def modify_degrade_rule_async(
        self,
        request: ahas_openapi_20190901_models.ModifyDegradeRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyDegradeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_degrade_rule_with_options_async(request, runtime)

    def modify_flow_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.ModifyFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyFlowRuleResponse().from_map(
            self.do_rpcrequest('ModifyFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ModifyFlowRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyFlowRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyFlowRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_rule(
        self,
        request: ahas_openapi_20190901_models.ModifyFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_rule_with_options(request, runtime)

    async def modify_flow_rule_async(
        self,
        request: ahas_openapi_20190901_models.ModifyFlowRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyFlowRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_rule_with_options_async(request, runtime)

    def modify_hot_param_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.ModifyHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyHotParamRuleResponse().from_map(
            self.do_rpcrequest('ModifyHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hot_param_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ModifyHotParamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyHotParamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyHotParamRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyHotParamRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hot_param_rule(
        self,
        request: ahas_openapi_20190901_models.ModifyHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hot_param_rule_with_options(request, runtime)

    async def modify_hot_param_rule_async(
        self,
        request: ahas_openapi_20190901_models.ModifyHotParamRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyHotParamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hot_param_rule_with_options_async(request, runtime)

    def modify_isolation_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.ModifyIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyIsolationRuleResponse().from_map(
            self.do_rpcrequest('ModifyIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_isolation_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ModifyIsolationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifyIsolationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifyIsolationRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyIsolationRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_isolation_rule(
        self,
        request: ahas_openapi_20190901_models.ModifyIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_isolation_rule_with_options(request, runtime)

    async def modify_isolation_rule_async(
        self,
        request: ahas_openapi_20190901_models.ModifyIsolationRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifyIsolationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_isolation_rule_with_options_async(request, runtime)

    def modify_system_rule_with_options(
        self,
        request: ahas_openapi_20190901_models.ModifySystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifySystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifySystemRuleResponse().from_map(
            self.do_rpcrequest('ModifySystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_system_rule_with_options_async(
        self,
        request: ahas_openapi_20190901_models.ModifySystemRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.ModifySystemRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.ModifySystemRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySystemRule', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_system_rule(
        self,
        request: ahas_openapi_20190901_models.ModifySystemRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifySystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_system_rule_with_options(request, runtime)

    async def modify_system_rule_async(
        self,
        request: ahas_openapi_20190901_models.ModifySystemRuleRequest,
    ) -> ahas_openapi_20190901_models.ModifySystemRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_system_rule_with_options_async(request, runtime)

    def open_ahas_service_with_options(
        self,
        request: ahas_openapi_20190901_models.OpenAhasServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.OpenAhasServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.OpenAhasServiceResponse().from_map(
            self.do_rpcrequest('OpenAhasService', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_ahas_service_with_options_async(
        self,
        request: ahas_openapi_20190901_models.OpenAhasServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.OpenAhasServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.OpenAhasServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenAhasService', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_ahas_service(
        self,
        request: ahas_openapi_20190901_models.OpenAhasServiceRequest,
    ) -> ahas_openapi_20190901_models.OpenAhasServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_ahas_service_with_options(request, runtime)

    async def open_ahas_service_async(
        self,
        request: ahas_openapi_20190901_models.OpenAhasServiceRequest,
    ) -> ahas_openapi_20190901_models.OpenAhasServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_ahas_service_with_options_async(request, runtime)

    def push_experiment_task_with_options(
        self,
        request: ahas_openapi_20190901_models.PushExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.PushExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.PushExperimentTaskResponse().from_map(
            self.do_rpcrequest('PushExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_experiment_task_with_options_async(
        self,
        request: ahas_openapi_20190901_models.PushExperimentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.PushExperimentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.PushExperimentTaskResponse().from_map(
            await self.do_rpcrequest_async('PushExperimentTask', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_experiment_task(
        self,
        request: ahas_openapi_20190901_models.PushExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.PushExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_experiment_task_with_options(request, runtime)

    async def push_experiment_task_async(
        self,
        request: ahas_openapi_20190901_models.PushExperimentTaskRequest,
    ) -> ahas_openapi_20190901_models.PushExperimentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_experiment_task_with_options_async(request, runtime)

    def query_experiments_by_emp_id_with_options(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentsByEmpIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse().from_map(
            self.do_rpcrequest('QueryExperimentsByEmpId', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_experiments_by_emp_id_with_options_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentsByEmpIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse().from_map(
            await self.do_rpcrequest_async('QueryExperimentsByEmpId', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_experiments_by_emp_id(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentsByEmpIdRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_experiments_by_emp_id_with_options(request, runtime)

    async def query_experiments_by_emp_id_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentsByEmpIdRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentsByEmpIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_experiments_by_emp_id_with_options_async(request, runtime)

    def query_experiment_simple_info_for_mk_with_options(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse().from_map(
            self.do_rpcrequest('QueryExperimentSimpleInfoForMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_experiment_simple_info_for_mk_with_options_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse().from_map(
            await self.do_rpcrequest_async('QueryExperimentSimpleInfoForMk', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_experiment_simple_info_for_mk(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_experiment_simple_info_for_mk_with_options(request, runtime)

    async def query_experiment_simple_info_for_mk_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentSimpleInfoForMkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_experiment_simple_info_for_mk_with_options_async(request, runtime)

    def query_experiment_task_id_by_exp_id_with_options(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse().from_map(
            self.do_rpcrequest('QueryExperimentTaskIdByExpId', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_experiment_task_id_by_exp_id_with_options_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse().from_map(
            await self.do_rpcrequest_async('QueryExperimentTaskIdByExpId', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_experiment_task_id_by_exp_id(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_experiment_task_id_by_exp_id_with_options(request, runtime)

    async def query_experiment_task_id_by_exp_id_async(
        self,
        request: ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdRequest,
    ) -> ahas_openapi_20190901_models.QueryExperimentTaskIdByExpIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_experiment_task_id_by_exp_id_with_options_async(request, runtime)

    def search_application_scopes_with_options(
        self,
        request: ahas_openapi_20190901_models.SearchApplicationScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.SearchApplicationScopesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.SearchApplicationScopesResponse().from_map(
            self.do_rpcrequest('SearchApplicationScopes', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_application_scopes_with_options_async(
        self,
        request: ahas_openapi_20190901_models.SearchApplicationScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.SearchApplicationScopesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.SearchApplicationScopesResponse().from_map(
            await self.do_rpcrequest_async('SearchApplicationScopes', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_application_scopes(
        self,
        request: ahas_openapi_20190901_models.SearchApplicationScopesRequest,
    ) -> ahas_openapi_20190901_models.SearchApplicationScopesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_application_scopes_with_options(request, runtime)

    async def search_application_scopes_async(
        self,
        request: ahas_openapi_20190901_models.SearchApplicationScopesRequest,
    ) -> ahas_openapi_20190901_models.SearchApplicationScopesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_application_scopes_with_options_async(request, runtime)

    def search_user_applications_with_options(
        self,
        request: ahas_openapi_20190901_models.SearchUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.SearchUserApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.SearchUserApplicationsResponse().from_map(
            self.do_rpcrequest('SearchUserApplications', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_user_applications_with_options_async(
        self,
        request: ahas_openapi_20190901_models.SearchUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.SearchUserApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.SearchUserApplicationsResponse().from_map(
            await self.do_rpcrequest_async('SearchUserApplications', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_user_applications(
        self,
        request: ahas_openapi_20190901_models.SearchUserApplicationsRequest,
    ) -> ahas_openapi_20190901_models.SearchUserApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_user_applications_with_options(request, runtime)

    async def search_user_applications_async(
        self,
        request: ahas_openapi_20190901_models.SearchUserApplicationsRequest,
    ) -> ahas_openapi_20190901_models.SearchUserApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_user_applications_with_options_async(request, runtime)

    def update_experiment_with_options(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.UpdateExperimentResponse().from_map(
            self.do_rpcrequest('UpdateExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.UpdateExperimentResponse().from_map(
            await self.do_rpcrequest_async('UpdateExperiment', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_experiment(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentRequest,
    ) -> ahas_openapi_20190901_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_experiment_with_options(request, runtime)

    async def update_experiment_async(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentRequest,
    ) -> ahas_openapi_20190901_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_experiment_with_options_async(request, runtime)

    def update_experiment_basic_info_with_options(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse().from_map(
            self.do_rpcrequest('UpdateExperimentBasicInfo', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_experiment_basic_info_with_options_async(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse().from_map(
            await self.do_rpcrequest_async('UpdateExperimentBasicInfo', '2019-09-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_experiment_basic_info(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentBasicInfoRequest,
    ) -> ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_experiment_basic_info_with_options(request, runtime)

    async def update_experiment_basic_info_async(
        self,
        request: ahas_openapi_20190901_models.UpdateExperimentBasicInfoRequest,
    ) -> ahas_openapi_20190901_models.UpdateExperimentBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_experiment_basic_info_with_options_async(request, runtime)
