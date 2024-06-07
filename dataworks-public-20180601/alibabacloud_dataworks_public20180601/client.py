# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20180601 import models as dataworks_public_20180601_models
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

    def create_manual_dag_with_options(
        self,
        request: dataworks_public_20180601_models.CreateManualDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.CreateManualDagResponse:
        """
        @param request: CreateManualDagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateManualDagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizdate):
            query['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.dag_para):
            query['DagPara'] = request.dag_para
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.node_para):
            query['NodePara'] = request.node_para
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateManualDag',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.CreateManualDagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_manual_dag_with_options_async(
        self,
        request: dataworks_public_20180601_models.CreateManualDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.CreateManualDagResponse:
        """
        @param request: CreateManualDagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateManualDagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizdate):
            query['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.dag_para):
            query['DagPara'] = request.dag_para
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.node_para):
            query['NodePara'] = request.node_para
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateManualDag',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.CreateManualDagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_manual_dag(
        self,
        request: dataworks_public_20180601_models.CreateManualDagRequest,
    ) -> dataworks_public_20180601_models.CreateManualDagResponse:
        """
        @param request: CreateManualDagRequest
        @return: CreateManualDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    async def create_manual_dag_async(
        self,
        request: dataworks_public_20180601_models.CreateManualDagRequest,
    ) -> dataworks_public_20180601_models.CreateManualDagResponse:
        """
        @param request: CreateManualDagRequest
        @return: CreateManualDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_manual_dag_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: dataworks_public_20180601_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.DeleteFileResponse:
        """
        @param request: DeleteFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: dataworks_public_20180601_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.DeleteFileResponse:
        """
        @param request: DeleteFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: dataworks_public_20180601_models.DeleteFileRequest,
    ) -> dataworks_public_20180601_models.DeleteFileResponse:
        """
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: dataworks_public_20180601_models.DeleteFileRequest,
    ) -> dataworks_public_20180601_models.DeleteFileResponse:
        """
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def describe_emr_hive_table_with_options(
        self,
        request: dataworks_public_20180601_models.DescribeEmrHiveTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.DescribeEmrHiveTableResponse:
        """
        @param request: DescribeEmrHiveTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEmrHiveTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmrHiveTable',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DescribeEmrHiveTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_emr_hive_table_with_options_async(
        self,
        request: dataworks_public_20180601_models.DescribeEmrHiveTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.DescribeEmrHiveTableResponse:
        """
        @param request: DescribeEmrHiveTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEmrHiveTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmrHiveTable',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DescribeEmrHiveTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_emr_hive_table(
        self,
        request: dataworks_public_20180601_models.DescribeEmrHiveTableRequest,
    ) -> dataworks_public_20180601_models.DescribeEmrHiveTableResponse:
        """
        @param request: DescribeEmrHiveTableRequest
        @return: DescribeEmrHiveTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_emr_hive_table_with_options(request, runtime)

    async def describe_emr_hive_table_async(
        self,
        request: dataworks_public_20180601_models.DescribeEmrHiveTableRequest,
    ) -> dataworks_public_20180601_models.DescribeEmrHiveTableResponse:
        """
        @param request: DescribeEmrHiveTableRequest
        @return: DescribeEmrHiveTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_emr_hive_table_with_options_async(request, runtime)

    def get_data_service_api_context_with_options(
        self,
        request: dataworks_public_20180601_models.GetDataServiceApiContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetDataServiceApiContextResponse:
        """
        @summary 查询apiContext接口
        
        @param request: GetDataServiceApiContextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataServiceApiContextResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataServiceApiContext',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDataServiceApiContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_context_with_options_async(
        self,
        request: dataworks_public_20180601_models.GetDataServiceApiContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetDataServiceApiContextResponse:
        """
        @summary 查询apiContext接口
        
        @param request: GetDataServiceApiContextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataServiceApiContextResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataServiceApiContext',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDataServiceApiContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_context(
        self,
        request: dataworks_public_20180601_models.GetDataServiceApiContextRequest,
    ) -> dataworks_public_20180601_models.GetDataServiceApiContextResponse:
        """
        @summary 查询apiContext接口
        
        @param request: GetDataServiceApiContextRequest
        @return: GetDataServiceApiContextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_context_with_options(request, runtime)

    async def get_data_service_api_context_async(
        self,
        request: dataworks_public_20180601_models.GetDataServiceApiContextRequest,
    ) -> dataworks_public_20180601_models.GetDataServiceApiContextResponse:
        """
        @summary 查询apiContext接口
        
        @param request: GetDataServiceApiContextRequest
        @return: GetDataServiceApiContextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_api_context_with_options_async(request, runtime)

    def get_data_service_context_update_event_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse:
        """
        @summary 查询apiContext更新事件接口
        
        @param request: GetDataServiceContextUpdateEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataServiceContextUpdateEventResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDataServiceContextUpdateEvent',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_context_update_event_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse:
        """
        @summary 查询apiContext更新事件接口
        
        @param request: GetDataServiceContextUpdateEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataServiceContextUpdateEventResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDataServiceContextUpdateEvent',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_context_update_event(self) -> dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse:
        """
        @summary 查询apiContext更新事件接口
        
        @return: GetDataServiceContextUpdateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_context_update_event_with_options(runtime)

    async def get_data_service_context_update_event_async(self) -> dataworks_public_20180601_models.GetDataServiceContextUpdateEventResponse:
        """
        @summary 查询apiContext更新事件接口
        
        @return: GetDataServiceContextUpdateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_context_update_event_with_options_async(runtime)

    def get_switch_value_with_options(
        self,
        request: dataworks_public_20180601_models.GetSwitchValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetSwitchValueResponse:
        """
        @summary 根据Switch名称获取值
        
        @param request: GetSwitchValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwitchValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_name):
            query['SwitchName'] = request.switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSwitchValue',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetSwitchValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_switch_value_with_options_async(
        self,
        request: dataworks_public_20180601_models.GetSwitchValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetSwitchValueResponse:
        """
        @summary 根据Switch名称获取值
        
        @param request: GetSwitchValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwitchValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_name):
            query['SwitchName'] = request.switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSwitchValue',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetSwitchValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_switch_value(
        self,
        request: dataworks_public_20180601_models.GetSwitchValueRequest,
    ) -> dataworks_public_20180601_models.GetSwitchValueResponse:
        """
        @summary 根据Switch名称获取值
        
        @param request: GetSwitchValueRequest
        @return: GetSwitchValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_switch_value_with_options(request, runtime)

    async def get_switch_value_async(
        self,
        request: dataworks_public_20180601_models.GetSwitchValueRequest,
    ) -> dataworks_public_20180601_models.GetSwitchValueResponse:
        """
        @summary 根据Switch名称获取值
        
        @param request: GetSwitchValueRequest
        @return: GetSwitchValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_switch_value_with_options_async(request, runtime)

    def get_time_machine_task_with_options(
        self,
        request: dataworks_public_20180601_models.GetTimeMachineTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetTimeMachineTaskResponse:
        """
        @summary 查询timeMachine任务详情
        
        @param request: GetTimeMachineTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTimeMachineTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTimeMachineTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetTimeMachineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_time_machine_task_with_options_async(
        self,
        request: dataworks_public_20180601_models.GetTimeMachineTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.GetTimeMachineTaskResponse:
        """
        @summary 查询timeMachine任务详情
        
        @param request: GetTimeMachineTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTimeMachineTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTimeMachineTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetTimeMachineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_time_machine_task(
        self,
        request: dataworks_public_20180601_models.GetTimeMachineTaskRequest,
    ) -> dataworks_public_20180601_models.GetTimeMachineTaskResponse:
        """
        @summary 查询timeMachine任务详情
        
        @param request: GetTimeMachineTaskRequest
        @return: GetTimeMachineTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_time_machine_task_with_options(request, runtime)

    async def get_time_machine_task_async(
        self,
        request: dataworks_public_20180601_models.GetTimeMachineTaskRequest,
    ) -> dataworks_public_20180601_models.GetTimeMachineTaskResponse:
        """
        @summary 查询timeMachine任务详情
        
        @param request: GetTimeMachineTaskRequest
        @return: GetTimeMachineTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_time_machine_task_with_options_async(request, runtime)

    def list_emr_hive_audit_logs_with_options(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse:
        """
        @param request: ListEmrHiveAuditLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveAuditLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveAuditLogs',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_hive_audit_logs_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse:
        """
        @param request: ListEmrHiveAuditLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveAuditLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveAuditLogs',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_emr_hive_audit_logs(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveAuditLogsRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse:
        """
        @param request: ListEmrHiveAuditLogsRequest
        @return: ListEmrHiveAuditLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_audit_logs_with_options(request, runtime)

    async def list_emr_hive_audit_logs_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveAuditLogsRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse:
        """
        @param request: ListEmrHiveAuditLogsRequest
        @return: ListEmrHiveAuditLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_hive_audit_logs_with_options_async(request, runtime)

    def list_emr_hive_databases_with_options(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveDatabasesResponse:
        """
        @param request: ListEmrHiveDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveDatabases',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_hive_databases_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveDatabasesResponse:
        """
        @param request: ListEmrHiveDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveDatabases',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_emr_hive_databases(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveDatabasesRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveDatabasesResponse:
        """
        @param request: ListEmrHiveDatabasesRequest
        @return: ListEmrHiveDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_databases_with_options(request, runtime)

    async def list_emr_hive_databases_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveDatabasesRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveDatabasesResponse:
        """
        @param request: ListEmrHiveDatabasesRequest
        @return: ListEmrHiveDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_hive_databases_with_options_async(request, runtime)

    def list_emr_hive_tables_with_options(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveTablesResponse:
        """
        @param request: ListEmrHiveTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveTables',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_hive_tables_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListEmrHiveTablesResponse:
        """
        @param request: ListEmrHiveTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmrHiveTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmrHiveTables',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_emr_hive_tables(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveTablesRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveTablesResponse:
        """
        @param request: ListEmrHiveTablesRequest
        @return: ListEmrHiveTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_tables_with_options(request, runtime)

    async def list_emr_hive_tables_async(
        self,
        request: dataworks_public_20180601_models.ListEmrHiveTablesRequest,
    ) -> dataworks_public_20180601_models.ListEmrHiveTablesResponse:
        """
        @param request: ListEmrHiveTablesRequest
        @return: ListEmrHiveTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_hive_tables_with_options_async(request, runtime)

    def list_governance_issue_data_service_apis_with_options(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse:
        """
        @summary 查询数据服务API
        
        @param request: ListGovernanceIssueDataServiceAPIsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueDataServiceAPIsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueDataServiceAPIs',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_governance_issue_data_service_apis_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse:
        """
        @summary 查询数据服务API
        
        @param request: ListGovernanceIssueDataServiceAPIsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueDataServiceAPIsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueDataServiceAPIs',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_governance_issue_data_service_apis(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse:
        """
        @summary 查询数据服务API
        
        @param request: ListGovernanceIssueDataServiceAPIsRequest
        @return: ListGovernanceIssueDataServiceAPIsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_governance_issue_data_service_apis_with_options(request, runtime)

    async def list_governance_issue_data_service_apis_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueDataServiceAPIsResponse:
        """
        @summary 查询数据服务API
        
        @param request: ListGovernanceIssueDataServiceAPIsRequest
        @return: ListGovernanceIssueDataServiceAPIsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_governance_issue_data_service_apis_with_options_async(request, runtime)

    def list_governance_issue_tables_with_options(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTablesResponse:
        """
        @summary 查询治理项问题详情
        
        @param request: ListGovernanceIssueTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueTables',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_governance_issue_tables_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTablesResponse:
        """
        @summary 查询治理项问题详情
        
        @param request: ListGovernanceIssueTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueTables',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_governance_issue_tables(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTablesRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTablesResponse:
        """
        @summary 查询治理项问题详情
        
        @param request: ListGovernanceIssueTablesRequest
        @return: ListGovernanceIssueTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_governance_issue_tables_with_options(request, runtime)

    async def list_governance_issue_tables_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTablesRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTablesResponse:
        """
        @summary 查询治理项问题详情
        
        @param request: ListGovernanceIssueTablesRequest
        @return: ListGovernanceIssueTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_governance_issue_tables_with_options_async(request, runtime)

    def list_governance_issue_tasks_with_options(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTasksResponse:
        """
        @summary 查询治理项-任务问题详情
        
        @param request: ListGovernanceIssueTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueTasks',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_governance_issue_tasks_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTasksResponse:
        """
        @summary 查询治理项-任务问题详情
        
        @param request: ListGovernanceIssueTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceIssueTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rule_category):
            body['RuleCategory'] = request.rule_category
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceIssueTasks',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceIssueTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_governance_issue_tasks(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTasksRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTasksResponse:
        """
        @summary 查询治理项-任务问题详情
        
        @param request: ListGovernanceIssueTasksRequest
        @return: ListGovernanceIssueTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_governance_issue_tasks_with_options(request, runtime)

    async def list_governance_issue_tasks_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceIssueTasksRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceIssueTasksResponse:
        """
        @summary 查询治理项-任务问题详情
        
        @param request: ListGovernanceIssueTasksRequest
        @return: ListGovernanceIssueTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_governance_issue_tasks_with_options_async(request, runtime)

    def list_governance_rules_with_options(
        self,
        request: dataworks_public_20180601_models.ListGovernanceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceRulesResponse:
        """
        @summary 查询治理项定义信息
        
        @param request: ListGovernanceRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.issue_type):
            body['IssueType'] = request.issue_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceRules',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_governance_rules_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListGovernanceRulesResponse:
        """
        @summary 查询治理项定义信息
        
        @param request: ListGovernanceRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGovernanceRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.issue_type):
            body['IssueType'] = request.issue_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGovernanceRules',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListGovernanceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_governance_rules(
        self,
        request: dataworks_public_20180601_models.ListGovernanceRulesRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceRulesResponse:
        """
        @summary 查询治理项定义信息
        
        @param request: ListGovernanceRulesRequest
        @return: ListGovernanceRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_governance_rules_with_options(request, runtime)

    async def list_governance_rules_async(
        self,
        request: dataworks_public_20180601_models.ListGovernanceRulesRequest,
    ) -> dataworks_public_20180601_models.ListGovernanceRulesResponse:
        """
        @summary 查询治理项定义信息
        
        @param request: ListGovernanceRulesRequest
        @return: ListGovernanceRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_governance_rules_with_options_async(request, runtime)

    def list_hive_column_lineages_with_options(
        self,
        request: dataworks_public_20180601_models.ListHiveColumnLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListHiveColumnLineagesResponse:
        """
        @param request: ListHiveColumnLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHiveColumnLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHiveColumnLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveColumnLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hive_column_lineages_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListHiveColumnLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListHiveColumnLineagesResponse:
        """
        @param request: ListHiveColumnLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHiveColumnLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHiveColumnLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveColumnLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hive_column_lineages(
        self,
        request: dataworks_public_20180601_models.ListHiveColumnLineagesRequest,
    ) -> dataworks_public_20180601_models.ListHiveColumnLineagesResponse:
        """
        @param request: ListHiveColumnLineagesRequest
        @return: ListHiveColumnLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hive_column_lineages_with_options(request, runtime)

    async def list_hive_column_lineages_async(
        self,
        request: dataworks_public_20180601_models.ListHiveColumnLineagesRequest,
    ) -> dataworks_public_20180601_models.ListHiveColumnLineagesResponse:
        """
        @param request: ListHiveColumnLineagesRequest
        @return: ListHiveColumnLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hive_column_lineages_with_options_async(request, runtime)

    def list_hive_table_lineages_with_options(
        self,
        request: dataworks_public_20180601_models.ListHiveTableLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListHiveTableLineagesResponse:
        """
        @param request: ListHiveTableLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHiveTableLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHiveTableLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveTableLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hive_table_lineages_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListHiveTableLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListHiveTableLineagesResponse:
        """
        @param request: ListHiveTableLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHiveTableLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHiveTableLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveTableLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hive_table_lineages(
        self,
        request: dataworks_public_20180601_models.ListHiveTableLineagesRequest,
    ) -> dataworks_public_20180601_models.ListHiveTableLineagesResponse:
        """
        @param request: ListHiveTableLineagesRequest
        @return: ListHiveTableLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hive_table_lineages_with_options(request, runtime)

    async def list_hive_table_lineages_async(
        self,
        request: dataworks_public_20180601_models.ListHiveTableLineagesRequest,
    ) -> dataworks_public_20180601_models.ListHiveTableLineagesResponse:
        """
        @param request: ListHiveTableLineagesRequest
        @return: ListHiveTableLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hive_table_lineages_with_options_async(request, runtime)

    def list_table_partitions_with_options(
        self,
        request: dataworks_public_20180601_models.ListTablePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListTablePartitionsResponse:
        """
        @param request: ListTablePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablePartitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTablePartitions',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListTablePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_partitions_with_options_async(
        self,
        request: dataworks_public_20180601_models.ListTablePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.ListTablePartitionsResponse:
        """
        @param request: ListTablePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablePartitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTablePartitions',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListTablePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_partitions(
        self,
        request: dataworks_public_20180601_models.ListTablePartitionsRequest,
    ) -> dataworks_public_20180601_models.ListTablePartitionsResponse:
        """
        @param request: ListTablePartitionsRequest
        @return: ListTablePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_table_partitions_with_options(request, runtime)

    async def list_table_partitions_async(
        self,
        request: dataworks_public_20180601_models.ListTablePartitionsRequest,
    ) -> dataworks_public_20180601_models.ListTablePartitionsResponse:
        """
        @param request: ListTablePartitionsRequest
        @return: ListTablePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_table_partitions_with_options_async(request, runtime)

    def open_data_works_standard_service_with_options(
        self,
        request: dataworks_public_20180601_models.OpenDataWorksStandardServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse:
        """
        @param request: OpenDataWorksStandardServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDataWorksStandardServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDataWorksStandardService',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_data_works_standard_service_with_options_async(
        self,
        request: dataworks_public_20180601_models.OpenDataWorksStandardServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse:
        """
        @param request: OpenDataWorksStandardServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDataWorksStandardServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDataWorksStandardService',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_data_works_standard_service(
        self,
        request: dataworks_public_20180601_models.OpenDataWorksStandardServiceRequest,
    ) -> dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse:
        """
        @param request: OpenDataWorksStandardServiceRequest
        @return: OpenDataWorksStandardServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_data_works_standard_service_with_options(request, runtime)

    async def open_data_works_standard_service_async(
        self,
        request: dataworks_public_20180601_models.OpenDataWorksStandardServiceRequest,
    ) -> dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse:
        """
        @param request: OpenDataWorksStandardServiceRequest
        @return: OpenDataWorksStandardServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_data_works_standard_service_with_options_async(request, runtime)

    def search_manual_dag_node_instance_with_options(
        self,
        request: dataworks_public_20180601_models.SearchManualDagNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse:
        """
        @param request: SearchManualDagNodeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchManualDagNodeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchManualDagNodeInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_manual_dag_node_instance_with_options_async(
        self,
        request: dataworks_public_20180601_models.SearchManualDagNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse:
        """
        @param request: SearchManualDagNodeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchManualDagNodeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchManualDagNodeInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_manual_dag_node_instance(
        self,
        request: dataworks_public_20180601_models.SearchManualDagNodeInstanceRequest,
    ) -> dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse:
        """
        @param request: SearchManualDagNodeInstanceRequest
        @return: SearchManualDagNodeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_manual_dag_node_instance_with_options(request, runtime)

    async def search_manual_dag_node_instance_async(
        self,
        request: dataworks_public_20180601_models.SearchManualDagNodeInstanceRequest,
    ) -> dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse:
        """
        @param request: SearchManualDagNodeInstanceRequest
        @return: SearchManualDagNodeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_manual_dag_node_instance_with_options_async(request, runtime)

    def send_task_meta_callback_with_options(
        self,
        request: dataworks_public_20180601_models.SendTaskMetaCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SendTaskMetaCallbackResponse:
        """
        @param request: SendTaskMetaCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTaskMetaCallbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.connection_info):
            body['ConnectionInfo'] = request.connection_info
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_type):
            body['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.task_env_param):
            body['TaskEnvParam'] = request.task_env_param
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTaskMetaCallback',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SendTaskMetaCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_task_meta_callback_with_options_async(
        self,
        request: dataworks_public_20180601_models.SendTaskMetaCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SendTaskMetaCallbackResponse:
        """
        @param request: SendTaskMetaCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTaskMetaCallbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.connection_info):
            body['ConnectionInfo'] = request.connection_info
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_type):
            body['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.task_env_param):
            body['TaskEnvParam'] = request.task_env_param
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTaskMetaCallback',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SendTaskMetaCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_task_meta_callback(
        self,
        request: dataworks_public_20180601_models.SendTaskMetaCallbackRequest,
    ) -> dataworks_public_20180601_models.SendTaskMetaCallbackResponse:
        """
        @param request: SendTaskMetaCallbackRequest
        @return: SendTaskMetaCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_task_meta_callback_with_options(request, runtime)

    async def send_task_meta_callback_async(
        self,
        request: dataworks_public_20180601_models.SendTaskMetaCallbackRequest,
    ) -> dataworks_public_20180601_models.SendTaskMetaCallbackResponse:
        """
        @param request: SendTaskMetaCallbackRequest
        @return: SendTaskMetaCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_task_meta_callback_with_options_async(request, runtime)

    def set_switch_value_with_options(
        self,
        request: dataworks_public_20180601_models.SetSwitchValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SetSwitchValueResponse:
        """
        @summary 设置Switch的值
        
        @param request: SetSwitchValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSwitchValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_name):
            query['SwitchName'] = request.switch_name
        if not UtilClient.is_unset(request.switch_value):
            query['SwitchValue'] = request.switch_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSwitchValue',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SetSwitchValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_switch_value_with_options_async(
        self,
        request: dataworks_public_20180601_models.SetSwitchValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.SetSwitchValueResponse:
        """
        @summary 设置Switch的值
        
        @param request: SetSwitchValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSwitchValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_name):
            query['SwitchName'] = request.switch_name
        if not UtilClient.is_unset(request.switch_value):
            query['SwitchValue'] = request.switch_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSwitchValue',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SetSwitchValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_switch_value(
        self,
        request: dataworks_public_20180601_models.SetSwitchValueRequest,
    ) -> dataworks_public_20180601_models.SetSwitchValueResponse:
        """
        @summary 设置Switch的值
        
        @param request: SetSwitchValueRequest
        @return: SetSwitchValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_switch_value_with_options(request, runtime)

    async def set_switch_value_async(
        self,
        request: dataworks_public_20180601_models.SetSwitchValueRequest,
    ) -> dataworks_public_20180601_models.SetSwitchValueResponse:
        """
        @summary 设置Switch的值
        
        @param request: SetSwitchValueRequest
        @return: SetSwitchValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_switch_value_with_options_async(request, runtime)

    def start_collect_quality_with_options(
        self,
        request: dataworks_public_20180601_models.StartCollectQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartCollectQualityResponse:
        """
        @summary startCollect
        
        @param request: StartCollectQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCollectQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCollectQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartCollectQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_collect_quality_with_options_async(
        self,
        request: dataworks_public_20180601_models.StartCollectQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartCollectQualityResponse:
        """
        @summary startCollect
        
        @param request: StartCollectQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCollectQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCollectQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartCollectQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_collect_quality(
        self,
        request: dataworks_public_20180601_models.StartCollectQualityRequest,
    ) -> dataworks_public_20180601_models.StartCollectQualityResponse:
        """
        @summary startCollect
        
        @param request: StartCollectQualityRequest
        @return: StartCollectQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_collect_quality_with_options(request, runtime)

    async def start_collect_quality_async(
        self,
        request: dataworks_public_20180601_models.StartCollectQualityRequest,
    ) -> dataworks_public_20180601_models.StartCollectQualityResponse:
        """
        @summary startCollect
        
        @param request: StartCollectQualityRequest
        @return: StartCollectQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_collect_quality_with_options_async(request, runtime)

    def start_do_check_quality_with_options(
        self,
        request: dataworks_public_20180601_models.StartDoCheckQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartDoCheckQualityResponse:
        """
        @param request: StartDoCheckQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDoCheckQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartDoCheckQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartDoCheckQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_do_check_quality_with_options_async(
        self,
        request: dataworks_public_20180601_models.StartDoCheckQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartDoCheckQualityResponse:
        """
        @param request: StartDoCheckQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDoCheckQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartDoCheckQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartDoCheckQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_do_check_quality(
        self,
        request: dataworks_public_20180601_models.StartDoCheckQualityRequest,
    ) -> dataworks_public_20180601_models.StartDoCheckQualityResponse:
        """
        @param request: StartDoCheckQualityRequest
        @return: StartDoCheckQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_do_check_quality_with_options(request, runtime)

    async def start_do_check_quality_async(
        self,
        request: dataworks_public_20180601_models.StartDoCheckQualityRequest,
    ) -> dataworks_public_20180601_models.StartDoCheckQualityResponse:
        """
        @param request: StartDoCheckQualityRequest
        @return: StartDoCheckQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_do_check_quality_with_options_async(request, runtime)

    def start_task_quality_with_options(
        self,
        request: dataworks_public_20180601_models.StartTaskQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartTaskQualityResponse:
        """
        @param request: StartTaskQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTaskQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartTaskQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_quality_with_options_async(
        self,
        request: dataworks_public_20180601_models.StartTaskQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.StartTaskQualityResponse:
        """
        @param request: StartTaskQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_result_string):
            body['CallbackResultString'] = request.callback_result_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTaskQuality',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartTaskQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task_quality(
        self,
        request: dataworks_public_20180601_models.StartTaskQualityRequest,
    ) -> dataworks_public_20180601_models.StartTaskQualityResponse:
        """
        @param request: StartTaskQualityRequest
        @return: StartTaskQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_task_quality_with_options(request, runtime)

    async def start_task_quality_async(
        self,
        request: dataworks_public_20180601_models.StartTaskQualityRequest,
    ) -> dataworks_public_20180601_models.StartTaskQualityResponse:
        """
        @param request: StartTaskQualityRequest
        @return: StartTaskQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_task_quality_with_options_async(request, runtime)

    def trigger_data_loader_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.TriggerDataLoaderResponse:
        """
        @summary 触发元数据的Merge操作
        
        @param request: TriggerDataLoaderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerDataLoaderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TriggerDataLoader',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TriggerDataLoaderResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_data_loader_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.TriggerDataLoaderResponse:
        """
        @summary 触发元数据的Merge操作
        
        @param request: TriggerDataLoaderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerDataLoaderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TriggerDataLoader',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TriggerDataLoaderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_data_loader(self) -> dataworks_public_20180601_models.TriggerDataLoaderResponse:
        """
        @summary 触发元数据的Merge操作
        
        @return: TriggerDataLoaderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_data_loader_with_options(runtime)

    async def trigger_data_loader_async(self) -> dataworks_public_20180601_models.TriggerDataLoaderResponse:
        """
        @summary 触发元数据的Merge操作
        
        @return: TriggerDataLoaderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_data_loader_with_options_async(runtime)

    def trigger_time_machine_task_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.TriggerTimeMachineTaskResponse:
        """
        @summary 触发timeMachine任务
        
        @param request: TriggerTimeMachineTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerTimeMachineTaskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TriggerTimeMachineTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TriggerTimeMachineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_time_machine_task_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20180601_models.TriggerTimeMachineTaskResponse:
        """
        @summary 触发timeMachine任务
        
        @param request: TriggerTimeMachineTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerTimeMachineTaskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TriggerTimeMachineTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TriggerTimeMachineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_time_machine_task(self) -> dataworks_public_20180601_models.TriggerTimeMachineTaskResponse:
        """
        @summary 触发timeMachine任务
        
        @return: TriggerTimeMachineTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_time_machine_task_with_options(runtime)

    async def trigger_time_machine_task_async(self) -> dataworks_public_20180601_models.TriggerTimeMachineTaskResponse:
        """
        @summary 触发timeMachine任务
        
        @return: TriggerTimeMachineTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_time_machine_task_with_options_async(runtime)
