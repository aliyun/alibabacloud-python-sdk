# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yuqing20210126 import models as yuqing_20210126_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yuqing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_alarm_data_list(
        self,
        request: yuqing_20210126_models.QueryAlarmDataListRequest,
    ) -> yuqing_20210126_models.QueryAlarmDataListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_alarm_data_list_with_options(request, headers, runtime)

    async def query_alarm_data_list_async(
        self,
        request: yuqing_20210126_models.QueryAlarmDataListRequest,
    ) -> yuqing_20210126_models.QueryAlarmDataListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_alarm_data_list_with_options_async(request, headers, runtime)

    def query_alarm_data_list_with_options(
        self,
        request: yuqing_20210126_models.QueryAlarmDataListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryAlarmDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_query):
            query['alarmQuery'] = request.alarm_query
        if not UtilClient.is_unset(request.order_by_key):
            query['orderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryAlarmDataListResponse().from_map(
            self.do_roarequest('QueryAlarmDataList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryAlarmDataList.json', 'json', req, runtime)
        )

    async def query_alarm_data_list_with_options_async(
        self,
        request: yuqing_20210126_models.QueryAlarmDataListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryAlarmDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_query):
            query['alarmQuery'] = request.alarm_query
        if not UtilClient.is_unset(request.order_by_key):
            query['orderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryAlarmDataListResponse().from_map(
            await self.do_roarequest_async('QueryAlarmDataList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryAlarmDataList.json', 'json', req, runtime)
        )

    def get_analysis_component_result(
        self,
        request: yuqing_20210126_models.GetAnalysisComponentResultRequest,
    ) -> yuqing_20210126_models.GetAnalysisComponentResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_analysis_component_result_with_options(request, headers, runtime)

    async def get_analysis_component_result_async(
        self,
        request: yuqing_20210126_models.GetAnalysisComponentResultRequest,
    ) -> yuqing_20210126_models.GetAnalysisComponentResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_analysis_component_result_with_options_async(request, headers, runtime)

    def get_analysis_component_result_with_options(
        self,
        request: yuqing_20210126_models.GetAnalysisComponentResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.GetAnalysisComponentResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.GetAnalysisComponentResultResponse().from_map(
            self.do_roarequest('GetAnalysisComponentResult', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/getAnalysisComponentResult.json', 'json', req, runtime)
        )

    async def get_analysis_component_result_with_options_async(
        self,
        request: yuqing_20210126_models.GetAnalysisComponentResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.GetAnalysisComponentResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.GetAnalysisComponentResultResponse().from_map(
            await self.do_roarequest_async('GetAnalysisComponentResult', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/getAnalysisComponentResult.json', 'json', req, runtime)
        )

    def get_message_detail(
        self,
        request: yuqing_20210126_models.GetMessageDetailRequest,
    ) -> yuqing_20210126_models.GetMessageDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_detail_with_options(request, headers, runtime)

    async def get_message_detail_async(
        self,
        request: yuqing_20210126_models.GetMessageDetailRequest,
    ) -> yuqing_20210126_models.GetMessageDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_message_detail_with_options_async(request, headers, runtime)

    def get_message_detail_with_options(
        self,
        request: yuqing_20210126_models.GetMessageDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.GetMessageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.GetMessageDetailResponse().from_map(
            self.do_roarequest('GetMessageDetail', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/getMessageFromHbase.json', 'json', req, runtime)
        )

    async def get_message_detail_with_options_async(
        self,
        request: yuqing_20210126_models.GetMessageDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.GetMessageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.GetMessageDetailResponse().from_map(
            await self.do_roarequest_async('GetMessageDetail', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/getMessageFromHbase.json', 'json', req, runtime)
        )

    def create_project(
        self,
        request: yuqing_20210126_models.CreateProjectRequest,
    ) -> yuqing_20210126_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: yuqing_20210126_models.CreateProjectRequest,
    ) -> yuqing_20210126_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: yuqing_20210126_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.create_user_id):
            body['createUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.create_user_name):
            body['createUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.CreateProjectResponse().from_map(
            self.do_roarequest_with_form('CreateProject', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/createProject.json', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: yuqing_20210126_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.create_user_id):
            body['createUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.create_user_name):
            body['createUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.CreateProjectResponse().from_map(
            await self.do_roarequest_with_form_async('CreateProject', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/createProject.json', 'json', req, runtime)
        )

    def query_project_list(
        self,
        request: yuqing_20210126_models.QueryProjectListRequest,
    ) -> yuqing_20210126_models.QueryProjectListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_project_list_with_options(request, headers, runtime)

    async def query_project_list_async(
        self,
        request: yuqing_20210126_models.QueryProjectListRequest,
    ) -> yuqing_20210126_models.QueryProjectListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_project_list_with_options_async(request, headers, runtime)

    def query_project_list_with_options(
        self,
        request: yuqing_20210126_models.QueryProjectListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryProjectListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_group_id):
            query['projectGroupId'] = request.project_group_id
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryProjectListResponse().from_map(
            self.do_roarequest('QueryProjectList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryProjectList.json', 'json', req, runtime)
        )

    async def query_project_list_with_options_async(
        self,
        request: yuqing_20210126_models.QueryProjectListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryProjectListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_group_id):
            query['projectGroupId'] = request.project_group_id
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryProjectListResponse().from_map(
            await self.do_roarequest_async('QueryProjectList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryProjectList.json', 'json', req, runtime)
        )

    def query_tag_nodes(
        self,
        request: yuqing_20210126_models.QueryTagNodesRequest,
    ) -> yuqing_20210126_models.QueryTagNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_tag_nodes_with_options(request, headers, runtime)

    async def query_tag_nodes_async(
        self,
        request: yuqing_20210126_models.QueryTagNodesRequest,
    ) -> yuqing_20210126_models.QueryTagNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_tag_nodes_with_options_async(request, headers, runtime)

    def query_tag_nodes_with_options(
        self,
        request: yuqing_20210126_models.QueryTagNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryTagNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryTagNodesResponse().from_map(
            self.do_roarequest('QueryTagNodes', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryTagNodes.json', 'json', req, runtime)
        )

    async def query_tag_nodes_with_options_async(
        self,
        request: yuqing_20210126_models.QueryTagNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryTagNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryTagNodesResponse().from_map(
            await self.do_roarequest_async('QueryTagNodes', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryTagNodes.json', 'json', req, runtime)
        )

    def query_report_notifies(
        self,
        request: yuqing_20210126_models.QueryReportNotifiesRequest,
    ) -> yuqing_20210126_models.QueryReportNotifiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_report_notifies_with_options(request, headers, runtime)

    async def query_report_notifies_async(
        self,
        request: yuqing_20210126_models.QueryReportNotifiesRequest,
    ) -> yuqing_20210126_models.QueryReportNotifiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_report_notifies_with_options_async(request, headers, runtime)

    def query_report_notifies_with_options(
        self,
        request: yuqing_20210126_models.QueryReportNotifiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryReportNotifiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cp_id):
            query['cpId'] = request.cp_id
        if not UtilClient.is_unset(request.create_end_timestamp):
            query['createEndTimestamp'] = request.create_end_timestamp
        if not UtilClient.is_unset(request.create_start_timestamp):
            query['createStartTimestamp'] = request.create_start_timestamp
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.subject):
            query['subject'] = request.subject
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryReportNotifiesResponse().from_map(
            self.do_roarequest('QueryReportNotifies', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryReportNotifies.json', 'json', req, runtime)
        )

    async def query_report_notifies_with_options_async(
        self,
        request: yuqing_20210126_models.QueryReportNotifiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryReportNotifiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cp_id):
            query['cpId'] = request.cp_id
        if not UtilClient.is_unset(request.create_end_timestamp):
            query['createEndTimestamp'] = request.create_end_timestamp
        if not UtilClient.is_unset(request.create_start_timestamp):
            query['createStartTimestamp'] = request.create_start_timestamp
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.subject):
            query['subject'] = request.subject
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryReportNotifiesResponse().from_map(
            await self.do_roarequest_async('QueryReportNotifies', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryReportNotifies.json', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: yuqing_20210126_models.DeleteProjectRequest,
    ) -> yuqing_20210126_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(request, headers, runtime)

    async def delete_project_async(
        self,
        request: yuqing_20210126_models.DeleteProjectRequest,
    ) -> yuqing_20210126_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(request, headers, runtime)

    def delete_project_with_options(
        self,
        request: yuqing_20210126_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.modified_user_id):
            body['modifiedUserId'] = request.modified_user_id
        if not UtilClient.is_unset(request.modified_user_name):
            body['modifiedUserName'] = request.modified_user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.DeleteProjectResponse().from_map(
            self.do_roarequest_with_form('DeleteProject', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/deleteProject.json', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: yuqing_20210126_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.modified_user_id):
            body['modifiedUserId'] = request.modified_user_id
        if not UtilClient.is_unset(request.modified_user_name):
            body['modifiedUserName'] = request.modified_user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.DeleteProjectResponse().from_map(
            await self.do_roarequest_with_form_async('DeleteProject', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/deleteProject.json', 'json', req, runtime)
        )

    def query_filter_list(
        self,
        request: yuqing_20210126_models.QueryFilterListRequest,
    ) -> yuqing_20210126_models.QueryFilterListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_filter_list_with_options(request, headers, runtime)

    async def query_filter_list_async(
        self,
        request: yuqing_20210126_models.QueryFilterListRequest,
    ) -> yuqing_20210126_models.QueryFilterListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_filter_list_with_options_async(request, headers, runtime)

    def query_filter_list_with_options(
        self,
        request: yuqing_20210126_models.QueryFilterListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryFilterListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.filter_id):
            query['filterId'] = request.filter_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryFilterListResponse().from_map(
            self.do_roarequest('QueryFilterList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryFilterList.json', 'json', req, runtime)
        )

    async def query_filter_list_with_options_async(
        self,
        request: yuqing_20210126_models.QueryFilterListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryFilterListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.filter_id):
            query['filterId'] = request.filter_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return yuqing_20210126_models.QueryFilterListResponse().from_map(
            await self.do_roarequest_async('QueryFilterList', '2021-01-26', 'HTTPS', 'GET', 'AK', f'/openapi/aliyun/queryFilterList.json', 'json', req, runtime)
        )

    def aggregate_search_yuqing(
        self,
        request: yuqing_20210126_models.AggregateSearchYuqingRequest,
    ) -> yuqing_20210126_models.AggregateSearchYuqingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aggregate_search_yuqing_with_options(request, headers, runtime)

    async def aggregate_search_yuqing_async(
        self,
        request: yuqing_20210126_models.AggregateSearchYuqingRequest,
    ) -> yuqing_20210126_models.AggregateSearchYuqingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.aggregate_search_yuqing_with_options_async(request, headers, runtime)

    def aggregate_search_yuqing_with_options(
        self,
        request: yuqing_20210126_models.AggregateSearchYuqingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.AggregateSearchYuqingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.aggregate_function):
            body['aggregateFunction'] = request.aggregate_function
        if not UtilClient.is_unset(request.group_by_key):
            body['groupByKey'] = request.group_by_key
        if not UtilClient.is_unset(request.group_limits):
            body['groupLimits'] = request.group_limits
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.AggregateSearchYuqingResponse().from_map(
            self.do_roarequest_with_form('AggregateSearchYuqing', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/aggSearch.json', 'json', req, runtime)
        )

    async def aggregate_search_yuqing_with_options_async(
        self,
        request: yuqing_20210126_models.AggregateSearchYuqingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.AggregateSearchYuqingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.aggregate_function):
            body['aggregateFunction'] = request.aggregate_function
        if not UtilClient.is_unset(request.group_by_key):
            body['groupByKey'] = request.group_by_key
        if not UtilClient.is_unset(request.group_limits):
            body['groupLimits'] = request.group_limits
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.AggregateSearchYuqingResponse().from_map(
            await self.do_roarequest_with_form_async('AggregateSearchYuqing', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/aggSearch.json', 'json', req, runtime)
        )

    def query_analysis_component(
        self,
        request: yuqing_20210126_models.QueryAnalysisComponentRequest,
    ) -> yuqing_20210126_models.QueryAnalysisComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_analysis_component_with_options(request, headers, runtime)

    async def query_analysis_component_async(
        self,
        request: yuqing_20210126_models.QueryAnalysisComponentRequest,
    ) -> yuqing_20210126_models.QueryAnalysisComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_analysis_component_with_options_async(request, headers, runtime)

    def query_analysis_component_with_options(
        self,
        request: yuqing_20210126_models.QueryAnalysisComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryAnalysisComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.analyse_type):
            body['analyseType'] = request.analyse_type
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.QueryAnalysisComponentResponse().from_map(
            self.do_roarequest_with_form('QueryAnalysisComponent', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/queryAnalysisComponent.json', 'json', req, runtime)
        )

    async def query_analysis_component_with_options_async(
        self,
        request: yuqing_20210126_models.QueryAnalysisComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.QueryAnalysisComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.analyse_type):
            body['analyseType'] = request.analyse_type
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.QueryAnalysisComponentResponse().from_map(
            await self.do_roarequest_with_form_async('QueryAnalysisComponent', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/queryAnalysisComponent.json', 'json', req, runtime)
        )

    def update_propagation(
        self,
        request: yuqing_20210126_models.UpdatePropagationRequest,
    ) -> yuqing_20210126_models.UpdatePropagationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_propagation_with_options(request, headers, runtime)

    async def update_propagation_async(
        self,
        request: yuqing_20210126_models.UpdatePropagationRequest,
    ) -> yuqing_20210126_models.UpdatePropagationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_propagation_with_options_async(request, headers, runtime)

    def update_propagation_with_options(
        self,
        request: yuqing_20210126_models.UpdatePropagationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.UpdatePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.weibo_urls):
            body['weiboUrls'] = request.weibo_urls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.UpdatePropagationResponse().from_map(
            self.do_roarequest_with_form('UpdatePropagation', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/updatePropagation.json', 'json', req, runtime)
        )

    async def update_propagation_with_options_async(
        self,
        request: yuqing_20210126_models.UpdatePropagationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.UpdatePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.weibo_urls):
            body['weiboUrls'] = request.weibo_urls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.UpdatePropagationResponse().from_map(
            await self.do_roarequest_with_form_async('UpdatePropagation', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/updatePropagation.json', 'json', req, runtime)
        )

    def list_yuqing_messages(
        self,
        request: yuqing_20210126_models.ListYuqingMessagesRequest,
    ) -> yuqing_20210126_models.ListYuqingMessagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_yuqing_messages_with_options(request, headers, runtime)

    async def list_yuqing_messages_async(
        self,
        request: yuqing_20210126_models.ListYuqingMessagesRequest,
    ) -> yuqing_20210126_models.ListYuqingMessagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_yuqing_messages_with_options_async(request, headers, runtime)

    def list_yuqing_messages_with_options(
        self,
        request: yuqing_20210126_models.ListYuqingMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.ListYuqingMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.ListYuqingMessagesResponse().from_map(
            self.do_roarequest_with_form('ListYuqingMessages', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/searchMessages.json', 'json', req, runtime)
        )

    async def list_yuqing_messages_with_options_async(
        self,
        request: yuqing_20210126_models.ListYuqingMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20210126_models.ListYuqingMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return yuqing_20210126_models.ListYuqingMessagesResponse().from_map(
            await self.do_roarequest_with_form_async('ListYuqingMessages', '2021-01-26', 'HTTPS', 'POST', 'AK', f'/openapi/aliyun/searchMessages.json', 'json', req, runtime)
        )
