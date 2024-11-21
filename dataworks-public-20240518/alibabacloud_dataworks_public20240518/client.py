# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20240518 import models as dataworks_public_20240518_models
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
            'ap-northeast-1': 'dataworks.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'dataworks.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'dataworks.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dataworks.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dataworks.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dataworks.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dataworks.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'dataworks.cn-chengdu.aliyuncs.com',
            'cn-hangzhou': 'dataworks.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dataworks.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'dataworks.aliyuncs.com',
            'cn-qingdao': 'dataworks.aliyuncs.com',
            'cn-shanghai': 'dataworks.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'dataworks.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'dataworks.aliyuncs.com',
            'eu-central-1': 'dataworks.eu-central-1.aliyuncs.com',
            'eu-west-1': 'dataworks.eu-west-1.aliyuncs.com',
            'me-east-1': 'dataworks.me-east-1.aliyuncs.com',
            'us-east-1': 'dataworks.us-east-1.aliyuncs.com',
            'us-west-1': 'dataworks.us-west-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dataworks.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dataworks.aliyuncs.com',
            'cn-shanghai-finance-1': 'dataworks.aliyuncs.com',
            'cn-north-2-gov-1': 'dataworks.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dataworks-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_deployment_with_options(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary Terminates the process for deploying or undeploying an entity. The process is not deleted and can still be queried by calling query operations.
        
        @param request: AbolishDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbolishDeploymentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbolishDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AbolishDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_deployment_with_options_async(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary Terminates the process for deploying or undeploying an entity. The process is not deleted and can still be queried by calling query operations.
        
        @param request: AbolishDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbolishDeploymentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbolishDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AbolishDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_deployment(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary Terminates the process for deploying or undeploying an entity. The process is not deleted and can still be queried by calling query operations.
        
        @param request: AbolishDeploymentRequest
        @return: AbolishDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abolish_deployment_with_options(request, runtime)

    async def abolish_deployment_async(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary Terminates the process for deploying or undeploying an entity. The process is not deleted and can still be queried by calling query operations.
        
        @param request: AbolishDeploymentRequest
        @return: AbolishDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abolish_deployment_with_options_async(request, runtime)

    def associate_project_to_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.AssociateProjectToResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse:
        """
        @summary Associates a resource group with a workspace.
        
        @param request: AssociateProjectToResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateProjectToResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateProjectToResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_project_to_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.AssociateProjectToResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse:
        """
        @summary Associates a resource group with a workspace.
        
        @param request: AssociateProjectToResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateProjectToResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateProjectToResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_project_to_resource_group(
        self,
        request: dataworks_public_20240518_models.AssociateProjectToResourceGroupRequest,
    ) -> dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse:
        """
        @summary Associates a resource group with a workspace.
        
        @param request: AssociateProjectToResourceGroupRequest
        @return: AssociateProjectToResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_project_to_resource_group_with_options(request, runtime)

    async def associate_project_to_resource_group_async(
        self,
        request: dataworks_public_20240518_models.AssociateProjectToResourceGroupRequest,
    ) -> dataworks_public_20240518_models.AssociateProjectToResourceGroupResponse:
        """
        @summary Associates a resource group with a workspace.
        
        @param request: AssociateProjectToResourceGroupRequest
        @return: AssociateProjectToResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_project_to_resource_group_with_options_async(request, runtime)

    def clone_data_source_with_options(
        self,
        request: dataworks_public_20240518_models.CloneDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CloneDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CloneDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clone_data_source_name):
            query['CloneDataSourceName'] = request.clone_data_source_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CloneDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_data_source_with_options_async(
        self,
        request: dataworks_public_20240518_models.CloneDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CloneDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CloneDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clone_data_source_name):
            query['CloneDataSourceName'] = request.clone_data_source_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CloneDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_data_source(
        self,
        request: dataworks_public_20240518_models.CloneDataSourceRequest,
    ) -> dataworks_public_20240518_models.CloneDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CloneDataSourceRequest
        @return: CloneDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clone_data_source_with_options(request, runtime)

    async def clone_data_source_async(
        self,
        request: dataworks_public_20240518_models.CloneDataSourceRequest,
    ) -> dataworks_public_20240518_models.CloneDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CloneDataSourceRequest
        @return: CloneDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clone_data_source_with_options_async(request, runtime)

    def create_alert_rule_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param tmp_req: CreateAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlertRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateAlertRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_condition):
            request.trigger_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_rule_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param tmp_req: CreateAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlertRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateAlertRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_condition):
            request.trigger_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_rule(
        self,
        request: dataworks_public_20240518_models.CreateAlertRuleRequest,
    ) -> dataworks_public_20240518_models.CreateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param request: CreateAlertRuleRequest
        @return: CreateAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alert_rule_with_options(request, runtime)

    async def create_alert_rule_async(
        self,
        request: dataworks_public_20240518_models.CreateAlertRuleRequest,
    ) -> dataworks_public_20240518_models.CreateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param request: CreateAlertRuleRequest
        @return: CreateAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_rule_with_options_async(request, runtime)

    def create_dialarm_rule_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDIAlarmRuleResponse:
        """
        @summary 创建数据集成报警规则
        
        @param tmp_req: CreateDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialarm_rule_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDIAlarmRuleResponse:
        """
        @summary 创建数据集成报警规则
        
        @param tmp_req: CreateDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialarm_rule(
        self,
        request: dataworks_public_20240518_models.CreateDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.CreateDIAlarmRuleResponse:
        """
        @summary 创建数据集成报警规则
        
        @param request: CreateDIAlarmRuleRequest
        @return: CreateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dialarm_rule_with_options(request, runtime)

    async def create_dialarm_rule_async(
        self,
        request: dataworks_public_20240518_models.CreateDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.CreateDIAlarmRuleResponse:
        """
        @summary 创建数据集成报警规则
        
        @param request: CreateDIAlarmRuleRequest
        @return: CreateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dialarm_rule_with_options_async(request, runtime)

    def create_dijob_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDIJobResponse:
        """
        @summary 创建数据集成任务
        
        @param tmp_req: CreateDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_data_source_settings):
            request.destination_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_data_source_settings, 'DestinationDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.source_data_source_settings):
            request.source_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_data_source_settings, 'SourceDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dijob_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDIJobResponse:
        """
        @summary 创建数据集成任务
        
        @param tmp_req: CreateDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_data_source_settings):
            request.destination_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_data_source_settings, 'DestinationDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.source_data_source_settings):
            request.source_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_data_source_settings, 'SourceDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dijob(
        self,
        request: dataworks_public_20240518_models.CreateDIJobRequest,
    ) -> dataworks_public_20240518_models.CreateDIJobResponse:
        """
        @summary 创建数据集成任务
        
        @param request: CreateDIJobRequest
        @return: CreateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dijob_with_options(request, runtime)

    async def create_dijob_async(
        self,
        request: dataworks_public_20240518_models.CreateDIJobRequest,
    ) -> dataworks_public_20240518_models.CreateDIJobResponse:
        """
        @summary 创建数据集成任务
        
        @param request: CreateDIJobRequest
        @return: CreateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dijob_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceRequest,
    ) -> dataworks_public_20240518_models.CreateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceRequest,
    ) -> dataworks_public_20240518_models.CreateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_data_source_shared_rule_with_options(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceSharedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceSharedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceSharedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.shared_user):
            query['SharedUser'] = request.shared_user
        if not UtilClient.is_unset(request.target_project_id):
            query['TargetProjectId'] = request.target_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSourceSharedRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_shared_rule_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceSharedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceSharedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceSharedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.shared_user):
            query['SharedUser'] = request.shared_user
        if not UtilClient.is_unset(request.target_project_id):
            query['TargetProjectId'] = request.target_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSourceSharedRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source_shared_rule(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceSharedRuleRequest,
    ) -> dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceSharedRuleRequest
        @return: CreateDataSourceSharedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_shared_rule_with_options(request, runtime)

    async def create_data_source_shared_rule_async(
        self,
        request: dataworks_public_20240518_models.CreateDataSourceSharedRuleRequest,
    ) -> dataworks_public_20240518_models.CreateDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: CreateDataSourceSharedRuleRequest
        @return: CreateDataSourceSharedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_shared_rule_with_options_async(request, runtime)

    def create_deployment_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary Creates a process for deploying or undeploying an entity in DataStudio.
        
        @description >  You cannot use this API operation to create a process for multiple entities at a time. If you specify multiple entities in a request, the system creates a process only for the first entity.
        
        @param tmp_req: CreateDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDeploymentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary Creates a process for deploying or undeploying an entity in DataStudio.
        
        @description >  You cannot use this API operation to create a process for multiple entities at a time. If you specify multiple entities in a request, the system creates a process only for the first entity.
        
        @param tmp_req: CreateDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDeploymentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment(
        self,
        request: dataworks_public_20240518_models.CreateDeploymentRequest,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary Creates a process for deploying or undeploying an entity in DataStudio.
        
        @description >  You cannot use this API operation to create a process for multiple entities at a time. If you specify multiple entities in a request, the system creates a process only for the first entity.
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_with_options(request, runtime)

    async def create_deployment_async(
        self,
        request: dataworks_public_20240518_models.CreateDeploymentRequest,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary Creates a process for deploying or undeploying an entity in DataStudio.
        
        @description >  You cannot use this API operation to create a process for multiple entities at a time. If you specify multiple entities in a request, the system creates a process only for the first entity.
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_deployment_with_options_async(request, runtime)

    def create_function_with_options(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary Creates a user-defined function (UDF) in DataStudio. The information about the UDF is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple UDFs at a time. If you specify multiple UDFs by using FlowSpec, the system creates only the first specified UDF.
        
        @param request: CreateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary Creates a user-defined function (UDF) in DataStudio. The information about the UDF is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple UDFs at a time. If you specify multiple UDFs by using FlowSpec, the system creates only the first specified UDF.
        
        @param request: CreateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary Creates a user-defined function (UDF) in DataStudio. The information about the UDF is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple UDFs at a time. If you specify multiple UDFs by using FlowSpec, the system creates only the first specified UDF.
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_function_with_options(request, runtime)

    async def create_function_async(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary Creates a user-defined function (UDF) in DataStudio. The information about the UDF is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple UDFs at a time. If you specify multiple UDFs by using FlowSpec, the system creates only the first specified UDF.
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_function_with_options_async(request, runtime)

    def create_network_with_options(
        self,
        request: dataworks_public_20240518_models.CreateNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNetworkResponse:
        """
        @summary 创建并绑定通用资源组网络资源。
        
        @param request: CreateNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNetworkResponse:
        """
        @summary 创建并绑定通用资源组网络资源。
        
        @param request: CreateNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network(
        self,
        request: dataworks_public_20240518_models.CreateNetworkRequest,
    ) -> dataworks_public_20240518_models.CreateNetworkResponse:
        """
        @summary 创建并绑定通用资源组网络资源。
        
        @param request: CreateNetworkRequest
        @return: CreateNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_with_options(request, runtime)

    async def create_network_async(
        self,
        request: dataworks_public_20240518_models.CreateNetworkRequest,
    ) -> dataworks_public_20240518_models.CreateNetworkResponse:
        """
        @summary 创建并绑定通用资源组网络资源。
        
        @param request: CreateNetworkRequest
        @return: CreateNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary Creates a node in DataStudio. The information about the node is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple nodes at a time. If you specify multiple nodes by using FlowSpec, the system creates only the first specified node.
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.container_id):
            body['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary Creates a node in DataStudio. The information about the node is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple nodes at a time. If you specify multiple nodes by using FlowSpec, the system creates only the first specified node.
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.container_id):
            body['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary Creates a node in DataStudio. The information about the node is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple nodes at a time. If you specify multiple nodes by using FlowSpec, the system creates only the first specified node.
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary Creates a node in DataStudio. The information about the node is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple nodes at a time. If you specify multiple nodes by using FlowSpec, the system creates only the first specified node.
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateProjectResponse:
        """
        @summary 创建工作空间
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not UtilClient.is_unset(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not UtilClient.is_unset(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateProjectResponse:
        """
        @summary 创建工作空间
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not UtilClient.is_unset(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not UtilClient.is_unset(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: dataworks_public_20240518_models.CreateProjectRequest,
    ) -> dataworks_public_20240518_models.CreateProjectResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: dataworks_public_20240518_models.CreateProjectRequest,
    ) -> dataworks_public_20240518_models.CreateProjectResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_member_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateProjectMemberResponse:
        """
        @summary 添加工作空间成员
        
        @param tmp_req: CreateProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateProjectMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_member_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateProjectMemberResponse:
        """
        @summary 添加工作空间成员
        
        @param tmp_req: CreateProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateProjectMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project_member(
        self,
        request: dataworks_public_20240518_models.CreateProjectMemberRequest,
    ) -> dataworks_public_20240518_models.CreateProjectMemberResponse:
        """
        @summary 添加工作空间成员
        
        @param request: CreateProjectMemberRequest
        @return: CreateProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    async def create_project_member_async(
        self,
        request: dataworks_public_20240518_models.CreateProjectMemberRequest,
    ) -> dataworks_public_20240518_models.CreateProjectMemberResponse:
        """
        @summary 添加工作空间成员
        
        @param request: CreateProjectMemberRequest
        @return: CreateProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_member_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary Creates a file resource in DataStudio. The information about the file resource is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple file resources at a time. If you specify multiple file resources by using FlowSpec, the system creates only the first specified resource.
        
        @param request: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary Creates a file resource in DataStudio. The information about the file resource is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple file resources at a time. If you specify multiple file resources by using FlowSpec, the system creates only the first specified resource.
        
        @param request: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary Creates a file resource in DataStudio. The information about the file resource is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple file resources at a time. If you specify multiple file resources by using FlowSpec, the system creates only the first specified resource.
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary Creates a file resource in DataStudio. The information about the file resource is described by using FlowSpec.
        
        @description >  You cannot use this API operation to create multiple file resources at a time. If you specify multiple file resources by using FlowSpec, the system creates only the first specified resource.
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def create_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceGroupResponse:
        """
        @summary 创建通用资源组。
        
        @param request: CreateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceGroupResponse:
        """
        @summary 创建通用资源组。
        
        @param request: CreateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: dataworks_public_20240518_models.CreateResourceGroupRequest,
    ) -> dataworks_public_20240518_models.CreateResourceGroupResponse:
        """
        @summary 创建通用资源组。
        
        @param request: CreateResourceGroupRequest
        @return: CreateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceGroupRequest,
    ) -> dataworks_public_20240518_models.CreateResourceGroupResponse:
        """
        @summary 创建通用资源组。
        
        @param request: CreateResourceGroupRequest
        @return: CreateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_route_with_options(
        self,
        request: dataworks_public_20240518_models.CreateRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateRouteResponse:
        """
        @summary 创建网络资源的路由。
        
        @param request: CreateRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_route_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateRouteResponse:
        """
        @summary 创建网络资源的路由。
        
        @param request: CreateRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_route(
        self,
        request: dataworks_public_20240518_models.CreateRouteRequest,
    ) -> dataworks_public_20240518_models.CreateRouteResponse:
        """
        @summary 创建网络资源的路由。
        
        @param request: CreateRouteRequest
        @return: CreateRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_route_with_options(request, runtime)

    async def create_route_async(
        self,
        request: dataworks_public_20240518_models.CreateRouteRequest,
    ) -> dataworks_public_20240518_models.CreateRouteResponse:
        """
        @summary 创建网络资源的路由。
        
        @param request: CreateRouteRequest
        @return: CreateRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_route_with_options_async(request, runtime)

    def create_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary Creates a workflow in a directory of DataStudio.
        
        @description > You cannot use this API operation to create multiple workflows at a time. If you specify multiple workflows by using FlowSpec, the system creates only the first specified workflow. Other specified workflows and the nodes in the workflows are ignored. You can call the CreateNode operation to create a node.
        
        @param request: CreateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary Creates a workflow in a directory of DataStudio.
        
        @description > You cannot use this API operation to create multiple workflows at a time. If you specify multiple workflows by using FlowSpec, the system creates only the first specified workflow. Other specified workflows and the nodes in the workflows are ignored. You can call the CreateNode operation to create a node.
        
        @param request: CreateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow_definition(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary Creates a workflow in a directory of DataStudio.
        
        @description > You cannot use this API operation to create multiple workflows at a time. If you specify multiple workflows by using FlowSpec, the system creates only the first specified workflow. Other specified workflows and the nodes in the workflows are ignored. You can call the CreateNode operation to create a node.
        
        @param request: CreateWorkflowDefinitionRequest
        @return: CreateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_workflow_definition_with_options(request, runtime)

    async def create_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary Creates a workflow in a directory of DataStudio.
        
        @description > You cannot use this API operation to create multiple workflows at a time. If you specify multiple workflows by using FlowSpec, the system creates only the first specified workflow. Other specified workflows and the nodes in the workflows are ignored. You can call the CreateNode operation to create a node.
        
        @param request: CreateWorkflowDefinitionRequest
        @return: CreateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_workflow_definition_with_options_async(request, runtime)

    def delete_alert_rule_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteAlertRuleResponse:
        """
        @summary 删除自定义监控报警规则
        
        @param request: DeleteAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rule_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteAlertRuleResponse:
        """
        @summary 删除自定义监控报警规则
        
        @param request: DeleteAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rule(
        self,
        request: dataworks_public_20240518_models.DeleteAlertRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteAlertRuleResponse:
        """
        @summary 删除自定义监控报警规则
        
        @param request: DeleteAlertRuleRequest
        @return: DeleteAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rule_with_options(request, runtime)

    async def delete_alert_rule_async(
        self,
        request: dataworks_public_20240518_models.DeleteAlertRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteAlertRuleResponse:
        """
        @summary 删除自定义监控报警规则
        
        @param request: DeleteAlertRuleRequest
        @return: DeleteAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rule_with_options_async(request, runtime)

    def delete_dialarm_rule_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDIAlarmRuleResponse:
        """
        @summary Deletes an alert rule configured for a synchronization task.
        
        @param request: DeleteDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDIAlarmRuleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dialarm_rule_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDIAlarmRuleResponse:
        """
        @summary Deletes an alert rule configured for a synchronization task.
        
        @param request: DeleteDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDIAlarmRuleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dialarm_rule(
        self,
        request: dataworks_public_20240518_models.DeleteDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteDIAlarmRuleResponse:
        """
        @summary Deletes an alert rule configured for a synchronization task.
        
        @param request: DeleteDIAlarmRuleRequest
        @return: DeleteDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dialarm_rule_with_options(request, runtime)

    async def delete_dialarm_rule_async(
        self,
        request: dataworks_public_20240518_models.DeleteDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteDIAlarmRuleResponse:
        """
        @summary Deletes an alert rule configured for a synchronization task.
        
        @param request: DeleteDIAlarmRuleRequest
        @return: DeleteDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dialarm_rule_with_options_async(request, runtime)

    def delete_dijob_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDIJobResponse:
        """
        @summary 删除数据集成任务
        
        @param request: DeleteDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dijob_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDIJobResponse:
        """
        @summary 删除数据集成任务
        
        @param request: DeleteDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dijob(
        self,
        request: dataworks_public_20240518_models.DeleteDIJobRequest,
    ) -> dataworks_public_20240518_models.DeleteDIJobResponse:
        """
        @summary 删除数据集成任务
        
        @param request: DeleteDIJobRequest
        @return: DeleteDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dijob_with_options(request, runtime)

    async def delete_dijob_async(
        self,
        request: dataworks_public_20240518_models.DeleteDIJobRequest,
    ) -> dataworks_public_20240518_models.DeleteDIJobResponse:
        """
        @summary 删除数据集成任务
        
        @param request: DeleteDIJobRequest
        @return: DeleteDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dijob_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDataSourceResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDataSourceResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceRequest,
    ) -> dataworks_public_20240518_models.DeleteDataSourceResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceRequest,
    ) -> dataworks_public_20240518_models.DeleteDataSourceResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_data_source_shared_rule_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceSharedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceSharedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceSharedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceSharedRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_shared_rule_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceSharedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceSharedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceSharedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceSharedRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source_shared_rule(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceSharedRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceSharedRuleRequest
        @return: DeleteDataSourceSharedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_shared_rule_with_options(request, runtime)

    async def delete_data_source_shared_rule_async(
        self,
        request: dataworks_public_20240518_models.DeleteDataSourceSharedRuleRequest,
    ) -> dataworks_public_20240518_models.DeleteDataSourceSharedRuleResponse:
        """
        @summary 验证用
        
        @param request: DeleteDataSourceSharedRuleRequest
        @return: DeleteDataSourceSharedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_shared_rule_with_options_async(request, runtime)

    def delete_function_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary Deletes a user-defined function (UDF) in DataStudio.
        
        @description >  A UDF that is deployed cannot be deleted. If you want to delete such a UDF, you must first undeploy the UDF.
        
        @param request: DeleteFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary Deletes a user-defined function (UDF) in DataStudio.
        
        @description >  A UDF that is deployed cannot be deleted. If you want to delete such a UDF, you must first undeploy the UDF.
        
        @param request: DeleteFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary Deletes a user-defined function (UDF) in DataStudio.
        
        @description >  A UDF that is deployed cannot be deleted. If you want to delete such a UDF, you must first undeploy the UDF.
        
        @param request: DeleteFunctionRequest
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_function_with_options(request, runtime)

    async def delete_function_async(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary Deletes a user-defined function (UDF) in DataStudio.
        
        @description >  A UDF that is deployed cannot be deleted. If you want to delete such a UDF, you must first undeploy the UDF.
        
        @param request: DeleteFunctionRequest
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_function_with_options_async(request, runtime)

    def delete_network_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNetworkResponse:
        """
        @summary 解绑并删除通用资源组网络资源。
        
        @param request: DeleteNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNetworkResponse:
        """
        @summary 解绑并删除通用资源组网络资源。
        
        @param request: DeleteNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network(
        self,
        request: dataworks_public_20240518_models.DeleteNetworkRequest,
    ) -> dataworks_public_20240518_models.DeleteNetworkResponse:
        """
        @summary 解绑并删除通用资源组网络资源。
        
        @param request: DeleteNetworkRequest
        @return: DeleteNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_with_options(request, runtime)

    async def delete_network_async(
        self,
        request: dataworks_public_20240518_models.DeleteNetworkRequest,
    ) -> dataworks_public_20240518_models.DeleteNetworkResponse:
        """
        @summary 解绑并删除通用资源组网络资源。
        
        @param request: DeleteNetworkRequest
        @return: DeleteNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary Deletes a node from DataStudio.
        
        @description >  A node that is deployed cannot be deleted. If you want to delete such a node, you must first undeploy the node.
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary Deletes a node from DataStudio.
        
        @description >  A node that is deployed cannot be deleted. If you want to delete such a node, you must first undeploy the node.
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary Deletes a node from DataStudio.
        
        @description >  A node that is deployed cannot be deleted. If you want to delete such a node, you must first undeploy the node.
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary Deletes a node from DataStudio.
        
        @description >  A node that is deployed cannot be deleted. If you want to delete such a node, you must first undeploy the node.
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteProjectResponse:
        """
        @summary 销毁工作空间
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteProjectResponse:
        """
        @summary 销毁工作空间
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: dataworks_public_20240518_models.DeleteProjectRequest,
    ) -> dataworks_public_20240518_models.DeleteProjectResponse:
        """
        @summary 销毁工作空间
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: dataworks_public_20240518_models.DeleteProjectRequest,
    ) -> dataworks_public_20240518_models.DeleteProjectResponse:
        """
        @summary 销毁工作空间
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_project_member_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteProjectMemberResponse:
        """
        @summary Removes a member from a workspace.
        
        @param request: DeleteProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_member_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteProjectMemberResponse:
        """
        @summary Removes a member from a workspace.
        
        @param request: DeleteProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project_member(
        self,
        request: dataworks_public_20240518_models.DeleteProjectMemberRequest,
    ) -> dataworks_public_20240518_models.DeleteProjectMemberResponse:
        """
        @summary Removes a member from a workspace.
        
        @param request: DeleteProjectMemberRequest
        @return: DeleteProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    async def delete_project_member_async(
        self,
        request: dataworks_public_20240518_models.DeleteProjectMemberRequest,
    ) -> dataworks_public_20240518_models.DeleteProjectMemberResponse:
        """
        @summary Removes a member from a workspace.
        
        @param request: DeleteProjectMemberRequest
        @return: DeleteProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_member_with_options_async(request, runtime)

    def delete_resource_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary Deletes a file resource from DataStudio.
        
        @description >  A file resource that is deployed cannot be deleted. If you want to delete such a file resource, you must first undeploy the file resource.
        
        @param request: DeleteResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary Deletes a file resource from DataStudio.
        
        @description >  A file resource that is deployed cannot be deleted. If you want to delete such a file resource, you must first undeploy the file resource.
        
        @param request: DeleteResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary Deletes a file resource from DataStudio.
        
        @description >  A file resource that is deployed cannot be deleted. If you want to delete such a file resource, you must first undeploy the file resource.
        
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    async def delete_resource_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary Deletes a file resource from DataStudio.
        
        @description >  A file resource that is deployed cannot be deleted. If you want to delete such a file resource, you must first undeploy the file resource.
        
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a serverless resource group.
        
        @param request: DeleteResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a serverless resource group.
        
        @param request: DeleteResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: dataworks_public_20240518_models.DeleteResourceGroupRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a serverless resource group.
        
        @param request: DeleteResourceGroupRequest
        @return: DeleteResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceGroupRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a serverless resource group.
        
        @param request: DeleteResourceGroupRequest
        @return: DeleteResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_route_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteRouteResponse:
        """
        @summary 删除网络资源的路由。
        
        @param request: DeleteRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteRouteResponse:
        """
        @summary 删除网络资源的路由。
        
        @param request: DeleteRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route(
        self,
        request: dataworks_public_20240518_models.DeleteRouteRequest,
    ) -> dataworks_public_20240518_models.DeleteRouteResponse:
        """
        @summary 删除网络资源的路由。
        
        @param request: DeleteRouteRequest
        @return: DeleteRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_route_with_options(request, runtime)

    async def delete_route_async(
        self,
        request: dataworks_public_20240518_models.DeleteRouteRequest,
    ) -> dataworks_public_20240518_models.DeleteRouteResponse:
        """
        @summary 删除网络资源的路由。
        
        @param request: DeleteRouteRequest
        @return: DeleteRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_with_options_async(request, runtime)

    def delete_task_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteTaskResponse:
        """
        @param request: DeleteTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_env):
            query['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteTaskResponse:
        """
        @param request: DeleteTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_env):
            query['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        request: dataworks_public_20240518_models.DeleteTaskRequest,
    ) -> dataworks_public_20240518_models.DeleteTaskResponse:
        """
        @param request: DeleteTaskRequest
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_task_with_options(request, runtime)

    async def delete_task_async(
        self,
        request: dataworks_public_20240518_models.DeleteTaskRequest,
    ) -> dataworks_public_20240518_models.DeleteTaskResponse:
        """
        @param request: DeleteTaskRequest
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_task_with_options_async(request, runtime)

    def delete_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary Deletes a workflow from DataStudio.
        
        @description >  A workflow that is deployed cannot be deleted. If you want to delete such a workflow, you must first undeploy the workflow.
        
        @param request: DeleteWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary Deletes a workflow from DataStudio.
        
        @description >  A workflow that is deployed cannot be deleted. If you want to delete such a workflow, you must first undeploy the workflow.
        
        @param request: DeleteWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow_definition(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary Deletes a workflow from DataStudio.
        
        @description >  A workflow that is deployed cannot be deleted. If you want to delete such a workflow, you must first undeploy the workflow.
        
        @param request: DeleteWorkflowDefinitionRequest
        @return: DeleteWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_workflow_definition_with_options(request, runtime)

    async def delete_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary Deletes a workflow from DataStudio.
        
        @description >  A workflow that is deployed cannot be deleted. If you want to delete such a workflow, you must first undeploy the workflow.
        
        @param request: DeleteWorkflowDefinitionRequest
        @return: DeleteWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_workflow_definition_with_options_async(request, runtime)

    def dissociate_project_from_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.DissociateProjectFromResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse:
        """
        @summary Disassociates a resource group from a workspace.
        
        @param request: DissociateProjectFromResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateProjectFromResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateProjectFromResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_project_from_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.DissociateProjectFromResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse:
        """
        @summary Disassociates a resource group from a workspace.
        
        @param request: DissociateProjectFromResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateProjectFromResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateProjectFromResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_project_from_resource_group(
        self,
        request: dataworks_public_20240518_models.DissociateProjectFromResourceGroupRequest,
    ) -> dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse:
        """
        @summary Disassociates a resource group from a workspace.
        
        @param request: DissociateProjectFromResourceGroupRequest
        @return: DissociateProjectFromResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_project_from_resource_group_with_options(request, runtime)

    async def dissociate_project_from_resource_group_async(
        self,
        request: dataworks_public_20240518_models.DissociateProjectFromResourceGroupRequest,
    ) -> dataworks_public_20240518_models.DissociateProjectFromResourceGroupResponse:
        """
        @summary Disassociates a resource group from a workspace.
        
        @param request: DissociateProjectFromResourceGroupRequest
        @return: DissociateProjectFromResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_project_from_resource_group_with_options_async(request, runtime)

    def exec_deployment_stage_with_options(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary Executes a stage in a process.
        
        @description >  The stages in a process are sequential. For more information, see the GetDeployment operation. Skipping or repeating a stage is not allowed.
        >  The execution of a stage is asynchronous. The response of this operation indicates only whether a stage is triggered but does not indicate whether the execution of the stage is successful. You can call the GetDeployment operation to check whether the execution is successful.
        
        @param request: ExecDeploymentStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecDeploymentStageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecDeploymentStage',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ExecDeploymentStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_deployment_stage_with_options_async(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary Executes a stage in a process.
        
        @description >  The stages in a process are sequential. For more information, see the GetDeployment operation. Skipping or repeating a stage is not allowed.
        >  The execution of a stage is asynchronous. The response of this operation indicates only whether a stage is triggered but does not indicate whether the execution of the stage is successful. You can call the GetDeployment operation to check whether the execution is successful.
        
        @param request: ExecDeploymentStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecDeploymentStageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecDeploymentStage',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ExecDeploymentStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_deployment_stage(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary Executes a stage in a process.
        
        @description >  The stages in a process are sequential. For more information, see the GetDeployment operation. Skipping or repeating a stage is not allowed.
        >  The execution of a stage is asynchronous. The response of this operation indicates only whether a stage is triggered but does not indicate whether the execution of the stage is successful. You can call the GetDeployment operation to check whether the execution is successful.
        
        @param request: ExecDeploymentStageRequest
        @return: ExecDeploymentStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exec_deployment_stage_with_options(request, runtime)

    async def exec_deployment_stage_async(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary Executes a stage in a process.
        
        @description >  The stages in a process are sequential. For more information, see the GetDeployment operation. Skipping or repeating a stage is not allowed.
        >  The execution of a stage is asynchronous. The response of this operation indicates only whether a stage is triggered but does not indicate whether the execution of the stage is successful. You can call the GetDeployment operation to check whether the execution is successful.
        
        @param request: ExecDeploymentStageRequest
        @return: ExecDeploymentStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exec_deployment_stage_with_options_async(request, runtime)

    def get_alert_rule_with_options(
        self,
        request: dataworks_public_20240518_models.GetAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetAlertRuleResponse:
        """
        @summary 获取自定义监控报警规则
        
        @param request: GetAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlertRuleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_rule_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetAlertRuleResponse:
        """
        @summary 获取自定义监控报警规则
        
        @param request: GetAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlertRuleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_rule(
        self,
        request: dataworks_public_20240518_models.GetAlertRuleRequest,
    ) -> dataworks_public_20240518_models.GetAlertRuleResponse:
        """
        @summary 获取自定义监控报警规则
        
        @param request: GetAlertRuleRequest
        @return: GetAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_alert_rule_with_options(request, runtime)

    async def get_alert_rule_async(
        self,
        request: dataworks_public_20240518_models.GetAlertRuleRequest,
    ) -> dataworks_public_20240518_models.GetAlertRuleResponse:
        """
        @summary 获取自定义监控报警规则
        
        @param request: GetAlertRuleRequest
        @return: GetAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_rule_with_options_async(request, runtime)

    def get_dijob_with_options(
        self,
        request: dataworks_public_20240518_models.GetDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDIJobResponse:
        """
        @summary 查看数据集成任务
        
        @param request: GetDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dijob_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDIJobResponse:
        """
        @summary 查看数据集成任务
        
        @param request: GetDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dijob(
        self,
        request: dataworks_public_20240518_models.GetDIJobRequest,
    ) -> dataworks_public_20240518_models.GetDIJobResponse:
        """
        @summary 查看数据集成任务
        
        @param request: GetDIJobRequest
        @return: GetDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dijob_with_options(request, runtime)

    async def get_dijob_async(
        self,
        request: dataworks_public_20240518_models.GetDIJobRequest,
    ) -> dataworks_public_20240518_models.GetDIJobResponse:
        """
        @summary 查看数据集成任务
        
        @param request: GetDIJobRequest
        @return: GetDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dijob_with_options_async(request, runtime)

    def get_dijob_log_with_options(
        self,
        request: dataworks_public_20240518_models.GetDIJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDIJobLogResponse:
        """
        @summary Obtains logs generated for a synchronization task.
        
        @param request: GetDIJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDIJobLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDIJobLog',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDIJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dijob_log_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetDIJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDIJobLogResponse:
        """
        @summary Obtains logs generated for a synchronization task.
        
        @param request: GetDIJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDIJobLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDIJobLog',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDIJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dijob_log(
        self,
        request: dataworks_public_20240518_models.GetDIJobLogRequest,
    ) -> dataworks_public_20240518_models.GetDIJobLogResponse:
        """
        @summary Obtains logs generated for a synchronization task.
        
        @param request: GetDIJobLogRequest
        @return: GetDIJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dijob_log_with_options(request, runtime)

    async def get_dijob_log_async(
        self,
        request: dataworks_public_20240518_models.GetDIJobLogRequest,
    ) -> dataworks_public_20240518_models.GetDIJobLogResponse:
        """
        @summary Obtains logs generated for a synchronization task.
        
        @param request: GetDIJobLogRequest
        @return: GetDIJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dijob_log_with_options_async(request, runtime)

    def get_data_source_with_options(
        self,
        request: dataworks_public_20240518_models.GetDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDataSourceResponse:
        """
        @summary Queries a data source by ID.
        
        @description You can call this operation only if you are assigned one of the following roles in DataWorks:
        Tenant Owner, Workspace Administrator, Deployment, Development, Project Owner, and O\\&M
        
        @param request: GetDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDataSourceResponse:
        """
        @summary Queries a data source by ID.
        
        @description You can call this operation only if you are assigned one of the following roles in DataWorks:
        Tenant Owner, Workspace Administrator, Deployment, Development, Project Owner, and O\\&M
        
        @param request: GetDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source(
        self,
        request: dataworks_public_20240518_models.GetDataSourceRequest,
    ) -> dataworks_public_20240518_models.GetDataSourceResponse:
        """
        @summary Queries a data source by ID.
        
        @description You can call this operation only if you are assigned one of the following roles in DataWorks:
        Tenant Owner, Workspace Administrator, Deployment, Development, Project Owner, and O\\&M
        
        @param request: GetDataSourceRequest
        @return: GetDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_with_options(request, runtime)

    async def get_data_source_async(
        self,
        request: dataworks_public_20240518_models.GetDataSourceRequest,
    ) -> dataworks_public_20240518_models.GetDataSourceResponse:
        """
        @summary Queries a data source by ID.
        
        @description You can call this operation only if you are assigned one of the following roles in DataWorks:
        Tenant Owner, Workspace Administrator, Deployment, Development, Project Owner, and O\\&M
        
        @param request: GetDataSourceRequest
        @return: GetDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_with_options_async(request, runtime)

    def get_deployment_with_options(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary Queries the information about a process for deploying or undeploying an entity.
        
        @param request: GetDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary Queries the information about a process for deploying or undeploying an entity.
        
        @param request: GetDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary Queries the information about a process for deploying or undeploying an entity.
        
        @param request: GetDeploymentRequest
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    async def get_deployment_async(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary Queries the information about a process for deploying or undeploying an entity.
        
        @param request: GetDeploymentRequest
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_deployment_with_options_async(request, runtime)

    def get_function_with_options(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary Queries the information about a user-defined function (UDF) in DataStudio.
        
        @param request: GetFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary Queries the information about a user-defined function (UDF) in DataStudio.
        
        @param request: GetFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary Queries the information about a user-defined function (UDF) in DataStudio.
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_function_with_options(request, runtime)

    async def get_function_async(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary Queries the information about a user-defined function (UDF) in DataStudio.
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_function_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: dataworks_public_20240518_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetJobStatusResponse:
        """
        @summary 返回异步任务的状态信息
        
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetJobStatusResponse:
        """
        @summary 返回异步任务的状态信息
        
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_status(
        self,
        request: dataworks_public_20240518_models.GetJobStatusRequest,
    ) -> dataworks_public_20240518_models.GetJobStatusResponse:
        """
        @summary 返回异步任务的状态信息
        
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: dataworks_public_20240518_models.GetJobStatusRequest,
    ) -> dataworks_public_20240518_models.GetJobStatusResponse:
        """
        @summary 返回异步任务的状态信息
        
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_network_with_options(
        self,
        request: dataworks_public_20240518_models.GetNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNetworkResponse:
        """
        @summary 获取某个网络资源详细信息。
        
        @param request: GetNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNetworkResponse:
        """
        @summary 获取某个网络资源详细信息。
        
        @param request: GetNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetwork',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network(
        self,
        request: dataworks_public_20240518_models.GetNetworkRequest,
    ) -> dataworks_public_20240518_models.GetNetworkResponse:
        """
        @summary 获取某个网络资源详细信息。
        
        @param request: GetNetworkRequest
        @return: GetNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_with_options(request, runtime)

    async def get_network_async(
        self,
        request: dataworks_public_20240518_models.GetNetworkRequest,
    ) -> dataworks_public_20240518_models.GetNetworkResponse:
        """
        @summary 获取某个网络资源详细信息。
        
        @param request: GetNetworkRequest
        @return: GetNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_with_options_async(request, runtime)

    def get_node_with_options(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @summary Queries the information about a node in DataStudio.
        
        @param request: GetNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @summary Queries the information about a node in DataStudio.
        
        @param request: GetNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @summary Queries the information about a node in DataStudio.
        
        @param request: GetNodeRequest
        @return: GetNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    async def get_node_async(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @summary Queries the information about a node in DataStudio.
        
        @param request: GetNodeRequest
        @return: GetNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: dataworks_public_20240518_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectResponse:
        """
        @summary Queries the information about a DataWorks workspace.
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectResponse:
        """
        @summary Queries the information about a DataWorks workspace.
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: dataworks_public_20240518_models.GetProjectRequest,
    ) -> dataworks_public_20240518_models.GetProjectResponse:
        """
        @summary Queries the information about a DataWorks workspace.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: dataworks_public_20240518_models.GetProjectRequest,
    ) -> dataworks_public_20240518_models.GetProjectResponse:
        """
        @summary Queries the information about a DataWorks workspace.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_project_member_with_options(
        self,
        request: dataworks_public_20240518_models.GetProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectMemberResponse:
        """
        @summary Queries the details about a member in a workspace.
        
        @param request: GetProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_member_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectMemberResponse:
        """
        @summary Queries the details about a member in a workspace.
        
        @param request: GetProjectMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_member(
        self,
        request: dataworks_public_20240518_models.GetProjectMemberRequest,
    ) -> dataworks_public_20240518_models.GetProjectMemberResponse:
        """
        @summary Queries the details about a member in a workspace.
        
        @param request: GetProjectMemberRequest
        @return: GetProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_member_with_options(request, runtime)

    async def get_project_member_async(
        self,
        request: dataworks_public_20240518_models.GetProjectMemberRequest,
    ) -> dataworks_public_20240518_models.GetProjectMemberResponse:
        """
        @summary Queries the details about a member in a workspace.
        
        @param request: GetProjectMemberRequest
        @return: GetProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_member_with_options_async(request, runtime)

    def get_project_role_with_options(
        self,
        request: dataworks_public_20240518_models.GetProjectRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectRoleResponse:
        """
        @summary 查询工作空间角色详情
        
        @param request: GetProjectRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectRole',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_role_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetProjectRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetProjectRoleResponse:
        """
        @summary 查询工作空间角色详情
        
        @param request: GetProjectRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectRole',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetProjectRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_role(
        self,
        request: dataworks_public_20240518_models.GetProjectRoleRequest,
    ) -> dataworks_public_20240518_models.GetProjectRoleResponse:
        """
        @summary 查询工作空间角色详情
        
        @param request: GetProjectRoleRequest
        @return: GetProjectRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_role_with_options(request, runtime)

    async def get_project_role_async(
        self,
        request: dataworks_public_20240518_models.GetProjectRoleRequest,
    ) -> dataworks_public_20240518_models.GetProjectRoleResponse:
        """
        @summary 查询工作空间角色详情
        
        @param request: GetProjectRoleRequest
        @return: GetProjectRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_role_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary Queries the information about a file resource.
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary Queries the information about a file resource.
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary Queries the information about a file resource.
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary Queries the information about a file resource.
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceGroupResponse:
        """
        @summary 根据id获取指定资源组。
        
        @param request: GetResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceGroupResponse:
        """
        @summary 根据id获取指定资源组。
        
        @param request: GetResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        request: dataworks_public_20240518_models.GetResourceGroupRequest,
    ) -> dataworks_public_20240518_models.GetResourceGroupResponse:
        """
        @summary 根据id获取指定资源组。
        
        @param request: GetResourceGroupRequest
        @return: GetResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: dataworks_public_20240518_models.GetResourceGroupRequest,
    ) -> dataworks_public_20240518_models.GetResourceGroupResponse:
        """
        @summary 根据id获取指定资源组。
        
        @param request: GetResourceGroupRequest
        @return: GetResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_route_with_options(
        self,
        request: dataworks_public_20240518_models.GetRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetRouteResponse:
        """
        @summary 根据id获取指定路由。
        
        @param request: GetRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_route_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetRouteResponse:
        """
        @summary 根据id获取指定路由。
        
        @param request: GetRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_route(
        self,
        request: dataworks_public_20240518_models.GetRouteRequest,
    ) -> dataworks_public_20240518_models.GetRouteResponse:
        """
        @summary 根据id获取指定路由。
        
        @param request: GetRouteRequest
        @return: GetRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_route_with_options(request, runtime)

    async def get_route_async(
        self,
        request: dataworks_public_20240518_models.GetRouteRequest,
    ) -> dataworks_public_20240518_models.GetRouteResponse:
        """
        @summary 根据id获取指定路由。
        
        @param request: GetRouteRequest
        @return: GetRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_route_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: dataworks_public_20240518_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskResponse:
        """
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskResponse:
        """
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: dataworks_public_20240518_models.GetTaskRequest,
    ) -> dataworks_public_20240518_models.GetTaskResponse:
        """
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: dataworks_public_20240518_models.GetTaskRequest,
    ) -> dataworks_public_20240518_models.GetTaskResponse:
        """
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_instance_with_options(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskInstanceResponse:
        """
        @summary Queries the information about an instance.
        
        @param request: GetTaskInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstance',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_instance_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskInstanceResponse:
        """
        @summary Queries the information about an instance.
        
        @param request: GetTaskInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstance',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_instance(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceRequest,
    ) -> dataworks_public_20240518_models.GetTaskInstanceResponse:
        """
        @summary Queries the information about an instance.
        
        @param request: GetTaskInstanceRequest
        @return: GetTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_instance_with_options(request, runtime)

    async def get_task_instance_async(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceRequest,
    ) -> dataworks_public_20240518_models.GetTaskInstanceResponse:
        """
        @summary Queries the information about an instance.
        
        @param request: GetTaskInstanceRequest
        @return: GetTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_instance_with_options_async(request, runtime)

    def get_task_instance_log_with_options(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskInstanceLogResponse:
        """
        @param request: GetTaskInstanceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstanceLog',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_instance_log_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetTaskInstanceLogResponse:
        """
        @param request: GetTaskInstanceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstanceLog',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetTaskInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_instance_log(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceLogRequest,
    ) -> dataworks_public_20240518_models.GetTaskInstanceLogResponse:
        """
        @param request: GetTaskInstanceLogRequest
        @return: GetTaskInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_instance_log_with_options(request, runtime)

    async def get_task_instance_log_async(
        self,
        request: dataworks_public_20240518_models.GetTaskInstanceLogRequest,
    ) -> dataworks_public_20240518_models.GetTaskInstanceLogResponse:
        """
        @param request: GetTaskInstanceLogRequest
        @return: GetTaskInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_instance_log_with_options_async(request, runtime)

    def get_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary Queries the infomation about a workflow.
        
        @param request: GetWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary Queries the infomation about a workflow.
        
        @param request: GetWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_definition(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary Queries the infomation about a workflow.
        
        @param request: GetWorkflowDefinitionRequest
        @return: GetWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_definition_with_options(request, runtime)

    async def get_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary Queries the infomation about a workflow.
        
        @param request: GetWorkflowDefinitionRequest
        @return: GetWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_workflow_definition_with_options_async(request, runtime)

    def grant_member_project_roles_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.GrantMemberProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GrantMemberProjectRolesResponse:
        """
        @summary Assigns roles to members in a workspace.
        
        @param tmp_req: GrantMemberProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantMemberProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.GrantMemberProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantMemberProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GrantMemberProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_member_project_roles_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.GrantMemberProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GrantMemberProjectRolesResponse:
        """
        @summary Assigns roles to members in a workspace.
        
        @param tmp_req: GrantMemberProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantMemberProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.GrantMemberProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantMemberProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GrantMemberProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_member_project_roles(
        self,
        request: dataworks_public_20240518_models.GrantMemberProjectRolesRequest,
    ) -> dataworks_public_20240518_models.GrantMemberProjectRolesResponse:
        """
        @summary Assigns roles to members in a workspace.
        
        @param request: GrantMemberProjectRolesRequest
        @return: GrantMemberProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_member_project_roles_with_options(request, runtime)

    async def grant_member_project_roles_async(
        self,
        request: dataworks_public_20240518_models.GrantMemberProjectRolesRequest,
    ) -> dataworks_public_20240518_models.GrantMemberProjectRolesResponse:
        """
        @summary Assigns roles to members in a workspace.
        
        @param request: GrantMemberProjectRolesRequest
        @return: GrantMemberProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_member_project_roles_with_options_async(request, runtime)

    def import_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.ImportWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ImportWorkflowDefinitionResponse:
        """
        @summary 调用此接口，可以将通过FlowSpec定义的工作流节点和其内部的子节点都导入到数据开发中
        
        @param request: ImportWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ImportWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.ImportWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ImportWorkflowDefinitionResponse:
        """
        @summary 调用此接口，可以将通过FlowSpec定义的工作流节点和其内部的子节点都导入到数据开发中
        
        @param request: ImportWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ImportWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_workflow_definition(
        self,
        request: dataworks_public_20240518_models.ImportWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.ImportWorkflowDefinitionResponse:
        """
        @summary 调用此接口，可以将通过FlowSpec定义的工作流节点和其内部的子节点都导入到数据开发中
        
        @param request: ImportWorkflowDefinitionRequest
        @return: ImportWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_workflow_definition_with_options(request, runtime)

    async def import_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.ImportWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.ImportWorkflowDefinitionResponse:
        """
        @summary 调用此接口，可以将通过FlowSpec定义的工作流节点和其内部的子节点都导入到数据开发中
        
        @param request: ImportWorkflowDefinitionRequest
        @return: ImportWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_workflow_definition_with_options_async(request, runtime)

    def list_alert_rules_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListAlertRulesResponse:
        """
        @summary 分页获取自定义监控报警规则
        
        @param tmp_req: ListAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListAlertRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_rules_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListAlertRulesResponse:
        """
        @summary 分页获取自定义监控报警规则
        
        @param tmp_req: ListAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListAlertRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_rules(
        self,
        request: dataworks_public_20240518_models.ListAlertRulesRequest,
    ) -> dataworks_public_20240518_models.ListAlertRulesResponse:
        """
        @summary 分页获取自定义监控报警规则
        
        @param request: ListAlertRulesRequest
        @return: ListAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alert_rules_with_options(request, runtime)

    async def list_alert_rules_async(
        self,
        request: dataworks_public_20240518_models.ListAlertRulesRequest,
    ) -> dataworks_public_20240518_models.ListAlertRulesResponse:
        """
        @summary 分页获取自定义监控报警规则
        
        @param request: ListAlertRulesRequest
        @return: ListAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_rules_with_options_async(request, runtime)

    def list_dialarm_rules_with_options(
        self,
        request: dataworks_public_20240518_models.ListDIAlarmRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIAlarmRulesResponse:
        """
        @summary 查看数据集成报警规则
        
        @param request: ListDIAlarmRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIAlarmRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIAlarmRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIAlarmRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialarm_rules_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDIAlarmRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIAlarmRulesResponse:
        """
        @summary 查看数据集成报警规则
        
        @param request: ListDIAlarmRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIAlarmRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIAlarmRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIAlarmRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialarm_rules(
        self,
        request: dataworks_public_20240518_models.ListDIAlarmRulesRequest,
    ) -> dataworks_public_20240518_models.ListDIAlarmRulesResponse:
        """
        @summary 查看数据集成报警规则
        
        @param request: ListDIAlarmRulesRequest
        @return: ListDIAlarmRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialarm_rules_with_options(request, runtime)

    async def list_dialarm_rules_async(
        self,
        request: dataworks_public_20240518_models.ListDIAlarmRulesRequest,
    ) -> dataworks_public_20240518_models.ListDIAlarmRulesResponse:
        """
        @summary 查看数据集成报警规则
        
        @param request: ListDIAlarmRulesRequest
        @return: ListDIAlarmRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dialarm_rules_with_options_async(request, runtime)

    def list_dijob_events_with_options(
        self,
        request: dataworks_public_20240518_models.ListDIJobEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobEventsResponse:
        """
        @summary 获取数据集成任务事件
        
        @param request: ListDIJobEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobEvents',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_events_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobEventsResponse:
        """
        @summary 获取数据集成任务事件
        
        @param request: ListDIJobEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobEvents',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_events(
        self,
        request: dataworks_public_20240518_models.ListDIJobEventsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobEventsResponse:
        """
        @summary 获取数据集成任务事件
        
        @param request: ListDIJobEventsRequest
        @return: ListDIJobEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dijob_events_with_options(request, runtime)

    async def list_dijob_events_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobEventsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobEventsResponse:
        """
        @summary 获取数据集成任务事件
        
        @param request: ListDIJobEventsRequest
        @return: ListDIJobEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dijob_events_with_options_async(request, runtime)

    def list_dijob_metrics_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListDIJobMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobMetricsResponse:
        """
        @summary 获取数据集成任务指标
        
        @param tmp_req: ListDIJobMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobMetricsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListDIJobMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_name):
            request.metric_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_name, 'MetricName', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobMetrics',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_metrics_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListDIJobMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobMetricsResponse:
        """
        @summary 获取数据集成任务指标
        
        @param tmp_req: ListDIJobMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobMetricsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListDIJobMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_name):
            request.metric_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_name, 'MetricName', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobMetrics',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_metrics(
        self,
        request: dataworks_public_20240518_models.ListDIJobMetricsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobMetricsResponse:
        """
        @summary 获取数据集成任务指标
        
        @param request: ListDIJobMetricsRequest
        @return: ListDIJobMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dijob_metrics_with_options(request, runtime)

    async def list_dijob_metrics_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobMetricsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobMetricsResponse:
        """
        @summary 获取数据集成任务指标
        
        @param request: ListDIJobMetricsRequest
        @return: ListDIJobMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dijob_metrics_with_options_async(request, runtime)

    def list_dijob_run_details_with_options(
        self,
        request: dataworks_public_20240518_models.ListDIJobRunDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobRunDetailsResponse:
        """
        @summary 获取数据集成运行信息
        
        @param request: ListDIJobRunDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobRunDetailsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobRunDetails',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobRunDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_run_details_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobRunDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobRunDetailsResponse:
        """
        @summary 获取数据集成运行信息
        
        @param request: ListDIJobRunDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobRunDetailsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobRunDetails',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobRunDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_run_details(
        self,
        request: dataworks_public_20240518_models.ListDIJobRunDetailsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobRunDetailsResponse:
        """
        @summary 获取数据集成运行信息
        
        @param request: ListDIJobRunDetailsRequest
        @return: ListDIJobRunDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dijob_run_details_with_options(request, runtime)

    async def list_dijob_run_details_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobRunDetailsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobRunDetailsResponse:
        """
        @summary 获取数据集成运行信息
        
        @param request: ListDIJobRunDetailsRequest
        @return: ListDIJobRunDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dijob_run_details_with_options_async(request, runtime)

    def list_dijobs_with_options(
        self,
        request: dataworks_public_20240518_models.ListDIJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobsResponse:
        """
        @summary Queries a list of synchronization tasks.
        
        @param request: ListDIJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijobs_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDIJobsResponse:
        """
        @summary Queries a list of synchronization tasks.
        
        @param request: ListDIJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDIJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIJobs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDIJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijobs(
        self,
        request: dataworks_public_20240518_models.ListDIJobsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobsResponse:
        """
        @summary Queries a list of synchronization tasks.
        
        @param request: ListDIJobsRequest
        @return: ListDIJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dijobs_with_options(request, runtime)

    async def list_dijobs_async(
        self,
        request: dataworks_public_20240518_models.ListDIJobsRequest,
    ) -> dataworks_public_20240518_models.ListDIJobsResponse:
        """
        @summary Queries a list of synchronization tasks.
        
        @param request: ListDIJobsRequest
        @return: ListDIJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dijobs_with_options_async(request, runtime)

    def list_data_quality_evaluation_task_instances_with_options(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse:
        """
        @summary Queries a list of instances generated by a data quality monitoring task by page.
        
        @param request: ListDataQualityEvaluationTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityEvaluationTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityEvaluationTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_evaluation_task_instances_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse:
        """
        @summary Queries a list of instances generated by a data quality monitoring task by page.
        
        @param request: ListDataQualityEvaluationTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityEvaluationTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityEvaluationTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_evaluation_task_instances(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse:
        """
        @summary Queries a list of instances generated by a data quality monitoring task by page.
        
        @param request: ListDataQualityEvaluationTaskInstancesRequest
        @return: ListDataQualityEvaluationTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_quality_evaluation_task_instances_with_options(request, runtime)

    async def list_data_quality_evaluation_task_instances_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTaskInstancesResponse:
        """
        @summary Queries a list of instances generated by a data quality monitoring task by page.
        
        @param request: ListDataQualityEvaluationTaskInstancesRequest
        @return: ListDataQualityEvaluationTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_quality_evaluation_task_instances_with_options_async(request, runtime)

    def list_data_quality_evaluation_tasks_with_options(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse:
        """
        @summary Queries a list of data quality monitoring tasks by page.
        
        @param request: ListDataQualityEvaluationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityEvaluationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityEvaluationTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_evaluation_tasks_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse:
        """
        @summary Queries a list of data quality monitoring tasks by page.
        
        @param request: ListDataQualityEvaluationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityEvaluationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityEvaluationTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_evaluation_tasks(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTasksRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse:
        """
        @summary Queries a list of data quality monitoring tasks by page.
        
        @param request: ListDataQualityEvaluationTasksRequest
        @return: ListDataQualityEvaluationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_quality_evaluation_tasks_with_options(request, runtime)

    async def list_data_quality_evaluation_tasks_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityEvaluationTasksRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityEvaluationTasksResponse:
        """
        @summary Queries a list of data quality monitoring tasks by page.
        
        @param request: ListDataQualityEvaluationTasksRequest
        @return: ListDataQualityEvaluationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_quality_evaluation_tasks_with_options_async(request, runtime)

    def list_data_quality_results_with_options(
        self,
        request: dataworks_public_20240518_models.ListDataQualityResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityResultsResponse:
        """
        @param request: ListDataQualityResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityResultsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityResults',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_results_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityResultsResponse:
        """
        @param request: ListDataQualityResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityResultsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityResults',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_results(
        self,
        request: dataworks_public_20240518_models.ListDataQualityResultsRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityResultsResponse:
        """
        @param request: ListDataQualityResultsRequest
        @return: ListDataQualityResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_quality_results_with_options(request, runtime)

    async def list_data_quality_results_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityResultsRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityResultsResponse:
        """
        @param request: ListDataQualityResultsRequest
        @return: ListDataQualityResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_quality_results_with_options_async(request, runtime)

    def list_data_quality_rules_with_options(
        self,
        request: dataworks_public_20240518_models.ListDataQualityRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityRulesResponse:
        """
        @summary Queries a list of data quality monitoring rules by page.
        
        @param request: ListDataQualityRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_rules_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataQualityRulesResponse:
        """
        @summary Queries a list of data quality monitoring rules by page.
        
        @param request: ListDataQualityRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataQualityRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataQualityRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataQualityRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_rules(
        self,
        request: dataworks_public_20240518_models.ListDataQualityRulesRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityRulesResponse:
        """
        @summary Queries a list of data quality monitoring rules by page.
        
        @param request: ListDataQualityRulesRequest
        @return: ListDataQualityRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_quality_rules_with_options(request, runtime)

    async def list_data_quality_rules_async(
        self,
        request: dataworks_public_20240518_models.ListDataQualityRulesRequest,
    ) -> dataworks_public_20240518_models.ListDataQualityRulesResponse:
        """
        @summary Queries a list of data quality monitoring rules by page.
        
        @param request: ListDataQualityRulesRequest
        @return: ListDataQualityRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_quality_rules_with_options_async(request, runtime)

    def list_data_source_shared_rules_with_options(
        self,
        request: dataworks_public_20240518_models.ListDataSourceSharedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataSourceSharedRulesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourceSharedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceSharedRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceSharedRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataSourceSharedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_shared_rules_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDataSourceSharedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataSourceSharedRulesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourceSharedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceSharedRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceSharedRules',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataSourceSharedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_shared_rules(
        self,
        request: dataworks_public_20240518_models.ListDataSourceSharedRulesRequest,
    ) -> dataworks_public_20240518_models.ListDataSourceSharedRulesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourceSharedRulesRequest
        @return: ListDataSourceSharedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_shared_rules_with_options(request, runtime)

    async def list_data_source_shared_rules_async(
        self,
        request: dataworks_public_20240518_models.ListDataSourceSharedRulesRequest,
    ) -> dataworks_public_20240518_models.ListDataSourceSharedRulesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourceSharedRulesRequest
        @return: ListDataSourceSharedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_shared_rules_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataSourcesResponse:
        """
        @summary 验证用
        
        @param tmp_req: ListDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDataSourcesResponse:
        """
        @summary 验证用
        
        @param tmp_req: ListDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: dataworks_public_20240518_models.ListDataSourcesRequest,
    ) -> dataworks_public_20240518_models.ListDataSourcesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: dataworks_public_20240518_models.ListDataSourcesRequest,
    ) -> dataworks_public_20240518_models.ListDataSourcesResponse:
        """
        @summary 验证用
        
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_deployments_with_options(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary Queries a list of processes that are used to deploy or undeploy entities in DataStudio. You can also specify filter conditions to query specific processes.
        
        @param request: ListDeploymentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary Queries a list of processes that are used to deploy or undeploy entities in DataStudio. You can also specify filter conditions to query specific processes.
        
        @param request: ListDeploymentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary Queries a list of processes that are used to deploy or undeploy entities in DataStudio. You can also specify filter conditions to query specific processes.
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployments_with_options(request, runtime)

    async def list_deployments_async(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary Queries a list of processes that are used to deploy or undeploy entities in DataStudio. You can also specify filter conditions to query specific processes.
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_deployments_with_options_async(request, runtime)

    def list_downstream_task_instances_with_options(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse:
        """
        @param request: ListDownstreamTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownstreamTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownstreamTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_downstream_task_instances_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse:
        """
        @param request: ListDownstreamTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownstreamTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownstreamTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_downstream_task_instances(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse:
        """
        @param request: ListDownstreamTaskInstancesRequest
        @return: ListDownstreamTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_downstream_task_instances_with_options(request, runtime)

    async def list_downstream_task_instances_async(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListDownstreamTaskInstancesResponse:
        """
        @param request: ListDownstreamTaskInstancesRequest
        @return: ListDownstreamTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_downstream_task_instances_with_options_async(request, runtime)

    def list_downstream_tasks_with_options(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDownstreamTasksResponse:
        """
        @param request: ListDownstreamTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownstreamTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownstreamTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDownstreamTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_downstream_tasks_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDownstreamTasksResponse:
        """
        @param request: ListDownstreamTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownstreamTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownstreamTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDownstreamTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_downstream_tasks(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTasksRequest,
    ) -> dataworks_public_20240518_models.ListDownstreamTasksResponse:
        """
        @param request: ListDownstreamTasksRequest
        @return: ListDownstreamTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_downstream_tasks_with_options(request, runtime)

    async def list_downstream_tasks_async(
        self,
        request: dataworks_public_20240518_models.ListDownstreamTasksRequest,
    ) -> dataworks_public_20240518_models.ListDownstreamTasksResponse:
        """
        @param request: ListDownstreamTasksRequest
        @return: ListDownstreamTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_downstream_tasks_with_options_async(request, runtime)

    def list_functions_with_options(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary Queries a list of user-defined functions (UDFs) in DataStudio. You can also specify filter conditions to query specific UDFs.
        
        @param request: ListFunctionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary Queries a list of user-defined functions (UDFs) in DataStudio. You can also specify filter conditions to query specific UDFs.
        
        @param request: ListFunctionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary Queries a list of user-defined functions (UDFs) in DataStudio. You can also specify filter conditions to query specific UDFs.
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_functions_with_options(request, runtime)

    async def list_functions_async(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary Queries a list of user-defined functions (UDFs) in DataStudio. You can also specify filter conditions to query specific UDFs.
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_functions_with_options_async(request, runtime)

    def list_networks_with_options(
        self,
        request: dataworks_public_20240518_models.ListNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNetworksResponse:
        """
        @summary 获取通用资源组网络资源列表。
        
        @param request: ListNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_networks_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNetworksResponse:
        """
        @summary 获取通用资源组网络资源列表。
        
        @param request: ListNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNetworksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_networks(
        self,
        request: dataworks_public_20240518_models.ListNetworksRequest,
    ) -> dataworks_public_20240518_models.ListNetworksResponse:
        """
        @summary 获取通用资源组网络资源列表。
        
        @param request: ListNetworksRequest
        @return: ListNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_networks_with_options(request, runtime)

    async def list_networks_async(
        self,
        request: dataworks_public_20240518_models.ListNetworksRequest,
    ) -> dataworks_public_20240518_models.ListNetworksResponse:
        """
        @summary 获取通用资源组网络资源列表。
        
        @param request: ListNetworksRequest
        @return: ListNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_networks_with_options_async(request, runtime)

    def list_node_dependencies_with_options(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary Queries a list of descendant nodes of a node in DataStudio.
        
        @param request: ListNodeDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDependenciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodeDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_dependencies_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary Queries a list of descendant nodes of a node in DataStudio.
        
        @param request: ListNodeDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDependenciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodeDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_dependencies(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary Queries a list of descendant nodes of a node in DataStudio.
        
        @param request: ListNodeDependenciesRequest
        @return: ListNodeDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_dependencies_with_options(request, runtime)

    async def list_node_dependencies_async(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary Queries a list of descendant nodes of a node in DataStudio.
        
        @param request: ListNodeDependenciesRequest
        @return: ListNodeDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_dependencies_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary Queries a list of nodes in DataStudio. You can also specify filter conditions to query specific nodes.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary Queries a list of nodes in DataStudio. You can also specify filter conditions to query specific nodes.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary Queries a list of nodes in DataStudio. You can also specify filter conditions to query specific nodes.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary Queries a list of nodes in DataStudio. You can also specify filter conditions to query specific nodes.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_project_members_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectMembersResponse:
        """
        @summary Queries details about members in a workspace.
        
        @param tmp_req: ListProjectMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_ids_shrink):
            body['UserIds'] = request.user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectMembersResponse:
        """
        @summary Queries details about members in a workspace.
        
        @param tmp_req: ListProjectMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_ids_shrink):
            body['UserIds'] = request.user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        request: dataworks_public_20240518_models.ListProjectMembersRequest,
    ) -> dataworks_public_20240518_models.ListProjectMembersResponse:
        """
        @summary Queries details about members in a workspace.
        
        @param request: ListProjectMembersRequest
        @return: ListProjectMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    async def list_project_members_async(
        self,
        request: dataworks_public_20240518_models.ListProjectMembersRequest,
    ) -> dataworks_public_20240518_models.ListProjectMembersResponse:
        """
        @summary Queries details about members in a workspace.
        
        @param request: ListProjectMembersRequest
        @return: ListProjectMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_members_with_options_async(request, runtime)

    def list_project_roles_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectRolesResponse:
        """
        @summary 分页查询工作空间角色详情
        
        @param tmp_req: ListProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not UtilClient.is_unset(request.codes_shrink):
            body['Codes'] = request.codes_shrink
        if not UtilClient.is_unset(request.names_shrink):
            body['Names'] = request.names_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_roles_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectRolesResponse:
        """
        @summary 分页查询工作空间角色详情
        
        @param tmp_req: ListProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not UtilClient.is_unset(request.codes_shrink):
            body['Codes'] = request.codes_shrink
        if not UtilClient.is_unset(request.names_shrink):
            body['Names'] = request.names_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_roles(
        self,
        request: dataworks_public_20240518_models.ListProjectRolesRequest,
    ) -> dataworks_public_20240518_models.ListProjectRolesResponse:
        """
        @summary 分页查询工作空间角色详情
        
        @param request: ListProjectRolesRequest
        @return: ListProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    async def list_project_roles_async(
        self,
        request: dataworks_public_20240518_models.ListProjectRolesRequest,
    ) -> dataworks_public_20240518_models.ListProjectRolesResponse:
        """
        @summary 分页查询工作空间角色详情
        
        @param request: ListProjectRolesRequest
        @return: ListProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_roles_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectsResponse:
        """
        @summary 分页查询工作空间详情
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not UtilClient.is_unset(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not UtilClient.is_unset(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.names_shrink):
            body['Names'] = request.names_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListProjectsResponse:
        """
        @summary 分页查询工作空间详情
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not UtilClient.is_unset(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not UtilClient.is_unset(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.names_shrink):
            body['Names'] = request.names_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: dataworks_public_20240518_models.ListProjectsRequest,
    ) -> dataworks_public_20240518_models.ListProjectsResponse:
        """
        @summary 分页查询工作空间详情
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: dataworks_public_20240518_models.ListProjectsRequest,
    ) -> dataworks_public_20240518_models.ListProjectsResponse:
        """
        @summary 分页查询工作空间详情
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourceGroupsResponse:
        """
        @summary 获取资源组列表。
        
        @param tmp_req: ListResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListResourceGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_group_types):
            request.resource_group_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_group_types, 'ResourceGroupTypes', 'json')
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourceGroupsResponse:
        """
        @summary 获取资源组列表。
        
        @param tmp_req: ListResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListResourceGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_group_types):
            request.resource_group_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_group_types, 'ResourceGroupTypes', 'json')
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: dataworks_public_20240518_models.ListResourceGroupsRequest,
    ) -> dataworks_public_20240518_models.ListResourceGroupsResponse:
        """
        @summary 获取资源组列表。
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: dataworks_public_20240518_models.ListResourceGroupsRequest,
    ) -> dataworks_public_20240518_models.ListResourceGroupsResponse:
        """
        @summary 获取资源组列表。
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary Queries a list of file resources in DataStudio. You can also specify filter conditions to query specific file resources.
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary Queries a list of file resources in DataStudio. You can also specify filter conditions to query specific file resources.
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary Queries a list of file resources in DataStudio. You can also specify filter conditions to query specific file resources.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary Queries a list of file resources in DataStudio. You can also specify filter conditions to query specific file resources.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_routes_with_options(
        self,
        request: dataworks_public_20240518_models.ListRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListRoutesResponse:
        """
        @summary 获取网络资源的路由列表。
        
        @param request: ListRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoutes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_routes_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListRoutesResponse:
        """
        @summary 获取网络资源的路由列表。
        
        @param request: ListRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoutes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_routes(
        self,
        request: dataworks_public_20240518_models.ListRoutesRequest,
    ) -> dataworks_public_20240518_models.ListRoutesResponse:
        """
        @summary 获取网络资源的路由列表。
        
        @param request: ListRoutesRequest
        @return: ListRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_routes_with_options(request, runtime)

    async def list_routes_async(
        self,
        request: dataworks_public_20240518_models.ListRoutesRequest,
    ) -> dataworks_public_20240518_models.ListRoutesResponse:
        """
        @summary 获取网络资源的路由列表。
        
        @param request: ListRoutesRequest
        @return: ListRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_routes_with_options_async(request, runtime)

    def list_task_instance_operation_logs_with_options(
        self,
        request: dataworks_public_20240518_models.ListTaskInstanceOperationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse:
        """
        @param request: ListTaskInstanceOperationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstanceOperationLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskInstanceOperationLogs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_instance_operation_logs_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListTaskInstanceOperationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse:
        """
        @param request: ListTaskInstanceOperationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstanceOperationLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskInstanceOperationLogs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_instance_operation_logs(
        self,
        request: dataworks_public_20240518_models.ListTaskInstanceOperationLogsRequest,
    ) -> dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse:
        """
        @param request: ListTaskInstanceOperationLogsRequest
        @return: ListTaskInstanceOperationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_instance_operation_logs_with_options(request, runtime)

    async def list_task_instance_operation_logs_async(
        self,
        request: dataworks_public_20240518_models.ListTaskInstanceOperationLogsRequest,
    ) -> dataworks_public_20240518_models.ListTaskInstanceOperationLogsResponse:
        """
        @param request: ListTaskInstanceOperationLogsRequest
        @return: ListTaskInstanceOperationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_instance_operation_logs_with_options_async(request, runtime)

    def list_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ListTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskInstancesResponse:
        """
        @param tmp_req: ListTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not UtilClient.is_unset(request.sort_by):
            body['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            body['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not UtilClient.is_unset(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workflow_instance_id):
            body['WorkflowInstanceId'] = request.workflow_instance_id
        if not UtilClient.is_unset(request.workflow_instance_type):
            body['WorkflowInstanceType'] = request.workflow_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ListTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskInstancesResponse:
        """
        @param tmp_req: ListTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ListTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not UtilClient.is_unset(request.sort_by):
            body['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            body['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not UtilClient.is_unset(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workflow_instance_id):
            body['WorkflowInstanceId'] = request.workflow_instance_id
        if not UtilClient.is_unset(request.workflow_instance_type):
            body['WorkflowInstanceType'] = request.workflow_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_instances(
        self,
        request: dataworks_public_20240518_models.ListTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListTaskInstancesResponse:
        """
        @param request: ListTaskInstancesRequest
        @return: ListTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_instances_with_options(request, runtime)

    async def list_task_instances_async(
        self,
        request: dataworks_public_20240518_models.ListTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListTaskInstancesResponse:
        """
        @param request: ListTaskInstancesRequest
        @return: ListTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_instances_with_options_async(request, runtime)

    def list_task_operation_logs_with_options(
        self,
        request: dataworks_public_20240518_models.ListTaskOperationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskOperationLogsResponse:
        """
        @param request: ListTaskOperationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskOperationLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskOperationLogs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskOperationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_operation_logs_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListTaskOperationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTaskOperationLogsResponse:
        """
        @param request: ListTaskOperationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskOperationLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskOperationLogs',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTaskOperationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_operation_logs(
        self,
        request: dataworks_public_20240518_models.ListTaskOperationLogsRequest,
    ) -> dataworks_public_20240518_models.ListTaskOperationLogsResponse:
        """
        @param request: ListTaskOperationLogsRequest
        @return: ListTaskOperationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_operation_logs_with_options(request, runtime)

    async def list_task_operation_logs_async(
        self,
        request: dataworks_public_20240518_models.ListTaskOperationLogsRequest,
    ) -> dataworks_public_20240518_models.ListTaskOperationLogsResponse:
        """
        @param request: ListTaskOperationLogsRequest
        @return: ListTaskOperationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_operation_logs_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: dataworks_public_20240518_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTasksResponse:
        """
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not UtilClient.is_unset(request.sort_by):
            body['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not UtilClient.is_unset(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListTasksResponse:
        """
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not UtilClient.is_unset(request.sort_by):
            body['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not UtilClient.is_unset(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: dataworks_public_20240518_models.ListTasksRequest,
    ) -> dataworks_public_20240518_models.ListTasksResponse:
        """
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: dataworks_public_20240518_models.ListTasksRequest,
    ) -> dataworks_public_20240518_models.ListTasksResponse:
        """
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_upstream_task_instances_with_options(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse:
        """
        @param request: ListUpstreamTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpstreamTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpstreamTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upstream_task_instances_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse:
        """
        @param request: ListUpstreamTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpstreamTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpstreamTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upstream_task_instances(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse:
        """
        @param request: ListUpstreamTaskInstancesRequest
        @return: ListUpstreamTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_task_instances_with_options(request, runtime)

    async def list_upstream_task_instances_async(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ListUpstreamTaskInstancesResponse:
        """
        @param request: ListUpstreamTaskInstancesRequest
        @return: ListUpstreamTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_upstream_task_instances_with_options_async(request, runtime)

    def list_upstream_tasks_with_options(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListUpstreamTasksResponse:
        """
        @param request: ListUpstreamTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpstreamTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpstreamTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListUpstreamTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upstream_tasks_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListUpstreamTasksResponse:
        """
        @param request: ListUpstreamTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpstreamTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpstreamTasks',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListUpstreamTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upstream_tasks(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTasksRequest,
    ) -> dataworks_public_20240518_models.ListUpstreamTasksResponse:
        """
        @param request: ListUpstreamTasksRequest
        @return: ListUpstreamTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_tasks_with_options(request, runtime)

    async def list_upstream_tasks_async(
        self,
        request: dataworks_public_20240518_models.ListUpstreamTasksRequest,
    ) -> dataworks_public_20240518_models.ListUpstreamTasksResponse:
        """
        @param request: ListUpstreamTasksRequest
        @return: ListUpstreamTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_upstream_tasks_with_options_async(request, runtime)

    def list_workflow_definitions_with_options(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary Queries a list of workflows in DataStudio. You can also specify filter conditions to query specific workflows.
        
        @param request: ListWorkflowDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDefinitions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListWorkflowDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_definitions_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary Queries a list of workflows in DataStudio. You can also specify filter conditions to query specific workflows.
        
        @param request: ListWorkflowDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDefinitions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListWorkflowDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_definitions(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary Queries a list of workflows in DataStudio. You can also specify filter conditions to query specific workflows.
        
        @param request: ListWorkflowDefinitionsRequest
        @return: ListWorkflowDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_definitions_with_options(request, runtime)

    async def list_workflow_definitions_async(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary Queries a list of workflows in DataStudio. You can also specify filter conditions to query specific workflows.
        
        @param request: ListWorkflowDefinitionsRequest
        @return: ListWorkflowDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workflow_definitions_with_options_async(request, runtime)

    def move_function_with_options(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary Moves a user-defined function (UDF) to a path in DataStudio.
        
        @param request: MoveFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary Moves a user-defined function (UDF) to a path in DataStudio.
        
        @param request: MoveFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_function(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary Moves a user-defined function (UDF) to a path in DataStudio.
        
        @param request: MoveFunctionRequest
        @return: MoveFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_function_with_options(request, runtime)

    async def move_function_async(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary Moves a user-defined function (UDF) to a path in DataStudio.
        
        @param request: MoveFunctionRequest
        @return: MoveFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_function_with_options_async(request, runtime)

    def move_node_with_options(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary Moves a node to a path in DataStudio.
        
        @param request: MoveNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary Moves a node to a path in DataStudio.
        
        @param request: MoveNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_node(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary Moves a node to a path in DataStudio.
        
        @param request: MoveNodeRequest
        @return: MoveNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_node_with_options(request, runtime)

    async def move_node_async(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary Moves a node to a path in DataStudio.
        
        @param request: MoveNodeRequest
        @return: MoveNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_node_with_options_async(request, runtime)

    def move_resource_with_options(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary Moves a file resource to a path in DataStudio.
        
        @param request: MoveResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary Moves a file resource to a path in DataStudio.
        
        @param request: MoveResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary Moves a file resource to a path in DataStudio.
        
        @param request: MoveResourceRequest
        @return: MoveResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_with_options(request, runtime)

    async def move_resource_async(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary Moves a file resource to a path in DataStudio.
        
        @param request: MoveResourceRequest
        @return: MoveResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_with_options_async(request, runtime)

    def move_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary Moves a workflow to a path in DataStudio.
        
        @param request: MoveWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary Moves a workflow to a path in DataStudio.
        
        @param request: MoveWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_workflow_definition(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary Moves a workflow to a path in DataStudio.
        
        @param request: MoveWorkflowDefinitionRequest
        @return: MoveWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_workflow_definition_with_options(request, runtime)

    async def move_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary Moves a workflow to a path in DataStudio.
        
        @param request: MoveWorkflowDefinitionRequest
        @return: MoveWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_workflow_definition_with_options_async(request, runtime)

    def remove_task_instance_dependencies_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.RemoveTaskInstanceDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse:
        """
        @param tmp_req: RemoveTaskInstanceDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTaskInstanceDependenciesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RemoveTaskInstanceDependenciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upstream_task_instance_ids):
            request.upstream_task_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upstream_task_instance_ids, 'UpstreamTaskInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.upstream_task_instance_ids_shrink):
            body['UpstreamTaskInstanceIds'] = request.upstream_task_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveTaskInstanceDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_task_instance_dependencies_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.RemoveTaskInstanceDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse:
        """
        @param tmp_req: RemoveTaskInstanceDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTaskInstanceDependenciesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RemoveTaskInstanceDependenciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upstream_task_instance_ids):
            request.upstream_task_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upstream_task_instance_ids, 'UpstreamTaskInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.upstream_task_instance_ids_shrink):
            body['UpstreamTaskInstanceIds'] = request.upstream_task_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveTaskInstanceDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_task_instance_dependencies(
        self,
        request: dataworks_public_20240518_models.RemoveTaskInstanceDependenciesRequest,
    ) -> dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse:
        """
        @param request: RemoveTaskInstanceDependenciesRequest
        @return: RemoveTaskInstanceDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_task_instance_dependencies_with_options(request, runtime)

    async def remove_task_instance_dependencies_async(
        self,
        request: dataworks_public_20240518_models.RemoveTaskInstanceDependenciesRequest,
    ) -> dataworks_public_20240518_models.RemoveTaskInstanceDependenciesResponse:
        """
        @param request: RemoveTaskInstanceDependenciesRequest
        @return: RemoveTaskInstanceDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_task_instance_dependencies_with_options_async(request, runtime)

    def rename_function_with_options(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary Renames a user-defined function (UDF) in DataStudio.
        
        @param request: RenameFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary Renames a user-defined function (UDF) in DataStudio.
        
        @param request: RenameFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_function(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary Renames a user-defined function (UDF) in DataStudio.
        
        @param request: RenameFunctionRequest
        @return: RenameFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_function_with_options(request, runtime)

    async def rename_function_async(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary Renames a user-defined function (UDF) in DataStudio.
        
        @param request: RenameFunctionRequest
        @return: RenameFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_function_with_options_async(request, runtime)

    def rename_node_with_options(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary Renames a node in DataStudio.
        
        @param request: RenameNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary Renames a node in DataStudio.
        
        @param request: RenameNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_node(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary Renames a node in DataStudio.
        
        @param request: RenameNodeRequest
        @return: RenameNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_node_with_options(request, runtime)

    async def rename_node_async(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary Renames a node in DataStudio.
        
        @param request: RenameNodeRequest
        @return: RenameNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_node_with_options_async(request, runtime)

    def rename_resource_with_options(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary Renames a file resource in DataStudio.
        
        @param request: RenameResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary Renames a file resource in DataStudio.
        
        @param request: RenameResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_resource(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary Renames a file resource in DataStudio.
        
        @param request: RenameResourceRequest
        @return: RenameResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_resource_with_options(request, runtime)

    async def rename_resource_async(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary Renames a file resource in DataStudio.
        
        @param request: RenameResourceRequest
        @return: RenameResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_resource_with_options_async(request, runtime)

    def rename_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary Renames a workflow in DataStudio.
        
        @param request: RenameWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary Renames a workflow in DataStudio.
        
        @param request: RenameWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_workflow_definition(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary Renames a workflow in DataStudio.
        
        @param request: RenameWorkflowDefinitionRequest
        @return: RenameWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_workflow_definition_with_options(request, runtime)

    async def rename_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary Renames a workflow in DataStudio.
        
        @param request: RenameWorkflowDefinitionRequest
        @return: RenameWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_workflow_definition_with_options_async(request, runtime)

    def rerun_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.RerunTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RerunTaskInstancesResponse:
        """
        @param tmp_req: RerunTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RerunTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RerunTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RerunTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.RerunTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RerunTaskInstancesResponse:
        """
        @param tmp_req: RerunTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RerunTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RerunTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RerunTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_task_instances(
        self,
        request: dataworks_public_20240518_models.RerunTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.RerunTaskInstancesResponse:
        """
        @param request: RerunTaskInstancesRequest
        @return: RerunTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rerun_task_instances_with_options(request, runtime)

    async def rerun_task_instances_async(
        self,
        request: dataworks_public_20240518_models.RerunTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.RerunTaskInstancesResponse:
        """
        @param request: RerunTaskInstancesRequest
        @return: RerunTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rerun_task_instances_with_options_async(request, runtime)

    def resume_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.ResumeTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ResumeTaskInstancesResponse:
        """
        @param tmp_req: ResumeTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ResumeTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ResumeTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.ResumeTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ResumeTaskInstancesResponse:
        """
        @param tmp_req: ResumeTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.ResumeTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ResumeTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task_instances(
        self,
        request: dataworks_public_20240518_models.ResumeTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ResumeTaskInstancesResponse:
        """
        @param request: ResumeTaskInstancesRequest
        @return: ResumeTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_task_instances_with_options(request, runtime)

    async def resume_task_instances_async(
        self,
        request: dataworks_public_20240518_models.ResumeTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.ResumeTaskInstancesResponse:
        """
        @param request: ResumeTaskInstancesRequest
        @return: ResumeTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_task_instances_with_options_async(request, runtime)

    def revoke_member_project_roles_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.RevokeMemberProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RevokeMemberProjectRolesResponse:
        """
        @summary Revokes roles that are assigned to a member in a workspace.
        
        @param tmp_req: RevokeMemberProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeMemberProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RevokeMemberProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeMemberProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RevokeMemberProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_member_project_roles_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.RevokeMemberProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RevokeMemberProjectRolesResponse:
        """
        @summary Revokes roles that are assigned to a member in a workspace.
        
        @param tmp_req: RevokeMemberProjectRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeMemberProjectRolesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.RevokeMemberProjectRolesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_codes):
            request.role_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeMemberProjectRoles',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RevokeMemberProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_member_project_roles(
        self,
        request: dataworks_public_20240518_models.RevokeMemberProjectRolesRequest,
    ) -> dataworks_public_20240518_models.RevokeMemberProjectRolesResponse:
        """
        @summary Revokes roles that are assigned to a member in a workspace.
        
        @param request: RevokeMemberProjectRolesRequest
        @return: RevokeMemberProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_member_project_roles_with_options(request, runtime)

    async def revoke_member_project_roles_async(
        self,
        request: dataworks_public_20240518_models.RevokeMemberProjectRolesRequest,
    ) -> dataworks_public_20240518_models.RevokeMemberProjectRolesResponse:
        """
        @summary Revokes roles that are assigned to a member in a workspace.
        
        @param request: RevokeMemberProjectRolesRequest
        @return: RevokeMemberProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_member_project_roles_with_options_async(request, runtime)

    def set_success_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.SetSuccessTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.SetSuccessTaskInstancesResponse:
        """
        @param tmp_req: SetSuccessTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSuccessTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.SetSuccessTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSuccessTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.SetSuccessTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_success_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.SetSuccessTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.SetSuccessTaskInstancesResponse:
        """
        @param tmp_req: SetSuccessTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSuccessTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.SetSuccessTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSuccessTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.SetSuccessTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_success_task_instances(
        self,
        request: dataworks_public_20240518_models.SetSuccessTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.SetSuccessTaskInstancesResponse:
        """
        @param request: SetSuccessTaskInstancesRequest
        @return: SetSuccessTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_success_task_instances_with_options(request, runtime)

    async def set_success_task_instances_async(
        self,
        request: dataworks_public_20240518_models.SetSuccessTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.SetSuccessTaskInstancesResponse:
        """
        @param request: SetSuccessTaskInstancesRequest
        @return: SetSuccessTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_success_task_instances_with_options_async(request, runtime)

    def start_dijob_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.StartDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StartDIJobResponse:
        """
        @summary 启动数据集成任务
        
        @param tmp_req: StartDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.StartDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.realtime_start_settings):
            request.realtime_start_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.realtime_start_settings, 'RealtimeStartSettings', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StartDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dijob_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.StartDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StartDIJobResponse:
        """
        @summary 启动数据集成任务
        
        @param tmp_req: StartDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.StartDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.realtime_start_settings):
            request.realtime_start_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.realtime_start_settings, 'RealtimeStartSettings', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StartDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dijob(
        self,
        request: dataworks_public_20240518_models.StartDIJobRequest,
    ) -> dataworks_public_20240518_models.StartDIJobResponse:
        """
        @summary 启动数据集成任务
        
        @param request: StartDIJobRequest
        @return: StartDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dijob_with_options(request, runtime)

    async def start_dijob_async(
        self,
        request: dataworks_public_20240518_models.StartDIJobRequest,
    ) -> dataworks_public_20240518_models.StartDIJobResponse:
        """
        @summary 启动数据集成任务
        
        @param request: StartDIJobRequest
        @return: StartDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dijob_with_options_async(request, runtime)

    def stop_dijob_with_options(
        self,
        request: dataworks_public_20240518_models.StopDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StopDIJobResponse:
        """
        @summary Stops a synchronization task.
        
        @param request: StopDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StopDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dijob_with_options_async(
        self,
        request: dataworks_public_20240518_models.StopDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StopDIJobResponse:
        """
        @summary Stops a synchronization task.
        
        @param request: StopDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDIJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StopDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dijob(
        self,
        request: dataworks_public_20240518_models.StopDIJobRequest,
    ) -> dataworks_public_20240518_models.StopDIJobResponse:
        """
        @summary Stops a synchronization task.
        
        @param request: StopDIJobRequest
        @return: StopDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dijob_with_options(request, runtime)

    async def stop_dijob_async(
        self,
        request: dataworks_public_20240518_models.StopDIJobRequest,
    ) -> dataworks_public_20240518_models.StopDIJobResponse:
        """
        @summary Stops a synchronization task.
        
        @param request: StopDIJobRequest
        @return: StopDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dijob_with_options_async(request, runtime)

    def stop_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.StopTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StopTaskInstancesResponse:
        """
        @param tmp_req: StopTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.StopTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StopTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.StopTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.StopTaskInstancesResponse:
        """
        @param tmp_req: StopTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.StopTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.StopTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task_instances(
        self,
        request: dataworks_public_20240518_models.StopTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.StopTaskInstancesResponse:
        """
        @param request: StopTaskInstancesRequest
        @return: StopTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_task_instances_with_options(request, runtime)

    async def stop_task_instances_async(
        self,
        request: dataworks_public_20240518_models.StopTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.StopTaskInstancesResponse:
        """
        @param request: StopTaskInstancesRequest
        @return: StopTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_task_instances_with_options_async(request, runtime)

    def suspend_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.SuspendTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.SuspendTaskInstancesResponse:
        """
        @param tmp_req: SuspendTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.SuspendTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.SuspendTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.SuspendTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.SuspendTaskInstancesResponse:
        """
        @param tmp_req: SuspendTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.SuspendTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.SuspendTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_task_instances(
        self,
        request: dataworks_public_20240518_models.SuspendTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.SuspendTaskInstancesResponse:
        """
        @param request: SuspendTaskInstancesRequest
        @return: SuspendTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_task_instances_with_options(request, runtime)

    async def suspend_task_instances_async(
        self,
        request: dataworks_public_20240518_models.SuspendTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.SuspendTaskInstancesResponse:
        """
        @param request: SuspendTaskInstancesRequest
        @return: SuspendTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_task_instances_with_options_async(request, runtime)

    def trigger_scheduler_task_instance_with_options(
        self,
        request: dataworks_public_20240518_models.TriggerSchedulerTaskInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse:
        """
        @param request: TriggerSchedulerTaskInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSchedulerTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.trigger_time):
            body['TriggerTime'] = request.trigger_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerSchedulerTaskInstance',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_scheduler_task_instance_with_options_async(
        self,
        request: dataworks_public_20240518_models.TriggerSchedulerTaskInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse:
        """
        @param request: TriggerSchedulerTaskInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSchedulerTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.trigger_time):
            body['TriggerTime'] = request.trigger_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerSchedulerTaskInstance',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_scheduler_task_instance(
        self,
        request: dataworks_public_20240518_models.TriggerSchedulerTaskInstanceRequest,
    ) -> dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse:
        """
        @param request: TriggerSchedulerTaskInstanceRequest
        @return: TriggerSchedulerTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_scheduler_task_instance_with_options(request, runtime)

    async def trigger_scheduler_task_instance_async(
        self,
        request: dataworks_public_20240518_models.TriggerSchedulerTaskInstanceRequest,
    ) -> dataworks_public_20240518_models.TriggerSchedulerTaskInstanceResponse:
        """
        @param request: TriggerSchedulerTaskInstanceRequest
        @return: TriggerSchedulerTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_scheduler_task_instance_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param tmp_req: UpdateAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlertRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateAlertRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_condition):
            request.trigger_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param tmp_req: UpdateAlertRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlertRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateAlertRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_condition):
            request.trigger_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_rule(
        self,
        request: dataworks_public_20240518_models.UpdateAlertRuleRequest,
    ) -> dataworks_public_20240518_models.UpdateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param request: UpdateAlertRuleRequest
        @return: UpdateAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: dataworks_public_20240518_models.UpdateAlertRuleRequest,
    ) -> dataworks_public_20240518_models.UpdateAlertRuleResponse:
        """
        @summary 创建自定义监控报警规则
        
        @param request: UpdateAlertRuleRequest
        @return: UpdateAlertRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_dialarm_rule_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDIAlarmRuleResponse:
        """
        @summary 更新数据集成报警规则
        
        @param tmp_req: UpdateDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dialarm_rule_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateDIAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDIAlarmRuleResponse:
        """
        @summary 更新数据集成报警规则
        
        @param tmp_req: UpdateDIAlarmRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDIAlarmRule',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dialarm_rule(
        self,
        request: dataworks_public_20240518_models.UpdateDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.UpdateDIAlarmRuleResponse:
        """
        @summary 更新数据集成报警规则
        
        @param request: UpdateDIAlarmRuleRequest
        @return: UpdateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dialarm_rule_with_options(request, runtime)

    async def update_dialarm_rule_async(
        self,
        request: dataworks_public_20240518_models.UpdateDIAlarmRuleRequest,
    ) -> dataworks_public_20240518_models.UpdateDIAlarmRuleResponse:
        """
        @summary 更新数据集成报警规则
        
        @param request: UpdateDIAlarmRuleRequest
        @return: UpdateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dialarm_rule_with_options_async(request, runtime)

    def update_dijob_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDIJobResponse:
        """
        @summary 更新数据集成任务
        
        @param tmp_req: UpdateDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dijob_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateDIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDIJobResponse:
        """
        @summary 更新数据集成任务
        
        @param tmp_req: UpdateDIJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDIJob',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dijob(
        self,
        request: dataworks_public_20240518_models.UpdateDIJobRequest,
    ) -> dataworks_public_20240518_models.UpdateDIJobResponse:
        """
        @summary 更新数据集成任务
        
        @param request: UpdateDIJobRequest
        @return: UpdateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dijob_with_options(request, runtime)

    async def update_dijob_async(
        self,
        request: dataworks_public_20240518_models.UpdateDIJobRequest,
    ) -> dataworks_public_20240518_models.UpdateDIJobResponse:
        """
        @summary 更新数据集成任务
        
        @param request: UpdateDIJobRequest
        @return: UpdateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dijob_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: UpdateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: UpdateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source(
        self,
        request: dataworks_public_20240518_models.UpdateDataSourceRequest,
    ) -> dataworks_public_20240518_models.UpdateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: UpdateDataSourceRequest
        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: dataworks_public_20240518_models.UpdateDataSourceRequest,
    ) -> dataworks_public_20240518_models.UpdateDataSourceResponse:
        """
        @summary 验证用
        
        @param request: UpdateDataSourceRequest
        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_function_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary Updates the basic information about a user-defined function (UDF) in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary Updates the basic information about a user-defined function (UDF) in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary Updates the basic information about a user-defined function (UDF) in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_function_with_options(request, runtime)

    async def update_function_async(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary Updates the basic information about a user-defined function (UDF) in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_function_with_options_async(request, runtime)

    def update_node_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary Updates the basic information about a node in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary Updates the basic information about a node in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary Updates the basic information about a node in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateNodeRequest
        @return: UpdateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_node_with_options(request, runtime)

    async def update_node_async(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary Updates the basic information about a node in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateNodeRequest
        @return: UpdateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_node_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateProjectResponse:
        """
        @summary 更新工作空间
        
        @param request: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateProjectResponse:
        """
        @summary 更新工作空间
        
        @param request: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not UtilClient.is_unset(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: dataworks_public_20240518_models.UpdateProjectRequest,
    ) -> dataworks_public_20240518_models.UpdateProjectResponse:
        """
        @summary 更新工作空间
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: dataworks_public_20240518_models.UpdateProjectRequest,
    ) -> dataworks_public_20240518_models.UpdateProjectResponse:
        """
        @summary 更新工作空间
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_resource_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary Updates the basic information about a file resource in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary Updates the basic information about a file resource in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary Updates the basic information about a file resource in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    async def update_resource_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary Updates the basic information about a file resource in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_with_options_async(request, runtime)

    def update_resource_group_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceGroupResponse:
        """
        @summary Updates basic information about a resource group.
        
        @param request: UpdateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceGroupResponse:
        """
        @summary Updates basic information about a resource group.
        
        @param request: UpdateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        request: dataworks_public_20240518_models.UpdateResourceGroupRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceGroupResponse:
        """
        @summary Updates basic information about a resource group.
        
        @param request: UpdateResourceGroupRequest
        @return: UpdateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceGroupRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceGroupResponse:
        """
        @summary Updates basic information about a resource group.
        
        @param request: UpdateResourceGroupRequest
        @return: UpdateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_route_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateRouteResponse:
        """
        @summary 更新网络资源的路由。
        
        @param request: UpdateRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_route_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateRouteResponse:
        """
        @summary 更新网络资源的路由。
        
        @param request: UpdateRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoute',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_route(
        self,
        request: dataworks_public_20240518_models.UpdateRouteRequest,
    ) -> dataworks_public_20240518_models.UpdateRouteResponse:
        """
        @summary 更新网络资源的路由。
        
        @param request: UpdateRouteRequest
        @return: UpdateRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_route_with_options(request, runtime)

    async def update_route_async(
        self,
        request: dataworks_public_20240518_models.UpdateRouteRequest,
    ) -> dataworks_public_20240518_models.UpdateRouteResponse:
        """
        @summary 更新网络资源的路由。
        
        @param request: UpdateRouteRequest
        @return: UpdateRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_route_with_options_async(request, runtime)

    def update_task_instances_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateTaskInstancesResponse:
        """
        @param tmp_req: UpdateTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_instances):
            request.task_instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_instances, 'TaskInstances', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.task_instances_shrink):
            body['TaskInstances'] = request.task_instances_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_instances_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.UpdateTaskInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateTaskInstancesResponse:
        """
        @param tmp_req: UpdateTaskInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.UpdateTaskInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_instances):
            request.task_instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_instances, 'TaskInstances', 'json')
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.task_instances_shrink):
            body['TaskInstances'] = request.task_instances_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskInstances',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_instances(
        self,
        request: dataworks_public_20240518_models.UpdateTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.UpdateTaskInstancesResponse:
        """
        @param request: UpdateTaskInstancesRequest
        @return: UpdateTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_task_instances_with_options(request, runtime)

    async def update_task_instances_async(
        self,
        request: dataworks_public_20240518_models.UpdateTaskInstancesRequest,
    ) -> dataworks_public_20240518_models.UpdateTaskInstancesResponse:
        """
        @param request: UpdateTaskInstancesRequest
        @return: UpdateTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_task_instances_with_options_async(request, runtime)

    def update_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary Updates the basic information about a workflow in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary Updates the basic information about a workflow in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_definition(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary Updates the basic information about a workflow in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateWorkflowDefinitionRequest
        @return: UpdateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_definition_with_options(request, runtime)

    async def update_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary Updates the basic information about a workflow in DataStudio. This API operation performs an incremental update. The update information is described by using FlowSpec.
        
        @param request: UpdateWorkflowDefinitionRequest
        @return: UpdateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workflow_definition_with_options_async(request, runtime)
