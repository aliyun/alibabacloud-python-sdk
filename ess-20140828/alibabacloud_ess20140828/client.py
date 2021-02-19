# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20140828 import models as ess_20140828_models
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
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'ess.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_dbinstances_with_options(
        self,
        request: ess_20140828_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachDBInstancesResponse().from_map(
            self.do_rpcrequest('AttachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_dbinstances_with_options_async(
        self,
        request: ess_20140828_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachDBInstancesResponse().from_map(
            await self.do_rpcrequest_async('AttachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_dbinstances(
        self,
        request: ess_20140828_models.AttachDBInstancesRequest,
    ) -> ess_20140828_models.AttachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    async def attach_dbinstances_async(
        self,
        request: ess_20140828_models.AttachDBInstancesRequest,
    ) -> ess_20140828_models.AttachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_dbinstances_with_options_async(request, runtime)

    def attach_instances_with_options(
        self,
        request: ess_20140828_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachInstancesResponse().from_map(
            self.do_rpcrequest('AttachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        request: ess_20140828_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachInstancesResponse().from_map(
            await self.do_rpcrequest_async('AttachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_instances(
        self,
        request: ess_20140828_models.AttachInstancesRequest,
    ) -> ess_20140828_models.AttachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    async def attach_instances_async(
        self,
        request: ess_20140828_models.AttachInstancesRequest,
    ) -> ess_20140828_models.AttachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_instances_with_options_async(request, runtime)

    def attach_load_balancers_with_options(
        self,
        request: ess_20140828_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachLoadBalancersResponse().from_map(
            self.do_rpcrequest('AttachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_load_balancers_with_options_async(
        self,
        request: ess_20140828_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachLoadBalancersResponse().from_map(
            await self.do_rpcrequest_async('AttachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_load_balancers(
        self,
        request: ess_20140828_models.AttachLoadBalancersRequest,
    ) -> ess_20140828_models.AttachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    async def attach_load_balancers_async(
        self,
        request: ess_20140828_models.AttachLoadBalancersRequest,
    ) -> ess_20140828_models.AttachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_load_balancers_with_options_async(request, runtime)

    def attach_vserver_groups_with_options(
        self,
        request: ess_20140828_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachVServerGroupsResponse().from_map(
            self.do_rpcrequest('AttachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_vserver_groups_with_options_async(
        self,
        request: ess_20140828_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.AttachVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.AttachVServerGroupsResponse().from_map(
            await self.do_rpcrequest_async('AttachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_vserver_groups(
        self,
        request: ess_20140828_models.AttachVServerGroupsRequest,
    ) -> ess_20140828_models.AttachVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    async def attach_vserver_groups_async(
        self,
        request: ess_20140828_models.AttachVServerGroupsRequest,
    ) -> ess_20140828_models.AttachVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_vserver_groups_with_options_async(request, runtime)

    def complete_lifecycle_action_with_options(
        self,
        request: ess_20140828_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CompleteLifecycleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CompleteLifecycleActionResponse().from_map(
            self.do_rpcrequest('CompleteLifecycleAction', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_lifecycle_action_with_options_async(
        self,
        request: ess_20140828_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CompleteLifecycleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CompleteLifecycleActionResponse().from_map(
            await self.do_rpcrequest_async('CompleteLifecycleAction', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_lifecycle_action(
        self,
        request: ess_20140828_models.CompleteLifecycleActionRequest,
    ) -> ess_20140828_models.CompleteLifecycleActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    async def complete_lifecycle_action_async(
        self,
        request: ess_20140828_models.CompleteLifecycleActionRequest,
    ) -> ess_20140828_models.CompleteLifecycleActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_lifecycle_action_with_options_async(request, runtime)

    def create_alarm_with_options(
        self,
        request: ess_20140828_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateAlarmResponse().from_map(
            self.do_rpcrequest('CreateAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        request: ess_20140828_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateAlarmResponse().from_map(
            await self.do_rpcrequest_async('CreateAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alarm(
        self,
        request: ess_20140828_models.CreateAlarmRequest,
    ) -> ess_20140828_models.CreateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    async def create_alarm_async(
        self,
        request: ess_20140828_models.CreateAlarmRequest,
    ) -> ess_20140828_models.CreateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_with_options_async(request, runtime)

    def create_lifecycle_hook_with_options(
        self,
        request: ess_20140828_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateLifecycleHookResponse().from_map(
            self.do_rpcrequest('CreateLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_lifecycle_hook_with_options_async(
        self,
        request: ess_20140828_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateLifecycleHookResponse().from_map(
            await self.do_rpcrequest_async('CreateLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_lifecycle_hook(
        self,
        request: ess_20140828_models.CreateLifecycleHookRequest,
    ) -> ess_20140828_models.CreateLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    async def create_lifecycle_hook_async(
        self,
        request: ess_20140828_models.CreateLifecycleHookRequest,
    ) -> ess_20140828_models.CreateLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_hook_with_options_async(request, runtime)

    def create_notification_configuration_with_options(
        self,
        request: ess_20140828_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateNotificationConfigurationResponse().from_map(
            self.do_rpcrequest('CreateNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_notification_configuration_with_options_async(
        self,
        request: ess_20140828_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateNotificationConfigurationResponse().from_map(
            await self.do_rpcrequest_async('CreateNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_notification_configuration(
        self,
        request: ess_20140828_models.CreateNotificationConfigurationRequest,
    ) -> ess_20140828_models.CreateNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    async def create_notification_configuration_async(
        self,
        request: ess_20140828_models.CreateNotificationConfigurationRequest,
    ) -> ess_20140828_models.CreateNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_notification_configuration_with_options_async(request, runtime)

    def create_scaling_configuration_with_options(
        self,
        tmp_req: ess_20140828_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingConfigurationResponse().from_map(
            self.do_rpcrequest('CreateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20140828_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingConfigurationResponse().from_map(
            await self.do_rpcrequest_async('CreateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_configuration(
        self,
        request: ess_20140828_models.CreateScalingConfigurationRequest,
    ) -> ess_20140828_models.CreateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    async def create_scaling_configuration_async(
        self,
        request: ess_20140828_models.CreateScalingConfigurationRequest,
    ) -> ess_20140828_models.CreateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_configuration_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: ess_20140828_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingGroupResponse().from_map(
            self.do_rpcrequest('CreateScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: ess_20140828_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_group(
        self,
        request: ess_20140828_models.CreateScalingGroupRequest,
    ) -> ess_20140828_models.CreateScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: ess_20140828_models.CreateScalingGroupRequest,
    ) -> ess_20140828_models.CreateScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: ess_20140828_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingRuleResponse().from_map(
            self.do_rpcrequest('CreateScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: ess_20140828_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_rule(
        self,
        request: ess_20140828_models.CreateScalingRuleRequest,
    ) -> ess_20140828_models.CreateScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: ess_20140828_models.CreateScalingRuleRequest,
    ) -> ess_20140828_models.CreateScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: ess_20140828_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScheduledTaskResponse().from_map(
            self.do_rpcrequest('CreateScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: ess_20140828_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.CreateScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.CreateScheduledTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scheduled_task(
        self,
        request: ess_20140828_models.CreateScheduledTaskRequest,
    ) -> ess_20140828_models.CreateScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: ess_20140828_models.CreateScheduledTaskRequest,
    ) -> ess_20140828_models.CreateScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def deactivate_scaling_configuration_with_options(
        self,
        request: ess_20140828_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeactivateScalingConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeactivateScalingConfigurationResponse().from_map(
            self.do_rpcrequest('DeactivateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactivate_scaling_configuration_with_options_async(
        self,
        request: ess_20140828_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeactivateScalingConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeactivateScalingConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DeactivateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_scaling_configuration(
        self,
        request: ess_20140828_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20140828_models.DeactivateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    async def deactivate_scaling_configuration_async(
        self,
        request: ess_20140828_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20140828_models.DeactivateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_scaling_configuration_with_options_async(request, runtime)

    def delete_alarm_with_options(
        self,
        request: ess_20140828_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteAlarmResponse().from_map(
            self.do_rpcrequest('DeleteAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alarm_with_options_async(
        self,
        request: ess_20140828_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteAlarmResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alarm(
        self,
        request: ess_20140828_models.DeleteAlarmRequest,
    ) -> ess_20140828_models.DeleteAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    async def delete_alarm_async(
        self,
        request: ess_20140828_models.DeleteAlarmRequest,
    ) -> ess_20140828_models.DeleteAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_with_options_async(request, runtime)

    def delete_lifecycle_hook_with_options(
        self,
        request: ess_20140828_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteLifecycleHookResponse().from_map(
            self.do_rpcrequest('DeleteLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_lifecycle_hook_with_options_async(
        self,
        request: ess_20140828_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteLifecycleHookResponse().from_map(
            await self.do_rpcrequest_async('DeleteLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_lifecycle_hook(
        self,
        request: ess_20140828_models.DeleteLifecycleHookRequest,
    ) -> ess_20140828_models.DeleteLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    async def delete_lifecycle_hook_async(
        self,
        request: ess_20140828_models.DeleteLifecycleHookRequest,
    ) -> ess_20140828_models.DeleteLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lifecycle_hook_with_options_async(request, runtime)

    def delete_notification_configuration_with_options(
        self,
        request: ess_20140828_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteNotificationConfigurationResponse().from_map(
            self.do_rpcrequest('DeleteNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_notification_configuration_with_options_async(
        self,
        request: ess_20140828_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteNotificationConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DeleteNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_notification_configuration(
        self,
        request: ess_20140828_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20140828_models.DeleteNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    async def delete_notification_configuration_async(
        self,
        request: ess_20140828_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20140828_models.DeleteNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_configuration_with_options_async(request, runtime)

    def delete_scaling_configuration_with_options(
        self,
        request: ess_20140828_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingConfigurationResponse().from_map(
            self.do_rpcrequest('DeleteScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scaling_configuration_with_options_async(
        self,
        request: ess_20140828_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DeleteScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_configuration(
        self,
        request: ess_20140828_models.DeleteScalingConfigurationRequest,
    ) -> ess_20140828_models.DeleteScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    async def delete_scaling_configuration_async(
        self,
        request: ess_20140828_models.DeleteScalingConfigurationRequest,
    ) -> ess_20140828_models.DeleteScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_configuration_with_options_async(request, runtime)

    def delete_scaling_group_with_options(
        self,
        request: ess_20140828_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingGroupResponse().from_map(
            self.do_rpcrequest('DeleteScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scaling_group_with_options_async(
        self,
        request: ess_20140828_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_group(
        self,
        request: ess_20140828_models.DeleteScalingGroupRequest,
    ) -> ess_20140828_models.DeleteScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    async def delete_scaling_group_async(
        self,
        request: ess_20140828_models.DeleteScalingGroupRequest,
    ) -> ess_20140828_models.DeleteScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_group_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: ess_20140828_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingRuleResponse().from_map(
            self.do_rpcrequest('DeleteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: ess_20140828_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: ess_20140828_models.DeleteScalingRuleRequest,
    ) -> ess_20140828_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: ess_20140828_models.DeleteScalingRuleRequest,
    ) -> ess_20140828_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_scheduled_task_with_options(
        self,
        request: ess_20140828_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScheduledTaskResponse().from_map(
            self.do_rpcrequest('DeleteScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: ess_20140828_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DeleteScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DeleteScheduledTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: ess_20140828_models.DeleteScheduledTaskRequest,
    ) -> ess_20140828_models.DeleteScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: ess_20140828_models.DeleteScheduledTaskRequest,
    ) -> ess_20140828_models.DeleteScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: ess_20140828_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeAlarmsResponse().from_map(
            self.do_rpcrequest('DescribeAlarms', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: ess_20140828_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeAlarmsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAlarms', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarms(
        self,
        request: ess_20140828_models.DescribeAlarmsRequest,
    ) -> ess_20140828_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: ess_20140828_models.DescribeAlarmsRequest,
    ) -> ess_20140828_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_lifecycle_actions_with_options(
        self,
        request: ess_20140828_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLifecycleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLifecycleActionsResponse().from_map(
            self.do_rpcrequest('DescribeLifecycleActions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lifecycle_actions_with_options_async(
        self,
        request: ess_20140828_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLifecycleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLifecycleActionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeLifecycleActions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lifecycle_actions(
        self,
        request: ess_20140828_models.DescribeLifecycleActionsRequest,
    ) -> ess_20140828_models.DescribeLifecycleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    async def describe_lifecycle_actions_async(
        self,
        request: ess_20140828_models.DescribeLifecycleActionsRequest,
    ) -> ess_20140828_models.DescribeLifecycleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_actions_with_options_async(request, runtime)

    def describe_lifecycle_hooks_with_options(
        self,
        request: ess_20140828_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLifecycleHooksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLifecycleHooksResponse().from_map(
            self.do_rpcrequest('DescribeLifecycleHooks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lifecycle_hooks_with_options_async(
        self,
        request: ess_20140828_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLifecycleHooksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLifecycleHooksResponse().from_map(
            await self.do_rpcrequest_async('DescribeLifecycleHooks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lifecycle_hooks(
        self,
        request: ess_20140828_models.DescribeLifecycleHooksRequest,
    ) -> ess_20140828_models.DescribeLifecycleHooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    async def describe_lifecycle_hooks_async(
        self,
        request: ess_20140828_models.DescribeLifecycleHooksRequest,
    ) -> ess_20140828_models.DescribeLifecycleHooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_hooks_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: ess_20140828_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLimitationResponse().from_map(
            self.do_rpcrequest('DescribeLimitation', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: ess_20140828_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeLimitationResponse().from_map(
            await self.do_rpcrequest_async('DescribeLimitation', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_limitation(
        self,
        request: ess_20140828_models.DescribeLimitationRequest,
    ) -> ess_20140828_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: ess_20140828_models.DescribeLimitationRequest,
    ) -> ess_20140828_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_notification_configurations_with_options(
        self,
        request: ess_20140828_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeNotificationConfigurationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeNotificationConfigurationsResponse().from_map(
            self.do_rpcrequest('DescribeNotificationConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_notification_configurations_with_options_async(
        self,
        request: ess_20140828_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeNotificationConfigurationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeNotificationConfigurationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNotificationConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notification_configurations(
        self,
        request: ess_20140828_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20140828_models.DescribeNotificationConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    async def describe_notification_configurations_async(
        self,
        request: ess_20140828_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20140828_models.DescribeNotificationConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_configurations_with_options_async(request, runtime)

    def describe_notification_types_with_options(
        self,
        request: ess_20140828_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeNotificationTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeNotificationTypesResponse().from_map(
            self.do_rpcrequest('DescribeNotificationTypes', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_notification_types_with_options_async(
        self,
        request: ess_20140828_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeNotificationTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeNotificationTypesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNotificationTypes', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notification_types(
        self,
        request: ess_20140828_models.DescribeNotificationTypesRequest,
    ) -> ess_20140828_models.DescribeNotificationTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    async def describe_notification_types_async(
        self,
        request: ess_20140828_models.DescribeNotificationTypesRequest,
    ) -> ess_20140828_models.DescribeNotificationTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_types_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ess_20140828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ess_20140828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ess_20140828_models.DescribeRegionsRequest,
    ) -> ess_20140828_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ess_20140828_models.DescribeRegionsRequest,
    ) -> ess_20140828_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scaling_activities_with_options(
        self,
        request: ess_20140828_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingActivitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingActivitiesResponse().from_map(
            self.do_rpcrequest('DescribeScalingActivities', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_activities_with_options_async(
        self,
        request: ess_20140828_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingActivitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingActivitiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingActivities', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_activities(
        self,
        request: ess_20140828_models.DescribeScalingActivitiesRequest,
    ) -> ess_20140828_models.DescribeScalingActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    async def describe_scaling_activities_async(
        self,
        request: ess_20140828_models.DescribeScalingActivitiesRequest,
    ) -> ess_20140828_models.DescribeScalingActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activities_with_options_async(request, runtime)

    def describe_scaling_activity_detail_with_options(
        self,
        request: ess_20140828_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingActivityDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingActivityDetailResponse().from_map(
            self.do_rpcrequest('DescribeScalingActivityDetail', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_activity_detail_with_options_async(
        self,
        request: ess_20140828_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingActivityDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingActivityDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingActivityDetail', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_activity_detail(
        self,
        request: ess_20140828_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20140828_models.DescribeScalingActivityDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    async def describe_scaling_activity_detail_async(
        self,
        request: ess_20140828_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20140828_models.DescribeScalingActivityDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activity_detail_with_options_async(request, runtime)

    def describe_scaling_configurations_with_options(
        self,
        request: ess_20140828_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingConfigurationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingConfigurationsResponse().from_map(
            self.do_rpcrequest('DescribeScalingConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_configurations_with_options_async(
        self,
        request: ess_20140828_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingConfigurationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingConfigurationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_configurations(
        self,
        request: ess_20140828_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20140828_models.DescribeScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    async def describe_scaling_configurations_async(
        self,
        request: ess_20140828_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20140828_models.DescribeScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_configurations_with_options_async(request, runtime)

    def describe_scaling_instances_with_options(
        self,
        request: ess_20140828_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingInstancesResponse().from_map(
            self.do_rpcrequest('DescribeScalingInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_instances_with_options_async(
        self,
        request: ess_20140828_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_instances(
        self,
        request: ess_20140828_models.DescribeScalingInstancesRequest,
    ) -> ess_20140828_models.DescribeScalingInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    async def describe_scaling_instances_async(
        self,
        request: ess_20140828_models.DescribeScalingInstancesRequest,
    ) -> ess_20140828_models.DescribeScalingInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_instances_with_options_async(request, runtime)

    def describe_scaling_rules_with_options(
        self,
        request: ess_20140828_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingRulesResponse().from_map(
            self.do_rpcrequest('DescribeScalingRules', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_rules_with_options_async(
        self,
        request: ess_20140828_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScalingRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScalingRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingRules', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_rules(
        self,
        request: ess_20140828_models.DescribeScalingRulesRequest,
    ) -> ess_20140828_models.DescribeScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    async def describe_scaling_rules_async(
        self,
        request: ess_20140828_models.DescribeScalingRulesRequest,
    ) -> ess_20140828_models.DescribeScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_rules_with_options_async(request, runtime)

    def describe_scheduled_tasks_with_options(
        self,
        request: ess_20140828_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScheduledTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScheduledTasksResponse().from_map(
            self.do_rpcrequest('DescribeScheduledTasks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scheduled_tasks_with_options_async(
        self,
        request: ess_20140828_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DescribeScheduledTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DescribeScheduledTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeScheduledTasks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scheduled_tasks(
        self,
        request: ess_20140828_models.DescribeScheduledTasksRequest,
    ) -> ess_20140828_models.DescribeScheduledTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    async def describe_scheduled_tasks_async(
        self,
        request: ess_20140828_models.DescribeScheduledTasksRequest,
    ) -> ess_20140828_models.DescribeScheduledTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduled_tasks_with_options_async(request, runtime)

    def detach_dbinstances_with_options(
        self,
        request: ess_20140828_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachDBInstancesResponse().from_map(
            self.do_rpcrequest('DetachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_dbinstances_with_options_async(
        self,
        request: ess_20140828_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachDBInstancesResponse().from_map(
            await self.do_rpcrequest_async('DetachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_dbinstances(
        self,
        request: ess_20140828_models.DetachDBInstancesRequest,
    ) -> ess_20140828_models.DetachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    async def detach_dbinstances_async(
        self,
        request: ess_20140828_models.DetachDBInstancesRequest,
    ) -> ess_20140828_models.DetachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_dbinstances_with_options_async(request, runtime)

    def detach_instances_with_options(
        self,
        request: ess_20140828_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachInstancesResponse().from_map(
            self.do_rpcrequest('DetachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_instances_with_options_async(
        self,
        request: ess_20140828_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachInstancesResponse().from_map(
            await self.do_rpcrequest_async('DetachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_instances(
        self,
        request: ess_20140828_models.DetachInstancesRequest,
    ) -> ess_20140828_models.DetachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    async def detach_instances_async(
        self,
        request: ess_20140828_models.DetachInstancesRequest,
    ) -> ess_20140828_models.DetachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_instances_with_options_async(request, runtime)

    def detach_load_balancers_with_options(
        self,
        request: ess_20140828_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachLoadBalancersResponse().from_map(
            self.do_rpcrequest('DetachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_load_balancers_with_options_async(
        self,
        request: ess_20140828_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachLoadBalancersResponse().from_map(
            await self.do_rpcrequest_async('DetachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_load_balancers(
        self,
        request: ess_20140828_models.DetachLoadBalancersRequest,
    ) -> ess_20140828_models.DetachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    async def detach_load_balancers_async(
        self,
        request: ess_20140828_models.DetachLoadBalancersRequest,
    ) -> ess_20140828_models.DetachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_load_balancers_with_options_async(request, runtime)

    def detach_vserver_groups_with_options(
        self,
        request: ess_20140828_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachVServerGroupsResponse().from_map(
            self.do_rpcrequest('DetachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_vserver_groups_with_options_async(
        self,
        request: ess_20140828_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DetachVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DetachVServerGroupsResponse().from_map(
            await self.do_rpcrequest_async('DetachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_vserver_groups(
        self,
        request: ess_20140828_models.DetachVServerGroupsRequest,
    ) -> ess_20140828_models.DetachVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    async def detach_vserver_groups_async(
        self,
        request: ess_20140828_models.DetachVServerGroupsRequest,
    ) -> ess_20140828_models.DetachVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_vserver_groups_with_options_async(request, runtime)

    def disable_alarm_with_options(
        self,
        request: ess_20140828_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DisableAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DisableAlarmResponse().from_map(
            self.do_rpcrequest('DisableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_alarm_with_options_async(
        self,
        request: ess_20140828_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DisableAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DisableAlarmResponse().from_map(
            await self.do_rpcrequest_async('DisableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_alarm(
        self,
        request: ess_20140828_models.DisableAlarmRequest,
    ) -> ess_20140828_models.DisableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    async def disable_alarm_async(
        self,
        request: ess_20140828_models.DisableAlarmRequest,
    ) -> ess_20140828_models.DisableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_alarm_with_options_async(request, runtime)

    def disable_scaling_group_with_options(
        self,
        request: ess_20140828_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DisableScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DisableScalingGroupResponse().from_map(
            self.do_rpcrequest('DisableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_scaling_group_with_options_async(
        self,
        request: ess_20140828_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.DisableScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.DisableScalingGroupResponse().from_map(
            await self.do_rpcrequest_async('DisableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_scaling_group(
        self,
        request: ess_20140828_models.DisableScalingGroupRequest,
    ) -> ess_20140828_models.DisableScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    async def disable_scaling_group_async(
        self,
        request: ess_20140828_models.DisableScalingGroupRequest,
    ) -> ess_20140828_models.DisableScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_scaling_group_with_options_async(request, runtime)

    def enable_alarm_with_options(
        self,
        request: ess_20140828_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnableAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnableAlarmResponse().from_map(
            self.do_rpcrequest('EnableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_alarm_with_options_async(
        self,
        request: ess_20140828_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnableAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnableAlarmResponse().from_map(
            await self.do_rpcrequest_async('EnableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_alarm(
        self,
        request: ess_20140828_models.EnableAlarmRequest,
    ) -> ess_20140828_models.EnableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    async def enable_alarm_async(
        self,
        request: ess_20140828_models.EnableAlarmRequest,
    ) -> ess_20140828_models.EnableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_alarm_with_options_async(request, runtime)

    def enable_scaling_group_with_options(
        self,
        request: ess_20140828_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnableScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnableScalingGroupResponse().from_map(
            self.do_rpcrequest('EnableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_scaling_group_with_options_async(
        self,
        request: ess_20140828_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnableScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnableScalingGroupResponse().from_map(
            await self.do_rpcrequest_async('EnableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_scaling_group(
        self,
        request: ess_20140828_models.EnableScalingGroupRequest,
    ) -> ess_20140828_models.EnableScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    async def enable_scaling_group_async(
        self,
        request: ess_20140828_models.EnableScalingGroupRequest,
    ) -> ess_20140828_models.EnableScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_scaling_group_with_options_async(request, runtime)

    def enter_standby_with_options(
        self,
        request: ess_20140828_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnterStandbyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnterStandbyResponse().from_map(
            self.do_rpcrequest('EnterStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enter_standby_with_options_async(
        self,
        request: ess_20140828_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.EnterStandbyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.EnterStandbyResponse().from_map(
            await self.do_rpcrequest_async('EnterStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enter_standby(
        self,
        request: ess_20140828_models.EnterStandbyRequest,
    ) -> ess_20140828_models.EnterStandbyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    async def enter_standby_async(
        self,
        request: ess_20140828_models.EnterStandbyRequest,
    ) -> ess_20140828_models.EnterStandbyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enter_standby_with_options_async(request, runtime)

    def execute_scaling_rule_with_options(
        self,
        request: ess_20140828_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ExecuteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ExecuteScalingRuleResponse().from_map(
            self.do_rpcrequest('ExecuteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_scaling_rule_with_options_async(
        self,
        request: ess_20140828_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ExecuteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ExecuteScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('ExecuteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_scaling_rule(
        self,
        request: ess_20140828_models.ExecuteScalingRuleRequest,
    ) -> ess_20140828_models.ExecuteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    async def execute_scaling_rule_async(
        self,
        request: ess_20140828_models.ExecuteScalingRuleRequest,
    ) -> ess_20140828_models.ExecuteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_scaling_rule_with_options_async(request, runtime)

    def exit_standby_with_options(
        self,
        request: ess_20140828_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ExitStandbyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ExitStandbyResponse().from_map(
            self.do_rpcrequest('ExitStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def exit_standby_with_options_async(
        self,
        request: ess_20140828_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ExitStandbyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ExitStandbyResponse().from_map(
            await self.do_rpcrequest_async('ExitStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exit_standby(
        self,
        request: ess_20140828_models.ExitStandbyRequest,
    ) -> ess_20140828_models.ExitStandbyResponse:
        runtime = util_models.RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    async def exit_standby_async(
        self,
        request: ess_20140828_models.ExitStandbyRequest,
    ) -> ess_20140828_models.ExitStandbyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.exit_standby_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ess_20140828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ess_20140828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: ess_20140828_models.ListTagKeysRequest,
    ) -> ess_20140828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ess_20140828_models.ListTagKeysRequest,
    ) -> ess_20140828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ess_20140828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ess_20140828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ess_20140828_models.ListTagResourcesRequest,
    ) -> ess_20140828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ess_20140828_models.ListTagResourcesRequest,
    ) -> ess_20140828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ess_20140828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagValuesResponse().from_map(
            self.do_rpcrequest('ListTagValues', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ess_20140828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ListTagValuesResponse().from_map(
            await self.do_rpcrequest_async('ListTagValues', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: ess_20140828_models.ListTagValuesRequest,
    ) -> ess_20140828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ess_20140828_models.ListTagValuesRequest,
    ) -> ess_20140828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_alarm_with_options(
        self,
        request: ess_20140828_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyAlarmResponse().from_map(
            self.do_rpcrequest('ModifyAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_alarm_with_options_async(
        self,
        request: ess_20140828_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyAlarmResponse().from_map(
            await self.do_rpcrequest_async('ModifyAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_alarm(
        self,
        request: ess_20140828_models.ModifyAlarmRequest,
    ) -> ess_20140828_models.ModifyAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    async def modify_alarm_async(
        self,
        request: ess_20140828_models.ModifyAlarmRequest,
    ) -> ess_20140828_models.ModifyAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_alarm_with_options_async(request, runtime)

    def modify_lifecycle_hook_with_options(
        self,
        request: ess_20140828_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyLifecycleHookResponse().from_map(
            self.do_rpcrequest('ModifyLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_lifecycle_hook_with_options_async(
        self,
        request: ess_20140828_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyLifecycleHookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyLifecycleHookResponse().from_map(
            await self.do_rpcrequest_async('ModifyLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_lifecycle_hook(
        self,
        request: ess_20140828_models.ModifyLifecycleHookRequest,
    ) -> ess_20140828_models.ModifyLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    async def modify_lifecycle_hook_async(
        self,
        request: ess_20140828_models.ModifyLifecycleHookRequest,
    ) -> ess_20140828_models.ModifyLifecycleHookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_lifecycle_hook_with_options_async(request, runtime)

    def modify_notification_configuration_with_options(
        self,
        request: ess_20140828_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyNotificationConfigurationResponse().from_map(
            self.do_rpcrequest('ModifyNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_notification_configuration_with_options_async(
        self,
        request: ess_20140828_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyNotificationConfigurationResponse().from_map(
            await self.do_rpcrequest_async('ModifyNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_notification_configuration(
        self,
        request: ess_20140828_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20140828_models.ModifyNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    async def modify_notification_configuration_async(
        self,
        request: ess_20140828_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20140828_models.ModifyNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_notification_configuration_with_options_async(request, runtime)

    def modify_scaling_configuration_with_options(
        self,
        tmp_req: ess_20140828_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingConfigurationResponse().from_map(
            self.do_rpcrequest('ModifyScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20140828_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingConfigurationResponse().from_map(
            await self.do_rpcrequest_async('ModifyScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_configuration(
        self,
        request: ess_20140828_models.ModifyScalingConfigurationRequest,
    ) -> ess_20140828_models.ModifyScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    async def modify_scaling_configuration_async(
        self,
        request: ess_20140828_models.ModifyScalingConfigurationRequest,
    ) -> ess_20140828_models.ModifyScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_configuration_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: ess_20140828_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingGroupResponse().from_map(
            self.do_rpcrequest('ModifyScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: ess_20140828_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_group(
        self,
        request: ess_20140828_models.ModifyScalingGroupRequest,
    ) -> ess_20140828_models.ModifyScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: ess_20140828_models.ModifyScalingGroupRequest,
    ) -> ess_20140828_models.ModifyScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: ess_20140828_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingRuleResponse().from_map(
            self.do_rpcrequest('ModifyScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: ess_20140828_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: ess_20140828_models.ModifyScalingRuleRequest,
    ) -> ess_20140828_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: ess_20140828_models.ModifyScalingRuleRequest,
    ) -> ess_20140828_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scheduled_task_with_options(
        self,
        request: ess_20140828_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScheduledTaskResponse().from_map(
            self.do_rpcrequest('ModifyScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: ess_20140828_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ModifyScheduledTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ModifyScheduledTaskResponse().from_map(
            await self.do_rpcrequest_async('ModifyScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: ess_20140828_models.ModifyScheduledTaskRequest,
    ) -> ess_20140828_models.ModifyScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: ess_20140828_models.ModifyScheduledTaskRequest,
    ) -> ess_20140828_models.ModifyScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def rebalance_instances_with_options(
        self,
        request: ess_20140828_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RebalanceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RebalanceInstancesResponse().from_map(
            self.do_rpcrequest('RebalanceInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rebalance_instances_with_options_async(
        self,
        request: ess_20140828_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RebalanceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RebalanceInstancesResponse().from_map(
            await self.do_rpcrequest_async('RebalanceInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebalance_instances(
        self,
        request: ess_20140828_models.RebalanceInstancesRequest,
    ) -> ess_20140828_models.RebalanceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    async def rebalance_instances_async(
        self,
        request: ess_20140828_models.RebalanceInstancesRequest,
    ) -> ess_20140828_models.RebalanceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebalance_instances_with_options_async(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(
        self,
        request: ess_20140828_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RecordLifecycleActionHeartbeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RecordLifecycleActionHeartbeatResponse().from_map(
            self.do_rpcrequest('RecordLifecycleActionHeartbeat', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def record_lifecycle_action_heartbeat_with_options_async(
        self,
        request: ess_20140828_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RecordLifecycleActionHeartbeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RecordLifecycleActionHeartbeatResponse().from_map(
            await self.do_rpcrequest_async('RecordLifecycleActionHeartbeat', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def record_lifecycle_action_heartbeat(
        self,
        request: ess_20140828_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20140828_models.RecordLifecycleActionHeartbeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    async def record_lifecycle_action_heartbeat_async(
        self,
        request: ess_20140828_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20140828_models.RecordLifecycleActionHeartbeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.record_lifecycle_action_heartbeat_with_options_async(request, runtime)

    def remove_instances_with_options(
        self,
        request: ess_20140828_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RemoveInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RemoveInstancesResponse().from_map(
            self.do_rpcrequest('RemoveInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_instances_with_options_async(
        self,
        request: ess_20140828_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.RemoveInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.RemoveInstancesResponse().from_map(
            await self.do_rpcrequest_async('RemoveInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_instances(
        self,
        request: ess_20140828_models.RemoveInstancesRequest,
    ) -> ess_20140828_models.RemoveInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    async def remove_instances_async(
        self,
        request: ess_20140828_models.RemoveInstancesRequest,
    ) -> ess_20140828_models.RemoveInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_instances_with_options_async(request, runtime)

    def resume_processes_with_options(
        self,
        request: ess_20140828_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ResumeProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ResumeProcessesResponse().from_map(
            self.do_rpcrequest('ResumeProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_processes_with_options_async(
        self,
        request: ess_20140828_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.ResumeProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.ResumeProcessesResponse().from_map(
            await self.do_rpcrequest_async('ResumeProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_processes(
        self,
        request: ess_20140828_models.ResumeProcessesRequest,
    ) -> ess_20140828_models.ResumeProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    async def resume_processes_async(
        self,
        request: ess_20140828_models.ResumeProcessesRequest,
    ) -> ess_20140828_models.ResumeProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_processes_with_options_async(request, runtime)

    def set_group_deletion_protection_with_options(
        self,
        request: ess_20140828_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetGroupDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetGroupDeletionProtectionResponse().from_map(
            self.do_rpcrequest('SetGroupDeletionProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_group_deletion_protection_with_options_async(
        self,
        request: ess_20140828_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetGroupDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetGroupDeletionProtectionResponse().from_map(
            await self.do_rpcrequest_async('SetGroupDeletionProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_deletion_protection(
        self,
        request: ess_20140828_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20140828_models.SetGroupDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    async def set_group_deletion_protection_async(
        self,
        request: ess_20140828_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20140828_models.SetGroupDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_group_deletion_protection_with_options_async(request, runtime)

    def set_instance_health_with_options(
        self,
        request: ess_20140828_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetInstanceHealthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetInstanceHealthResponse().from_map(
            self.do_rpcrequest('SetInstanceHealth', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_instance_health_with_options_async(
        self,
        request: ess_20140828_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetInstanceHealthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetInstanceHealthResponse().from_map(
            await self.do_rpcrequest_async('SetInstanceHealth', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_instance_health(
        self,
        request: ess_20140828_models.SetInstanceHealthRequest,
    ) -> ess_20140828_models.SetInstanceHealthResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    async def set_instance_health_async(
        self,
        request: ess_20140828_models.SetInstanceHealthRequest,
    ) -> ess_20140828_models.SetInstanceHealthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_health_with_options_async(request, runtime)

    def set_instances_protection_with_options(
        self,
        request: ess_20140828_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetInstancesProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetInstancesProtectionResponse().from_map(
            self.do_rpcrequest('SetInstancesProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_instances_protection_with_options_async(
        self,
        request: ess_20140828_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SetInstancesProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SetInstancesProtectionResponse().from_map(
            await self.do_rpcrequest_async('SetInstancesProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_instances_protection(
        self,
        request: ess_20140828_models.SetInstancesProtectionRequest,
    ) -> ess_20140828_models.SetInstancesProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    async def set_instances_protection_async(
        self,
        request: ess_20140828_models.SetInstancesProtectionRequest,
    ) -> ess_20140828_models.SetInstancesProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instances_protection_with_options_async(request, runtime)

    def suspend_processes_with_options(
        self,
        request: ess_20140828_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SuspendProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SuspendProcessesResponse().from_map(
            self.do_rpcrequest('SuspendProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_processes_with_options_async(
        self,
        request: ess_20140828_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.SuspendProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.SuspendProcessesResponse().from_map(
            await self.do_rpcrequest_async('SuspendProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_processes(
        self,
        request: ess_20140828_models.SuspendProcessesRequest,
    ) -> ess_20140828_models.SuspendProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    async def suspend_processes_async(
        self,
        request: ess_20140828_models.SuspendProcessesRequest,
    ) -> ess_20140828_models.SuspendProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_processes_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ess_20140828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ess_20140828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ess_20140828_models.TagResourcesRequest,
    ) -> ess_20140828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ess_20140828_models.TagResourcesRequest,
    ) -> ess_20140828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ess_20140828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ess_20140828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ess_20140828_models.UntagResourcesRequest,
    ) -> ess_20140828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ess_20140828_models.UntagResourcesRequest,
    ) -> ess_20140828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def verify_authentication_with_options(
        self,
        request: ess_20140828_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.VerifyAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.VerifyAuthenticationResponse().from_map(
            self.do_rpcrequest('VerifyAuthentication', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_authentication_with_options_async(
        self,
        request: ess_20140828_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.VerifyAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.VerifyAuthenticationResponse().from_map(
            await self.do_rpcrequest_async('VerifyAuthentication', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_authentication(
        self,
        request: ess_20140828_models.VerifyAuthenticationRequest,
    ) -> ess_20140828_models.VerifyAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    async def verify_authentication_async(
        self,
        request: ess_20140828_models.VerifyAuthenticationRequest,
    ) -> ess_20140828_models.VerifyAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_authentication_with_options_async(request, runtime)

    def verify_user_with_options(
        self,
        request: ess_20140828_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.VerifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.VerifyUserResponse().from_map(
            self.do_rpcrequest('VerifyUser', '2014-08-28', 'HTTPS', 'POST', 'AK', 'none', req, runtime)
        )

    async def verify_user_with_options_async(
        self,
        request: ess_20140828_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20140828_models.VerifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ess_20140828_models.VerifyUserResponse().from_map(
            await self.do_rpcrequest_async('VerifyUser', '2014-08-28', 'HTTPS', 'POST', 'AK', 'none', req, runtime)
        )

    def verify_user(
        self,
        request: ess_20140828_models.VerifyUserRequest,
    ) -> ess_20140828_models.VerifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)

    async def verify_user_async(
        self,
        request: ess_20140828_models.VerifyUserRequest,
    ) -> ess_20140828_models.VerifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_with_options_async(request, runtime)
