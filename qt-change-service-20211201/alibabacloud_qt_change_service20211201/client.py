# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qt_change_service20211201 import models as qt_change_service_20211201_models
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
        self._endpoint = self.get_endpoint('qt-change-service', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_component_enum(self) -> qt_change_service_20211201_models.ChangeComponentEnumResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_component_enum_with_options(headers, runtime)

    async def change_component_enum_async(self) -> qt_change_service_20211201_models.ChangeComponentEnumResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_component_enum_with_options_async(headers, runtime)

    def change_component_enum_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.ChangeComponentEnumResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ChangeComponentEnum',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/changeComponentEnum',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.ChangeComponentEnumResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_component_enum_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.ChangeComponentEnumResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ChangeComponentEnum',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/changeComponentEnum',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.ChangeComponentEnumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scence(
        self,
        request: qt_change_service_20211201_models.CreateScenceRequest,
    ) -> qt_change_service_20211201_models.CreateScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scence_with_options(request, headers, runtime)

    async def create_scence_async(
        self,
        request: qt_change_service_20211201_models.CreateScenceRequest,
    ) -> qt_change_service_20211201_models.CreateScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scence_with_options_async(request, headers, runtime)

    def create_scence_with_options(
        self,
        request: qt_change_service_20211201_models.CreateScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.CreateScenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dst_knowledge):
            body['DstKnowledge'] = request.dst_knowledge
        if not UtilClient.is_unset(request.graph_id):
            body['GraphId'] = request.graph_id
        if not UtilClient.is_unset(request.is_non_profit):
            body['IsNonProfit'] = request.is_non_profit
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.result_type):
            body['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.src_knowledge):
            body['SrcKnowledge'] = request.src_knowledge
        if not UtilClient.is_unset(request.work_name):
            body['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.CreateScenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scence_with_options_async(
        self,
        request: qt_change_service_20211201_models.CreateScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.CreateScenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dst_knowledge):
            body['DstKnowledge'] = request.dst_knowledge
        if not UtilClient.is_unset(request.graph_id):
            body['GraphId'] = request.graph_id
        if not UtilClient.is_unset(request.is_non_profit):
            body['IsNonProfit'] = request.is_non_profit
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.result_type):
            body['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.src_knowledge):
            body['SrcKnowledge'] = request.src_knowledge
        if not UtilClient.is_unset(request.work_name):
            body['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.CreateScenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scence(
        self,
        request: qt_change_service_20211201_models.DeleteScenceRequest,
    ) -> qt_change_service_20211201_models.DeleteScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scence_with_options(request, headers, runtime)

    async def delete_scence_async(
        self,
        request: qt_change_service_20211201_models.DeleteScenceRequest,
    ) -> qt_change_service_20211201_models.DeleteScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scence_with_options_async(request, headers, runtime)

    def delete_scence_with_options(
        self,
        request: qt_change_service_20211201_models.DeleteScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.DeleteScenceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.DeleteScenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scence_with_options_async(
        self,
        request: qt_change_service_20211201_models.DeleteScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.DeleteScenceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.DeleteScenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scence_result(
        self,
        request: qt_change_service_20211201_models.GetScenceResultRequest,
    ) -> qt_change_service_20211201_models.GetScenceResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scence_result_with_options(request, headers, runtime)

    async def get_scence_result_async(
        self,
        request: qt_change_service_20211201_models.GetScenceResultRequest,
    ) -> qt_change_service_20211201_models.GetScenceResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scence_result_with_options_async(request, headers, runtime)

    def get_scence_result_with_options(
        self,
        request: qt_change_service_20211201_models.GetScenceResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.GetScenceResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenceResult',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.GetScenceResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scence_result_with_options_async(
        self,
        request: qt_change_service_20211201_models.GetScenceResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.GetScenceResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenceResult',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.GetScenceResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scences_list(
        self,
        request: qt_change_service_20211201_models.GetScencesListRequest,
    ) -> qt_change_service_20211201_models.GetScencesListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scences_list_with_options(request, headers, runtime)

    async def get_scences_list_async(
        self,
        request: qt_change_service_20211201_models.GetScencesListRequest,
    ) -> qt_change_service_20211201_models.GetScencesListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scences_list_with_options_async(request, headers, runtime)

    def get_scences_list_with_options(
        self,
        request: qt_change_service_20211201_models.GetScencesListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.GetScencesListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.work_name):
            query['workName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScencesList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.GetScencesListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scences_list_with_options_async(
        self,
        request: qt_change_service_20211201_models.GetScencesListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.GetScencesListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.work_name):
            query['workName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScencesList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.GetScencesListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scence(
        self,
        request: qt_change_service_20211201_models.ModifyScenceRequest,
    ) -> qt_change_service_20211201_models.ModifyScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scence_with_options(request, headers, runtime)

    async def modify_scence_async(
        self,
        request: qt_change_service_20211201_models.ModifyScenceRequest,
    ) -> qt_change_service_20211201_models.ModifyScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scence_with_options_async(request, headers, runtime)

    def modify_scence_with_options(
        self,
        request: qt_change_service_20211201_models.ModifyScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.ModifyScenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creater):
            body['Creater'] = request.creater
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.rule_body):
            body['RuleBody'] = request.rule_body
        if not UtilClient.is_unset(request.rule_describe):
            body['RuleDescribe'] = request.rule_describe
        if not UtilClient.is_unset(request.rule_status):
            body['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.work_id):
            body['WorkId'] = request.work_id
        if not UtilClient.is_unset(request.work_name):
            body['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.ModifyScenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scence_with_options_async(
        self,
        request: qt_change_service_20211201_models.ModifyScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.ModifyScenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creater):
            body['Creater'] = request.creater
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.rule_body):
            body['RuleBody'] = request.rule_body
        if not UtilClient.is_unset(request.rule_describe):
            body['RuleDescribe'] = request.rule_describe
        if not UtilClient.is_unset(request.rule_status):
            body['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.work_id):
            body['WorkId'] = request.work_id
        if not UtilClient.is_unset(request.work_name):
            body['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scene/scenario',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.ModifyScenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scence(
        self,
        request: qt_change_service_20211201_models.QueryScenceRequest,
    ) -> qt_change_service_20211201_models.QueryScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scence_with_options(request, headers, runtime)

    async def query_scence_async(
        self,
        request: qt_change_service_20211201_models.QueryScenceRequest,
    ) -> qt_change_service_20211201_models.QueryScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_scence_with_options_async(request, headers, runtime)

    def query_scence_with_options(
        self,
        request: qt_change_service_20211201_models.QueryScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.QueryScenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='QueryScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.QueryScenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scence_with_options_async(
        self,
        request: qt_change_service_20211201_models.QueryScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.QueryScenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='QueryScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.QueryScenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def status_scence(
        self,
        request: qt_change_service_20211201_models.StatusScenceRequest,
    ) -> qt_change_service_20211201_models.StatusScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.status_scence_with_options(request, headers, runtime)

    async def status_scence_async(
        self,
        request: qt_change_service_20211201_models.StatusScenceRequest,
    ) -> qt_change_service_20211201_models.StatusScenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.status_scence_with_options_async(request, headers, runtime)

    def status_scence_with_options(
        self,
        request: qt_change_service_20211201_models.StatusScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.StatusScenceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StatusScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.StatusScenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def status_scence_with_options_async(
        self,
        request: qt_change_service_20211201_models.StatusScenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qt_change_service_20211201_models.StatusScenceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StatusScence',
            version='2021-12-01',
            protocol='HTTPS',
            pathname=f'/scenario/service/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qt_change_service_20211201_models.StatusScenceResponse(),
            await self.call_api_async(params, req, runtime)
        )
