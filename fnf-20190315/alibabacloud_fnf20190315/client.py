# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fnf20190315 import models as fnf_20190315_models
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
            'cn-beijing': 'cn-beijing.fnf.aliyuncs.com',
            'cn-hangzhou': 'cn-hangzhou.fnf.aliyuncs.com',
            'cn-shanghai': 'cn-shanghai.fnf.aliyuncs.com',
            'cn-shenzhen': 'cn-shenzhen.fnf.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('fnf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_flow_with_options(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.CreateFlowResponse().from_map(
            self.do_rpcrequest('CreateFlow', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.CreateFlowResponse().from_map(
            await self.do_rpcrequest_async('CreateFlow', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
    ) -> fnf_20190315_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
    ) -> fnf_20190315_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_schedule_with_options(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.CreateScheduleResponse().from_map(
            self.do_rpcrequest('CreateSchedule', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_schedule_with_options_async(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.CreateScheduleResponse().from_map(
            await self.do_rpcrequest_async('CreateSchedule', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schedule(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_with_options(request, runtime)

    async def create_schedule_async(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DeleteFlowResponse().from_map(
            self.do_rpcrequest('DeleteFlow', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DeleteFlowResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlow', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_flow(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_schedule_with_options(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DeleteScheduleResponse().from_map(
            self.do_rpcrequest('DeleteSchedule', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_schedule_with_options_async(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DeleteScheduleResponse().from_map(
            await self.do_rpcrequest_async('DeleteSchedule', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_schedule(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_with_options(request, runtime)

    async def delete_schedule_async(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_with_options_async(request, runtime)

    def describe_execution_with_options(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeExecutionResponse().from_map(
            self.do_rpcrequest('DescribeExecution', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_execution_with_options_async(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeExecutionResponse().from_map(
            await self.do_rpcrequest_async('DescribeExecution', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_execution(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_execution_with_options(request, runtime)

    async def describe_execution_async(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_execution_with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeFlowResponse().from_map(
            self.do_rpcrequest('DescribeFlow', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlow', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_flow(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def describe_schedule_with_options(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeScheduleResponse().from_map(
            self.do_rpcrequest('DescribeSchedule', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_schedule_with_options_async(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.DescribeScheduleResponse().from_map(
            await self.do_rpcrequest_async('DescribeSchedule', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_schedule(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_with_options(request, runtime)

    async def describe_schedule_async(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_with_options_async(request, runtime)

    def get_execution_history_with_options(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.GetExecutionHistoryResponse().from_map(
            self.do_rpcrequest('GetExecutionHistory', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_execution_history_with_options_async(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.GetExecutionHistoryResponse().from_map(
            await self.do_rpcrequest_async('GetExecutionHistory', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_execution_history(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_execution_history_with_options(request, runtime)

    async def get_execution_history_async(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_execution_history_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListExecutionsResponse().from_map(
            self.do_rpcrequest('ListExecutions', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListExecutionsResponse().from_map(
            await self.do_rpcrequest_async('ListExecutions', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_executions(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_flows_with_options(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListFlowsResponse().from_map(
            self.do_rpcrequest('ListFlows', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListFlowsResponse().from_map(
            await self.do_rpcrequest_async('ListFlows', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_flows(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
    ) -> fnf_20190315_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    async def list_flows_async(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
    ) -> fnf_20190315_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flows_with_options_async(request, runtime)

    def list_schedules_with_options(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListSchedulesResponse().from_map(
            self.do_rpcrequest('ListSchedules', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_schedules_with_options_async(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return fnf_20190315_models.ListSchedulesResponse().from_map(
            await self.do_rpcrequest_async('ListSchedules', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schedules(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schedules_with_options(request, runtime)

    async def list_schedules_async(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schedules_with_options_async(request, runtime)

    def report_task_failed_with_options(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.ReportTaskFailedResponse().from_map(
            self.do_rpcrequest('ReportTaskFailed', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_task_failed_with_options_async(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.ReportTaskFailedResponse().from_map(
            await self.do_rpcrequest_async('ReportTaskFailed', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_task_failed(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_task_failed_with_options(request, runtime)

    async def report_task_failed_async(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_task_failed_with_options_async(request, runtime)

    def report_task_succeeded_with_options(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.ReportTaskSucceededResponse().from_map(
            self.do_rpcrequest('ReportTaskSucceeded', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_task_succeeded_with_options_async(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.ReportTaskSucceededResponse().from_map(
            await self.do_rpcrequest_async('ReportTaskSucceeded', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_task_succeeded(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_task_succeeded_with_options(request, runtime)

    async def report_task_succeeded_async(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_task_succeeded_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.StartExecutionResponse().from_map(
            self.do_rpcrequest('StartExecution', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.StartExecutionResponse().from_map(
            await self.do_rpcrequest_async('StartExecution', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_execution(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
    ) -> fnf_20190315_models.StartExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
    ) -> fnf_20190315_models.StartExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def stop_execution_with_options(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StopExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.StopExecutionResponse().from_map(
            self.do_rpcrequest('StopExecution', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_execution_with_options_async(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StopExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.StopExecutionResponse().from_map(
            await self.do_rpcrequest_async('StopExecution', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_execution(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
    ) -> fnf_20190315_models.StopExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_execution_with_options(request, runtime)

    async def stop_execution_async(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
    ) -> fnf_20190315_models.StopExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_execution_with_options_async(request, runtime)

    def update_flow_with_options(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.UpdateFlowResponse().from_map(
            self.do_rpcrequest('UpdateFlow', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.UpdateFlowResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlow', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flow(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    async def update_flow_async(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_with_options_async(request, runtime)

    def update_schedule_with_options(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.UpdateScheduleResponse().from_map(
            self.do_rpcrequest('UpdateSchedule', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_schedule_with_options_async(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return fnf_20190315_models.UpdateScheduleResponse().from_map(
            await self.do_rpcrequest_async('UpdateSchedule', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schedule(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_with_options(request, runtime)

    async def update_schedule_async(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_with_options_async(request, runtime)
