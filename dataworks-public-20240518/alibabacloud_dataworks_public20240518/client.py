# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from alibabacloud_tea_openapi import exceptions as open_api_exceptions
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore
from darabonba.core import DaraCore as DaraCore
from darabonba.exceptions import UnretryableException
from darabonba.policy.retry import RetryPolicyContext
from darabonba.request import DaraRequest
from darabonba.runtime import RuntimeOptions
from darabonba.utils.form import FileField
from darabonba.utils.form import Form as DaraForm
from darabonba.utils.stream import Stream as DaraStream
from darabonba.utils.xml import XML as DaraXML

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'dataworks.ap-northeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'dataworks.aliyuncs.com',
            'ap-south-1': 'dataworks.aliyuncs.com',
            'ap-southeast-1': 'dataworks.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dataworks.aliyuncs.com',
            'ap-southeast-3': 'dataworks.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dataworks.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dataworks.cn-beijing.aliyuncs.com',
            'cn-beijing-finance-1': 'dataworks.cn-beijing-finance-1.aliyuncs.com',
            'cn-beijing-finance-pop': 'dataworks.aliyuncs.com',
            'cn-beijing-gov-1': 'dataworks.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dataworks.aliyuncs.com',
            'cn-chengdu': 'dataworks.cn-chengdu.aliyuncs.com',
            'cn-edge-1': 'dataworks.aliyuncs.com',
            'cn-fujian': 'dataworks.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dataworks.aliyuncs.com',
            'cn-hangzhou': 'dataworks.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dataworks.aliyuncs.com',
            'cn-hangzhou-finance': 'dataworks.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dataworks.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dataworks.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dataworks.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dataworks.aliyuncs.com',
            'cn-hangzhou-test-306': 'dataworks.aliyuncs.com',
            'cn-hongkong': 'dataworks.cn-hongkong.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dataworks.aliyuncs.com',
            'cn-huhehaote': 'dataworks.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dataworks.aliyuncs.com',
            'cn-north-2-gov-1': 'dataworks.cn-north-2-gov-1.aliyuncs.com',
            'cn-qingdao': 'dataworks.aliyuncs.com',
            'cn-qingdao-nebula': 'dataworks.aliyuncs.com',
            'cn-shanghai': 'dataworks.cn-shanghai.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dataworks.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dataworks.aliyuncs.com',
            'cn-shanghai-finance-1': 'dataworks.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai-inner': 'dataworks.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dataworks.aliyuncs.com',
            'cn-shenzhen': 'dataworks.cn-shenzhen.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dataworks.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen-inner': 'dataworks.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dataworks.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dataworks.aliyuncs.com',
            'cn-wuhan': 'dataworks.aliyuncs.com',
            'cn-wulanchabu': 'dataworks.cn-wulanchabu.aliyuncs.com',
            'cn-yushanfang': 'dataworks.aliyuncs.com',
            'cn-zhangbei': 'dataworks.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dataworks.aliyuncs.com',
            'cn-zhangjiakou': 'dataworks.cn-zhangjiakou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dataworks.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dataworks.aliyuncs.com',
            'eu-central-1': 'dataworks.eu-central-1.aliyuncs.com',
            'eu-west-1': 'dataworks.eu-west-1.aliyuncs.com',
            'eu-west-1-oxs': 'dataworks.aliyuncs.com',
            'me-east-1': 'dataworks.me-east-1.aliyuncs.com',
            'rus-west-1-pop': 'dataworks.aliyuncs.com',
            'us-east-1': 'dataworks.us-east-1.aliyuncs.com',
            'us-west-1': 'dataworks.us-west-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dataworks-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = DaraCore.do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = DaraStream.read_as_string(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = await DaraCore.async_do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = await DaraStream.read_as_string_async(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abolish_pipeline_run_with_options(
        self,
        request: main_models.AbolishPipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbolishPipelineRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AbolishPipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbolishPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_pipeline_run_with_options_async(
        self,
        request: main_models.AbolishPipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbolishPipelineRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AbolishPipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbolishPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_pipeline_run(
        self,
        request: main_models.AbolishPipelineRunRequest,
    ) -> main_models.AbolishPipelineRunResponse:
        runtime = RuntimeOptions()
        return self.abolish_pipeline_run_with_options(request, runtime)

    async def abolish_pipeline_run_async(
        self,
        request: main_models.AbolishPipelineRunRequest,
    ) -> main_models.AbolishPipelineRunResponse:
        runtime = RuntimeOptions()
        return await self.abolish_pipeline_run_with_options_async(request, runtime)

    def add_entity_into_meta_collection_with_options(
        self,
        request: main_models.AddEntityIntoMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEntityIntoMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.meta_collection_id):
            query['MetaCollectionId'] = request.meta_collection_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntityIntoMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEntityIntoMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_entity_into_meta_collection_with_options_async(
        self,
        request: main_models.AddEntityIntoMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEntityIntoMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.meta_collection_id):
            query['MetaCollectionId'] = request.meta_collection_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntityIntoMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEntityIntoMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_entity_into_meta_collection(
        self,
        request: main_models.AddEntityIntoMetaCollectionRequest,
    ) -> main_models.AddEntityIntoMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.add_entity_into_meta_collection_with_options(request, runtime)

    async def add_entity_into_meta_collection_async(
        self,
        request: main_models.AddEntityIntoMetaCollectionRequest,
    ) -> main_models.AddEntityIntoMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.add_entity_into_meta_collection_with_options_async(request, runtime)

    def associate_project_to_resource_group_with_options(
        self,
        request: main_models.AssociateProjectToResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateProjectToResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateProjectToResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateProjectToResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_project_to_resource_group_with_options_async(
        self,
        request: main_models.AssociateProjectToResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateProjectToResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateProjectToResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateProjectToResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_project_to_resource_group(
        self,
        request: main_models.AssociateProjectToResourceGroupRequest,
    ) -> main_models.AssociateProjectToResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.associate_project_to_resource_group_with_options(request, runtime)

    async def associate_project_to_resource_group_async(
        self,
        request: main_models.AssociateProjectToResourceGroupRequest,
    ) -> main_models.AssociateProjectToResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.associate_project_to_resource_group_with_options_async(request, runtime)

    def attach_data_quality_rules_to_evaluation_task_with_options(
        self,
        tmp_req: main_models.AttachDataQualityRulesToEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDataQualityRulesToEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.AttachDataQualityRulesToEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rule_ids):
            request.data_quality_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rule_ids, 'DataQualityRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.data_quality_rule_ids_shrink):
            body['DataQualityRuleIds'] = request.data_quality_rule_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachDataQualityRulesToEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDataQualityRulesToEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_data_quality_rules_to_evaluation_task_with_options_async(
        self,
        tmp_req: main_models.AttachDataQualityRulesToEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDataQualityRulesToEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.AttachDataQualityRulesToEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rule_ids):
            request.data_quality_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rule_ids, 'DataQualityRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.data_quality_rule_ids_shrink):
            body['DataQualityRuleIds'] = request.data_quality_rule_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachDataQualityRulesToEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDataQualityRulesToEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_data_quality_rules_to_evaluation_task(
        self,
        request: main_models.AttachDataQualityRulesToEvaluationTaskRequest,
    ) -> main_models.AttachDataQualityRulesToEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.attach_data_quality_rules_to_evaluation_task_with_options(request, runtime)

    async def attach_data_quality_rules_to_evaluation_task_async(
        self,
        request: main_models.AttachDataQualityRulesToEvaluationTaskRequest,
    ) -> main_models.AttachDataQualityRulesToEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.attach_data_quality_rules_to_evaluation_task_with_options_async(request, runtime)

    def batch_update_tasks_with_options(
        self,
        tmp_req: main_models.BatchUpdateTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateTasksResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_tasks_with_options_async(
        self,
        tmp_req: main_models.BatchUpdateTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateTasksResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_tasks(
        self,
        request: main_models.BatchUpdateTasksRequest,
    ) -> main_models.BatchUpdateTasksResponse:
        runtime = RuntimeOptions()
        return self.batch_update_tasks_with_options(request, runtime)

    async def batch_update_tasks_async(
        self,
        request: main_models.BatchUpdateTasksRequest,
    ) -> main_models.BatchUpdateTasksResponse:
        runtime = RuntimeOptions()
        return await self.batch_update_tasks_with_options_async(request, runtime)

    def clone_data_source_with_options(
        self,
        request: main_models.CloneDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clone_data_source_name):
            query['CloneDataSourceName'] = request.clone_data_source_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_data_source_with_options_async(
        self,
        request: main_models.CloneDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clone_data_source_name):
            query['CloneDataSourceName'] = request.clone_data_source_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_data_source(
        self,
        request: main_models.CloneDataSourceRequest,
    ) -> main_models.CloneDataSourceResponse:
        runtime = RuntimeOptions()
        return self.clone_data_source_with_options(request, runtime)

    async def clone_data_source_async(
        self,
        request: main_models.CloneDataSourceRequest,
    ) -> main_models.CloneDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.clone_data_source_with_options_async(request, runtime)

    def create_alert_rule_with_options(
        self,
        tmp_req: main_models.CreateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertRuleResponse:
        tmp_req.validate()
        request = main_models.CreateAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.trigger_condition):
            request.trigger_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_rule_with_options_async(
        self,
        tmp_req: main_models.CreateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertRuleResponse:
        tmp_req.validate()
        request = main_models.CreateAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.trigger_condition):
            request.trigger_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_rule(
        self,
        request: main_models.CreateAlertRuleRequest,
    ) -> main_models.CreateAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.create_alert_rule_with_options(request, runtime)

    async def create_alert_rule_async(
        self,
        request: main_models.CreateAlertRuleRequest,
    ) -> main_models.CreateAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_alert_rule_with_options_async(request, runtime)

    def create_business_with_options(
        self,
        request: main_models.CreateBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_business_with_options_async(
        self,
        request: main_models.CreateBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_business(
        self,
        request: main_models.CreateBusinessRequest,
    ) -> main_models.CreateBusinessResponse:
        runtime = RuntimeOptions()
        return self.create_business_with_options(request, runtime)

    async def create_business_async(
        self,
        request: main_models.CreateBusinessRequest,
    ) -> main_models.CreateBusinessResponse:
        runtime = RuntimeOptions()
        return await self.create_business_with_options_async(request, runtime)

    def create_component_with_options(
        self,
        request: main_models.CreateComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_with_options_async(
        self,
        request: main_models.CreateComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component(
        self,
        request: main_models.CreateComponentRequest,
    ) -> main_models.CreateComponentResponse:
        runtime = RuntimeOptions()
        return self.create_component_with_options(request, runtime)

    async def create_component_async(
        self,
        request: main_models.CreateComponentRequest,
    ) -> main_models.CreateComponentResponse:
        runtime = RuntimeOptions()
        return await self.create_component_with_options_async(request, runtime)

    def create_compute_resource_with_options(
        self,
        request: main_models.CreateComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_resource_with_options_async(
        self,
        request: main_models.CreateComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_resource(
        self,
        request: main_models.CreateComputeResourceRequest,
    ) -> main_models.CreateComputeResourceResponse:
        runtime = RuntimeOptions()
        return self.create_compute_resource_with_options(request, runtime)

    async def create_compute_resource_async(
        self,
        request: main_models.CreateComputeResourceRequest,
    ) -> main_models.CreateComputeResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_compute_resource_with_options_async(request, runtime)

    def create_dialarm_rule_with_options(
        self,
        tmp_req: main_models.CreateDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDIAlarmRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDIAlarmRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_settings):
            request.notification_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not DaraCore.is_null(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialarm_rule_with_options_async(
        self,
        tmp_req: main_models.CreateDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDIAlarmRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDIAlarmRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_settings):
            request.notification_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not DaraCore.is_null(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialarm_rule(
        self,
        request: main_models.CreateDIAlarmRuleRequest,
    ) -> main_models.CreateDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return self.create_dialarm_rule_with_options(request, runtime)

    async def create_dialarm_rule_async(
        self,
        request: main_models.CreateDIAlarmRuleRequest,
    ) -> main_models.CreateDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_dialarm_rule_with_options_async(request, runtime)

    def create_dijob_with_options(
        self,
        tmp_req: main_models.CreateDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDIJobResponse:
        tmp_req.validate()
        request = main_models.CreateDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.destination_data_source_settings):
            request.destination_data_source_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.destination_data_source_settings, 'DestinationDataSourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.job_settings):
            request.job_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not DaraCore.is_null(tmp_req.resource_settings):
            request.resource_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.source_data_source_settings):
            request.source_data_source_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_data_source_settings, 'SourceDataSourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.table_mappings):
            request.table_mappings_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not DaraCore.is_null(tmp_req.transformation_rules):
            request.transformation_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = {}
        if not DaraCore.is_null(request.destination_data_source_type):
            query['DestinationDataSourceType'] = request.destination_data_source_type
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.migration_type):
            query['MigrationType'] = request.migration_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.source_data_source_type):
            query['SourceDataSourceType'] = request.source_data_source_type
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.destination_data_source_settings_shrink):
            body['DestinationDataSourceSettings'] = request.destination_data_source_settings_shrink
        if not DaraCore.is_null(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not DaraCore.is_null(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not DaraCore.is_null(request.source_data_source_settings_shrink):
            body['SourceDataSourceSettings'] = request.source_data_source_settings_shrink
        if not DaraCore.is_null(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not DaraCore.is_null(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dijob_with_options_async(
        self,
        tmp_req: main_models.CreateDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDIJobResponse:
        tmp_req.validate()
        request = main_models.CreateDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.destination_data_source_settings):
            request.destination_data_source_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.destination_data_source_settings, 'DestinationDataSourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.job_settings):
            request.job_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not DaraCore.is_null(tmp_req.resource_settings):
            request.resource_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.source_data_source_settings):
            request.source_data_source_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_data_source_settings, 'SourceDataSourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.table_mappings):
            request.table_mappings_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not DaraCore.is_null(tmp_req.transformation_rules):
            request.transformation_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = {}
        if not DaraCore.is_null(request.destination_data_source_type):
            query['DestinationDataSourceType'] = request.destination_data_source_type
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.migration_type):
            query['MigrationType'] = request.migration_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.source_data_source_type):
            query['SourceDataSourceType'] = request.source_data_source_type
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.destination_data_source_settings_shrink):
            body['DestinationDataSourceSettings'] = request.destination_data_source_settings_shrink
        if not DaraCore.is_null(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not DaraCore.is_null(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not DaraCore.is_null(request.source_data_source_settings_shrink):
            body['SourceDataSourceSettings'] = request.source_data_source_settings_shrink
        if not DaraCore.is_null(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not DaraCore.is_null(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dijob(
        self,
        request: main_models.CreateDIJobRequest,
    ) -> main_models.CreateDIJobResponse:
        runtime = RuntimeOptions()
        return self.create_dijob_with_options(request, runtime)

    async def create_dijob_async(
        self,
        request: main_models.CreateDIJobRequest,
    ) -> main_models.CreateDIJobResponse:
        runtime = RuntimeOptions()
        return await self.create_dijob_with_options_async(request, runtime)

    def create_data_asset_tag_with_options(
        self,
        tmp_req: main_models.CreateDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.CreateDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.managers):
            request.managers_shrink = Utils.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.managers_shrink):
            query['Managers'] = request.managers_shrink
        if not DaraCore.is_null(request.value_type):
            query['ValueType'] = request.value_type
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAssetTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_asset_tag_with_options_async(
        self,
        tmp_req: main_models.CreateDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.CreateDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.managers):
            request.managers_shrink = Utils.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.managers_shrink):
            query['Managers'] = request.managers_shrink
        if not DaraCore.is_null(request.value_type):
            query['ValueType'] = request.value_type
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAssetTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_asset_tag(
        self,
        request: main_models.CreateDataAssetTagRequest,
    ) -> main_models.CreateDataAssetTagResponse:
        runtime = RuntimeOptions()
        return self.create_data_asset_tag_with_options(request, runtime)

    async def create_data_asset_tag_async(
        self,
        request: main_models.CreateDataAssetTagRequest,
    ) -> main_models.CreateDataAssetTagResponse:
        runtime = RuntimeOptions()
        return await self.create_data_asset_tag_with_options_async(request, runtime)

    def create_data_quality_alert_rule_with_options(
        self,
        tmp_req: main_models.CreateDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityAlertRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.condition):
            body['Condition'] = request.condition
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_alert_rule_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityAlertRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.condition):
            body['Condition'] = request.condition
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_alert_rule(
        self,
        request: main_models.CreateDataQualityAlertRuleRequest,
    ) -> main_models.CreateDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_alert_rule_with_options(request, runtime)

    async def create_data_quality_alert_rule_async(
        self,
        request: main_models.CreateDataQualityAlertRuleRequest,
    ) -> main_models.CreateDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_alert_rule_with_options_async(request, runtime)

    def create_data_quality_evaluation_task_with_options(
        self,
        tmp_req: main_models.CreateDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rules):
            request.data_quality_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rules, 'DataQualityRules', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.notifications):
            request.notifications_shrink = Utils.array_to_string_with_specified_style(tmp_req.notifications, 'Notifications', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_rules_shrink):
            body['DataQualityRules'] = request.data_quality_rules_shrink
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notifications_shrink):
            body['Notifications'] = request.notifications_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_conf):
            body['RuntimeConf'] = request.runtime_conf
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_evaluation_task_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rules):
            request.data_quality_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rules, 'DataQualityRules', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.notifications):
            request.notifications_shrink = Utils.array_to_string_with_specified_style(tmp_req.notifications, 'Notifications', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_rules_shrink):
            body['DataQualityRules'] = request.data_quality_rules_shrink
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notifications_shrink):
            body['Notifications'] = request.notifications_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_conf):
            body['RuntimeConf'] = request.runtime_conf
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_evaluation_task(
        self,
        request: main_models.CreateDataQualityEvaluationTaskRequest,
    ) -> main_models.CreateDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_evaluation_task_with_options(request, runtime)

    async def create_data_quality_evaluation_task_async(
        self,
        request: main_models.CreateDataQualityEvaluationTaskRequest,
    ) -> main_models.CreateDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_evaluation_task_with_options_async(request, runtime)

    def create_data_quality_evaluation_task_instance_with_options(
        self,
        tmp_req: main_models.CreateDataQualityEvaluationTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityEvaluationTaskInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityEvaluationTaskInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityEvaluationTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityEvaluationTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_evaluation_task_instance_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityEvaluationTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityEvaluationTaskInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityEvaluationTaskInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityEvaluationTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityEvaluationTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_evaluation_task_instance(
        self,
        request: main_models.CreateDataQualityEvaluationTaskInstanceRequest,
    ) -> main_models.CreateDataQualityEvaluationTaskInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_evaluation_task_instance_with_options(request, runtime)

    async def create_data_quality_evaluation_task_instance_async(
        self,
        request: main_models.CreateDataQualityEvaluationTaskInstanceRequest,
    ) -> main_models.CreateDataQualityEvaluationTaskInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_evaluation_task_instance_with_options_async(request, runtime)

    def create_data_quality_rule_with_options(
        self,
        tmp_req: main_models.CreateDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.error_handlers):
            request.error_handlers_shrink = Utils.array_to_string_with_specified_style(tmp_req.error_handlers, 'ErrorHandlers', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.error_handlers_shrink):
            body['ErrorHandlers'] = request.error_handlers_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_rule_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.error_handlers):
            request.error_handlers_shrink = Utils.array_to_string_with_specified_style(tmp_req.error_handlers, 'ErrorHandlers', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.error_handlers_shrink):
            body['ErrorHandlers'] = request.error_handlers_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_rule(
        self,
        request: main_models.CreateDataQualityRuleRequest,
    ) -> main_models.CreateDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_rule_with_options(request, runtime)

    async def create_data_quality_rule_async(
        self,
        request: main_models.CreateDataQualityRuleRequest,
    ) -> main_models.CreateDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_rule_with_options_async(request, runtime)

    def create_data_quality_rule_template_with_options(
        self,
        tmp_req: main_models.CreateDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityRuleTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityRuleTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.directory_path):
            body['DirectoryPath'] = request.directory_path
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.visible_scope):
            body['VisibleScope'] = request.visible_scope
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_rule_template_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityRuleTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityRuleTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.directory_path):
            body['DirectoryPath'] = request.directory_path
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.visible_scope):
            body['VisibleScope'] = request.visible_scope
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_rule_template(
        self,
        request: main_models.CreateDataQualityRuleTemplateRequest,
    ) -> main_models.CreateDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_rule_template_with_options(request, runtime)

    async def create_data_quality_rule_template_async(
        self,
        request: main_models.CreateDataQualityRuleTemplateRequest,
    ) -> main_models.CreateDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_rule_template_with_options_async(request, runtime)

    def create_data_quality_scan_with_options(
        self,
        tmp_req: main_models.CreateDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityScanResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityScanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_resource):
            request.compute_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_resource, 'ComputeResource', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compute_resource_shrink):
            body['ComputeResource'] = request.compute_resource_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_scan_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityScanResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityScanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_resource):
            request.compute_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_resource, 'ComputeResource', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compute_resource_shrink):
            body['ComputeResource'] = request.compute_resource_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_scan(
        self,
        request: main_models.CreateDataQualityScanRequest,
    ) -> main_models.CreateDataQualityScanResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_scan_with_options(request, runtime)

    async def create_data_quality_scan_async(
        self,
        request: main_models.CreateDataQualityScanRequest,
    ) -> main_models.CreateDataQualityScanResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_scan_with_options_async(request, runtime)

    def create_data_quality_scan_run_with_options(
        self,
        tmp_req: main_models.CreateDataQualityScanRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityScanRunResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityScanRunShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_scan_id):
            body['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityScanRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityScanRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_scan_run_with_options_async(
        self,
        tmp_req: main_models.CreateDataQualityScanRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityScanRunResponse:
        tmp_req.validate()
        request = main_models.CreateDataQualityScanRunShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_scan_id):
            body['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityScanRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityScanRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_scan_run(
        self,
        request: main_models.CreateDataQualityScanRunRequest,
    ) -> main_models.CreateDataQualityScanRunResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_scan_run_with_options(request, runtime)

    async def create_data_quality_scan_run_async(
        self,
        request: main_models.CreateDataQualityScanRunRequest,
    ) -> main_models.CreateDataQualityScanRunResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_scan_run_with_options_async(request, runtime)

    def create_data_quality_template_with_options(
        self,
        request: main_models.CreateDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_quality_template_with_options_async(
        self,
        request: main_models.CreateDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataQualityTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_quality_template(
        self,
        request: main_models.CreateDataQualityTemplateRequest,
    ) -> main_models.CreateDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_data_quality_template_with_options(request, runtime)

    async def create_data_quality_template_async(
        self,
        request: main_models.CreateDataQualityTemplateRequest,
    ) -> main_models.CreateDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_data_quality_template_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_data_source_shared_rule_with_options(
        self,
        request: main_models.CreateDataSourceSharedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceSharedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.shared_user):
            query['SharedUser'] = request.shared_user
        if not DaraCore.is_null(request.target_project_id):
            query['TargetProjectId'] = request.target_project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSourceSharedRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceSharedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_shared_rule_with_options_async(
        self,
        request: main_models.CreateDataSourceSharedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceSharedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.shared_user):
            query['SharedUser'] = request.shared_user
        if not DaraCore.is_null(request.target_project_id):
            query['TargetProjectId'] = request.target_project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSourceSharedRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceSharedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source_shared_rule(
        self,
        request: main_models.CreateDataSourceSharedRuleRequest,
    ) -> main_models.CreateDataSourceSharedRuleResponse:
        runtime = RuntimeOptions()
        return self.create_data_source_shared_rule_with_options(request, runtime)

    async def create_data_source_shared_rule_async(
        self,
        request: main_models.CreateDataSourceSharedRuleRequest,
    ) -> main_models.CreateDataSourceSharedRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_data_source_shared_rule_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_version):
            request.init_version_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_version, 'InitVersion', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.init_version_shrink):
            body['InitVersion'] = request.init_version_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_version):
            request.init_version_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_version, 'InitVersion', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.init_version_shrink):
            body['InitVersion'] = request.init_version_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_dataset_version_with_options(
        self,
        tmp_req: main_models.CreateDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.import_info):
            request.import_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.import_info, 'ImportInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.import_info_shrink):
            body['ImportInfo'] = request.import_info_shrink
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_version_with_options_async(
        self,
        tmp_req: main_models.CreateDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.import_info):
            request.import_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.import_info, 'ImportInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.import_info_shrink):
            body['ImportInfo'] = request.import_info_shrink
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_version(
        self,
        request: main_models.CreateDatasetVersionRequest,
    ) -> main_models.CreateDatasetVersionResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_version_with_options(request, runtime)

    async def create_dataset_version_async(
        self,
        request: main_models.CreateDatasetVersionRequest,
    ) -> main_models.CreateDatasetVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_version_with_options_async(request, runtime)

    def create_file_with_options(
        self,
        request: main_models.CreateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not DaraCore.is_null(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
        if not DaraCore.is_null(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not DaraCore.is_null(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not DaraCore.is_null(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
        if not DaraCore.is_null(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not DaraCore.is_null(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not DaraCore.is_null(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not DaraCore.is_null(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.input_list):
            body['InputList'] = request.input_list
        if not DaraCore.is_null(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not DaraCore.is_null(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.para_value):
            body['ParaValue'] = request.para_value
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not DaraCore.is_null(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not DaraCore.is_null(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not DaraCore.is_null(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.stop):
            body['Stop'] = request.stop
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: main_models.CreateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not DaraCore.is_null(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
        if not DaraCore.is_null(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not DaraCore.is_null(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not DaraCore.is_null(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
        if not DaraCore.is_null(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not DaraCore.is_null(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not DaraCore.is_null(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not DaraCore.is_null(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.input_list):
            body['InputList'] = request.input_list
        if not DaraCore.is_null(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not DaraCore.is_null(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.para_value):
            body['ParaValue'] = request.para_value
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not DaraCore.is_null(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not DaraCore.is_null(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not DaraCore.is_null(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.stop):
            body['Stop'] = request.stop
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    async def create_file_async(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        return await self.create_file_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: main_models.CreateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: main_models.CreateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_function_with_options(
        self,
        request: main_models.CreateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: main_models.CreateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: main_models.CreateFunctionRequest,
    ) -> main_models.CreateFunctionResponse:
        runtime = RuntimeOptions()
        return self.create_function_with_options(request, runtime)

    async def create_function_async(
        self,
        request: main_models.CreateFunctionRequest,
    ) -> main_models.CreateFunctionResponse:
        runtime = RuntimeOptions()
        return await self.create_function_with_options_async(request, runtime)

    def create_identify_credential_with_options(
        self,
        tmp_req: main_models.CreateIdentifyCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentifyCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateIdentifyCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.identify_credential):
            request.identify_credential_shrink = Utils.array_to_string_with_specified_style(tmp_req.identify_credential, 'IdentifyCredential', 'json')
        body = {}
        if not DaraCore.is_null(request.identify_credential_shrink):
            body['IdentifyCredential'] = request.identify_credential_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentifyCredential',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentifyCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identify_credential_with_options_async(
        self,
        tmp_req: main_models.CreateIdentifyCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentifyCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateIdentifyCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.identify_credential):
            request.identify_credential_shrink = Utils.array_to_string_with_specified_style(tmp_req.identify_credential, 'IdentifyCredential', 'json')
        body = {}
        if not DaraCore.is_null(request.identify_credential_shrink):
            body['IdentifyCredential'] = request.identify_credential_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentifyCredential',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentifyCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identify_credential(
        self,
        request: main_models.CreateIdentifyCredentialRequest,
    ) -> main_models.CreateIdentifyCredentialResponse:
        runtime = RuntimeOptions()
        return self.create_identify_credential_with_options(request, runtime)

    async def create_identify_credential_async(
        self,
        request: main_models.CreateIdentifyCredentialRequest,
    ) -> main_models.CreateIdentifyCredentialResponse:
        runtime = RuntimeOptions()
        return await self.create_identify_credential_with_options_async(request, runtime)

    def create_lineage_relationship_with_options(
        self,
        tmp_req: main_models.CreateLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLineageRelationshipResponse:
        tmp_req.validate()
        request = main_models.CreateLineageRelationshipShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dst_entity):
            request.dst_entity_shrink = Utils.array_to_string_with_specified_style(tmp_req.dst_entity, 'DstEntity', 'json')
        if not DaraCore.is_null(tmp_req.src_entity):
            request.src_entity_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_entity, 'SrcEntity', 'json')
        if not DaraCore.is_null(tmp_req.task):
            request.task_shrink = Utils.array_to_string_with_specified_style(tmp_req.task, 'Task', 'json')
        query = {}
        if not DaraCore.is_null(request.dst_entity_shrink):
            query['DstEntity'] = request.dst_entity_shrink
        if not DaraCore.is_null(request.src_entity_shrink):
            query['SrcEntity'] = request.src_entity_shrink
        if not DaraCore.is_null(request.task_shrink):
            query['Task'] = request.task_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLineageRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lineage_relationship_with_options_async(
        self,
        tmp_req: main_models.CreateLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLineageRelationshipResponse:
        tmp_req.validate()
        request = main_models.CreateLineageRelationshipShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dst_entity):
            request.dst_entity_shrink = Utils.array_to_string_with_specified_style(tmp_req.dst_entity, 'DstEntity', 'json')
        if not DaraCore.is_null(tmp_req.src_entity):
            request.src_entity_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_entity, 'SrcEntity', 'json')
        if not DaraCore.is_null(tmp_req.task):
            request.task_shrink = Utils.array_to_string_with_specified_style(tmp_req.task, 'Task', 'json')
        query = {}
        if not DaraCore.is_null(request.dst_entity_shrink):
            query['DstEntity'] = request.dst_entity_shrink
        if not DaraCore.is_null(request.src_entity_shrink):
            query['SrcEntity'] = request.src_entity_shrink
        if not DaraCore.is_null(request.task_shrink):
            query['Task'] = request.task_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLineageRelationshipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lineage_relationship(
        self,
        request: main_models.CreateLineageRelationshipRequest,
    ) -> main_models.CreateLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return self.create_lineage_relationship_with_options(request, runtime)

    async def create_lineage_relationship_async(
        self,
        request: main_models.CreateLineageRelationshipRequest,
    ) -> main_models.CreateLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return await self.create_lineage_relationship_with_options_async(request, runtime)

    def create_meta_collection_with_options(
        self,
        request: main_models.CreateMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meta_collection_with_options_async(
        self,
        request: main_models.CreateMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_meta_collection(
        self,
        request: main_models.CreateMetaCollectionRequest,
    ) -> main_models.CreateMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.create_meta_collection_with_options(request, runtime)

    async def create_meta_collection_async(
        self,
        request: main_models.CreateMetaCollectionRequest,
    ) -> main_models.CreateMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.create_meta_collection_with_options_async(request, runtime)

    def create_network_with_options(
        self,
        request: main_models.CreateNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_with_options_async(
        self,
        request: main_models.CreateNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network(
        self,
        request: main_models.CreateNetworkRequest,
    ) -> main_models.CreateNetworkResponse:
        runtime = RuntimeOptions()
        return self.create_network_with_options(request, runtime)

    async def create_network_async(
        self,
        request: main_models.CreateNetworkRequest,
    ) -> main_models.CreateNetworkResponse:
        runtime = RuntimeOptions()
        return await self.create_network_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: main_models.CreateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.container_id):
            body['ContainerId'] = request.container_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: main_models.CreateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.container_id):
            body['ContainerId'] = request.container_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node(
        self,
        request: main_models.CreateNodeRequest,
    ) -> main_models.CreateNodeResponse:
        runtime = RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: main_models.CreateNodeRequest,
    ) -> main_models.CreateNodeResponse:
        runtime = RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_pipeline_run_with_options(
        self,
        tmp_req: main_models.CreatePipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineRunResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineRunShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_run_with_options_async(
        self,
        tmp_req: main_models.CreatePipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineRunResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineRunShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_run(
        self,
        request: main_models.CreatePipelineRunRequest,
    ) -> main_models.CreatePipelineRunResponse:
        runtime = RuntimeOptions()
        return self.create_pipeline_run_with_options(request, runtime)

    async def create_pipeline_run_async(
        self,
        request: main_models.CreatePipelineRunRequest,
    ) -> main_models.CreatePipelineRunResponse:
        runtime = RuntimeOptions()
        return await self.create_pipeline_run_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: main_models.CreateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        tmp_req.validate()
        request = main_models.CreateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: main_models.CreateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        tmp_req.validate()
        request = main_models.CreateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_member_with_options(
        self,
        tmp_req: main_models.CreateProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectMemberResponse:
        tmp_req.validate()
        request = main_models.CreateProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_member_with_options_async(
        self,
        tmp_req: main_models.CreateProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectMemberResponse:
        tmp_req.validate()
        request = main_models.CreateProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project_member(
        self,
        request: main_models.CreateProjectMemberRequest,
    ) -> main_models.CreateProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    async def create_project_member_async(
        self,
        request: main_models.CreateProjectMemberRequest,
    ) -> main_models.CreateProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.create_project_member_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        request: main_models.CreateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: main_models.CreateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def create_resource_advance(
        self,
        request: main_models.CreateResourceAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        create_resource_req = main_models.CreateResourceRequest()
        Utils.convert(request, create_resource_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            create_resource_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_resource_resp = self.create_resource_with_options(create_resource_req, runtime)
        return create_resource_resp

    async def create_resource_advance_async(
        self,
        request: main_models.CreateResourceAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        create_resource_req = main_models.CreateResourceRequest()
        Utils.convert(request, create_resource_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            create_resource_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_resource_resp = await self.create_resource_with_options_async(create_resource_req, runtime)
        return create_resource_resp

    def create_resource_file_with_options(
        self,
        request: main_models.CreateResourceFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.origin_resource_name):
            body['OriginResourceName'] = request.origin_resource_name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.register_to_calc_engine):
            body['RegisterToCalcEngine'] = request.register_to_calc_engine
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.storage_url):
            body['StorageURL'] = request.storage_url
        if not DaraCore.is_null(request.upload_mode):
            body['UploadMode'] = request.upload_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_file_with_options_async(
        self,
        request: main_models.CreateResourceFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.origin_resource_name):
            body['OriginResourceName'] = request.origin_resource_name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.register_to_calc_engine):
            body['RegisterToCalcEngine'] = request.register_to_calc_engine
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.storage_url):
            body['StorageURL'] = request.storage_url
        if not DaraCore.is_null(request.upload_mode):
            body['UploadMode'] = request.upload_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_file(
        self,
        request: main_models.CreateResourceFileRequest,
    ) -> main_models.CreateResourceFileResponse:
        runtime = RuntimeOptions()
        return self.create_resource_file_with_options(request, runtime)

    async def create_resource_file_async(
        self,
        request: main_models.CreateResourceFileRequest,
    ) -> main_models.CreateResourceFileResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_file_with_options_async(request, runtime)

    def create_resource_file_advance(
        self,
        request: main_models.CreateResourceFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        create_resource_file_req = main_models.CreateResourceFileRequest()
        Utils.convert(request, create_resource_file_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            create_resource_file_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_resource_file_resp = self.create_resource_file_with_options(create_resource_file_req, runtime)
        return create_resource_file_resp

    async def create_resource_file_advance_async(
        self,
        request: main_models.CreateResourceFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        create_resource_file_req = main_models.CreateResourceFileRequest()
        Utils.convert(request, create_resource_file_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            create_resource_file_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_resource_file_resp = await self.create_resource_file_with_options_async(create_resource_file_req, runtime)
        return create_resource_file_resp

    def create_resource_group_with_options(
        self,
        tmp_req: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.auto_renew_enabled):
            body['AutoRenewEnabled'] = request.auto_renew_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        tmp_req: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.auto_renew_enabled):
            body['AutoRenewEnabled'] = request.auto_renew_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_route_with_options(
        self,
        request: main_models.CreateRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.network_id):
            body['NetworkId'] = request.network_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_route_with_options_async(
        self,
        request: main_models.CreateRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.network_id):
            body['NetworkId'] = request.network_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_route(
        self,
        request: main_models.CreateRouteRequest,
    ) -> main_models.CreateRouteResponse:
        runtime = RuntimeOptions()
        return self.create_route_with_options(request, runtime)

    async def create_route_async(
        self,
        request: main_models.CreateRouteRequest,
    ) -> main_models.CreateRouteResponse:
        runtime = RuntimeOptions()
        return await self.create_route_with_options_async(request, runtime)

    def create_udf_file_with_options(
        self,
        request: main_models.CreateUdfFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not DaraCore.is_null(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
        if not DaraCore.is_null(request.example):
            body['Example'] = request.example
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.function_type):
            body['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.return_value):
            body['ReturnValue'] = request.return_value
        if not DaraCore.is_null(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdfFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_udf_file_with_options_async(
        self,
        request: main_models.CreateUdfFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not DaraCore.is_null(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
        if not DaraCore.is_null(request.example):
            body['Example'] = request.example
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.function_type):
            body['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.return_value):
            body['ReturnValue'] = request.return_value
        if not DaraCore.is_null(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdfFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_udf_file(
        self,
        request: main_models.CreateUdfFileRequest,
    ) -> main_models.CreateUdfFileResponse:
        runtime = RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    async def create_udf_file_async(
        self,
        request: main_models.CreateUdfFileRequest,
    ) -> main_models.CreateUdfFileResponse:
        runtime = RuntimeOptions()
        return await self.create_udf_file_with_options_async(request, runtime)

    def create_workflow_definition_with_options(
        self,
        request: main_models.CreateWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_definition_with_options_async(
        self,
        request: main_models.CreateWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow_definition(
        self,
        request: main_models.CreateWorkflowDefinitionRequest,
    ) -> main_models.CreateWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.create_workflow_definition_with_options(request, runtime)

    async def create_workflow_definition_async(
        self,
        request: main_models.CreateWorkflowDefinitionRequest,
    ) -> main_models.CreateWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.create_workflow_definition_with_options_async(request, runtime)

    def create_workflow_instances_with_options(
        self,
        tmp_req: main_models.CreateWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.CreateWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_run_properties):
            request.default_run_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_run_properties, 'DefaultRunProperties', 'json')
        if not DaraCore.is_null(tmp_req.periods):
            request.periods_shrink = Utils.array_to_string_with_specified_style(tmp_req.periods, 'Periods', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.auto_start_enabled):
            body['AutoStartEnabled'] = request.auto_start_enabled
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.default_run_properties_shrink):
            body['DefaultRunProperties'] = request.default_run_properties_shrink
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.periods_shrink):
            body['Periods'] = request.periods_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tag_creation_policy):
            body['TagCreationPolicy'] = request.tag_creation_policy
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_parameters):
            body['TaskParameters'] = request.task_parameters
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_parameters):
            body['WorkflowParameters'] = request.workflow_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_instances_with_options_async(
        self,
        tmp_req: main_models.CreateWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.CreateWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_run_properties):
            request.default_run_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_run_properties, 'DefaultRunProperties', 'json')
        if not DaraCore.is_null(tmp_req.periods):
            request.periods_shrink = Utils.array_to_string_with_specified_style(tmp_req.periods, 'Periods', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.auto_start_enabled):
            body['AutoStartEnabled'] = request.auto_start_enabled
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.default_run_properties_shrink):
            body['DefaultRunProperties'] = request.default_run_properties_shrink
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.periods_shrink):
            body['Periods'] = request.periods_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tag_creation_policy):
            body['TagCreationPolicy'] = request.tag_creation_policy
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_parameters):
            body['TaskParameters'] = request.task_parameters
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_parameters):
            body['WorkflowParameters'] = request.workflow_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow_instances(
        self,
        request: main_models.CreateWorkflowInstancesRequest,
    ) -> main_models.CreateWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return self.create_workflow_instances_with_options(request, runtime)

    async def create_workflow_instances_async(
        self,
        request: main_models.CreateWorkflowInstancesRequest,
    ) -> main_models.CreateWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return await self.create_workflow_instances_with_options_async(request, runtime)

    def delete_alert_rule_with_options(
        self,
        request: main_models.DeleteAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rule_with_options_async(
        self,
        request: main_models.DeleteAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rule(
        self,
        request: main_models.DeleteAlertRuleRequest,
    ) -> main_models.DeleteAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_rule_with_options(request, runtime)

    async def delete_alert_rule_async(
        self,
        request: main_models.DeleteAlertRuleRequest,
    ) -> main_models.DeleteAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_rule_with_options_async(request, runtime)

    def delete_business_with_options(
        self,
        request: main_models.DeleteBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_business_with_options_async(
        self,
        request: main_models.DeleteBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_business(
        self,
        request: main_models.DeleteBusinessRequest,
    ) -> main_models.DeleteBusinessResponse:
        runtime = RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    async def delete_business_async(
        self,
        request: main_models.DeleteBusinessRequest,
    ) -> main_models.DeleteBusinessResponse:
        runtime = RuntimeOptions()
        return await self.delete_business_with_options_async(request, runtime)

    def delete_certificate_with_options(
        self,
        request: main_models.DeleteCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_certificate_with_options_async(
        self,
        request: main_models.DeleteCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_certificate(
        self,
        request: main_models.DeleteCertificateRequest,
    ) -> main_models.DeleteCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    async def delete_certificate_async(
        self,
        request: main_models.DeleteCertificateRequest,
    ) -> main_models.DeleteCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_certificate_with_options_async(request, runtime)

    def delete_component_with_options(
        self,
        request: main_models.DeleteComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_id):
            body['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_with_options_async(
        self,
        request: main_models.DeleteComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_id):
            body['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component(
        self,
        request: main_models.DeleteComponentRequest,
    ) -> main_models.DeleteComponentResponse:
        runtime = RuntimeOptions()
        return self.delete_component_with_options(request, runtime)

    async def delete_component_async(
        self,
        request: main_models.DeleteComponentRequest,
    ) -> main_models.DeleteComponentResponse:
        runtime = RuntimeOptions()
        return await self.delete_component_with_options_async(request, runtime)

    def delete_compute_resource_with_options(
        self,
        request: main_models.DeleteComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_resource_with_options_async(
        self,
        request: main_models.DeleteComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_resource(
        self,
        request: main_models.DeleteComputeResourceRequest,
    ) -> main_models.DeleteComputeResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_compute_resource_with_options(request, runtime)

    async def delete_compute_resource_async(
        self,
        request: main_models.DeleteComputeResourceRequest,
    ) -> main_models.DeleteComputeResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_compute_resource_with_options_async(request, runtime)

    def delete_dialarm_rule_with_options(
        self,
        request: main_models.DeleteDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDIAlarmRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dialarm_rule_with_options_async(
        self,
        request: main_models.DeleteDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDIAlarmRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dialarm_rule(
        self,
        request: main_models.DeleteDIAlarmRuleRequest,
    ) -> main_models.DeleteDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_dialarm_rule_with_options(request, runtime)

    async def delete_dialarm_rule_async(
        self,
        request: main_models.DeleteDIAlarmRuleRequest,
    ) -> main_models.DeleteDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_dialarm_rule_with_options_async(request, runtime)

    def delete_dijob_with_options(
        self,
        request: main_models.DeleteDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dijob_with_options_async(
        self,
        request: main_models.DeleteDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dijob(
        self,
        request: main_models.DeleteDIJobRequest,
    ) -> main_models.DeleteDIJobResponse:
        runtime = RuntimeOptions()
        return self.delete_dijob_with_options(request, runtime)

    async def delete_dijob_async(
        self,
        request: main_models.DeleteDIJobRequest,
    ) -> main_models.DeleteDIJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_dijob_with_options_async(request, runtime)

    def delete_data_asset_tag_with_options(
        self,
        tmp_req: main_models.DeleteDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.DeleteDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAssetTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_asset_tag_with_options_async(
        self,
        tmp_req: main_models.DeleteDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.DeleteDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAssetTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_asset_tag(
        self,
        request: main_models.DeleteDataAssetTagRequest,
    ) -> main_models.DeleteDataAssetTagResponse:
        runtime = RuntimeOptions()
        return self.delete_data_asset_tag_with_options(request, runtime)

    async def delete_data_asset_tag_async(
        self,
        request: main_models.DeleteDataAssetTagRequest,
    ) -> main_models.DeleteDataAssetTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_asset_tag_with_options_async(request, runtime)

    def delete_data_quality_alert_rule_with_options(
        self,
        request: main_models.DeleteDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_alert_rule_with_options_async(
        self,
        request: main_models.DeleteDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_alert_rule(
        self,
        request: main_models.DeleteDataQualityAlertRuleRequest,
    ) -> main_models.DeleteDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_alert_rule_with_options(request, runtime)

    async def delete_data_quality_alert_rule_async(
        self,
        request: main_models.DeleteDataQualityAlertRuleRequest,
    ) -> main_models.DeleteDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_alert_rule_with_options_async(request, runtime)

    def delete_data_quality_evaluation_task_with_options(
        self,
        request: main_models.DeleteDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_evaluation_task_with_options_async(
        self,
        request: main_models.DeleteDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_evaluation_task(
        self,
        request: main_models.DeleteDataQualityEvaluationTaskRequest,
    ) -> main_models.DeleteDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_evaluation_task_with_options(request, runtime)

    async def delete_data_quality_evaluation_task_async(
        self,
        request: main_models.DeleteDataQualityEvaluationTaskRequest,
    ) -> main_models.DeleteDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_evaluation_task_with_options_async(request, runtime)

    def delete_data_quality_rule_with_options(
        self,
        request: main_models.DeleteDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_rule_with_options_async(
        self,
        request: main_models.DeleteDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_rule(
        self,
        request: main_models.DeleteDataQualityRuleRequest,
    ) -> main_models.DeleteDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_rule_with_options(request, runtime)

    async def delete_data_quality_rule_async(
        self,
        request: main_models.DeleteDataQualityRuleRequest,
    ) -> main_models.DeleteDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_rule_with_options_async(request, runtime)

    def delete_data_quality_rule_template_with_options(
        self,
        request: main_models.DeleteDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_rule_template_with_options_async(
        self,
        request: main_models.DeleteDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_rule_template(
        self,
        request: main_models.DeleteDataQualityRuleTemplateRequest,
    ) -> main_models.DeleteDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_rule_template_with_options(request, runtime)

    async def delete_data_quality_rule_template_async(
        self,
        request: main_models.DeleteDataQualityRuleTemplateRequest,
    ) -> main_models.DeleteDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_rule_template_with_options_async(request, runtime)

    def delete_data_quality_scan_with_options(
        self,
        request: main_models.DeleteDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityScanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_scan_with_options_async(
        self,
        request: main_models.DeleteDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityScanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_scan(
        self,
        request: main_models.DeleteDataQualityScanRequest,
    ) -> main_models.DeleteDataQualityScanResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_scan_with_options(request, runtime)

    async def delete_data_quality_scan_async(
        self,
        request: main_models.DeleteDataQualityScanRequest,
    ) -> main_models.DeleteDataQualityScanResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_scan_with_options_async(request, runtime)

    def delete_data_quality_template_with_options(
        self,
        request: main_models.DeleteDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_quality_template_with_options_async(
        self,
        request: main_models.DeleteDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataQualityTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_quality_template(
        self,
        request: main_models.DeleteDataQualityTemplateRequest,
    ) -> main_models.DeleteDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_data_quality_template_with_options(request, runtime)

    async def delete_data_quality_template_async(
        self,
        request: main_models.DeleteDataQualityTemplateRequest,
    ) -> main_models.DeleteDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_quality_template_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_data_source_shared_rule_with_options(
        self,
        request: main_models.DeleteDataSourceSharedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceSharedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSourceSharedRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceSharedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_shared_rule_with_options_async(
        self,
        request: main_models.DeleteDataSourceSharedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceSharedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSourceSharedRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceSharedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source_shared_rule(
        self,
        request: main_models.DeleteDataSourceSharedRuleRequest,
    ) -> main_models.DeleteDataSourceSharedRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_shared_rule_with_options(request, runtime)

    async def delete_data_source_shared_rule_async(
        self,
        request: main_models.DeleteDataSourceSharedRuleRequest,
    ) -> main_models.DeleteDataSourceSharedRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_shared_rule_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_dataset_version_with_options(
        self,
        request: main_models.DeleteDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_version_with_options_async(
        self,
        request: main_models.DeleteDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_version(
        self,
        request: main_models.DeleteDatasetVersionRequest,
    ) -> main_models.DeleteDatasetVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_version_with_options(request, runtime)

    async def delete_dataset_version_async(
        self,
        request: main_models.DeleteDatasetVersionRequest,
    ) -> main_models.DeleteDatasetVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_version_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: main_models.DeleteFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: main_models.DeleteFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: main_models.DeleteFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: main_models.DeleteFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_function_with_options(
        self,
        request: main_models.DeleteFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        request: main_models.DeleteFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        request: main_models.DeleteFunctionRequest,
    ) -> main_models.DeleteFunctionResponse:
        runtime = RuntimeOptions()
        return self.delete_function_with_options(request, runtime)

    async def delete_function_async(
        self,
        request: main_models.DeleteFunctionRequest,
    ) -> main_models.DeleteFunctionResponse:
        runtime = RuntimeOptions()
        return await self.delete_function_with_options_async(request, runtime)

    def delete_lineage_relationship_with_options(
        self,
        request: main_models.DeleteLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLineageRelationshipResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLineageRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lineage_relationship_with_options_async(
        self,
        request: main_models.DeleteLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLineageRelationshipResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLineageRelationshipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lineage_relationship(
        self,
        request: main_models.DeleteLineageRelationshipRequest,
    ) -> main_models.DeleteLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return self.delete_lineage_relationship_with_options(request, runtime)

    async def delete_lineage_relationship_async(
        self,
        request: main_models.DeleteLineageRelationshipRequest,
    ) -> main_models.DeleteLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return await self.delete_lineage_relationship_with_options_async(request, runtime)

    def delete_meta_collection_with_options(
        self,
        request: main_models.DeleteMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_meta_collection_with_options_async(
        self,
        request: main_models.DeleteMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_meta_collection(
        self,
        request: main_models.DeleteMetaCollectionRequest,
    ) -> main_models.DeleteMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.delete_meta_collection_with_options(request, runtime)

    async def delete_meta_collection_async(
        self,
        request: main_models.DeleteMetaCollectionRequest,
    ) -> main_models.DeleteMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.delete_meta_collection_with_options_async(request, runtime)

    def delete_network_with_options(
        self,
        request: main_models.DeleteNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_with_options_async(
        self,
        request: main_models.DeleteNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network(
        self,
        request: main_models.DeleteNetworkRequest,
    ) -> main_models.DeleteNetworkResponse:
        runtime = RuntimeOptions()
        return self.delete_network_with_options(request, runtime)

    async def delete_network_async(
        self,
        request: main_models.DeleteNetworkRequest,
    ) -> main_models.DeleteNetworkResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: main_models.DeleteProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: main_models.DeleteProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_project_member_with_options(
        self,
        request: main_models.DeleteProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_member_with_options_async(
        self,
        request: main_models.DeleteProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project_member(
        self,
        request: main_models.DeleteProjectMemberRequest,
    ) -> main_models.DeleteProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    async def delete_project_member_async(
        self,
        request: main_models.DeleteProjectMemberRequest,
    ) -> main_models.DeleteProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.delete_project_member_with_options_async(request, runtime)

    def delete_resource_with_options(
        self,
        request: main_models.DeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request: main_models.DeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    async def delete_resource_async(
        self,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_route_with_options(
        self,
        request: main_models.DeleteRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_with_options_async(
        self,
        request: main_models.DeleteRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route(
        self,
        request: main_models.DeleteRouteRequest,
    ) -> main_models.DeleteRouteResponse:
        runtime = RuntimeOptions()
        return self.delete_route_with_options(request, runtime)

    async def delete_route_async(
        self,
        request: main_models.DeleteRouteRequest,
    ) -> main_models.DeleteRouteResponse:
        runtime = RuntimeOptions()
        return await self.delete_route_with_options_async(request, runtime)

    def delete_task_with_options(
        self,
        request: main_models.DeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_env):
            query['ProjectEnv'] = request.project_env
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        request: main_models.DeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_env):
            query['ProjectEnv'] = request.project_env
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        request: main_models.DeleteTaskRequest,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_task_with_options(request, runtime)

    async def delete_task_async(
        self,
        request: main_models.DeleteTaskRequest,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_task_with_options_async(request, runtime)

    def delete_workflow_with_options(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_with_options_async(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    async def delete_workflow_async(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.delete_workflow_with_options_async(request, runtime)

    def delete_workflow_definition_with_options(
        self,
        request: main_models.DeleteWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_definition_with_options_async(
        self,
        request: main_models.DeleteWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow_definition(
        self,
        request: main_models.DeleteWorkflowDefinitionRequest,
    ) -> main_models.DeleteWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.delete_workflow_definition_with_options(request, runtime)

    async def delete_workflow_definition_async(
        self,
        request: main_models.DeleteWorkflowDefinitionRequest,
    ) -> main_models.DeleteWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.delete_workflow_definition_with_options_async(request, runtime)

    def deploy_file_with_options(
        self,
        request: main_models.DeployFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_file_with_options_async(
        self,
        request: main_models.DeployFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_file(
        self,
        request: main_models.DeployFileRequest,
    ) -> main_models.DeployFileResponse:
        runtime = RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    async def deploy_file_async(
        self,
        request: main_models.DeployFileRequest,
    ) -> main_models.DeployFileResponse:
        runtime = RuntimeOptions()
        return await self.deploy_file_with_options_async(request, runtime)

    def detach_data_quality_rules_from_evaluation_task_with_options(
        self,
        tmp_req: main_models.DetachDataQualityRulesFromEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDataQualityRulesFromEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.DetachDataQualityRulesFromEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rule_ids):
            request.data_quality_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rule_ids, 'DataQualityRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.data_quality_rule_ids_shrink):
            body['DataQualityRuleIds'] = request.data_quality_rule_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachDataQualityRulesFromEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDataQualityRulesFromEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_data_quality_rules_from_evaluation_task_with_options_async(
        self,
        tmp_req: main_models.DetachDataQualityRulesFromEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDataQualityRulesFromEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.DetachDataQualityRulesFromEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rule_ids):
            request.data_quality_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rule_ids, 'DataQualityRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_evaluation_task_id):
            body['DataQualityEvaluationTaskId'] = request.data_quality_evaluation_task_id
        if not DaraCore.is_null(request.data_quality_rule_ids_shrink):
            body['DataQualityRuleIds'] = request.data_quality_rule_ids_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachDataQualityRulesFromEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDataQualityRulesFromEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_data_quality_rules_from_evaluation_task(
        self,
        request: main_models.DetachDataQualityRulesFromEvaluationTaskRequest,
    ) -> main_models.DetachDataQualityRulesFromEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.detach_data_quality_rules_from_evaluation_task_with_options(request, runtime)

    async def detach_data_quality_rules_from_evaluation_task_async(
        self,
        request: main_models.DetachDataQualityRulesFromEvaluationTaskRequest,
    ) -> main_models.DetachDataQualityRulesFromEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.detach_data_quality_rules_from_evaluation_task_with_options_async(request, runtime)

    def dissociate_project_from_resource_group_with_options(
        self,
        request: main_models.DissociateProjectFromResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateProjectFromResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateProjectFromResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateProjectFromResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_project_from_resource_group_with_options_async(
        self,
        request: main_models.DissociateProjectFromResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateProjectFromResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateProjectFromResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateProjectFromResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_project_from_resource_group(
        self,
        request: main_models.DissociateProjectFromResourceGroupRequest,
    ) -> main_models.DissociateProjectFromResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.dissociate_project_from_resource_group_with_options(request, runtime)

    async def dissociate_project_from_resource_group_async(
        self,
        request: main_models.DissociateProjectFromResourceGroupRequest,
    ) -> main_models.DissociateProjectFromResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_project_from_resource_group_with_options_async(request, runtime)

    def establish_relation_table_to_business_with_options(
        self,
        request: main_models.EstablishRelationTableToBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EstablishRelationTableToBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.table_guid):
            body['TableGuid'] = request.table_guid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EstablishRelationTableToBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstablishRelationTableToBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def establish_relation_table_to_business_with_options_async(
        self,
        request: main_models.EstablishRelationTableToBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EstablishRelationTableToBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.table_guid):
            body['TableGuid'] = request.table_guid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EstablishRelationTableToBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstablishRelationTableToBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def establish_relation_table_to_business(
        self,
        request: main_models.EstablishRelationTableToBusinessRequest,
    ) -> main_models.EstablishRelationTableToBusinessResponse:
        runtime = RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    async def establish_relation_table_to_business_async(
        self,
        request: main_models.EstablishRelationTableToBusinessRequest,
    ) -> main_models.EstablishRelationTableToBusinessResponse:
        runtime = RuntimeOptions()
        return await self.establish_relation_table_to_business_with_options_async(request, runtime)

    def exec_pipeline_run_stage_with_options(
        self,
        request: main_models.ExecPipelineRunStageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecPipelineRunStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecPipelineRunStage',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecPipelineRunStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_pipeline_run_stage_with_options_async(
        self,
        request: main_models.ExecPipelineRunStageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecPipelineRunStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecPipelineRunStage',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecPipelineRunStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_pipeline_run_stage(
        self,
        request: main_models.ExecPipelineRunStageRequest,
    ) -> main_models.ExecPipelineRunStageResponse:
        runtime = RuntimeOptions()
        return self.exec_pipeline_run_stage_with_options(request, runtime)

    async def exec_pipeline_run_stage_async(
        self,
        request: main_models.ExecPipelineRunStageRequest,
    ) -> main_models.ExecPipelineRunStageResponse:
        runtime = RuntimeOptions()
        return await self.exec_pipeline_run_stage_with_options_async(request, runtime)

    def execute_adhoc_workflow_instance_with_options(
        self,
        tmp_req: main_models.ExecuteAdhocWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAdhocWorkflowInstanceResponse:
        tmp_req.validate()
        request = main_models.ExecuteAdhocWorkflowInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_date):
            body['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAdhocWorkflowInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAdhocWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_adhoc_workflow_instance_with_options_async(
        self,
        tmp_req: main_models.ExecuteAdhocWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAdhocWorkflowInstanceResponse:
        tmp_req.validate()
        request = main_models.ExecuteAdhocWorkflowInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_date):
            body['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAdhocWorkflowInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAdhocWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_adhoc_workflow_instance(
        self,
        request: main_models.ExecuteAdhocWorkflowInstanceRequest,
    ) -> main_models.ExecuteAdhocWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return self.execute_adhoc_workflow_instance_with_options(request, runtime)

    async def execute_adhoc_workflow_instance_async(
        self,
        request: main_models.ExecuteAdhocWorkflowInstanceRequest,
    ) -> main_models.ExecuteAdhocWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return await self.execute_adhoc_workflow_instance_with_options_async(request, runtime)

    def get_alert_rule_with_options(
        self,
        request: main_models.GetAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_rule_with_options_async(
        self,
        request: main_models.GetAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_rule(
        self,
        request: main_models.GetAlertRuleRequest,
    ) -> main_models.GetAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.get_alert_rule_with_options(request, runtime)

    async def get_alert_rule_async(
        self,
        request: main_models.GetAlertRuleRequest,
    ) -> main_models.GetAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_alert_rule_with_options_async(request, runtime)

    def get_business_with_options(
        self,
        request: main_models.GetBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_with_options_async(
        self,
        request: main_models.GetBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business(
        self,
        request: main_models.GetBusinessRequest,
    ) -> main_models.GetBusinessResponse:
        runtime = RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    async def get_business_async(
        self,
        request: main_models.GetBusinessRequest,
    ) -> main_models.GetBusinessResponse:
        runtime = RuntimeOptions()
        return await self.get_business_with_options_async(request, runtime)

    def get_catalog_with_options(
        self,
        request: main_models.GetCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_with_options_async(
        self,
        request: main_models.GetCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog(
        self,
        request: main_models.GetCatalogRequest,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        return self.get_catalog_with_options(request, runtime)

    async def get_catalog_async(
        self,
        request: main_models.GetCatalogRequest,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        return await self.get_catalog_with_options_async(request, runtime)

    def get_certificate_with_options(
        self,
        request: main_models.GetCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_certificate_with_options_async(
        self,
        request: main_models.GetCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_certificate(
        self,
        request: main_models.GetCertificateRequest,
    ) -> main_models.GetCertificateResponse:
        runtime = RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    async def get_certificate_async(
        self,
        request: main_models.GetCertificateRequest,
    ) -> main_models.GetCertificateResponse:
        runtime = RuntimeOptions()
        return await self.get_certificate_with_options_async(request, runtime)

    def get_column_with_options(
        self,
        request: main_models.GetColumnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetColumnResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetColumn',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetColumnResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_column_with_options_async(
        self,
        request: main_models.GetColumnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetColumnResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetColumn',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetColumnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_column(
        self,
        request: main_models.GetColumnRequest,
    ) -> main_models.GetColumnResponse:
        runtime = RuntimeOptions()
        return self.get_column_with_options(request, runtime)

    async def get_column_async(
        self,
        request: main_models.GetColumnRequest,
    ) -> main_models.GetColumnResponse:
        runtime = RuntimeOptions()
        return await self.get_column_with_options_async(request, runtime)

    def get_component_with_options(
        self,
        request: main_models.GetComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_id):
            query['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_component_with_options_async(
        self,
        request: main_models.GetComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_id):
            query['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_component(
        self,
        request: main_models.GetComponentRequest,
    ) -> main_models.GetComponentResponse:
        runtime = RuntimeOptions()
        return self.get_component_with_options(request, runtime)

    async def get_component_async(
        self,
        request: main_models.GetComponentRequest,
    ) -> main_models.GetComponentResponse:
        runtime = RuntimeOptions()
        return await self.get_component_with_options_async(request, runtime)

    def get_compute_resource_with_options(
        self,
        request: main_models.GetComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_resource_with_options_async(
        self,
        request: main_models.GetComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_resource(
        self,
        request: main_models.GetComputeResourceRequest,
    ) -> main_models.GetComputeResourceResponse:
        runtime = RuntimeOptions()
        return self.get_compute_resource_with_options(request, runtime)

    async def get_compute_resource_async(
        self,
        request: main_models.GetComputeResourceRequest,
    ) -> main_models.GetComputeResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_compute_resource_with_options_async(request, runtime)

    def get_create_workflow_instances_result_with_options(
        self,
        request: main_models.GetCreateWorkflowInstancesResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateWorkflowInstancesResultResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateWorkflowInstancesResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateWorkflowInstancesResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_workflow_instances_result_with_options_async(
        self,
        request: main_models.GetCreateWorkflowInstancesResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateWorkflowInstancesResultResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateWorkflowInstancesResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateWorkflowInstancesResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_workflow_instances_result(
        self,
        request: main_models.GetCreateWorkflowInstancesResultRequest,
    ) -> main_models.GetCreateWorkflowInstancesResultResponse:
        runtime = RuntimeOptions()
        return self.get_create_workflow_instances_result_with_options(request, runtime)

    async def get_create_workflow_instances_result_async(
        self,
        request: main_models.GetCreateWorkflowInstancesResultRequest,
    ) -> main_models.GetCreateWorkflowInstancesResultResponse:
        runtime = RuntimeOptions()
        return await self.get_create_workflow_instances_result_with_options_async(request, runtime)

    def get_dijob_with_options(
        self,
        request: main_models.GetDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dijob_with_options_async(
        self,
        request: main_models.GetDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dijob(
        self,
        request: main_models.GetDIJobRequest,
    ) -> main_models.GetDIJobResponse:
        runtime = RuntimeOptions()
        return self.get_dijob_with_options(request, runtime)

    async def get_dijob_async(
        self,
        request: main_models.GetDIJobRequest,
    ) -> main_models.GetDIJobResponse:
        runtime = RuntimeOptions()
        return await self.get_dijob_with_options_async(request, runtime)

    def get_dijob_log_with_options(
        self,
        request: main_models.GetDIJobLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDIJobLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDIJobLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDIJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dijob_log_with_options_async(
        self,
        request: main_models.GetDIJobLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDIJobLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDIJobLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDIJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dijob_log(
        self,
        request: main_models.GetDIJobLogRequest,
    ) -> main_models.GetDIJobLogResponse:
        runtime = RuntimeOptions()
        return self.get_dijob_log_with_options(request, runtime)

    async def get_dijob_log_async(
        self,
        request: main_models.GetDIJobLogRequest,
    ) -> main_models.GetDIJobLogResponse:
        runtime = RuntimeOptions()
        return await self.get_dijob_log_with_options_async(request, runtime)

    def get_data_quality_alert_rule_with_options(
        self,
        request: main_models.GetDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_alert_rule_with_options_async(
        self,
        request: main_models.GetDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_alert_rule(
        self,
        request: main_models.GetDataQualityAlertRuleRequest,
    ) -> main_models.GetDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_alert_rule_with_options(request, runtime)

    async def get_data_quality_alert_rule_async(
        self,
        request: main_models.GetDataQualityAlertRuleRequest,
    ) -> main_models.GetDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_alert_rule_with_options_async(request, runtime)

    def get_data_quality_evaluation_task_with_options(
        self,
        request: main_models.GetDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityEvaluationTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_evaluation_task_with_options_async(
        self,
        request: main_models.GetDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityEvaluationTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_evaluation_task(
        self,
        request: main_models.GetDataQualityEvaluationTaskRequest,
    ) -> main_models.GetDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_evaluation_task_with_options(request, runtime)

    async def get_data_quality_evaluation_task_async(
        self,
        request: main_models.GetDataQualityEvaluationTaskRequest,
    ) -> main_models.GetDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_evaluation_task_with_options_async(request, runtime)

    def get_data_quality_evaluation_task_instance_with_options(
        self,
        request: main_models.GetDataQualityEvaluationTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityEvaluationTaskInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityEvaluationTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityEvaluationTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_evaluation_task_instance_with_options_async(
        self,
        request: main_models.GetDataQualityEvaluationTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityEvaluationTaskInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityEvaluationTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityEvaluationTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_evaluation_task_instance(
        self,
        request: main_models.GetDataQualityEvaluationTaskInstanceRequest,
    ) -> main_models.GetDataQualityEvaluationTaskInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_evaluation_task_instance_with_options(request, runtime)

    async def get_data_quality_evaluation_task_instance_async(
        self,
        request: main_models.GetDataQualityEvaluationTaskInstanceRequest,
    ) -> main_models.GetDataQualityEvaluationTaskInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_evaluation_task_instance_with_options_async(request, runtime)

    def get_data_quality_rule_with_options(
        self,
        request: main_models.GetDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_rule_with_options_async(
        self,
        request: main_models.GetDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_rule(
        self,
        request: main_models.GetDataQualityRuleRequest,
    ) -> main_models.GetDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_rule_with_options(request, runtime)

    async def get_data_quality_rule_async(
        self,
        request: main_models.GetDataQualityRuleRequest,
    ) -> main_models.GetDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_rule_with_options_async(request, runtime)

    def get_data_quality_rule_template_with_options(
        self,
        request: main_models.GetDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityRuleTemplateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_rule_template_with_options_async(
        self,
        request: main_models.GetDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityRuleTemplateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_rule_template(
        self,
        request: main_models.GetDataQualityRuleTemplateRequest,
    ) -> main_models.GetDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_rule_template_with_options(request, runtime)

    async def get_data_quality_rule_template_async(
        self,
        request: main_models.GetDataQualityRuleTemplateRequest,
    ) -> main_models.GetDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_rule_template_with_options_async(request, runtime)

    def get_data_quality_scan_with_options(
        self,
        request: main_models.GetDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_scan_with_options_async(
        self,
        request: main_models.GetDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_scan(
        self,
        request: main_models.GetDataQualityScanRequest,
    ) -> main_models.GetDataQualityScanResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_scan_with_options(request, runtime)

    async def get_data_quality_scan_async(
        self,
        request: main_models.GetDataQualityScanRequest,
    ) -> main_models.GetDataQualityScanResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_scan_with_options_async(request, runtime)

    def get_data_quality_scan_run_with_options(
        self,
        request: main_models.GetDataQualityScanRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScanRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_scan_run_with_options_async(
        self,
        request: main_models.GetDataQualityScanRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScanRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_scan_run(
        self,
        request: main_models.GetDataQualityScanRunRequest,
    ) -> main_models.GetDataQualityScanRunResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_scan_run_with_options(request, runtime)

    async def get_data_quality_scan_run_async(
        self,
        request: main_models.GetDataQualityScanRunRequest,
    ) -> main_models.GetDataQualityScanRunResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_scan_run_with_options_async(request, runtime)

    def get_data_quality_scan_run_log_with_options(
        self,
        request: main_models.GetDataQualityScanRunLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanRunLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScanRunLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanRunLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_scan_run_log_with_options_async(
        self,
        request: main_models.GetDataQualityScanRunLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityScanRunLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityScanRunLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityScanRunLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_scan_run_log(
        self,
        request: main_models.GetDataQualityScanRunLogRequest,
    ) -> main_models.GetDataQualityScanRunLogResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_scan_run_log_with_options(request, runtime)

    async def get_data_quality_scan_run_log_async(
        self,
        request: main_models.GetDataQualityScanRunLogRequest,
    ) -> main_models.GetDataQualityScanRunLogResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_scan_run_log_with_options_async(request, runtime)

    def get_data_quality_template_with_options(
        self,
        request: main_models.GetDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_template_with_options_async(
        self,
        request: main_models.GetDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_template(
        self,
        request: main_models.GetDataQualityTemplateRequest,
    ) -> main_models.GetDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_data_quality_template_with_options(request, runtime)

    async def get_data_quality_template_async(
        self,
        request: main_models.GetDataQualityTemplateRequest,
    ) -> main_models.GetDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_data_quality_template_with_options_async(request, runtime)

    def get_data_source_with_options(
        self,
        request: main_models.GetDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_with_options_async(
        self,
        request: main_models.GetDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source(
        self,
        request: main_models.GetDataSourceRequest,
    ) -> main_models.GetDataSourceResponse:
        runtime = RuntimeOptions()
        return self.get_data_source_with_options(request, runtime)

    async def get_data_source_async(
        self,
        request: main_models.GetDataSourceRequest,
    ) -> main_models.GetDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.get_data_source_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: main_models.GetDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: main_models.GetDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        request: main_models.GetDatabaseRequest,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: main_models.GetDatabaseRequest,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_dataset_version_with_options(
        self,
        request: main_models.GetDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_version_with_options_async(
        self,
        request: main_models.GetDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_version(
        self,
        request: main_models.GetDatasetVersionRequest,
    ) -> main_models.GetDatasetVersionResponse:
        runtime = RuntimeOptions()
        return self.get_dataset_version_with_options(request, runtime)

    async def get_dataset_version_async(
        self,
        request: main_models.GetDatasetVersionRequest,
    ) -> main_models.GetDatasetVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_dataset_version_with_options_async(request, runtime)

    def get_deployment_package_with_options(
        self,
        request: main_models.GetDeploymentPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deployment_id):
            body['DeploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentPackage',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_package_with_options_async(
        self,
        request: main_models.GetDeploymentPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deployment_id):
            body['DeploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentPackage',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_package(
        self,
        request: main_models.GetDeploymentPackageRequest,
    ) -> main_models.GetDeploymentPackageResponse:
        runtime = RuntimeOptions()
        return self.get_deployment_package_with_options(request, runtime)

    async def get_deployment_package_async(
        self,
        request: main_models.GetDeploymentPackageRequest,
    ) -> main_models.GetDeploymentPackageResponse:
        runtime = RuntimeOptions()
        return await self.get_deployment_package_with_options_async(request, runtime)

    def get_file_with_options(
        self,
        request: main_models.GetFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: main_models.GetFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file(
        self,
        request: main_models.GetFileRequest,
    ) -> main_models.GetFileResponse:
        runtime = RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    async def get_file_async(
        self,
        request: main_models.GetFileRequest,
    ) -> main_models.GetFileResponse:
        runtime = RuntimeOptions()
        return await self.get_file_with_options_async(request, runtime)

    def get_file_version_with_options(
        self,
        request: main_models.GetFileVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_version):
            body['FileVersion'] = request.file_version
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_version_with_options_async(
        self,
        request: main_models.GetFileVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_version):
            body['FileVersion'] = request.file_version
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_version(
        self,
        request: main_models.GetFileVersionRequest,
    ) -> main_models.GetFileVersionResponse:
        runtime = RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    async def get_file_version_async(
        self,
        request: main_models.GetFileVersionRequest,
    ) -> main_models.GetFileVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_file_version_with_options_async(request, runtime)

    def get_folder_with_options(
        self,
        request: main_models.GetFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: main_models.GetFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_function_with_options(
        self,
        request: main_models.GetFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        request: main_models.GetFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        request: main_models.GetFunctionRequest,
    ) -> main_models.GetFunctionResponse:
        runtime = RuntimeOptions()
        return self.get_function_with_options(request, runtime)

    async def get_function_async(
        self,
        request: main_models.GetFunctionRequest,
    ) -> main_models.GetFunctionResponse:
        runtime = RuntimeOptions()
        return await self.get_function_with_options_async(request, runtime)

    def get_ideevent_detail_with_options(
        self,
        request: main_models.GetIDEEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIDEEventDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIDEEventDetail',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIDEEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ideevent_detail_with_options_async(
        self,
        request: main_models.GetIDEEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIDEEventDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIDEEventDetail',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIDEEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ideevent_detail(
        self,
        request: main_models.GetIDEEventDetailRequest,
    ) -> main_models.GetIDEEventDetailResponse:
        runtime = RuntimeOptions()
        return self.get_ideevent_detail_with_options(request, runtime)

    async def get_ideevent_detail_async(
        self,
        request: main_models.GetIDEEventDetailRequest,
    ) -> main_models.GetIDEEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_ideevent_detail_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: main_models.GetJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobStatus',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: main_models.GetJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobStatus',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_status(
        self,
        request: main_models.GetJobStatusRequest,
    ) -> main_models.GetJobStatusResponse:
        runtime = RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: main_models.GetJobStatusRequest,
    ) -> main_models.GetJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_lineage_relationship_with_options(
        self,
        request: main_models.GetLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLineageRelationshipResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLineageRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lineage_relationship_with_options_async(
        self,
        request: main_models.GetLineageRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLineageRelationshipResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLineageRelationship',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLineageRelationshipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lineage_relationship(
        self,
        request: main_models.GetLineageRelationshipRequest,
    ) -> main_models.GetLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return self.get_lineage_relationship_with_options(request, runtime)

    async def get_lineage_relationship_async(
        self,
        request: main_models.GetLineageRelationshipRequest,
    ) -> main_models.GetLineageRelationshipResponse:
        runtime = RuntimeOptions()
        return await self.get_lineage_relationship_with_options_async(request, runtime)

    def get_meta_collection_with_options(
        self,
        request: main_models.GetMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMetaCollectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_meta_collection_with_options_async(
        self,
        request: main_models.GetMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMetaCollectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_meta_collection(
        self,
        request: main_models.GetMetaCollectionRequest,
    ) -> main_models.GetMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.get_meta_collection_with_options(request, runtime)

    async def get_meta_collection_async(
        self,
        request: main_models.GetMetaCollectionRequest,
    ) -> main_models.GetMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.get_meta_collection_with_options_async(request, runtime)

    def get_network_with_options(
        self,
        request: main_models.GetNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_with_options_async(
        self,
        request: main_models.GetNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetwork',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network(
        self,
        request: main_models.GetNetworkRequest,
    ) -> main_models.GetNetworkResponse:
        runtime = RuntimeOptions()
        return self.get_network_with_options(request, runtime)

    async def get_network_async(
        self,
        request: main_models.GetNetworkRequest,
    ) -> main_models.GetNetworkResponse:
        runtime = RuntimeOptions()
        return await self.get_network_with_options_async(request, runtime)

    def get_node_with_options(
        self,
        request: main_models.GetNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_with_options_async(
        self,
        request: main_models.GetNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node(
        self,
        request: main_models.GetNodeRequest,
    ) -> main_models.GetNodeResponse:
        runtime = RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    async def get_node_async(
        self,
        request: main_models.GetNodeRequest,
    ) -> main_models.GetNodeResponse:
        runtime = RuntimeOptions()
        return await self.get_node_with_options_async(request, runtime)

    def get_partition_with_options(
        self,
        request: main_models.GetPartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPartitionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPartition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partition_with_options_async(
        self,
        request: main_models.GetPartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPartitionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPartition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partition(
        self,
        request: main_models.GetPartitionRequest,
    ) -> main_models.GetPartitionResponse:
        runtime = RuntimeOptions()
        return self.get_partition_with_options(request, runtime)

    async def get_partition_async(
        self,
        request: main_models.GetPartitionRequest,
    ) -> main_models.GetPartitionResponse:
        runtime = RuntimeOptions()
        return await self.get_partition_with_options_async(request, runtime)

    def get_pipeline_run_with_options(
        self,
        request: main_models.GetPipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_with_options_async(
        self,
        request: main_models.GetPipelineRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineRun',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run(
        self,
        request: main_models.GetPipelineRunRequest,
    ) -> main_models.GetPipelineRunResponse:
        runtime = RuntimeOptions()
        return self.get_pipeline_run_with_options(request, runtime)

    async def get_pipeline_run_async(
        self,
        request: main_models.GetPipelineRunRequest,
    ) -> main_models.GetPipelineRunResponse:
        runtime = RuntimeOptions()
        return await self.get_pipeline_run_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_project_member_with_options(
        self,
        request: main_models.GetProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_member_with_options_async(
        self,
        request: main_models.GetProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectMember',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_member(
        self,
        request: main_models.GetProjectMemberRequest,
    ) -> main_models.GetProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.get_project_member_with_options(request, runtime)

    async def get_project_member_async(
        self,
        request: main_models.GetProjectMemberRequest,
    ) -> main_models.GetProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.get_project_member_with_options_async(request, runtime)

    def get_project_role_with_options(
        self,
        request: main_models.GetProjectRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectRole',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_role_with_options_async(
        self,
        request: main_models.GetProjectRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectRole',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_role(
        self,
        request: main_models.GetProjectRoleRequest,
    ) -> main_models.GetProjectRoleResponse:
        runtime = RuntimeOptions()
        return self.get_project_role_with_options(request, runtime)

    async def get_project_role_async(
        self,
        request: main_models.GetProjectRoleRequest,
    ) -> main_models.GetProjectRoleResponse:
        runtime = RuntimeOptions()
        return await self.get_project_role_with_options_async(request, runtime)

    def get_rerun_workflow_instances_result_with_options(
        self,
        request: main_models.GetRerunWorkflowInstancesResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRerunWorkflowInstancesResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRerunWorkflowInstancesResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRerunWorkflowInstancesResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rerun_workflow_instances_result_with_options_async(
        self,
        request: main_models.GetRerunWorkflowInstancesResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRerunWorkflowInstancesResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRerunWorkflowInstancesResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRerunWorkflowInstancesResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rerun_workflow_instances_result(
        self,
        request: main_models.GetRerunWorkflowInstancesResultRequest,
    ) -> main_models.GetRerunWorkflowInstancesResultResponse:
        runtime = RuntimeOptions()
        return self.get_rerun_workflow_instances_result_with_options(request, runtime)

    async def get_rerun_workflow_instances_result_async(
        self,
        request: main_models.GetRerunWorkflowInstancesResultRequest,
    ) -> main_models.GetRerunWorkflowInstancesResultResponse:
        runtime = RuntimeOptions()
        return await self.get_rerun_workflow_instances_result_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: main_models.GetResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: main_models.GetResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: main_models.GetResourceRequest,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: main_models.GetResourceRequest,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_resource_group_with_options(
        self,
        request: main_models.GetResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: main_models.GetResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_route_with_options(
        self,
        request: main_models.GetRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_route_with_options_async(
        self,
        request: main_models.GetRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_route(
        self,
        request: main_models.GetRouteRequest,
    ) -> main_models.GetRouteResponse:
        runtime = RuntimeOptions()
        return self.get_route_with_options(request, runtime)

    async def get_route_async(
        self,
        request: main_models.GetRouteRequest,
    ) -> main_models.GetRouteResponse:
        runtime = RuntimeOptions()
        return await self.get_route_with_options_async(request, runtime)

    def get_schema_with_options(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_with_options_async(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return self.get_schema_with_options(request, runtime)

    async def get_schema_async(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_schema_with_options_async(request, runtime)

    def get_table_with_options(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return self.get_table_with_options(request, runtime)

    async def get_table_async(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return await self.get_table_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_instance_with_options(
        self,
        request: main_models.GetTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_instance_with_options_async(
        self,
        request: main_models.GetTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_instance(
        self,
        request: main_models.GetTaskInstanceRequest,
    ) -> main_models.GetTaskInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_task_instance_with_options(request, runtime)

    async def get_task_instance_async(
        self,
        request: main_models.GetTaskInstanceRequest,
    ) -> main_models.GetTaskInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_task_instance_with_options_async(request, runtime)

    def get_task_instance_log_with_options(
        self,
        request: main_models.GetTaskInstanceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInstanceLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInstanceLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_instance_log_with_options_async(
        self,
        request: main_models.GetTaskInstanceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInstanceLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInstanceLog',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_instance_log(
        self,
        request: main_models.GetTaskInstanceLogRequest,
    ) -> main_models.GetTaskInstanceLogResponse:
        runtime = RuntimeOptions()
        return self.get_task_instance_log_with_options(request, runtime)

    async def get_task_instance_log_async(
        self,
        request: main_models.GetTaskInstanceLogRequest,
    ) -> main_models.GetTaskInstanceLogResponse:
        runtime = RuntimeOptions()
        return await self.get_task_instance_log_with_options_async(request, runtime)

    def get_workflow_with_options(
        self,
        request: main_models.GetWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_with_options_async(
        self,
        request: main_models.GetWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow(
        self,
        request: main_models.GetWorkflowRequest,
    ) -> main_models.GetWorkflowResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_with_options(request, runtime)

    async def get_workflow_async(
        self,
        request: main_models.GetWorkflowRequest,
    ) -> main_models.GetWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_with_options_async(request, runtime)

    def get_workflow_definition_with_options(
        self,
        request: main_models.GetWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDefinitionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_definition_with_options_async(
        self,
        request: main_models.GetWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDefinitionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_definition(
        self,
        request: main_models.GetWorkflowDefinitionRequest,
    ) -> main_models.GetWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_definition_with_options(request, runtime)

    async def get_workflow_definition_async(
        self,
        request: main_models.GetWorkflowDefinitionRequest,
    ) -> main_models.GetWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_definition_with_options_async(request, runtime)

    def get_workflow_instance_with_options(
        self,
        request: main_models.GetWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_instance_with_options_async(
        self,
        request: main_models.GetWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_instance(
        self,
        request: main_models.GetWorkflowInstanceRequest,
    ) -> main_models.GetWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_instance_with_options(request, runtime)

    async def get_workflow_instance_async(
        self,
        request: main_models.GetWorkflowInstanceRequest,
    ) -> main_models.GetWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_instance_with_options_async(request, runtime)

    def grant_member_project_roles_with_options(
        self,
        tmp_req: main_models.GrantMemberProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantMemberProjectRolesResponse:
        tmp_req.validate()
        request = main_models.GrantMemberProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantMemberProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantMemberProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_member_project_roles_with_options_async(
        self,
        tmp_req: main_models.GrantMemberProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantMemberProjectRolesResponse:
        tmp_req.validate()
        request = main_models.GrantMemberProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantMemberProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantMemberProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_member_project_roles(
        self,
        request: main_models.GrantMemberProjectRolesRequest,
    ) -> main_models.GrantMemberProjectRolesResponse:
        runtime = RuntimeOptions()
        return self.grant_member_project_roles_with_options(request, runtime)

    async def grant_member_project_roles_async(
        self,
        request: main_models.GrantMemberProjectRolesRequest,
    ) -> main_models.GrantMemberProjectRolesResponse:
        runtime = RuntimeOptions()
        return await self.grant_member_project_roles_with_options_async(request, runtime)

    def import_certificate_with_options(
        self,
        request: main_models.ImportCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_file):
            query['CertificateFile'] = request.certificate_file
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_certificate_with_options_async(
        self,
        request: main_models.ImportCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_file):
            query['CertificateFile'] = request.certificate_file
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCertificate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_certificate(
        self,
        request: main_models.ImportCertificateRequest,
    ) -> main_models.ImportCertificateResponse:
        runtime = RuntimeOptions()
        return self.import_certificate_with_options(request, runtime)

    async def import_certificate_async(
        self,
        request: main_models.ImportCertificateRequest,
    ) -> main_models.ImportCertificateResponse:
        runtime = RuntimeOptions()
        return await self.import_certificate_with_options_async(request, runtime)

    def import_certificate_advance(
        self,
        request: main_models.ImportCertificateAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCertificateResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        import_certificate_req = main_models.ImportCertificateRequest()
        Utils.convert(request, import_certificate_req)
        if not DaraCore.is_null(request.certificate_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.certificate_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            import_certificate_req.certificate_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        import_certificate_resp = self.import_certificate_with_options(import_certificate_req, runtime)
        return import_certificate_resp

    async def import_certificate_advance_async(
        self,
        request: main_models.ImportCertificateAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCertificateResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        import_certificate_req = main_models.ImportCertificateRequest()
        Utils.convert(request, import_certificate_req)
        if not DaraCore.is_null(request.certificate_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.certificate_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            import_certificate_req.certificate_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        import_certificate_resp = await self.import_certificate_with_options_async(import_certificate_req, runtime)
        return import_certificate_resp

    def import_workflow_definition_with_options(
        self,
        request: main_models.ImportWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_workflow_definition_with_options_async(
        self,
        request: main_models.ImportWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_workflow_definition(
        self,
        request: main_models.ImportWorkflowDefinitionRequest,
    ) -> main_models.ImportWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.import_workflow_definition_with_options(request, runtime)

    async def import_workflow_definition_async(
        self,
        request: main_models.ImportWorkflowDefinitionRequest,
    ) -> main_models.ImportWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.import_workflow_definition_with_options_async(request, runtime)

    def list_alert_rules_with_options(
        self,
        tmp_req: main_models.ListAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertRulesResponse:
        tmp_req.validate()
        request = main_models.ListAlertRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.receiver):
            query['Receiver'] = request.receiver
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_rules_with_options_async(
        self,
        tmp_req: main_models.ListAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertRulesResponse:
        tmp_req.validate()
        request = main_models.ListAlertRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.receiver):
            query['Receiver'] = request.receiver
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_rules(
        self,
        request: main_models.ListAlertRulesRequest,
    ) -> main_models.ListAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.list_alert_rules_with_options(request, runtime)

    async def list_alert_rules_async(
        self,
        request: main_models.ListAlertRulesRequest,
    ) -> main_models.ListAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_alert_rules_with_options_async(request, runtime)

    def list_business_with_options(
        self,
        request: main_models.ListBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_business_with_options_async(
        self,
        request: main_models.ListBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_business(
        self,
        request: main_models.ListBusinessRequest,
    ) -> main_models.ListBusinessResponse:
        runtime = RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    async def list_business_async(
        self,
        request: main_models.ListBusinessRequest,
    ) -> main_models.ListBusinessResponse:
        runtime = RuntimeOptions()
        return await self.list_business_with_options_async(request, runtime)

    def list_catalogs_with_options(
        self,
        tmp_req: main_models.ListCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        tmp_req.validate()
        request = main_models.ListCatalogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        tmp_req: main_models.ListCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        tmp_req.validate()
        request = main_models.ListCatalogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        return self.list_catalogs_with_options(request, runtime)

    async def list_catalogs_async(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        return await self.list_catalogs_with_options_async(request, runtime)

    def list_certificates_with_options(
        self,
        request: main_models.ListCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertificatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertificates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_certificates_with_options_async(
        self,
        request: main_models.ListCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertificatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertificates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_certificates(
        self,
        request: main_models.ListCertificatesRequest,
    ) -> main_models.ListCertificatesResponse:
        runtime = RuntimeOptions()
        return self.list_certificates_with_options(request, runtime)

    async def list_certificates_async(
        self,
        request: main_models.ListCertificatesRequest,
    ) -> main_models.ListCertificatesResponse:
        runtime = RuntimeOptions()
        return await self.list_certificates_with_options_async(request, runtime)

    def list_columns_with_options(
        self,
        request: main_models.ListColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListColumnsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListColumns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_columns_with_options_async(
        self,
        request: main_models.ListColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListColumnsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListColumns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_columns(
        self,
        request: main_models.ListColumnsRequest,
    ) -> main_models.ListColumnsResponse:
        runtime = RuntimeOptions()
        return self.list_columns_with_options(request, runtime)

    async def list_columns_async(
        self,
        request: main_models.ListColumnsRequest,
    ) -> main_models.ListColumnsResponse:
        runtime = RuntimeOptions()
        return await self.list_columns_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_compute_resources_with_options(
        self,
        tmp_req: main_models.ListComputeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeResourcesResponse:
        tmp_req.validate()
        request = main_models.ListComputeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeResources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_resources_with_options_async(
        self,
        tmp_req: main_models.ListComputeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeResourcesResponse:
        tmp_req.validate()
        request = main_models.ListComputeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeResources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_resources(
        self,
        request: main_models.ListComputeResourcesRequest,
    ) -> main_models.ListComputeResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_compute_resources_with_options(request, runtime)

    async def list_compute_resources_async(
        self,
        request: main_models.ListComputeResourcesRequest,
    ) -> main_models.ListComputeResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_compute_resources_with_options_async(request, runtime)

    def list_crawler_types_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCrawlerTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCrawlerTypes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrawlerTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crawler_types_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCrawlerTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCrawlerTypes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrawlerTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crawler_types(self) -> main_models.ListCrawlerTypesResponse:
        runtime = RuntimeOptions()
        return self.list_crawler_types_with_options(runtime)

    async def list_crawler_types_async(self) -> main_models.ListCrawlerTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_crawler_types_with_options_async(runtime)

    def list_dialarm_rules_with_options(
        self,
        request: main_models.ListDIAlarmRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIAlarmRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIAlarmRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIAlarmRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialarm_rules_with_options_async(
        self,
        request: main_models.ListDIAlarmRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIAlarmRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIAlarmRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIAlarmRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialarm_rules(
        self,
        request: main_models.ListDIAlarmRulesRequest,
    ) -> main_models.ListDIAlarmRulesResponse:
        runtime = RuntimeOptions()
        return self.list_dialarm_rules_with_options(request, runtime)

    async def list_dialarm_rules_async(
        self,
        request: main_models.ListDIAlarmRulesRequest,
    ) -> main_models.ListDIAlarmRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_dialarm_rules_with_options_async(request, runtime)

    def list_dijob_events_with_options(
        self,
        request: main_models.ListDIJobEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobEventsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobEvents',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_events_with_options_async(
        self,
        request: main_models.ListDIJobEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobEventsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobEvents',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_events(
        self,
        request: main_models.ListDIJobEventsRequest,
    ) -> main_models.ListDIJobEventsResponse:
        runtime = RuntimeOptions()
        return self.list_dijob_events_with_options(request, runtime)

    async def list_dijob_events_async(
        self,
        request: main_models.ListDIJobEventsRequest,
    ) -> main_models.ListDIJobEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_dijob_events_with_options_async(request, runtime)

    def list_dijob_metrics_with_options(
        self,
        tmp_req: main_models.ListDIJobMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobMetricsResponse:
        tmp_req.validate()
        request = main_models.ListDIJobMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_name):
            request.metric_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_name, 'MetricName', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobMetrics',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_metrics_with_options_async(
        self,
        tmp_req: main_models.ListDIJobMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobMetricsResponse:
        tmp_req.validate()
        request = main_models.ListDIJobMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_name):
            request.metric_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_name, 'MetricName', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobMetrics',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_metrics(
        self,
        request: main_models.ListDIJobMetricsRequest,
    ) -> main_models.ListDIJobMetricsResponse:
        runtime = RuntimeOptions()
        return self.list_dijob_metrics_with_options(request, runtime)

    async def list_dijob_metrics_async(
        self,
        request: main_models.ListDIJobMetricsRequest,
    ) -> main_models.ListDIJobMetricsResponse:
        runtime = RuntimeOptions()
        return await self.list_dijob_metrics_with_options_async(request, runtime)

    def list_dijob_run_details_with_options(
        self,
        request: main_models.ListDIJobRunDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobRunDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobRunDetails',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobRunDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijob_run_details_with_options_async(
        self,
        request: main_models.ListDIJobRunDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobRunDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobRunDetails',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobRunDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijob_run_details(
        self,
        request: main_models.ListDIJobRunDetailsRequest,
    ) -> main_models.ListDIJobRunDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_dijob_run_details_with_options(request, runtime)

    async def list_dijob_run_details_async(
        self,
        request: main_models.ListDIJobRunDetailsRequest,
    ) -> main_models.ListDIJobRunDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_dijob_run_details_with_options_async(request, runtime)

    def list_dijobs_with_options(
        self,
        request: main_models.ListDIJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dijobs_with_options_async(
        self,
        request: main_models.ListDIJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDIJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDIJobs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDIJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dijobs(
        self,
        request: main_models.ListDIJobsRequest,
    ) -> main_models.ListDIJobsResponse:
        runtime = RuntimeOptions()
        return self.list_dijobs_with_options(request, runtime)

    async def list_dijobs_async(
        self,
        request: main_models.ListDIJobsRequest,
    ) -> main_models.ListDIJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_dijobs_with_options_async(request, runtime)

    def list_data_asset_tags_with_options(
        self,
        request: main_models.ListDataAssetTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssetTags',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_asset_tags_with_options_async(
        self,
        request: main_models.ListDataAssetTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssetTags',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_asset_tags(
        self,
        request: main_models.ListDataAssetTagsRequest,
    ) -> main_models.ListDataAssetTagsResponse:
        runtime = RuntimeOptions()
        return self.list_data_asset_tags_with_options(request, runtime)

    async def list_data_asset_tags_async(
        self,
        request: main_models.ListDataAssetTagsRequest,
    ) -> main_models.ListDataAssetTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_asset_tags_with_options_async(request, runtime)

    def list_data_assets_with_options(
        self,
        tmp_req: main_models.ListDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetsResponse:
        tmp_req.validate()
        request = main_models.ListDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_assets_with_options_async(
        self,
        tmp_req: main_models.ListDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetsResponse:
        tmp_req.validate()
        request = main_models.ListDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_assets(
        self,
        request: main_models.ListDataAssetsRequest,
    ) -> main_models.ListDataAssetsResponse:
        runtime = RuntimeOptions()
        return self.list_data_assets_with_options(request, runtime)

    async def list_data_assets_async(
        self,
        request: main_models.ListDataAssetsRequest,
    ) -> main_models.ListDataAssetsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_assets_with_options_async(request, runtime)

    def list_data_quality_alert_rules_with_options(
        self,
        request: main_models.ListDataQualityAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_quality_scan_id):
            query['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityAlertRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_alert_rules_with_options_async(
        self,
        request: main_models.ListDataQualityAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_quality_scan_id):
            query['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityAlertRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_alert_rules(
        self,
        request: main_models.ListDataQualityAlertRulesRequest,
    ) -> main_models.ListDataQualityAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_alert_rules_with_options(request, runtime)

    async def list_data_quality_alert_rules_async(
        self,
        request: main_models.ListDataQualityAlertRulesRequest,
    ) -> main_models.ListDataQualityAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_alert_rules_with_options_async(request, runtime)

    def list_data_quality_evaluation_task_instances_with_options(
        self,
        request: main_models.ListDataQualityEvaluationTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityEvaluationTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityEvaluationTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityEvaluationTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_evaluation_task_instances_with_options_async(
        self,
        request: main_models.ListDataQualityEvaluationTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityEvaluationTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityEvaluationTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityEvaluationTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_evaluation_task_instances(
        self,
        request: main_models.ListDataQualityEvaluationTaskInstancesRequest,
    ) -> main_models.ListDataQualityEvaluationTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_evaluation_task_instances_with_options(request, runtime)

    async def list_data_quality_evaluation_task_instances_async(
        self,
        request: main_models.ListDataQualityEvaluationTaskInstancesRequest,
    ) -> main_models.ListDataQualityEvaluationTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_evaluation_task_instances_with_options_async(request, runtime)

    def list_data_quality_evaluation_tasks_with_options(
        self,
        request: main_models.ListDataQualityEvaluationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityEvaluationTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityEvaluationTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityEvaluationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_evaluation_tasks_with_options_async(
        self,
        request: main_models.ListDataQualityEvaluationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityEvaluationTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityEvaluationTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityEvaluationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_evaluation_tasks(
        self,
        request: main_models.ListDataQualityEvaluationTasksRequest,
    ) -> main_models.ListDataQualityEvaluationTasksResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_evaluation_tasks_with_options(request, runtime)

    async def list_data_quality_evaluation_tasks_async(
        self,
        request: main_models.ListDataQualityEvaluationTasksRequest,
    ) -> main_models.ListDataQualityEvaluationTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_evaluation_tasks_with_options_async(request, runtime)

    def list_data_quality_results_with_options(
        self,
        request: main_models.ListDataQualityResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityResultsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityResults',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_results_with_options_async(
        self,
        request: main_models.ListDataQualityResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityResultsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityResults',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_results(
        self,
        request: main_models.ListDataQualityResultsRequest,
    ) -> main_models.ListDataQualityResultsResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_results_with_options(request, runtime)

    async def list_data_quality_results_async(
        self,
        request: main_models.ListDataQualityResultsRequest,
    ) -> main_models.ListDataQualityResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_results_with_options_async(request, runtime)

    def list_data_quality_rule_templates_with_options(
        self,
        request: main_models.ListDataQualityRuleTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityRuleTemplatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityRuleTemplates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityRuleTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_rule_templates_with_options_async(
        self,
        request: main_models.ListDataQualityRuleTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityRuleTemplatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityRuleTemplates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityRuleTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_rule_templates(
        self,
        request: main_models.ListDataQualityRuleTemplatesRequest,
    ) -> main_models.ListDataQualityRuleTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_rule_templates_with_options(request, runtime)

    async def list_data_quality_rule_templates_async(
        self,
        request: main_models.ListDataQualityRuleTemplatesRequest,
    ) -> main_models.ListDataQualityRuleTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_rule_templates_with_options_async(request, runtime)

    def list_data_quality_rules_with_options(
        self,
        request: main_models.ListDataQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_rules_with_options_async(
        self,
        request: main_models.ListDataQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_rules(
        self,
        request: main_models.ListDataQualityRulesRequest,
    ) -> main_models.ListDataQualityRulesResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_rules_with_options(request, runtime)

    async def list_data_quality_rules_async(
        self,
        request: main_models.ListDataQualityRulesRequest,
    ) -> main_models.ListDataQualityRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_rules_with_options_async(request, runtime)

    def list_data_quality_scan_runs_with_options(
        self,
        tmp_req: main_models.ListDataQualityScanRunsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityScanRunsResponse:
        tmp_req.validate()
        request = main_models.ListDataQualityScanRunsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_from):
            query['CreateTimeFrom'] = request.create_time_from
        if not DaraCore.is_null(request.create_time_to):
            query['CreateTimeTo'] = request.create_time_to
        if not DaraCore.is_null(request.data_quality_scan_id):
            query['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityScanRuns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityScanRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_scan_runs_with_options_async(
        self,
        tmp_req: main_models.ListDataQualityScanRunsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityScanRunsResponse:
        tmp_req.validate()
        request = main_models.ListDataQualityScanRunsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_from):
            query['CreateTimeFrom'] = request.create_time_from
        if not DaraCore.is_null(request.create_time_to):
            query['CreateTimeTo'] = request.create_time_to
        if not DaraCore.is_null(request.data_quality_scan_id):
            query['DataQualityScanId'] = request.data_quality_scan_id
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityScanRuns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityScanRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_scan_runs(
        self,
        request: main_models.ListDataQualityScanRunsRequest,
    ) -> main_models.ListDataQualityScanRunsResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_scan_runs_with_options(request, runtime)

    async def list_data_quality_scan_runs_async(
        self,
        request: main_models.ListDataQualityScanRunsRequest,
    ) -> main_models.ListDataQualityScanRunsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_scan_runs_with_options_async(request, runtime)

    def list_data_quality_scans_with_options(
        self,
        request: main_models.ListDataQualityScansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityScansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityScans',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityScansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_scans_with_options_async(
        self,
        request: main_models.ListDataQualityScansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityScansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityScans',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityScansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_scans(
        self,
        request: main_models.ListDataQualityScansRequest,
    ) -> main_models.ListDataQualityScansResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_scans_with_options(request, runtime)

    async def list_data_quality_scans_async(
        self,
        request: main_models.ListDataQualityScansRequest,
    ) -> main_models.ListDataQualityScansResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_scans_with_options_async(request, runtime)

    def list_data_quality_templates_with_options(
        self,
        request: main_models.ListDataQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityTemplates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_quality_templates_with_options_async(
        self,
        request: main_models.ListDataQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataQualityTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataQualityTemplates',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataQualityTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_quality_templates(
        self,
        request: main_models.ListDataQualityTemplatesRequest,
    ) -> main_models.ListDataQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_data_quality_templates_with_options(request, runtime)

    async def list_data_quality_templates_async(
        self,
        request: main_models.ListDataQualityTemplatesRequest,
    ) -> main_models.ListDataQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_quality_templates_with_options_async(request, runtime)

    def list_data_source_shared_rules_with_options(
        self,
        request: main_models.ListDataSourceSharedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceSharedRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceSharedRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceSharedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_shared_rules_with_options_async(
        self,
        request: main_models.ListDataSourceSharedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceSharedRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceSharedRules',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceSharedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_shared_rules(
        self,
        request: main_models.ListDataSourceSharedRulesRequest,
    ) -> main_models.ListDataSourceSharedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_shared_rules_with_options(request, runtime)

    async def list_data_source_shared_rules_async(
        self,
        request: main_models.ListDataSourceSharedRulesRequest,
    ) -> main_models.ListDataSourceSharedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_shared_rules_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        tmp_req: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        tmp_req: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: main_models.ListDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: main_models.ListDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    async def list_databases_async(
        self,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.list_databases_with_options_async(request, runtime)

    def list_dataset_versions_with_options(
        self,
        request: main_models.ListDatasetVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetVersions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_versions_with_options_async(
        self,
        request: main_models.ListDatasetVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetVersions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_versions(
        self,
        request: main_models.ListDatasetVersionsRequest,
    ) -> main_models.ListDatasetVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_dataset_versions_with_options(request, runtime)

    async def list_dataset_versions_async(
        self,
        request: main_models.ListDatasetVersionsRequest,
    ) -> main_models.ListDatasetVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_dataset_versions_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        tmp_req: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        tmp_req.validate()
        request = main_models.ListDatasetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_type_list):
            request.data_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_type_list, 'DataTypeList', 'simple')
        if not DaraCore.is_null(tmp_req.storage_type_list):
            request.storage_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_type_list, 'StorageTypeList', 'simple')
        body = {}
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.data_type_list_shrink):
            body['DataTypeList'] = request.data_type_list_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.storage_type_list_shrink):
            body['StorageTypeList'] = request.storage_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        tmp_req: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        tmp_req.validate()
        request = main_models.ListDatasetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_type_list):
            request.data_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_type_list, 'DataTypeList', 'simple')
        if not DaraCore.is_null(tmp_req.storage_type_list):
            request.storage_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_type_list, 'StorageTypeList', 'simple')
        body = {}
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.data_type_list_shrink):
            body['DataTypeList'] = request.data_type_list_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.storage_type_list_shrink):
            body['StorageTypeList'] = request.storage_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_deployment_package_files_with_options(
        self,
        tmp_req: main_models.ListDeploymentPackageFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentPackageFilesResponse:
        tmp_req.validate()
        request = main_models.ListDeploymentPackageFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.change_type):
            query['ChangeType'] = request.change_type
        if not DaraCore.is_null(request.commit_from):
            query['CommitFrom'] = request.commit_from
        if not DaraCore.is_null(request.commit_to):
            query['CommitTo'] = request.commit_to
        if not DaraCore.is_null(request.commit_user_id):
            query['CommitUserId'] = request.commit_user_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentPackageFiles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentPackageFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_package_files_with_options_async(
        self,
        tmp_req: main_models.ListDeploymentPackageFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentPackageFilesResponse:
        tmp_req.validate()
        request = main_models.ListDeploymentPackageFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_ids):
            request.file_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.change_type):
            query['ChangeType'] = request.change_type
        if not DaraCore.is_null(request.commit_from):
            query['CommitFrom'] = request.commit_from
        if not DaraCore.is_null(request.commit_to):
            query['CommitTo'] = request.commit_to
        if not DaraCore.is_null(request.commit_user_id):
            query['CommitUserId'] = request.commit_user_id
        if not DaraCore.is_null(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentPackageFiles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentPackageFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_package_files(
        self,
        request: main_models.ListDeploymentPackageFilesRequest,
    ) -> main_models.ListDeploymentPackageFilesResponse:
        runtime = RuntimeOptions()
        return self.list_deployment_package_files_with_options(request, runtime)

    async def list_deployment_package_files_async(
        self,
        request: main_models.ListDeploymentPackageFilesRequest,
    ) -> main_models.ListDeploymentPackageFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_deployment_package_files_with_options_async(request, runtime)

    def list_deployment_packages_with_options(
        self,
        request: main_models.ListDeploymentPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentPackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator):
            body['Creator'] = request.creator
        if not DaraCore.is_null(request.end_create_time):
            body['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.end_execute_time):
            body['EndExecuteTime'] = request.end_execute_time
        if not DaraCore.is_null(request.executor):
            body['Executor'] = request.executor
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentPackages',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_packages_with_options_async(
        self,
        request: main_models.ListDeploymentPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentPackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator):
            body['Creator'] = request.creator
        if not DaraCore.is_null(request.end_create_time):
            body['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.end_execute_time):
            body['EndExecuteTime'] = request.end_execute_time
        if not DaraCore.is_null(request.executor):
            body['Executor'] = request.executor
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentPackages',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_packages(
        self,
        request: main_models.ListDeploymentPackagesRequest,
    ) -> main_models.ListDeploymentPackagesResponse:
        runtime = RuntimeOptions()
        return self.list_deployment_packages_with_options(request, runtime)

    async def list_deployment_packages_async(
        self,
        request: main_models.ListDeploymentPackagesRequest,
    ) -> main_models.ListDeploymentPackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_deployment_packages_with_options_async(request, runtime)

    def list_downstream_task_instances_with_options(
        self,
        request: main_models.ListDownstreamTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_downstream_task_instances_with_options_async(
        self,
        request: main_models.ListDownstreamTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_downstream_task_instances(
        self,
        request: main_models.ListDownstreamTaskInstancesRequest,
    ) -> main_models.ListDownstreamTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_downstream_task_instances_with_options(request, runtime)

    async def list_downstream_task_instances_async(
        self,
        request: main_models.ListDownstreamTaskInstancesRequest,
    ) -> main_models.ListDownstreamTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_downstream_task_instances_with_options_async(request, runtime)

    def list_downstream_tasks_with_options(
        self,
        request: main_models.ListDownstreamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_downstream_tasks_with_options_async(
        self,
        request: main_models.ListDownstreamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_downstream_tasks(
        self,
        request: main_models.ListDownstreamTasksRequest,
    ) -> main_models.ListDownstreamTasksResponse:
        runtime = RuntimeOptions()
        return self.list_downstream_tasks_with_options(request, runtime)

    async def list_downstream_tasks_async(
        self,
        request: main_models.ListDownstreamTasksRequest,
    ) -> main_models.ListDownstreamTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_downstream_tasks_with_options_async(request, runtime)

    def list_entities_in_meta_collection_with_options(
        self,
        request: main_models.ListEntitiesInMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesInMetaCollectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEntitiesInMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesInMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_in_meta_collection_with_options_async(
        self,
        request: main_models.ListEntitiesInMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesInMetaCollectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEntitiesInMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesInMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities_in_meta_collection(
        self,
        request: main_models.ListEntitiesInMetaCollectionRequest,
    ) -> main_models.ListEntitiesInMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.list_entities_in_meta_collection_with_options(request, runtime)

    async def list_entities_in_meta_collection_async(
        self,
        request: main_models.ListEntitiesInMetaCollectionRequest,
    ) -> main_models.ListEntitiesInMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.list_entities_in_meta_collection_with_options_async(request, runtime)

    def list_file_versions_with_options(
        self,
        request: main_models.ListFileVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFileVersions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_versions_with_options_async(
        self,
        request: main_models.ListFileVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFileVersions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_versions(
        self,
        request: main_models.ListFileVersionsRequest,
    ) -> main_models.ListFileVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    async def list_file_versions_async(
        self,
        request: main_models.ListFileVersionsRequest,
    ) -> main_models.ListFileVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_file_versions_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.commit_status):
            body['CommitStatus'] = request.commit_status
        if not DaraCore.is_null(request.exact_file_name):
            body['ExactFileName'] = request.exact_file_name
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id_in):
            body['FileIdIn'] = request.file_id_in
        if not DaraCore.is_null(request.file_types):
            body['FileTypes'] = request.file_types
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.last_edit_user):
            body['LastEditUser'] = request.last_edit_user
        if not DaraCore.is_null(request.need_absolute_folder_path):
            body['NeedAbsoluteFolderPath'] = request.need_absolute_folder_path
        if not DaraCore.is_null(request.need_content):
            body['NeedContent'] = request.need_content
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.commit_status):
            body['CommitStatus'] = request.commit_status
        if not DaraCore.is_null(request.exact_file_name):
            body['ExactFileName'] = request.exact_file_name
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id_in):
            body['FileIdIn'] = request.file_id_in
        if not DaraCore.is_null(request.file_types):
            body['FileTypes'] = request.file_types
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.last_edit_user):
            body['LastEditUser'] = request.last_edit_user
        if not DaraCore.is_null(request.need_absolute_folder_path):
            body['NeedAbsoluteFolderPath'] = request.need_absolute_folder_path
        if not DaraCore.is_null(request.need_content):
            body['NeedContent'] = request.need_content
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_folders_with_options(
        self,
        request: main_models.ListFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFoldersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_path):
            body['ParentFolderPath'] = request.parent_folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFolders',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFoldersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_folders_with_options_async(
        self,
        request: main_models.ListFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFoldersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_path):
            body['ParentFolderPath'] = request.parent_folder_path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFolders',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFoldersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_folders(
        self,
        request: main_models.ListFoldersRequest,
    ) -> main_models.ListFoldersResponse:
        runtime = RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    async def list_folders_async(
        self,
        request: main_models.ListFoldersRequest,
    ) -> main_models.ListFoldersResponse:
        runtime = RuntimeOptions()
        return await self.list_folders_with_options_async(request, runtime)

    def list_functions_with_options(
        self,
        request: main_models.ListFunctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        request: main_models.ListFunctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        return self.list_functions_with_options(request, runtime)

    async def list_functions_async(
        self,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        return await self.list_functions_with_options_async(request, runtime)

    def list_lineage_relationships_with_options(
        self,
        request: main_models.ListLineageRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLineageRelationshipsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLineageRelationships',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLineageRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lineage_relationships_with_options_async(
        self,
        request: main_models.ListLineageRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLineageRelationshipsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLineageRelationships',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLineageRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lineage_relationships(
        self,
        request: main_models.ListLineageRelationshipsRequest,
    ) -> main_models.ListLineageRelationshipsResponse:
        runtime = RuntimeOptions()
        return self.list_lineage_relationships_with_options(request, runtime)

    async def list_lineage_relationships_async(
        self,
        request: main_models.ListLineageRelationshipsRequest,
    ) -> main_models.ListLineageRelationshipsResponse:
        runtime = RuntimeOptions()
        return await self.list_lineage_relationships_with_options_async(request, runtime)

    def list_lineages_with_options(
        self,
        request: main_models.ListLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLineagesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLineages',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lineages_with_options_async(
        self,
        request: main_models.ListLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLineagesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLineages',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lineages(
        self,
        request: main_models.ListLineagesRequest,
    ) -> main_models.ListLineagesResponse:
        runtime = RuntimeOptions()
        return self.list_lineages_with_options(request, runtime)

    async def list_lineages_async(
        self,
        request: main_models.ListLineagesRequest,
    ) -> main_models.ListLineagesResponse:
        runtime = RuntimeOptions()
        return await self.list_lineages_with_options_async(request, runtime)

    def list_meta_collections_with_options(
        self,
        request: main_models.ListMetaCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMetaCollectionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetaCollections',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetaCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_meta_collections_with_options_async(
        self,
        request: main_models.ListMetaCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMetaCollectionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetaCollections',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetaCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_meta_collections(
        self,
        request: main_models.ListMetaCollectionsRequest,
    ) -> main_models.ListMetaCollectionsResponse:
        runtime = RuntimeOptions()
        return self.list_meta_collections_with_options(request, runtime)

    async def list_meta_collections_async(
        self,
        request: main_models.ListMetaCollectionsRequest,
    ) -> main_models.ListMetaCollectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_meta_collections_with_options_async(request, runtime)

    def list_networks_with_options(
        self,
        request: main_models.ListNetworksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_networks_with_options_async(
        self,
        request: main_models.ListNetworksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_networks(
        self,
        request: main_models.ListNetworksRequest,
    ) -> main_models.ListNetworksResponse:
        runtime = RuntimeOptions()
        return self.list_networks_with_options(request, runtime)

    async def list_networks_async(
        self,
        request: main_models.ListNetworksRequest,
    ) -> main_models.ListNetworksResponse:
        runtime = RuntimeOptions()
        return await self.list_networks_with_options_async(request, runtime)

    def list_node_dependencies_with_options(
        self,
        request: main_models.ListNodeDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeDependenciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeDependencies',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_dependencies_with_options_async(
        self,
        request: main_models.ListNodeDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeDependenciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeDependencies',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_dependencies(
        self,
        request: main_models.ListNodeDependenciesRequest,
    ) -> main_models.ListNodeDependenciesResponse:
        runtime = RuntimeOptions()
        return self.list_node_dependencies_with_options(request, runtime)

    async def list_node_dependencies_async(
        self,
        request: main_models.ListNodeDependenciesRequest,
    ) -> main_models.ListNodeDependenciesResponse:
        runtime = RuntimeOptions()
        return await self.list_node_dependencies_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_partitions_with_options(
        self,
        request: main_models.ListPartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partitions_with_options_async(
        self,
        request: main_models.ListPartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partitions(
        self,
        request: main_models.ListPartitionsRequest,
    ) -> main_models.ListPartitionsResponse:
        runtime = RuntimeOptions()
        return self.list_partitions_with_options(request, runtime)

    async def list_partitions_async(
        self,
        request: main_models.ListPartitionsRequest,
    ) -> main_models.ListPartitionsResponse:
        runtime = RuntimeOptions()
        return await self.list_partitions_with_options_async(request, runtime)

    def list_pipeline_run_items_with_options(
        self,
        request: main_models.ListPipelineRunItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineRunItemsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineRunItems',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineRunItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_run_items_with_options_async(
        self,
        request: main_models.ListPipelineRunItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineRunItemsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineRunItems',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineRunItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_run_items(
        self,
        request: main_models.ListPipelineRunItemsRequest,
    ) -> main_models.ListPipelineRunItemsResponse:
        runtime = RuntimeOptions()
        return self.list_pipeline_run_items_with_options(request, runtime)

    async def list_pipeline_run_items_async(
        self,
        request: main_models.ListPipelineRunItemsRequest,
    ) -> main_models.ListPipelineRunItemsResponse:
        runtime = RuntimeOptions()
        return await self.list_pipeline_run_items_with_options_async(request, runtime)

    def list_pipeline_runs_with_options(
        self,
        request: main_models.ListPipelineRunsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineRunsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineRuns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_with_options_async(
        self,
        request: main_models.ListPipelineRunsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineRunsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineRuns',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs(
        self,
        request: main_models.ListPipelineRunsRequest,
    ) -> main_models.ListPipelineRunsResponse:
        runtime = RuntimeOptions()
        return self.list_pipeline_runs_with_options(request, runtime)

    async def list_pipeline_runs_async(
        self,
        request: main_models.ListPipelineRunsRequest,
    ) -> main_models.ListPipelineRunsResponse:
        runtime = RuntimeOptions()
        return await self.list_pipeline_runs_with_options_async(request, runtime)

    def list_project_members_with_options(
        self,
        tmp_req: main_models.ListProjectMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectMembersResponse:
        tmp_req.validate()
        request = main_models.ListProjectMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['UserIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectMembers',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        tmp_req: main_models.ListProjectMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectMembersResponse:
        tmp_req.validate()
        request = main_models.ListProjectMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['UserIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectMembers',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        request: main_models.ListProjectMembersRequest,
    ) -> main_models.ListProjectMembersResponse:
        runtime = RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    async def list_project_members_async(
        self,
        request: main_models.ListProjectMembersRequest,
    ) -> main_models.ListProjectMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_project_members_with_options_async(request, runtime)

    def list_project_roles_with_options(
        self,
        tmp_req: main_models.ListProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectRolesResponse:
        tmp_req.validate()
        request = main_models.ListProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.codes):
            request.codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        if not DaraCore.is_null(tmp_req.names):
            request.names_shrink = Utils.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not DaraCore.is_null(request.codes_shrink):
            body['Codes'] = request.codes_shrink
        if not DaraCore.is_null(request.names_shrink):
            body['Names'] = request.names_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_roles_with_options_async(
        self,
        tmp_req: main_models.ListProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectRolesResponse:
        tmp_req.validate()
        request = main_models.ListProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.codes):
            request.codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        if not DaraCore.is_null(tmp_req.names):
            request.names_shrink = Utils.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not DaraCore.is_null(request.codes_shrink):
            body['Codes'] = request.codes_shrink
        if not DaraCore.is_null(request.names_shrink):
            body['Names'] = request.names_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_roles(
        self,
        request: main_models.ListProjectRolesRequest,
    ) -> main_models.ListProjectRolesResponse:
        runtime = RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    async def list_project_roles_async(
        self,
        request: main_models.ListProjectRolesRequest,
    ) -> main_models.ListProjectRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_project_roles_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.names):
            request.names_shrink = Utils.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.names_shrink):
            body['Names'] = request.names_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.names):
            request.names_shrink = Utils.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.aliyun_resource_tags_shrink):
            body['AliyunResourceTags'] = request.aliyun_resource_tags_shrink
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.names_shrink):
            body['Names'] = request.names_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_resource_group_associate_projects_with_options(
        self,
        request: main_models.ListResourceGroupAssociateProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupAssociateProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupAssociateProjects',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupAssociateProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_associate_projects_with_options_async(
        self,
        request: main_models.ListResourceGroupAssociateProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupAssociateProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupAssociateProjects',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupAssociateProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_associate_projects(
        self,
        request: main_models.ListResourceGroupAssociateProjectsRequest,
    ) -> main_models.ListResourceGroupAssociateProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_group_associate_projects_with_options(request, runtime)

    async def list_resource_group_associate_projects_async(
        self,
        request: main_models.ListResourceGroupAssociateProjectsRequest,
    ) -> main_models.ListResourceGroupAssociateProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_group_associate_projects_with_options_async(request, runtime)

    def list_resource_group_metric_data_with_options(
        self,
        request: main_models.ListResourceGroupMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMetricDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMetricData',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_metric_data_with_options_async(
        self,
        request: main_models.ListResourceGroupMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMetricDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMetricData',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_metric_data(
        self,
        request: main_models.ListResourceGroupMetricDataRequest,
    ) -> main_models.ListResourceGroupMetricDataResponse:
        runtime = RuntimeOptions()
        return self.list_resource_group_metric_data_with_options(request, runtime)

    async def list_resource_group_metric_data_async(
        self,
        request: main_models.ListResourceGroupMetricDataRequest,
    ) -> main_models.ListResourceGroupMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_group_metric_data_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        tmp_req: main_models.ListResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        tmp_req.validate()
        request = main_models.ListResourceGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_types):
            request.resource_group_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_types, 'ResourceGroupTypes', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        tmp_req: main_models.ListResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        tmp_req.validate()
        request = main_models.ListResourceGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aliyun_resource_tags):
            request.aliyun_resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.aliyun_resource_tags, 'AliyunResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_types):
            request.resource_group_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_types, 'ResourceGroupTypes', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: main_models.ListResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: main_models.ListResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_routes_with_options(
        self,
        request: main_models.ListRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRoutesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoutes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_routes_with_options_async(
        self,
        request: main_models.ListRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRoutesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoutes',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_routes(
        self,
        request: main_models.ListRoutesRequest,
    ) -> main_models.ListRoutesResponse:
        runtime = RuntimeOptions()
        return self.list_routes_with_options(request, runtime)

    async def list_routes_async(
        self,
        request: main_models.ListRoutesRequest,
    ) -> main_models.ListRoutesResponse:
        runtime = RuntimeOptions()
        return await self.list_routes_with_options_async(request, runtime)

    def list_schemas_with_options(
        self,
        tmp_req: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        tmp_req.validate()
        request = main_models.ListSchemasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schemas_with_options_async(
        self,
        tmp_req: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        tmp_req.validate()
        request = main_models.ListSchemasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schemas(
        self,
        request: main_models.ListSchemasRequest,
    ) -> main_models.ListSchemasResponse:
        runtime = RuntimeOptions()
        return self.list_schemas_with_options(request, runtime)

    async def list_schemas_async(
        self,
        request: main_models.ListSchemasRequest,
    ) -> main_models.ListSchemasResponse:
        runtime = RuntimeOptions()
        return await self.list_schemas_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        tmp_req: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        tmp_req.validate()
        request = main_models.ListTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_types):
            request.table_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_types, 'TableTypes', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        tmp_req: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        tmp_req.validate()
        request = main_models.ListTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_types):
            request.table_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_types, 'TableTypes', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    async def list_tables_async(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_tables_with_options_async(request, runtime)

    def list_task_instance_operation_logs_with_options(
        self,
        request: main_models.ListTaskInstanceOperationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskInstanceOperationLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskInstanceOperationLogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskInstanceOperationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_instance_operation_logs_with_options_async(
        self,
        request: main_models.ListTaskInstanceOperationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskInstanceOperationLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskInstanceOperationLogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskInstanceOperationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_instance_operation_logs(
        self,
        request: main_models.ListTaskInstanceOperationLogsRequest,
    ) -> main_models.ListTaskInstanceOperationLogsResponse:
        runtime = RuntimeOptions()
        return self.list_task_instance_operation_logs_with_options(request, runtime)

    async def list_task_instance_operation_logs_async(
        self,
        request: main_models.ListTaskInstanceOperationLogsRequest,
    ) -> main_models.ListTaskInstanceOperationLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_task_instance_operation_logs_with_options_async(request, runtime)

    def list_task_instances_with_options(
        self,
        tmp_req: main_models.ListTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.ListTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        body = {}
        if not DaraCore.is_null(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_ids_shrink):
            body['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.unified_workflow_instance_id):
            body['UnifiedWorkflowInstanceId'] = request.unified_workflow_instance_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_instance_id):
            body['WorkflowInstanceId'] = request.workflow_instance_id
        if not DaraCore.is_null(request.workflow_instance_type):
            body['WorkflowInstanceType'] = request.workflow_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_instances_with_options_async(
        self,
        tmp_req: main_models.ListTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.ListTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        body = {}
        if not DaraCore.is_null(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_ids_shrink):
            body['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.unified_workflow_instance_id):
            body['UnifiedWorkflowInstanceId'] = request.unified_workflow_instance_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_instance_id):
            body['WorkflowInstanceId'] = request.workflow_instance_id
        if not DaraCore.is_null(request.workflow_instance_type):
            body['WorkflowInstanceType'] = request.workflow_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_instances(
        self,
        request: main_models.ListTaskInstancesRequest,
    ) -> main_models.ListTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_task_instances_with_options(request, runtime)

    async def list_task_instances_async(
        self,
        request: main_models.ListTaskInstancesRequest,
    ) -> main_models.ListTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_task_instances_with_options_async(request, runtime)

    def list_task_operation_logs_with_options(
        self,
        request: main_models.ListTaskOperationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskOperationLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskOperationLogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskOperationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_operation_logs_with_options_async(
        self,
        request: main_models.ListTaskOperationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskOperationLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskOperationLogs',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskOperationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_operation_logs(
        self,
        request: main_models.ListTaskOperationLogsRequest,
    ) -> main_models.ListTaskOperationLogsResponse:
        runtime = RuntimeOptions()
        return self.list_task_operation_logs_with_options(request, runtime)

    async def list_task_operation_logs_async(
        self,
        request: main_models.ListTaskOperationLogsRequest,
    ) -> main_models.ListTaskOperationLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_task_operation_logs_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource):
            body['RuntimeResource'] = request.runtime_resource
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.trigger_recurrence):
            body['TriggerRecurrence'] = request.trigger_recurrence
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_upstream_task_instances_with_options(
        self,
        request: main_models.ListUpstreamTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upstream_task_instances_with_options_async(
        self,
        request: main_models.ListUpstreamTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamTaskInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upstream_task_instances(
        self,
        request: main_models.ListUpstreamTaskInstancesRequest,
    ) -> main_models.ListUpstreamTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_upstream_task_instances_with_options(request, runtime)

    async def list_upstream_task_instances_async(
        self,
        request: main_models.ListUpstreamTaskInstancesRequest,
    ) -> main_models.ListUpstreamTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_upstream_task_instances_with_options_async(request, runtime)

    def list_upstream_tasks_with_options(
        self,
        request: main_models.ListUpstreamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upstream_tasks_with_options_async(
        self,
        request: main_models.ListUpstreamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamTasks',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upstream_tasks(
        self,
        request: main_models.ListUpstreamTasksRequest,
    ) -> main_models.ListUpstreamTasksResponse:
        runtime = RuntimeOptions()
        return self.list_upstream_tasks_with_options(request, runtime)

    async def list_upstream_tasks_async(
        self,
        request: main_models.ListUpstreamTasksRequest,
    ) -> main_models.ListUpstreamTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_upstream_tasks_with_options_async(request, runtime)

    def list_workflow_definitions_with_options(
        self,
        request: main_models.ListWorkflowDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowDefinitionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowDefinitions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_definitions_with_options_async(
        self,
        request: main_models.ListWorkflowDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowDefinitionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowDefinitions',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_definitions(
        self,
        request: main_models.ListWorkflowDefinitionsRequest,
    ) -> main_models.ListWorkflowDefinitionsResponse:
        runtime = RuntimeOptions()
        return self.list_workflow_definitions_with_options(request, runtime)

    async def list_workflow_definitions_async(
        self,
        request: main_models.ListWorkflowDefinitionsRequest,
    ) -> main_models.ListWorkflowDefinitionsResponse:
        runtime = RuntimeOptions()
        return await self.list_workflow_definitions_with_options_async(request, runtime)

    def list_workflow_instances_with_options(
        self,
        tmp_req: main_models.ListWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.ListWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_date):
            body['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unified_workflow_instance_id):
            body['UnifiedWorkflowInstanceId'] = request.unified_workflow_instance_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_instances_with_options_async(
        self,
        tmp_req: main_models.ListWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.ListWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_date):
            body['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unified_workflow_instance_id):
            body['UnifiedWorkflowInstanceId'] = request.unified_workflow_instance_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_instances(
        self,
        request: main_models.ListWorkflowInstancesRequest,
    ) -> main_models.ListWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_workflow_instances_with_options(request, runtime)

    async def list_workflow_instances_async(
        self,
        request: main_models.ListWorkflowInstancesRequest,
    ) -> main_models.ListWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_workflow_instances_with_options_async(request, runtime)

    def list_workflows_with_options(
        self,
        tmp_req: main_models.ListWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowsResponse:
        tmp_req.validate()
        request = main_models.ListWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflows',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflows_with_options_async(
        self,
        tmp_req: main_models.ListWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowsResponse:
        tmp_req.validate()
        request = main_models.ListWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            body['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.trigger_type):
            body['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflows',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflows(
        self,
        request: main_models.ListWorkflowsRequest,
    ) -> main_models.ListWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.list_workflows_with_options(request, runtime)

    async def list_workflows_async(
        self,
        request: main_models.ListWorkflowsRequest,
    ) -> main_models.ListWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.list_workflows_with_options_async(request, runtime)

    def move_function_with_options(
        self,
        request: main_models.MoveFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_function_with_options_async(
        self,
        request: main_models.MoveFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_function(
        self,
        request: main_models.MoveFunctionRequest,
    ) -> main_models.MoveFunctionResponse:
        runtime = RuntimeOptions()
        return self.move_function_with_options(request, runtime)

    async def move_function_async(
        self,
        request: main_models.MoveFunctionRequest,
    ) -> main_models.MoveFunctionResponse:
        runtime = RuntimeOptions()
        return await self.move_function_with_options_async(request, runtime)

    def move_node_with_options(
        self,
        request: main_models.MoveNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_node_with_options_async(
        self,
        request: main_models.MoveNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_node(
        self,
        request: main_models.MoveNodeRequest,
    ) -> main_models.MoveNodeResponse:
        runtime = RuntimeOptions()
        return self.move_node_with_options(request, runtime)

    async def move_node_async(
        self,
        request: main_models.MoveNodeRequest,
    ) -> main_models.MoveNodeResponse:
        runtime = RuntimeOptions()
        return await self.move_node_with_options_async(request, runtime)

    def move_resource_with_options(
        self,
        request: main_models.MoveResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_with_options_async(
        self,
        request: main_models.MoveResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource(
        self,
        request: main_models.MoveResourceRequest,
    ) -> main_models.MoveResourceResponse:
        runtime = RuntimeOptions()
        return self.move_resource_with_options(request, runtime)

    async def move_resource_async(
        self,
        request: main_models.MoveResourceRequest,
    ) -> main_models.MoveResourceResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_with_options_async(request, runtime)

    def move_workflow_definition_with_options(
        self,
        request: main_models.MoveWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_workflow_definition_with_options_async(
        self,
        request: main_models.MoveWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_workflow_definition(
        self,
        request: main_models.MoveWorkflowDefinitionRequest,
    ) -> main_models.MoveWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.move_workflow_definition_with_options(request, runtime)

    async def move_workflow_definition_async(
        self,
        request: main_models.MoveWorkflowDefinitionRequest,
    ) -> main_models.MoveWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.move_workflow_definition_with_options_async(request, runtime)

    def preview_dataset_version_with_options(
        self,
        request: main_models.PreviewDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_dataset_version_with_options_async(
        self,
        request: main_models.PreviewDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewDatasetVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_dataset_version(
        self,
        request: main_models.PreviewDatasetVersionRequest,
    ) -> main_models.PreviewDatasetVersionResponse:
        runtime = RuntimeOptions()
        return self.preview_dataset_version_with_options(request, runtime)

    async def preview_dataset_version_async(
        self,
        request: main_models.PreviewDatasetVersionRequest,
    ) -> main_models.PreviewDatasetVersionResponse:
        runtime = RuntimeOptions()
        return await self.preview_dataset_version_with_options_async(request, runtime)

    def remove_entity_from_meta_collection_with_options(
        self,
        request: main_models.RemoveEntityFromMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEntityFromMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.meta_collection_id):
            query['MetaCollectionId'] = request.meta_collection_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntityFromMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEntityFromMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_entity_from_meta_collection_with_options_async(
        self,
        request: main_models.RemoveEntityFromMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEntityFromMetaCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.meta_collection_id):
            query['MetaCollectionId'] = request.meta_collection_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntityFromMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEntityFromMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_entity_from_meta_collection(
        self,
        request: main_models.RemoveEntityFromMetaCollectionRequest,
    ) -> main_models.RemoveEntityFromMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.remove_entity_from_meta_collection_with_options(request, runtime)

    async def remove_entity_from_meta_collection_async(
        self,
        request: main_models.RemoveEntityFromMetaCollectionRequest,
    ) -> main_models.RemoveEntityFromMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.remove_entity_from_meta_collection_with_options_async(request, runtime)

    def remove_task_instance_dependencies_with_options(
        self,
        tmp_req: main_models.RemoveTaskInstanceDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTaskInstanceDependenciesResponse:
        tmp_req.validate()
        request = main_models.RemoveTaskInstanceDependenciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upstream_task_instance_ids):
            request.upstream_task_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.upstream_task_instance_ids, 'UpstreamTaskInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.upstream_task_instance_ids_shrink):
            body['UpstreamTaskInstanceIds'] = request.upstream_task_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTaskInstanceDependencies',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTaskInstanceDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_task_instance_dependencies_with_options_async(
        self,
        tmp_req: main_models.RemoveTaskInstanceDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTaskInstanceDependenciesResponse:
        tmp_req.validate()
        request = main_models.RemoveTaskInstanceDependenciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upstream_task_instance_ids):
            request.upstream_task_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.upstream_task_instance_ids, 'UpstreamTaskInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.upstream_task_instance_ids_shrink):
            body['UpstreamTaskInstanceIds'] = request.upstream_task_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTaskInstanceDependencies',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTaskInstanceDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_task_instance_dependencies(
        self,
        request: main_models.RemoveTaskInstanceDependenciesRequest,
    ) -> main_models.RemoveTaskInstanceDependenciesResponse:
        runtime = RuntimeOptions()
        return self.remove_task_instance_dependencies_with_options(request, runtime)

    async def remove_task_instance_dependencies_async(
        self,
        request: main_models.RemoveTaskInstanceDependenciesRequest,
    ) -> main_models.RemoveTaskInstanceDependenciesResponse:
        runtime = RuntimeOptions()
        return await self.remove_task_instance_dependencies_with_options_async(request, runtime)

    def rename_function_with_options(
        self,
        request: main_models.RenameFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_function_with_options_async(
        self,
        request: main_models.RenameFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_function(
        self,
        request: main_models.RenameFunctionRequest,
    ) -> main_models.RenameFunctionResponse:
        runtime = RuntimeOptions()
        return self.rename_function_with_options(request, runtime)

    async def rename_function_async(
        self,
        request: main_models.RenameFunctionRequest,
    ) -> main_models.RenameFunctionResponse:
        runtime = RuntimeOptions()
        return await self.rename_function_with_options_async(request, runtime)

    def rename_node_with_options(
        self,
        request: main_models.RenameNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_node_with_options_async(
        self,
        request: main_models.RenameNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_node(
        self,
        request: main_models.RenameNodeRequest,
    ) -> main_models.RenameNodeResponse:
        runtime = RuntimeOptions()
        return self.rename_node_with_options(request, runtime)

    async def rename_node_async(
        self,
        request: main_models.RenameNodeRequest,
    ) -> main_models.RenameNodeResponse:
        runtime = RuntimeOptions()
        return await self.rename_node_with_options_async(request, runtime)

    def rename_resource_with_options(
        self,
        request: main_models.RenameResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_resource_with_options_async(
        self,
        request: main_models.RenameResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_resource(
        self,
        request: main_models.RenameResourceRequest,
    ) -> main_models.RenameResourceResponse:
        runtime = RuntimeOptions()
        return self.rename_resource_with_options(request, runtime)

    async def rename_resource_async(
        self,
        request: main_models.RenameResourceRequest,
    ) -> main_models.RenameResourceResponse:
        runtime = RuntimeOptions()
        return await self.rename_resource_with_options_async(request, runtime)

    def rename_workflow_definition_with_options(
        self,
        request: main_models.RenameWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameWorkflowDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenameWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_workflow_definition_with_options_async(
        self,
        request: main_models.RenameWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenameWorkflowDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenameWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_workflow_definition(
        self,
        request: main_models.RenameWorkflowDefinitionRequest,
    ) -> main_models.RenameWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.rename_workflow_definition_with_options(request, runtime)

    async def rename_workflow_definition_async(
        self,
        request: main_models.RenameWorkflowDefinitionRequest,
    ) -> main_models.RenameWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.rename_workflow_definition_with_options_async(request, runtime)

    def rerun_task_instances_with_options(
        self,
        tmp_req: main_models.RerunTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.RerunTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_task_instances_with_options_async(
        self,
        tmp_req: main_models.RerunTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.RerunTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_task_instances(
        self,
        request: main_models.RerunTaskInstancesRequest,
    ) -> main_models.RerunTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.rerun_task_instances_with_options(request, runtime)

    async def rerun_task_instances_async(
        self,
        request: main_models.RerunTaskInstancesRequest,
    ) -> main_models.RerunTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.rerun_task_instances_with_options_async(request, runtime)

    def rerun_workflow_instances_with_options(
        self,
        tmp_req: main_models.RerunWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.RerunWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not DaraCore.is_null(request.end_trigger_time):
            body['EndTriggerTime'] = request.end_trigger_time
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_trigger_time):
            body['StartTriggerTime'] = request.start_trigger_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_workflow_instances_with_options_async(
        self,
        tmp_req: main_models.RerunWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.RerunWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not DaraCore.is_null(request.end_trigger_time):
            body['EndTriggerTime'] = request.end_trigger_time
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_trigger_time):
            body['StartTriggerTime'] = request.start_trigger_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_workflow_instances(
        self,
        request: main_models.RerunWorkflowInstancesRequest,
    ) -> main_models.RerunWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return self.rerun_workflow_instances_with_options(request, runtime)

    async def rerun_workflow_instances_async(
        self,
        request: main_models.RerunWorkflowInstancesRequest,
    ) -> main_models.RerunWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return await self.rerun_workflow_instances_with_options_async(request, runtime)

    def resume_task_instances_with_options(
        self,
        tmp_req: main_models.ResumeTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.ResumeTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_instances_with_options_async(
        self,
        tmp_req: main_models.ResumeTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.ResumeTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task_instances(
        self,
        request: main_models.ResumeTaskInstancesRequest,
    ) -> main_models.ResumeTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.resume_task_instances_with_options(request, runtime)

    async def resume_task_instances_async(
        self,
        request: main_models.ResumeTaskInstancesRequest,
    ) -> main_models.ResumeTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.resume_task_instances_with_options_async(request, runtime)

    def revoke_member_project_roles_with_options(
        self,
        tmp_req: main_models.RevokeMemberProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeMemberProjectRolesResponse:
        tmp_req.validate()
        request = main_models.RevokeMemberProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeMemberProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeMemberProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_member_project_roles_with_options_async(
        self,
        tmp_req: main_models.RevokeMemberProjectRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeMemberProjectRolesResponse:
        tmp_req.validate()
        request = main_models.RevokeMemberProjectRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'RoleCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.role_codes_shrink):
            body['RoleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeMemberProjectRoles',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeMemberProjectRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_member_project_roles(
        self,
        request: main_models.RevokeMemberProjectRolesRequest,
    ) -> main_models.RevokeMemberProjectRolesResponse:
        runtime = RuntimeOptions()
        return self.revoke_member_project_roles_with_options(request, runtime)

    async def revoke_member_project_roles_async(
        self,
        request: main_models.RevokeMemberProjectRolesRequest,
    ) -> main_models.RevokeMemberProjectRolesResponse:
        runtime = RuntimeOptions()
        return await self.revoke_member_project_roles_with_options_async(request, runtime)

    def set_success_task_instances_with_options(
        self,
        tmp_req: main_models.SetSuccessTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSuccessTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.SetSuccessTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSuccessTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSuccessTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_success_task_instances_with_options_async(
        self,
        tmp_req: main_models.SetSuccessTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSuccessTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.SetSuccessTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSuccessTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSuccessTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_success_task_instances(
        self,
        request: main_models.SetSuccessTaskInstancesRequest,
    ) -> main_models.SetSuccessTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.set_success_task_instances_with_options(request, runtime)

    async def set_success_task_instances_async(
        self,
        request: main_models.SetSuccessTaskInstancesRequest,
    ) -> main_models.SetSuccessTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.set_success_task_instances_with_options_async(request, runtime)

    def start_dijob_with_options(
        self,
        tmp_req: main_models.StartDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDIJobResponse:
        tmp_req.validate()
        request = main_models.StartDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.realtime_start_settings):
            request.realtime_start_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.realtime_start_settings, 'RealtimeStartSettings', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dijob_with_options_async(
        self,
        tmp_req: main_models.StartDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDIJobResponse:
        tmp_req.validate()
        request = main_models.StartDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.realtime_start_settings):
            request.realtime_start_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.realtime_start_settings, 'RealtimeStartSettings', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dijob(
        self,
        request: main_models.StartDIJobRequest,
    ) -> main_models.StartDIJobResponse:
        runtime = RuntimeOptions()
        return self.start_dijob_with_options(request, runtime)

    async def start_dijob_async(
        self,
        request: main_models.StartDIJobRequest,
    ) -> main_models.StartDIJobResponse:
        runtime = RuntimeOptions()
        return await self.start_dijob_with_options_async(request, runtime)

    def start_workflow_instances_with_options(
        self,
        tmp_req: main_models.StartWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.StartWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_workflow_instances_with_options_async(
        self,
        tmp_req: main_models.StartWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.StartWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_workflow_instances(
        self,
        request: main_models.StartWorkflowInstancesRequest,
    ) -> main_models.StartWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return self.start_workflow_instances_with_options(request, runtime)

    async def start_workflow_instances_async(
        self,
        request: main_models.StartWorkflowInstancesRequest,
    ) -> main_models.StartWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return await self.start_workflow_instances_with_options_async(request, runtime)

    def stop_dijob_with_options(
        self,
        request: main_models.StopDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dijob_with_options_async(
        self,
        request: main_models.StopDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDIJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dijob(
        self,
        request: main_models.StopDIJobRequest,
    ) -> main_models.StopDIJobResponse:
        runtime = RuntimeOptions()
        return self.stop_dijob_with_options(request, runtime)

    async def stop_dijob_async(
        self,
        request: main_models.StopDIJobRequest,
    ) -> main_models.StopDIJobResponse:
        runtime = RuntimeOptions()
        return await self.stop_dijob_with_options_async(request, runtime)

    def stop_task_instances_with_options(
        self,
        tmp_req: main_models.StopTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.StopTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_instances_with_options_async(
        self,
        tmp_req: main_models.StopTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.StopTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task_instances(
        self,
        request: main_models.StopTaskInstancesRequest,
    ) -> main_models.StopTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.stop_task_instances_with_options(request, runtime)

    async def stop_task_instances_async(
        self,
        request: main_models.StopTaskInstancesRequest,
    ) -> main_models.StopTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.stop_task_instances_with_options_async(request, runtime)

    def stop_workflow_instances_with_options(
        self,
        tmp_req: main_models.StopWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.StopWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_workflow_instances_with_options_async(
        self,
        tmp_req: main_models.StopWorkflowInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopWorkflowInstancesResponse:
        tmp_req.validate()
        request = main_models.StopWorkflowInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopWorkflowInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_workflow_instances(
        self,
        request: main_models.StopWorkflowInstancesRequest,
    ) -> main_models.StopWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return self.stop_workflow_instances_with_options(request, runtime)

    async def stop_workflow_instances_async(
        self,
        request: main_models.StopWorkflowInstancesRequest,
    ) -> main_models.StopWorkflowInstancesResponse:
        runtime = RuntimeOptions()
        return await self.stop_workflow_instances_with_options_async(request, runtime)

    def submit_file_with_options(
        self,
        request: main_models.SubmitFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.skip_all_deploy_file_extensions):
            body['SkipAllDeployFileExtensions'] = request.skip_all_deploy_file_extensions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_file_with_options_async(
        self,
        request: main_models.SubmitFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.skip_all_deploy_file_extensions):
            body['SkipAllDeployFileExtensions'] = request.skip_all_deploy_file_extensions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_file(
        self,
        request: main_models.SubmitFileRequest,
    ) -> main_models.SubmitFileResponse:
        runtime = RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    async def submit_file_async(
        self,
        request: main_models.SubmitFileRequest,
    ) -> main_models.SubmitFileResponse:
        runtime = RuntimeOptions()
        return await self.submit_file_with_options_async(request, runtime)

    def suspend_task_instances_with_options(
        self,
        tmp_req: main_models.SuspendTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.SuspendTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_task_instances_with_options_async(
        self,
        tmp_req: main_models.SuspendTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.SuspendTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_task_instances(
        self,
        request: main_models.SuspendTaskInstancesRequest,
    ) -> main_models.SuspendTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.suspend_task_instances_with_options(request, runtime)

    async def suspend_task_instances_async(
        self,
        request: main_models.SuspendTaskInstancesRequest,
    ) -> main_models.SuspendTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.suspend_task_instances_with_options_async(request, runtime)

    def tag_data_assets_with_options(
        self,
        tmp_req: main_models.TagDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagDataAssetsResponse:
        tmp_req.validate()
        request = main_models.TagDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_trace_enabled):
            query['AutoTraceEnabled'] = request.auto_trace_enabled
        if not DaraCore.is_null(request.data_asset_ids_shrink):
            query['DataAssetIds'] = request.data_asset_ids_shrink
        if not DaraCore.is_null(request.data_asset_type):
            query['DataAssetType'] = request.data_asset_type
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_data_assets_with_options_async(
        self,
        tmp_req: main_models.TagDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagDataAssetsResponse:
        tmp_req.validate()
        request = main_models.TagDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_trace_enabled):
            query['AutoTraceEnabled'] = request.auto_trace_enabled
        if not DaraCore.is_null(request.data_asset_ids_shrink):
            query['DataAssetIds'] = request.data_asset_ids_shrink
        if not DaraCore.is_null(request.data_asset_type):
            query['DataAssetType'] = request.data_asset_type
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_data_assets(
        self,
        request: main_models.TagDataAssetsRequest,
    ) -> main_models.TagDataAssetsResponse:
        runtime = RuntimeOptions()
        return self.tag_data_assets_with_options(request, runtime)

    async def tag_data_assets_async(
        self,
        request: main_models.TagDataAssetsRequest,
    ) -> main_models.TagDataAssetsResponse:
        runtime = RuntimeOptions()
        return await self.tag_data_assets_with_options_async(request, runtime)

    def test_data_source_connectivity_with_options(
        self,
        request: main_models.TestDataSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestDataSourceConnectivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestDataSourceConnectivity',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestDataSourceConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_data_source_connectivity_with_options_async(
        self,
        request: main_models.TestDataSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestDataSourceConnectivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestDataSourceConnectivity',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestDataSourceConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_data_source_connectivity(
        self,
        request: main_models.TestDataSourceConnectivityRequest,
    ) -> main_models.TestDataSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return self.test_data_source_connectivity_with_options(request, runtime)

    async def test_data_source_connectivity_async(
        self,
        request: main_models.TestDataSourceConnectivityRequest,
    ) -> main_models.TestDataSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return await self.test_data_source_connectivity_with_options_async(request, runtime)

    def trigger_scheduler_task_instance_with_options(
        self,
        request: main_models.TriggerSchedulerTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerSchedulerTaskInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.trigger_time):
            body['TriggerTime'] = request.trigger_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerSchedulerTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerSchedulerTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_scheduler_task_instance_with_options_async(
        self,
        request: main_models.TriggerSchedulerTaskInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerSchedulerTaskInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.trigger_time):
            body['TriggerTime'] = request.trigger_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerSchedulerTaskInstance',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerSchedulerTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_scheduler_task_instance(
        self,
        request: main_models.TriggerSchedulerTaskInstanceRequest,
    ) -> main_models.TriggerSchedulerTaskInstanceResponse:
        runtime = RuntimeOptions()
        return self.trigger_scheduler_task_instance_with_options(request, runtime)

    async def trigger_scheduler_task_instance_async(
        self,
        request: main_models.TriggerSchedulerTaskInstanceRequest,
    ) -> main_models.TriggerSchedulerTaskInstanceResponse:
        runtime = RuntimeOptions()
        return await self.trigger_scheduler_task_instance_with_options_async(request, runtime)

    def un_tag_data_assets_with_options(
        self,
        tmp_req: main_models.UnTagDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagDataAssetsResponse:
        tmp_req.validate()
        request = main_models.UnTagDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.data_asset_ids_shrink):
            query['DataAssetIds'] = request.data_asset_ids_shrink
        if not DaraCore.is_null(request.data_asset_type):
            query['DataAssetType'] = request.data_asset_type
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_data_assets_with_options_async(
        self,
        tmp_req: main_models.UnTagDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagDataAssetsResponse:
        tmp_req.validate()
        request = main_models.UnTagDataAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_asset_ids):
            request.data_asset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_asset_ids, 'DataAssetIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.data_asset_ids_shrink):
            query['DataAssetIds'] = request.data_asset_ids_shrink
        if not DaraCore.is_null(request.data_asset_type):
            query['DataAssetType'] = request.data_asset_type
        if not DaraCore.is_null(request.env_type):
            query['EnvType'] = request.env_type
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagDataAssets',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_data_assets(
        self,
        request: main_models.UnTagDataAssetsRequest,
    ) -> main_models.UnTagDataAssetsResponse:
        runtime = RuntimeOptions()
        return self.un_tag_data_assets_with_options(request, runtime)

    async def un_tag_data_assets_async(
        self,
        request: main_models.UnTagDataAssetsRequest,
    ) -> main_models.UnTagDataAssetsResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_data_assets_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        tmp_req: main_models.UpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.trigger_condition):
            request.trigger_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.trigger_condition):
            request.trigger_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_condition, 'TriggerCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.trigger_condition_shrink):
            query['TriggerCondition'] = request.trigger_condition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_rule(
        self,
        request: main_models.UpdateAlertRuleRequest,
    ) -> main_models.UpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: main_models.UpdateAlertRuleRequest,
    ) -> main_models.UpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_business_with_options(
        self,
        request: main_models.UpdateBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_business_with_options_async(
        self,
        request: main_models.UpdateBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBusinessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_id):
            body['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBusiness',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_business(
        self,
        request: main_models.UpdateBusinessRequest,
    ) -> main_models.UpdateBusinessResponse:
        runtime = RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    async def update_business_async(
        self,
        request: main_models.UpdateBusinessRequest,
    ) -> main_models.UpdateBusinessResponse:
        runtime = RuntimeOptions()
        return await self.update_business_with_options_async(request, runtime)

    def update_column_business_metadata_with_options(
        self,
        request: main_models.UpdateColumnBusinessMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateColumnBusinessMetadataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateColumnBusinessMetadata',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateColumnBusinessMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_column_business_metadata_with_options_async(
        self,
        request: main_models.UpdateColumnBusinessMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateColumnBusinessMetadataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateColumnBusinessMetadata',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateColumnBusinessMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_column_business_metadata(
        self,
        request: main_models.UpdateColumnBusinessMetadataRequest,
    ) -> main_models.UpdateColumnBusinessMetadataResponse:
        runtime = RuntimeOptions()
        return self.update_column_business_metadata_with_options(request, runtime)

    async def update_column_business_metadata_async(
        self,
        request: main_models.UpdateColumnBusinessMetadataRequest,
    ) -> main_models.UpdateColumnBusinessMetadataResponse:
        runtime = RuntimeOptions()
        return await self.update_column_business_metadata_with_options_async(request, runtime)

    def update_component_with_options(
        self,
        request: main_models.UpdateComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.component_id):
            body['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_with_options_async(
        self,
        request: main_models.UpdateComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.component_id):
            body['ComponentId'] = request.component_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponent',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component(
        self,
        request: main_models.UpdateComponentRequest,
    ) -> main_models.UpdateComponentResponse:
        runtime = RuntimeOptions()
        return self.update_component_with_options(request, runtime)

    async def update_component_async(
        self,
        request: main_models.UpdateComponentRequest,
    ) -> main_models.UpdateComponentResponse:
        runtime = RuntimeOptions()
        return await self.update_component_with_options_async(request, runtime)

    def update_compute_resource_with_options(
        self,
        request: main_models.UpdateComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_resource_with_options_async(
        self,
        request: main_models.UpdateComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_resource(
        self,
        request: main_models.UpdateComputeResourceRequest,
    ) -> main_models.UpdateComputeResourceResponse:
        runtime = RuntimeOptions()
        return self.update_compute_resource_with_options(request, runtime)

    async def update_compute_resource_async(
        self,
        request: main_models.UpdateComputeResourceRequest,
    ) -> main_models.UpdateComputeResourceResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_resource_with_options_async(request, runtime)

    def update_dialarm_rule_with_options(
        self,
        tmp_req: main_models.UpdateDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDIAlarmRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDIAlarmRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_settings):
            request.notification_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not DaraCore.is_null(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dialarm_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateDIAlarmRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDIAlarmRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDIAlarmRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_settings):
            request.notification_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not DaraCore.is_null(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDIAlarmRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDIAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dialarm_rule(
        self,
        request: main_models.UpdateDIAlarmRuleRequest,
    ) -> main_models.UpdateDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return self.update_dialarm_rule_with_options(request, runtime)

    async def update_dialarm_rule_async(
        self,
        request: main_models.UpdateDIAlarmRuleRequest,
    ) -> main_models.UpdateDIAlarmRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_dialarm_rule_with_options_async(request, runtime)

    def update_dijob_with_options(
        self,
        tmp_req: main_models.UpdateDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDIJobResponse:
        tmp_req.validate()
        request = main_models.UpdateDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_settings):
            request.job_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not DaraCore.is_null(tmp_req.resource_settings):
            request.resource_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.table_mappings):
            request.table_mappings_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not DaraCore.is_null(tmp_req.transformation_rules):
            request.transformation_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = {}
        if not DaraCore.is_null(request.dijob_id):
            query['DIJobId'] = request.dijob_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not DaraCore.is_null(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not DaraCore.is_null(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not DaraCore.is_null(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dijob_with_options_async(
        self,
        tmp_req: main_models.UpdateDIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDIJobResponse:
        tmp_req.validate()
        request = main_models.UpdateDIJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_settings):
            request.job_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not DaraCore.is_null(tmp_req.resource_settings):
            request.resource_settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not DaraCore.is_null(tmp_req.table_mappings):
            request.table_mappings_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not DaraCore.is_null(tmp_req.transformation_rules):
            request.transformation_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = {}
        if not DaraCore.is_null(request.dijob_id):
            query['DIJobId'] = request.dijob_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not DaraCore.is_null(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not DaraCore.is_null(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not DaraCore.is_null(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDIJob',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dijob(
        self,
        request: main_models.UpdateDIJobRequest,
    ) -> main_models.UpdateDIJobResponse:
        runtime = RuntimeOptions()
        return self.update_dijob_with_options(request, runtime)

    async def update_dijob_async(
        self,
        request: main_models.UpdateDIJobRequest,
    ) -> main_models.UpdateDIJobResponse:
        runtime = RuntimeOptions()
        return await self.update_dijob_with_options_async(request, runtime)

    def update_data_asset_tag_with_options(
        self,
        tmp_req: main_models.UpdateDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.UpdateDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.managers):
            request.managers_shrink = Utils.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.managers_shrink):
            query['Managers'] = request.managers_shrink
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAssetTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_asset_tag_with_options_async(
        self,
        tmp_req: main_models.UpdateDataAssetTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAssetTagResponse:
        tmp_req.validate()
        request = main_models.UpdateDataAssetTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.managers):
            request.managers_shrink = Utils.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.managers_shrink):
            query['Managers'] = request.managers_shrink
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAssetTag',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAssetTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_asset_tag(
        self,
        request: main_models.UpdateDataAssetTagRequest,
    ) -> main_models.UpdateDataAssetTagResponse:
        runtime = RuntimeOptions()
        return self.update_data_asset_tag_with_options(request, runtime)

    async def update_data_asset_tag_async(
        self,
        request: main_models.UpdateDataAssetTagRequest,
    ) -> main_models.UpdateDataAssetTagResponse:
        runtime = RuntimeOptions()
        return await self.update_data_asset_tag_with_options_async(request, runtime)

    def update_data_quality_alert_rule_with_options(
        self,
        tmp_req: main_models.UpdateDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityAlertRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.condition):
            body['Condition'] = request.condition
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_alert_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateDataQualityAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityAlertRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityAlertRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        body = {}
        if not DaraCore.is_null(request.condition):
            body['Condition'] = request.condition
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityAlertRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_alert_rule(
        self,
        request: main_models.UpdateDataQualityAlertRuleRequest,
    ) -> main_models.UpdateDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_alert_rule_with_options(request, runtime)

    async def update_data_quality_alert_rule_async(
        self,
        request: main_models.UpdateDataQualityAlertRuleRequest,
    ) -> main_models.UpdateDataQualityAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_alert_rule_with_options_async(request, runtime)

    def update_data_quality_evaluation_task_with_options(
        self,
        tmp_req: main_models.UpdateDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rules):
            request.data_quality_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rules, 'DataQualityRules', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.notifications):
            request.notifications_shrink = Utils.array_to_string_with_specified_style(tmp_req.notifications, 'Notifications', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_rules_shrink):
            body['DataQualityRules'] = request.data_quality_rules_shrink
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notifications_shrink):
            body['Notifications'] = request.notifications_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_conf):
            body['RuntimeConf'] = request.runtime_conf
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_evaluation_task_with_options_async(
        self,
        tmp_req: main_models.UpdateDataQualityEvaluationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityEvaluationTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityEvaluationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_quality_rules):
            request.data_quality_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_quality_rules, 'DataQualityRules', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.notifications):
            request.notifications_shrink = Utils.array_to_string_with_specified_style(tmp_req.notifications, 'Notifications', 'json')
        if not DaraCore.is_null(tmp_req.target):
            request.target_shrink = Utils.array_to_string_with_specified_style(tmp_req.target, 'Target', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.data_quality_rules_shrink):
            body['DataQualityRules'] = request.data_quality_rules_shrink
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notifications_shrink):
            body['Notifications'] = request.notifications_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_conf):
            body['RuntimeConf'] = request.runtime_conf
        if not DaraCore.is_null(request.target_shrink):
            body['Target'] = request.target_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityEvaluationTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_evaluation_task(
        self,
        request: main_models.UpdateDataQualityEvaluationTaskRequest,
    ) -> main_models.UpdateDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_evaluation_task_with_options(request, runtime)

    async def update_data_quality_evaluation_task_async(
        self,
        request: main_models.UpdateDataQualityEvaluationTaskRequest,
    ) -> main_models.UpdateDataQualityEvaluationTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_evaluation_task_with_options_async(request, runtime)

    def update_data_quality_rule_with_options(
        self,
        tmp_req: main_models.UpdateDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.error_handlers):
            request.error_handlers_shrink = Utils.array_to_string_with_specified_style(tmp_req.error_handlers, 'ErrorHandlers', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.error_handlers_shrink):
            body['ErrorHandlers'] = request.error_handlers_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateDataQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.error_handlers):
            request.error_handlers_shrink = Utils.array_to_string_with_specified_style(tmp_req.error_handlers, 'ErrorHandlers', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.error_handlers_shrink):
            body['ErrorHandlers'] = request.error_handlers_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityRule',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_rule(
        self,
        request: main_models.UpdateDataQualityRuleRequest,
    ) -> main_models.UpdateDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_rule_with_options(request, runtime)

    async def update_data_quality_rule_async(
        self,
        request: main_models.UpdateDataQualityRuleRequest,
    ) -> main_models.UpdateDataQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_rule_with_options_async(request, runtime)

    def update_data_quality_rule_template_with_options(
        self,
        tmp_req: main_models.UpdateDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityRuleTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityRuleTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.directory_path):
            body['DirectoryPath'] = request.directory_path
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_rule_template_with_options_async(
        self,
        tmp_req: main_models.UpdateDataQualityRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityRuleTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityRuleTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.checking_config):
            request.checking_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.checking_config, 'CheckingConfig', 'json')
        if not DaraCore.is_null(tmp_req.sampling_config):
            request.sampling_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sampling_config, 'SamplingConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.checking_config_shrink):
            body['CheckingConfig'] = request.checking_config_shrink
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.directory_path):
            body['DirectoryPath'] = request.directory_path
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.sampling_config_shrink):
            body['SamplingConfig'] = request.sampling_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityRuleTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_rule_template(
        self,
        request: main_models.UpdateDataQualityRuleTemplateRequest,
    ) -> main_models.UpdateDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_rule_template_with_options(request, runtime)

    async def update_data_quality_rule_template_async(
        self,
        request: main_models.UpdateDataQualityRuleTemplateRequest,
    ) -> main_models.UpdateDataQualityRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_rule_template_with_options_async(request, runtime)

    def update_data_quality_scan_with_options(
        self,
        tmp_req: main_models.UpdateDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityScanResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityScanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_resource):
            request.compute_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_resource, 'ComputeResource', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.compute_resource_shrink):
            body['ComputeResource'] = request.compute_resource_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_scan_with_options_async(
        self,
        tmp_req: main_models.UpdateDataQualityScanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityScanResponse:
        tmp_req.validate()
        request = main_models.UpdateDataQualityScanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_resource):
            request.compute_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_resource, 'ComputeResource', 'json')
        if not DaraCore.is_null(tmp_req.hooks):
            request.hooks_shrink = Utils.array_to_string_with_specified_style(tmp_req.hooks, 'Hooks', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.compute_resource_shrink):
            body['ComputeResource'] = request.compute_resource_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.hooks_shrink):
            body['Hooks'] = request.hooks_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityScan',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_scan(
        self,
        request: main_models.UpdateDataQualityScanRequest,
    ) -> main_models.UpdateDataQualityScanResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_scan_with_options(request, runtime)

    async def update_data_quality_scan_async(
        self,
        request: main_models.UpdateDataQualityScanRequest,
    ) -> main_models.UpdateDataQualityScanResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_scan_with_options_async(request, runtime)

    def update_data_quality_template_with_options(
        self,
        request: main_models.UpdateDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_quality_template_with_options_async(
        self,
        request: main_models.UpdateDataQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataQualityTemplate',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_quality_template(
        self,
        request: main_models.UpdateDataQualityTemplateRequest,
    ) -> main_models.UpdateDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_data_quality_template_with_options(request, runtime)

    async def update_data_quality_template_async(
        self,
        request: main_models.UpdateDataQualityTemplateRequest,
    ) -> main_models.UpdateDataQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_data_quality_template_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_properties):
            query['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.connection_properties_mode):
            query['ConnectionPropertiesMode'] = request.connection_properties_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        request: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.readme):
            body['Readme'] = request.readme
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        request: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.readme):
            body['Readme'] = request.readme
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_dataset_version_with_options(
        self,
        request: main_models.UpdateDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_version_with_options_async(
        self,
        request: main_models.UpdateDatasetVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetVersion',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_version(
        self,
        request: main_models.UpdateDatasetVersionRequest,
    ) -> main_models.UpdateDatasetVersionResponse:
        runtime = RuntimeOptions()
        return self.update_dataset_version_with_options(request, runtime)

    async def update_dataset_version_async(
        self,
        request: main_models.UpdateDatasetVersionRequest,
    ) -> main_models.UpdateDatasetVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_dataset_version_with_options_async(request, runtime)

    def update_file_with_options(
        self,
        request: main_models.UpdateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not DaraCore.is_null(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
        if not DaraCore.is_null(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not DaraCore.is_null(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not DaraCore.is_null(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not DaraCore.is_null(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not DaraCore.is_null(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not DaraCore.is_null(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.input_list):
            body['InputList'] = request.input_list
        if not DaraCore.is_null(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not DaraCore.is_null(request.output_list):
            body['OutputList'] = request.output_list
        if not DaraCore.is_null(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.para_value):
            body['ParaValue'] = request.para_value
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not DaraCore.is_null(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not DaraCore.is_null(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not DaraCore.is_null(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.stop):
            body['Stop'] = request.stop
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        request: main_models.UpdateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not DaraCore.is_null(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
        if not DaraCore.is_null(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not DaraCore.is_null(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not DaraCore.is_null(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not DaraCore.is_null(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not DaraCore.is_null(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not DaraCore.is_null(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not DaraCore.is_null(request.file_description):
            body['FileDescription'] = request.file_description
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.input_list):
            body['InputList'] = request.input_list
        if not DaraCore.is_null(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not DaraCore.is_null(request.output_list):
            body['OutputList'] = request.output_list
        if not DaraCore.is_null(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.para_value):
            body['ParaValue'] = request.para_value
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not DaraCore.is_null(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not DaraCore.is_null(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not DaraCore.is_null(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.stop):
            body['Stop'] = request.stop
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file(
        self,
        request: main_models.UpdateFileRequest,
    ) -> main_models.UpdateFileResponse:
        runtime = RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    async def update_file_async(
        self,
        request: main_models.UpdateFileRequest,
    ) -> main_models.UpdateFileResponse:
        runtime = RuntimeOptions()
        return await self.update_file_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: main_models.UpdateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.folder_name):
            body['FolderName'] = request.folder_name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: main_models.UpdateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.folder_name):
            body['FolderName'] = request.folder_name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_function_with_options(
        self,
        request: main_models.UpdateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        request: main_models.UpdateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunction',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        request: main_models.UpdateFunctionRequest,
    ) -> main_models.UpdateFunctionResponse:
        runtime = RuntimeOptions()
        return self.update_function_with_options(request, runtime)

    async def update_function_async(
        self,
        request: main_models.UpdateFunctionRequest,
    ) -> main_models.UpdateFunctionResponse:
        runtime = RuntimeOptions()
        return await self.update_function_with_options_async(request, runtime)

    def update_ideevent_result_with_options(
        self,
        request: main_models.UpdateIDEEventResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIDEEventResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_result):
            body['CheckResult'] = request.check_result
        if not DaraCore.is_null(request.check_result_tip):
            body['CheckResultTip'] = request.check_result_tip
        if not DaraCore.is_null(request.extension_code):
            body['ExtensionCode'] = request.extension_code
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIDEEventResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIDEEventResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ideevent_result_with_options_async(
        self,
        request: main_models.UpdateIDEEventResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIDEEventResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_result):
            body['CheckResult'] = request.check_result
        if not DaraCore.is_null(request.check_result_tip):
            body['CheckResultTip'] = request.check_result_tip
        if not DaraCore.is_null(request.extension_code):
            body['ExtensionCode'] = request.extension_code
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIDEEventResult',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIDEEventResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ideevent_result(
        self,
        request: main_models.UpdateIDEEventResultRequest,
    ) -> main_models.UpdateIDEEventResultResponse:
        runtime = RuntimeOptions()
        return self.update_ideevent_result_with_options(request, runtime)

    async def update_ideevent_result_async(
        self,
        request: main_models.UpdateIDEEventResultRequest,
    ) -> main_models.UpdateIDEEventResultResponse:
        runtime = RuntimeOptions()
        return await self.update_ideevent_result_with_options_async(request, runtime)

    def update_meta_collection_with_options(
        self,
        tmp_req: main_models.UpdateMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetaCollectionResponse:
        tmp_req.validate()
        request = main_models.UpdateMetaCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.administrators):
            request.administrators_shrink = Utils.array_to_string_with_specified_style(tmp_req.administrators, 'Administrators', 'simple')
        query = {}
        if not DaraCore.is_null(request.administrators_shrink):
            query['Administrators'] = request.administrators_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_meta_collection_with_options_async(
        self,
        tmp_req: main_models.UpdateMetaCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetaCollectionResponse:
        tmp_req.validate()
        request = main_models.UpdateMetaCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.administrators):
            request.administrators_shrink = Utils.array_to_string_with_specified_style(tmp_req.administrators, 'Administrators', 'simple')
        query = {}
        if not DaraCore.is_null(request.administrators_shrink):
            query['Administrators'] = request.administrators_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetaCollection',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMetaCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_meta_collection(
        self,
        request: main_models.UpdateMetaCollectionRequest,
    ) -> main_models.UpdateMetaCollectionResponse:
        runtime = RuntimeOptions()
        return self.update_meta_collection_with_options(request, runtime)

    async def update_meta_collection_async(
        self,
        request: main_models.UpdateMetaCollectionRequest,
    ) -> main_models.UpdateMetaCollectionResponse:
        runtime = RuntimeOptions()
        return await self.update_meta_collection_with_options_async(request, runtime)

    def update_node_with_options(
        self,
        request: main_models.UpdateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_with_options_async(
        self,
        request: main_models.UpdateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNode',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node(
        self,
        request: main_models.UpdateNodeRequest,
    ) -> main_models.UpdateNodeResponse:
        runtime = RuntimeOptions()
        return self.update_node_with_options(request, runtime)

    async def update_node_async(
        self,
        request: main_models.UpdateNodeRequest,
    ) -> main_models.UpdateNodeResponse:
        runtime = RuntimeOptions()
        return await self.update_node_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dev_environment_enabled):
            body['DevEnvironmentEnabled'] = request.dev_environment_enabled
        if not DaraCore.is_null(request.dev_role_disabled):
            body['DevRoleDisabled'] = request.dev_role_disabled
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.pai_task_enabled):
            body['PaiTaskEnabled'] = request.pai_task_enabled
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_resource_with_options(
        self,
        request: main_models.UpdateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request: main_models.UpdateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    async def update_resource_async(
        self,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_with_options_async(request, runtime)

    def update_resource_advance(
        self,
        request: main_models.UpdateResourceAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        update_resource_req = main_models.UpdateResourceRequest()
        Utils.convert(request, update_resource_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            update_resource_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        update_resource_resp = self.update_resource_with_options(update_resource_req, runtime)
        return update_resource_resp

    async def update_resource_advance_async(
        self,
        request: main_models.UpdateResourceAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'dataworks-public',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        update_resource_req = main_models.UpdateResourceRequest()
        Utils.convert(request, update_resource_req)
        if not DaraCore.is_null(request.resource_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.resource_file_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            update_resource_req.resource_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        update_resource_resp = await self.update_resource_with_options_async(update_resource_req, runtime)
        return update_resource_resp

    def update_resource_group_with_options(
        self,
        request: main_models.UpdateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: main_models.UpdateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_resource_group_id):
            body['AliyunResourceGroupId'] = request.aliyun_resource_group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_route_with_options(
        self,
        request: main_models.UpdateRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_route_with_options_async(
        self,
        request: main_models.UpdateRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr):
            body['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRoute',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_route(
        self,
        request: main_models.UpdateRouteRequest,
    ) -> main_models.UpdateRouteResponse:
        runtime = RuntimeOptions()
        return self.update_route_with_options(request, runtime)

    async def update_route_async(
        self,
        request: main_models.UpdateRouteRequest,
    ) -> main_models.UpdateRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_route_with_options_async(request, runtime)

    def update_table_business_metadata_with_options(
        self,
        request: main_models.UpdateTableBusinessMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableBusinessMetadataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.readme):
            body['Readme'] = request.readme
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTableBusinessMetadata',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableBusinessMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_business_metadata_with_options_async(
        self,
        request: main_models.UpdateTableBusinessMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableBusinessMetadataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.readme):
            body['Readme'] = request.readme
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTableBusinessMetadata',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableBusinessMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table_business_metadata(
        self,
        request: main_models.UpdateTableBusinessMetadataRequest,
    ) -> main_models.UpdateTableBusinessMetadataResponse:
        runtime = RuntimeOptions()
        return self.update_table_business_metadata_with_options(request, runtime)

    async def update_table_business_metadata_async(
        self,
        request: main_models.UpdateTableBusinessMetadataRequest,
    ) -> main_models.UpdateTableBusinessMetadataResponse:
        runtime = RuntimeOptions()
        return await self.update_table_business_metadata_with_options_async(request, runtime)

    def update_task_with_options(
        self,
        tmp_req: main_models.UpdateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.dependencies):
            request.dependencies_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not DaraCore.is_null(tmp_req.outputs):
            request.outputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.script):
            request.script_shrink = Utils.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.data_source_shrink):
            body['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.inputs_shrink):
            body['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.instance_mode):
            body['InstanceMode'] = request.instance_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.outputs_shrink):
            body['Outputs'] = request.outputs_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.rerun_interval):
            body['RerunInterval'] = request.rerun_interval
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.rerun_times):
            body['RerunTimes'] = request.rerun_times
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.script_shrink):
            body['Script'] = request.script_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_with_options_async(
        self,
        tmp_req: main_models.UpdateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.dependencies):
            request.dependencies_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not DaraCore.is_null(tmp_req.inputs):
            request.inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not DaraCore.is_null(tmp_req.outputs):
            request.outputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        if not DaraCore.is_null(tmp_req.runtime_resource):
            request.runtime_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_resource, 'RuntimeResource', 'json')
        if not DaraCore.is_null(tmp_req.script):
            request.script_shrink = Utils.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.data_source_shrink):
            body['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.inputs_shrink):
            body['Inputs'] = request.inputs_shrink
        if not DaraCore.is_null(request.instance_mode):
            body['InstanceMode'] = request.instance_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.outputs_shrink):
            body['Outputs'] = request.outputs_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.rerun_interval):
            body['RerunInterval'] = request.rerun_interval
        if not DaraCore.is_null(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not DaraCore.is_null(request.rerun_times):
            body['RerunTimes'] = request.rerun_times
        if not DaraCore.is_null(request.runtime_resource_shrink):
            body['RuntimeResource'] = request.runtime_resource_shrink
        if not DaraCore.is_null(request.script_shrink):
            body['Script'] = request.script_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTask',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task(
        self,
        request: main_models.UpdateTaskRequest,
    ) -> main_models.UpdateTaskResponse:
        runtime = RuntimeOptions()
        return self.update_task_with_options(request, runtime)

    async def update_task_async(
        self,
        request: main_models.UpdateTaskRequest,
    ) -> main_models.UpdateTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_task_with_options_async(request, runtime)

    def update_task_instances_with_options(
        self,
        tmp_req: main_models.UpdateTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_instances):
            request.task_instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_instances, 'TaskInstances', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.task_instances_shrink):
            body['TaskInstances'] = request.task_instances_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_instances_with_options_async(
        self,
        tmp_req: main_models.UpdateTaskInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskInstancesResponse:
        tmp_req.validate()
        request = main_models.UpdateTaskInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_instances):
            request.task_instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_instances, 'TaskInstances', 'json')
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.task_instances_shrink):
            body['TaskInstances'] = request.task_instances_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskInstances',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_instances(
        self,
        request: main_models.UpdateTaskInstancesRequest,
    ) -> main_models.UpdateTaskInstancesResponse:
        runtime = RuntimeOptions()
        return self.update_task_instances_with_options(request, runtime)

    async def update_task_instances_async(
        self,
        request: main_models.UpdateTaskInstancesRequest,
    ) -> main_models.UpdateTaskInstancesResponse:
        runtime = RuntimeOptions()
        return await self.update_task_instances_with_options_async(request, runtime)

    def update_udf_file_with_options(
        self,
        request: main_models.UpdateUdfFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not DaraCore.is_null(request.example):
            body['Example'] = request.example
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.function_type):
            body['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.return_value):
            body['ReturnValue'] = request.return_value
        if not DaraCore.is_null(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdfFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_udf_file_with_options_async(
        self,
        request: main_models.UpdateUdfFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not DaraCore.is_null(request.example):
            body['Example'] = request.example
        if not DaraCore.is_null(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.function_type):
            body['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.return_value):
            body['ReturnValue'] = request.return_value
        if not DaraCore.is_null(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdfFile',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_udf_file(
        self,
        request: main_models.UpdateUdfFileRequest,
    ) -> main_models.UpdateUdfFileResponse:
        runtime = RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)

    async def update_udf_file_async(
        self,
        request: main_models.UpdateUdfFileRequest,
    ) -> main_models.UpdateUdfFileResponse:
        runtime = RuntimeOptions()
        return await self.update_udf_file_with_options_async(request, runtime)

    def update_workflow_with_options(
        self,
        tmp_req: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dependencies):
            request.dependencies_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not DaraCore.is_null(tmp_req.outputs):
            request.outputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_mode):
            body['InstanceMode'] = request.instance_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.outputs_shrink):
            body['Outputs'] = request.outputs_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_with_options_async(
        self,
        tmp_req: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dependencies):
            request.dependencies_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not DaraCore.is_null(tmp_req.outputs):
            request.outputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        if not DaraCore.is_null(tmp_req.trigger):
            request.trigger_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger, 'Trigger', 'json')
        body = {}
        if not DaraCore.is_null(request.client_unique_code):
            body['ClientUniqueCode'] = request.client_unique_code
        if not DaraCore.is_null(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_type):
            body['EnvType'] = request.env_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_mode):
            body['InstanceMode'] = request.instance_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.outputs_shrink):
            body['Outputs'] = request.outputs_shrink
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.tasks_shrink):
            body['Tasks'] = request.tasks_shrink
        if not DaraCore.is_null(request.trigger_shrink):
            body['Trigger'] = request.trigger_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_with_options(request, runtime)

    async def update_workflow_async(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_with_options_async(request, runtime)

    def update_workflow_definition_with_options(
        self,
        request: main_models.UpdateWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_definition_with_options_async(
        self,
        request: main_models.UpdateWorkflowDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDefinitionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDefinition',
            version = '2024-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_definition(
        self,
        request: main_models.UpdateWorkflowDefinitionRequest,
    ) -> main_models.UpdateWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_definition_with_options(request, runtime)

    async def update_workflow_definition_async(
        self,
        request: main_models.UpdateWorkflowDefinitionRequest,
    ) -> main_models.UpdateWorkflowDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_definition_with_options_async(request, runtime)
