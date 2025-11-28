# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gpdb20160503 import models as main_models
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
            'cn-beijing': 'gpdb.aliyuncs.com',
            'cn-hangzhou': 'gpdb.aliyuncs.com',
            'cn-shanghai': 'gpdb.aliyuncs.com',
            'cn-shenzhen': 'gpdb.aliyuncs.com',
            'cn-hongkong': 'gpdb.aliyuncs.com',
            'ap-southeast-1': 'gpdb.aliyuncs.com',
            'us-west-1': 'gpdb.aliyuncs.com',
            'us-east-1': 'gpdb.aliyuncs.com',
            'cn-hangzhou-finance': 'gpdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'gpdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'gpdb.aliyuncs.com',
            'cn-qingdao': 'gpdb.aliyuncs.com',
            'cn-north-2-gov-1': 'gpdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gpdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ainode_with_options(
        self,
        request: main_models.AddAINodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAINodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_pool_id):
            query['AINodePoolId'] = request.ainode_pool_id
        if not DaraCore.is_null(request.ainode_spec_infos):
            query['AINodeSpecInfos'] = request.ainode_spec_infos
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAINode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAINodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ainode_with_options_async(
        self,
        request: main_models.AddAINodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAINodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_pool_id):
            query['AINodePoolId'] = request.ainode_pool_id
        if not DaraCore.is_null(request.ainode_spec_infos):
            query['AINodeSpecInfos'] = request.ainode_spec_infos
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAINode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAINodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ainode(
        self,
        request: main_models.AddAINodeRequest,
    ) -> main_models.AddAINodeResponse:
        runtime = RuntimeOptions()
        return self.add_ainode_with_options(request, runtime)

    async def add_ainode_async(
        self,
        request: main_models.AddAINodeRequest,
    ) -> main_models.AddAINodeResponse:
        runtime = RuntimeOptions()
        return await self.add_ainode_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateInstancePublicConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateInstancePublicConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def bind_dbresource_group_with_role_with_options(
        self,
        tmp_req: main_models.BindDBResourceGroupWithRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourceGroupWithRoleResponse:
        tmp_req.validate()
        request = main_models.BindDBResourceGroupWithRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_list):
            request.role_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourceGroupWithRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_group_with_role_with_options_async(
        self,
        tmp_req: main_models.BindDBResourceGroupWithRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourceGroupWithRoleResponse:
        tmp_req.validate()
        request = main_models.BindDBResourceGroupWithRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_list):
            request.role_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourceGroupWithRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_group_with_role(
        self,
        request: main_models.BindDBResourceGroupWithRoleRequest,
    ) -> main_models.BindDBResourceGroupWithRoleResponse:
        runtime = RuntimeOptions()
        return self.bind_dbresource_group_with_role_with_options(request, runtime)

    async def bind_dbresource_group_with_role_async(
        self,
        request: main_models.BindDBResourceGroupWithRoleRequest,
    ) -> main_models.BindDBResourceGroupWithRoleResponse:
        runtime = RuntimeOptions()
        return await self.bind_dbresource_group_with_role_with_options_async(request, runtime)

    def cancel_create_index_job_with_options(
        self,
        request: main_models.CancelCreateIndexJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCreateIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCreateIndexJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCreateIndexJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_create_index_job_with_options_async(
        self,
        request: main_models.CancelCreateIndexJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCreateIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCreateIndexJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCreateIndexJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_create_index_job(
        self,
        request: main_models.CancelCreateIndexJobRequest,
    ) -> main_models.CancelCreateIndexJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_create_index_job_with_options(request, runtime)

    async def cancel_create_index_job_async(
        self,
        request: main_models.CancelCreateIndexJobRequest,
    ) -> main_models.CancelCreateIndexJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_create_index_job_with_options_async(request, runtime)

    def cancel_upload_document_job_with_options(
        self,
        request: main_models.CancelUploadDocumentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUploadDocumentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelUploadDocumentJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUploadDocumentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_upload_document_job_with_options_async(
        self,
        request: main_models.CancelUploadDocumentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUploadDocumentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelUploadDocumentJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUploadDocumentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_upload_document_job(
        self,
        request: main_models.CancelUploadDocumentJobRequest,
    ) -> main_models.CancelUploadDocumentJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_upload_document_job_with_options(request, runtime)

    async def cancel_upload_document_job_async(
        self,
        request: main_models.CancelUploadDocumentJobRequest,
    ) -> main_models.CancelUploadDocumentJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_upload_document_job_with_options_async(request, runtime)

    def cancel_upsert_collection_data_job_with_options(
        self,
        request: main_models.CancelUpsertCollectionDataJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUpsertCollectionDataJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelUpsertCollectionDataJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUpsertCollectionDataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_upsert_collection_data_job_with_options_async(
        self,
        request: main_models.CancelUpsertCollectionDataJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUpsertCollectionDataJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelUpsertCollectionDataJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUpsertCollectionDataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_upsert_collection_data_job(
        self,
        request: main_models.CancelUpsertCollectionDataJobRequest,
    ) -> main_models.CancelUpsertCollectionDataJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_upsert_collection_data_job_with_options(request, runtime)

    async def cancel_upsert_collection_data_job_async(
        self,
        request: main_models.CancelUpsertCollectionDataJobRequest,
    ) -> main_models.CancelUpsertCollectionDataJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_upsert_collection_data_job_with_options_async(request, runtime)

    def chat_with_knowledge_base_with_options(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatWithKnowledgeBaseResponse:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatWithKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_knowledge_base_with_options_async(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatWithKnowledgeBaseResponse:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatWithKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_with_knowledge_base(
        self,
        request: main_models.ChatWithKnowledgeBaseRequest,
    ) -> main_models.ChatWithKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return self.chat_with_knowledge_base_with_options(request, runtime)

    async def chat_with_knowledge_base_async(
        self,
        request: main_models.ChatWithKnowledgeBaseRequest,
    ) -> main_models.ChatWithKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return await self.chat_with_knowledge_base_with_options_async(request, runtime)

    def chat_with_knowledge_base_stream_with_sse(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseStreamRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatWithKnowledgeBaseStreamResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBaseStream',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatWithKnowledgeBaseStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def chat_with_knowledge_base_stream_with_sse_async(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseStreamRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatWithKnowledgeBaseStreamResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBaseStream',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatWithKnowledgeBaseStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def chat_with_knowledge_base_stream_with_options(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatWithKnowledgeBaseStreamResponse:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBaseStream',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatWithKnowledgeBaseStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_knowledge_base_stream_with_options_async(
        self,
        tmp_req: main_models.ChatWithKnowledgeBaseStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatWithKnowledgeBaseStreamResponse:
        tmp_req.validate()
        request = main_models.ChatWithKnowledgeBaseStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.knowledge_params):
            request.knowledge_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_params, 'KnowledgeParams', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.include_knowledge_base_results):
            query['IncludeKnowledgeBaseResults'] = request.include_knowledge_base_results
        if not DaraCore.is_null(request.knowledge_params_shrink):
            query['KnowledgeParams'] = request.knowledge_params_shrink
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_params):
            query['PromptParams'] = request.prompt_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatWithKnowledgeBaseStream',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatWithKnowledgeBaseStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_with_knowledge_base_stream(
        self,
        request: main_models.ChatWithKnowledgeBaseStreamRequest,
    ) -> main_models.ChatWithKnowledgeBaseStreamResponse:
        runtime = RuntimeOptions()
        return self.chat_with_knowledge_base_stream_with_options(request, runtime)

    async def chat_with_knowledge_base_stream_async(
        self,
        request: main_models.ChatWithKnowledgeBaseStreamRequest,
    ) -> main_models.ChatWithKnowledgeBaseStreamResponse:
        runtime = RuntimeOptions()
        return await self.chat_with_knowledge_base_stream_with_options_async(request, runtime)

    def check_hadoop_data_source_with_options(
        self,
        request: main_models.CheckHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_dir):
            query['CheckDir'] = request.check_dir
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_hadoop_data_source_with_options_async(
        self,
        request: main_models.CheckHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_dir):
            query['CheckDir'] = request.check_dir
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHadoopDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_hadoop_data_source(
        self,
        request: main_models.CheckHadoopDataSourceRequest,
    ) -> main_models.CheckHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return self.check_hadoop_data_source_with_options(request, runtime)

    async def check_hadoop_data_source_async(
        self,
        request: main_models.CheckHadoopDataSourceRequest,
    ) -> main_models.CheckHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.check_hadoop_data_source_with_options_async(request, runtime)

    def check_hadoop_net_connection_with_options(
        self,
        request: main_models.CheckHadoopNetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckHadoopNetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHadoopNetConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHadoopNetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_hadoop_net_connection_with_options_async(
        self,
        request: main_models.CheckHadoopNetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckHadoopNetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHadoopNetConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHadoopNetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_hadoop_net_connection(
        self,
        request: main_models.CheckHadoopNetConnectionRequest,
    ) -> main_models.CheckHadoopNetConnectionResponse:
        runtime = RuntimeOptions()
        return self.check_hadoop_net_connection_with_options(request, runtime)

    async def check_hadoop_net_connection_async(
        self,
        request: main_models.CheckHadoopNetConnectionRequest,
    ) -> main_models.CheckHadoopNetConnectionResponse:
        runtime = RuntimeOptions()
        return await self.check_hadoop_net_connection_with_options_async(request, runtime)

    def check_jdbcsource_net_connection_with_options(
        self,
        request: main_models.CheckJDBCSourceNetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckJDBCSourceNetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.jdbc_connection_string):
            query['JdbcConnectionString'] = request.jdbc_connection_string
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckJDBCSourceNetConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckJDBCSourceNetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_jdbcsource_net_connection_with_options_async(
        self,
        request: main_models.CheckJDBCSourceNetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckJDBCSourceNetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.jdbc_connection_string):
            query['JdbcConnectionString'] = request.jdbc_connection_string
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckJDBCSourceNetConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckJDBCSourceNetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_jdbcsource_net_connection(
        self,
        request: main_models.CheckJDBCSourceNetConnectionRequest,
    ) -> main_models.CheckJDBCSourceNetConnectionResponse:
        runtime = RuntimeOptions()
        return self.check_jdbcsource_net_connection_with_options(request, runtime)

    async def check_jdbcsource_net_connection_async(
        self,
        request: main_models.CheckJDBCSourceNetConnectionRequest,
    ) -> main_models.CheckJDBCSourceNetConnectionResponse:
        runtime = RuntimeOptions()
        return await self.check_jdbcsource_net_connection_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def clone_dbinstance_with_options(
        self,
        request: main_models.CloneDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_dbinstance_with_options_async(
        self,
        request: main_models.CloneDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_dbinstance(
        self,
        request: main_models.CloneDBInstanceRequest,
    ) -> main_models.CloneDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    async def clone_dbinstance_async(
        self,
        request: main_models.CloneDBInstanceRequest,
    ) -> main_models.CloneDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.clone_dbinstance_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_collection_with_options(
        self,
        tmp_req: main_models.CreateCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCollectionResponse:
        tmp_req.validate()
        request = main_models.CreateCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sparse_vector_index_config):
            request.sparse_vector_index_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sparse_vector_index_config, 'SparseVectorIndexConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.metadata_indices):
            query['MetadataIndices'] = request.metadata_indices
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parser):
            query['Parser'] = request.parser
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sparse_vector_index_config_shrink):
            query['SparseVectorIndexConfig'] = request.sparse_vector_index_config_shrink
        if not DaraCore.is_null(request.support_sparse):
            query['SupportSparse'] = request.support_sparse
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_collection_with_options_async(
        self,
        tmp_req: main_models.CreateCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCollectionResponse:
        tmp_req.validate()
        request = main_models.CreateCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sparse_vector_index_config):
            request.sparse_vector_index_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sparse_vector_index_config, 'SparseVectorIndexConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.metadata_indices):
            query['MetadataIndices'] = request.metadata_indices
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parser):
            query['Parser'] = request.parser
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sparse_vector_index_config_shrink):
            query['SparseVectorIndexConfig'] = request.sparse_vector_index_config_shrink
        if not DaraCore.is_null(request.support_sparse):
            query['SupportSparse'] = request.support_sparse
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_collection(
        self,
        request: main_models.CreateCollectionRequest,
    ) -> main_models.CreateCollectionResponse:
        runtime = RuntimeOptions()
        return self.create_collection_with_options(request, runtime)

    async def create_collection_async(
        self,
        request: main_models.CreateCollectionRequest,
    ) -> main_models.CreateCollectionResponse:
        runtime = RuntimeOptions()
        return await self.create_collection_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_spec_infos):
            query['AINodeSpecInfos'] = request.ainode_spec_infos
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cache_storage_size):
            query['CacheStorageSize'] = request.cache_storage_size
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_sample_data):
            query['CreateSampleData'] = request.create_sample_data
        if not DaraCore.is_null(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not DaraCore.is_null(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.master_aispec):
            query['MasterAISpec'] = request.master_aispec
        if not DaraCore.is_null(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not DaraCore.is_null(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.prod_type):
            query['ProdType'] = request.prod_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not DaraCore.is_null(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not DaraCore.is_null(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not DaraCore.is_null(request.serverless_mode):
            query['ServerlessMode'] = request.serverless_mode
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not DaraCore.is_null(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_spec_infos):
            query['AINodeSpecInfos'] = request.ainode_spec_infos
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cache_storage_size):
            query['CacheStorageSize'] = request.cache_storage_size
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_sample_data):
            query['CreateSampleData'] = request.create_sample_data
        if not DaraCore.is_null(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not DaraCore.is_null(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.master_aispec):
            query['MasterAISpec'] = request.master_aispec
        if not DaraCore.is_null(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not DaraCore.is_null(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.prod_type):
            query['ProdType'] = request.prod_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not DaraCore.is_null(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not DaraCore.is_null(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not DaraCore.is_null(request.serverless_mode):
            query['ServerlessMode'] = request.serverless_mode
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not DaraCore.is_null(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: main_models.CreateDBInstanceRequest,
    ) -> main_models.CreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: main_models.CreateDBInstanceRequest,
    ) -> main_models.CreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_dbinstance_iparray_with_options(
        self,
        tmp_req: main_models.CreateDBInstanceIPArrayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceIPArrayResponse:
        tmp_req.validate()
        request = main_models.CreateDBInstanceIPArrayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.security_iplist):
            request.security_iplist_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_iplist, 'SecurityIPList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.iparray_attribute):
            query['IPArrayAttribute'] = request.iparray_attribute
        if not DaraCore.is_null(request.iparray_name):
            query['IPArrayName'] = request.iparray_name
        if not DaraCore.is_null(request.security_iplist_shrink):
            query['SecurityIPList'] = request.security_iplist_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstanceIPArray',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceIPArrayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_iparray_with_options_async(
        self,
        tmp_req: main_models.CreateDBInstanceIPArrayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceIPArrayResponse:
        tmp_req.validate()
        request = main_models.CreateDBInstanceIPArrayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.security_iplist):
            request.security_iplist_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_iplist, 'SecurityIPList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.iparray_attribute):
            query['IPArrayAttribute'] = request.iparray_attribute
        if not DaraCore.is_null(request.iparray_name):
            query['IPArrayName'] = request.iparray_name
        if not DaraCore.is_null(request.security_iplist_shrink):
            query['SecurityIPList'] = request.security_iplist_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstanceIPArray',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceIPArrayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance_iparray(
        self,
        request: main_models.CreateDBInstanceIPArrayRequest,
    ) -> main_models.CreateDBInstanceIPArrayResponse:
        runtime = RuntimeOptions()
        return self.create_dbinstance_iparray_with_options(request, runtime)

    async def create_dbinstance_iparray_async(
        self,
        request: main_models.CreateDBInstanceIPArrayRequest,
    ) -> main_models.CreateDBInstanceIPArrayResponse:
        runtime = RuntimeOptions()
        return await self.create_dbinstance_iparray_with_options_async(request, runtime)

    def create_dbinstance_plan_with_options(
        self,
        request: main_models.CreateDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not DaraCore.is_null(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_plan_with_options_async(
        self,
        request: main_models.CreateDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not DaraCore.is_null(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance_plan(
        self,
        request: main_models.CreateDBInstancePlanRequest,
    ) -> main_models.CreateDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return self.create_dbinstance_plan_with_options(request, runtime)

    async def create_dbinstance_plan_async(
        self,
        request: main_models.CreateDBInstancePlanRequest,
    ) -> main_models.CreateDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return await self.create_dbinstance_plan_with_options_async(request, runtime)

    def create_dbresource_group_with_options(
        self,
        request: main_models.CreateDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_config):
            query['ResourceGroupConfig'] = request.resource_group_config
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_group_with_options_async(
        self,
        request: main_models.CreateDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_config):
            query['ResourceGroupConfig'] = request.resource_group_config
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_group(
        self,
        request: main_models.CreateDBResourceGroupRequest,
    ) -> main_models.CreateDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    async def create_dbresource_group_async(
        self,
        request: main_models.CreateDBResourceGroupRequest,
    ) -> main_models.CreateDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_dbresource_group_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: main_models.CreateDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not DaraCore.is_null(request.collate):
            query['Collate'] = request.collate
        if not DaraCore.is_null(request.ctype):
            query['Ctype'] = request.ctype
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: main_models.CreateDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not DaraCore.is_null(request.collate):
            query['Collate'] = request.collate
        if not DaraCore.is_null(request.ctype):
            query['Ctype'] = request.ctype
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_document_collection_with_options(
        self,
        tmp_req: main_models.CreateDocumentCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocumentCollectionResponse:
        tmp_req.validate()
        request = main_models.CreateDocumentCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.entity_types):
            request.entity_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.entity_types, 'EntityTypes', 'json')
        if not DaraCore.is_null(tmp_req.relationship_types):
            request.relationship_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.relationship_types, 'RelationshipTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not DaraCore.is_null(request.enable_graph):
            query['EnableGraph'] = request.enable_graph
        if not DaraCore.is_null(request.entity_types_shrink):
            query['EntityTypes'] = request.entity_types_shrink
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.llmmodel):
            query['LLMModel'] = request.llmmodel
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.metadata_indices):
            query['MetadataIndices'] = request.metadata_indices
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parser):
            query['Parser'] = request.parser
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relationship_types_shrink):
            query['RelationshipTypes'] = request.relationship_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocumentCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_document_collection_with_options_async(
        self,
        tmp_req: main_models.CreateDocumentCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocumentCollectionResponse:
        tmp_req.validate()
        request = main_models.CreateDocumentCollectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.entity_types):
            request.entity_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.entity_types, 'EntityTypes', 'json')
        if not DaraCore.is_null(tmp_req.relationship_types):
            request.relationship_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.relationship_types, 'RelationshipTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not DaraCore.is_null(request.enable_graph):
            query['EnableGraph'] = request.enable_graph
        if not DaraCore.is_null(request.entity_types_shrink):
            query['EntityTypes'] = request.entity_types_shrink
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.llmmodel):
            query['LLMModel'] = request.llmmodel
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.metadata_indices):
            query['MetadataIndices'] = request.metadata_indices
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parser):
            query['Parser'] = request.parser
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relationship_types_shrink):
            query['RelationshipTypes'] = request.relationship_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocumentCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocumentCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_document_collection(
        self,
        request: main_models.CreateDocumentCollectionRequest,
    ) -> main_models.CreateDocumentCollectionResponse:
        runtime = RuntimeOptions()
        return self.create_document_collection_with_options(request, runtime)

    async def create_document_collection_async(
        self,
        request: main_models.CreateDocumentCollectionRequest,
    ) -> main_models.CreateDocumentCollectionResponse:
        runtime = RuntimeOptions()
        return await self.create_document_collection_with_options_async(request, runtime)

    def create_extensions_with_options(
        self,
        request: main_models.CreateExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbnames):
            query['DBNames'] = request.dbnames
        if not DaraCore.is_null(request.extensions):
            query['Extensions'] = request.extensions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_extensions_with_options_async(
        self,
        request: main_models.CreateExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbnames):
            query['DBNames'] = request.dbnames
        if not DaraCore.is_null(request.extensions):
            query['Extensions'] = request.extensions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_extensions(
        self,
        request: main_models.CreateExtensionsRequest,
    ) -> main_models.CreateExtensionsResponse:
        runtime = RuntimeOptions()
        return self.create_extensions_with_options(request, runtime)

    async def create_extensions_async(
        self,
        request: main_models.CreateExtensionsRequest,
    ) -> main_models.CreateExtensionsResponse:
        runtime = RuntimeOptions()
        return await self.create_extensions_with_options_async(request, runtime)

    def create_external_data_service_with_options(
        self,
        request: main_models.CreateExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_external_data_service_with_options_async(
        self,
        request: main_models.CreateExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_external_data_service(
        self,
        request: main_models.CreateExternalDataServiceRequest,
    ) -> main_models.CreateExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return self.create_external_data_service_with_options(request, runtime)

    async def create_external_data_service_async(
        self,
        request: main_models.CreateExternalDataServiceRequest,
    ) -> main_models.CreateExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_external_data_service_with_options_async(request, runtime)

    def create_hadoop_data_source_with_options(
        self,
        request: main_models.CreateHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not DaraCore.is_null(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not DaraCore.is_null(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not DaraCore.is_null(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not DaraCore.is_null(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not DaraCore.is_null(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hadoop_data_source_with_options_async(
        self,
        request: main_models.CreateHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not DaraCore.is_null(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not DaraCore.is_null(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not DaraCore.is_null(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not DaraCore.is_null(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not DaraCore.is_null(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHadoopDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hadoop_data_source(
        self,
        request: main_models.CreateHadoopDataSourceRequest,
    ) -> main_models.CreateHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_hadoop_data_source_with_options(request, runtime)

    async def create_hadoop_data_source_async(
        self,
        request: main_models.CreateHadoopDataSourceRequest,
    ) -> main_models.CreateHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_hadoop_data_source_with_options_async(request, runtime)

    def create_index_with_options(
        self,
        request: main_models.CreateIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_config):
            query['IndexConfig'] = request.index_config
        if not DaraCore.is_null(request.index_field):
            query['IndexField'] = request.index_field
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        request: main_models.CreateIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_config):
            query['IndexConfig'] = request.index_config
        if not DaraCore.is_null(request.index_field):
            query['IndexField'] = request.index_field
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_index(
        self,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        return self.create_index_with_options(request, runtime)

    async def create_index_async(
        self,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        return await self.create_index_with_options_async(request, runtime)

    def create_jdbcdata_source_with_options(
        self,
        request: main_models.CreateJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not DaraCore.is_null(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not DaraCore.is_null(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_jdbcdata_source_with_options_async(
        self,
        request: main_models.CreateJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not DaraCore.is_null(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not DaraCore.is_null(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJDBCDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_jdbcdata_source(
        self,
        request: main_models.CreateJDBCDataSourceRequest,
    ) -> main_models.CreateJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_jdbcdata_source_with_options(request, runtime)

    async def create_jdbcdata_source_async(
        self,
        request: main_models.CreateJDBCDataSourceRequest,
    ) -> main_models.CreateJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_jdbcdata_source_with_options_async(request, runtime)

    def create_model_service_with_options(
        self,
        tmp_req: main_models.CreateModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelServiceResponse:
        tmp_req.validate()
        request = main_models.CreateModelServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_nodes):
            request.ai_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_nodes, 'AiNodes', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.ai_nodes_shrink):
            query['AiNodes'] = request.ai_nodes_shrink
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_public_connection):
            query['EnablePublicConnection'] = request.enable_public_connection
        if not DaraCore.is_null(request.inference_engine):
            query['InferenceEngine'] = request.inference_engine
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_service_with_options_async(
        self,
        tmp_req: main_models.CreateModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelServiceResponse:
        tmp_req.validate()
        request = main_models.CreateModelServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_nodes):
            request.ai_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_nodes, 'AiNodes', 'json')
        if not DaraCore.is_null(tmp_req.model_params):
            request.model_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_params, 'ModelParams', 'json')
        query = {}
        if not DaraCore.is_null(request.ai_nodes_shrink):
            query['AiNodes'] = request.ai_nodes_shrink
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_public_connection):
            query['EnablePublicConnection'] = request.enable_public_connection
        if not DaraCore.is_null(request.inference_engine):
            query['InferenceEngine'] = request.inference_engine
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_params_shrink):
            query['ModelParams'] = request.model_params_shrink
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_service(
        self,
        request: main_models.CreateModelServiceRequest,
    ) -> main_models.CreateModelServiceResponse:
        runtime = RuntimeOptions()
        return self.create_model_service_with_options(request, runtime)

    async def create_model_service_async(
        self,
        request: main_models.CreateModelServiceRequest,
    ) -> main_models.CreateModelServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_model_service_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_remote_adbdata_source_with_options(
        self,
        request: main_models.CreateRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.local_database):
            query['LocalDatabase'] = request.local_database
        if not DaraCore.is_null(request.manager_user_name):
            query['ManagerUserName'] = request.manager_user_name
        if not DaraCore.is_null(request.manager_user_password):
            query['ManagerUserPassword'] = request.manager_user_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remote_dbinstance_id):
            query['RemoteDBInstanceId'] = request.remote_dbinstance_id
        if not DaraCore.is_null(request.remote_database):
            query['RemoteDatabase'] = request.remote_database
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_password):
            query['UserPassword'] = request.user_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRemoteADBDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_remote_adbdata_source_with_options_async(
        self,
        request: main_models.CreateRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.local_database):
            query['LocalDatabase'] = request.local_database
        if not DaraCore.is_null(request.manager_user_name):
            query['ManagerUserName'] = request.manager_user_name
        if not DaraCore.is_null(request.manager_user_password):
            query['ManagerUserPassword'] = request.manager_user_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remote_dbinstance_id):
            query['RemoteDBInstanceId'] = request.remote_dbinstance_id
        if not DaraCore.is_null(request.remote_database):
            query['RemoteDatabase'] = request.remote_database
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_password):
            query['UserPassword'] = request.user_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRemoteADBDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_remote_adbdata_source(
        self,
        request: main_models.CreateRemoteADBDataSourceRequest,
    ) -> main_models.CreateRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_remote_adbdata_source_with_options(request, runtime)

    async def create_remote_adbdata_source_async(
        self,
        request: main_models.CreateRemoteADBDataSourceRequest,
    ) -> main_models.CreateRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_remote_adbdata_source_with_options_async(request, runtime)

    def create_sample_data_with_options(
        self,
        request: main_models.CreateSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_data_with_options_async(
        self,
        request: main_models.CreateSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_data(
        self,
        request: main_models.CreateSampleDataRequest,
    ) -> main_models.CreateSampleDataResponse:
        runtime = RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    async def create_sample_data_async(
        self,
        request: main_models.CreateSampleDataRequest,
    ) -> main_models.CreateSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.create_sample_data_with_options_async(request, runtime)

    def create_secret_with_options(
        self,
        request: main_models.CreateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.test_connection):
            query['TestConnection'] = request.test_connection
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        request: main_models.CreateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.test_connection):
            query['TestConnection'] = request.test_connection
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    async def create_secret_async(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        return await self.create_secret_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_streaming_data_service_with_options(
        self,
        request: main_models.CreateStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_streaming_data_service_with_options_async(
        self,
        request: main_models.CreateStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_streaming_data_service(
        self,
        request: main_models.CreateStreamingDataServiceRequest,
    ) -> main_models.CreateStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return self.create_streaming_data_service_with_options(request, runtime)

    async def create_streaming_data_service_async(
        self,
        request: main_models.CreateStreamingDataServiceRequest,
    ) -> main_models.CreateStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_streaming_data_service_with_options_async(request, runtime)

    def create_streaming_data_source_with_options(
        self,
        request: main_models.CreateStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_streaming_data_source_with_options_async(
        self,
        request: main_models.CreateStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_streaming_data_source(
        self,
        request: main_models.CreateStreamingDataSourceRequest,
    ) -> main_models.CreateStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_streaming_data_source_with_options(request, runtime)

    async def create_streaming_data_source_async(
        self,
        request: main_models.CreateStreamingDataSourceRequest,
    ) -> main_models.CreateStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_streaming_data_source_with_options_async(request, runtime)

    def create_streaming_job_with_options(
        self,
        tmp_req: main_models.CreateStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingJobResponse:
        tmp_req.validate()
        request = main_models.CreateStreamingJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_columns):
            request.dest_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not DaraCore.is_null(tmp_req.match_columns):
            request.match_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not DaraCore.is_null(tmp_req.src_columns):
            request.src_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not DaraCore.is_null(tmp_req.update_columns):
            request.update_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.consistency):
            query['Consistency'] = request.consistency
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not DaraCore.is_null(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not DaraCore.is_null(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not DaraCore.is_null(request.dest_table):
            query['DestTable'] = request.dest_table
        if not DaraCore.is_null(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not DaraCore.is_null(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not DaraCore.is_null(request.try_run):
            query['TryRun'] = request.try_run
        if not DaraCore.is_null(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not DaraCore.is_null(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_streaming_job_with_options_async(
        self,
        tmp_req: main_models.CreateStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamingJobResponse:
        tmp_req.validate()
        request = main_models.CreateStreamingJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_columns):
            request.dest_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not DaraCore.is_null(tmp_req.match_columns):
            request.match_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not DaraCore.is_null(tmp_req.src_columns):
            request.src_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not DaraCore.is_null(tmp_req.update_columns):
            request.update_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.consistency):
            query['Consistency'] = request.consistency
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not DaraCore.is_null(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not DaraCore.is_null(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not DaraCore.is_null(request.dest_table):
            query['DestTable'] = request.dest_table
        if not DaraCore.is_null(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not DaraCore.is_null(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not DaraCore.is_null(request.try_run):
            query['TryRun'] = request.try_run
        if not DaraCore.is_null(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not DaraCore.is_null(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_streaming_job(
        self,
        request: main_models.CreateStreamingJobRequest,
    ) -> main_models.CreateStreamingJobResponse:
        runtime = RuntimeOptions()
        return self.create_streaming_job_with_options(request, runtime)

    async def create_streaming_job_async(
        self,
        request: main_models.CreateStreamingJobRequest,
    ) -> main_models.CreateStreamingJobResponse:
        runtime = RuntimeOptions()
        return await self.create_streaming_job_with_options_async(request, runtime)

    def create_supabase_project_with_options(
        self,
        request: main_models.CreateSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.project_spec):
            query['ProjectSpec'] = request.project_spec
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSupabaseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_supabase_project_with_options_async(
        self,
        request: main_models.CreateSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.project_spec):
            query['ProjectSpec'] = request.project_spec
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSupabaseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_supabase_project(
        self,
        request: main_models.CreateSupabaseProjectRequest,
    ) -> main_models.CreateSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return self.create_supabase_project_with_options(request, runtime)

    async def create_supabase_project_async(
        self,
        request: main_models.CreateSupabaseProjectRequest,
    ) -> main_models.CreateSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_supabase_project_with_options_async(request, runtime)

    def create_vector_index_with_options(
        self,
        request: main_models.CreateVectorIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVectorIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVectorIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vector_index_with_options_async(
        self,
        request: main_models.CreateVectorIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVectorIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not DaraCore.is_null(request.hnsw_ef_construction):
            query['HnswEfConstruction'] = request.hnsw_ef_construction
        if not DaraCore.is_null(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVectorIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVectorIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vector_index(
        self,
        request: main_models.CreateVectorIndexRequest,
    ) -> main_models.CreateVectorIndexResponse:
        runtime = RuntimeOptions()
        return self.create_vector_index_with_options(request, runtime)

    async def create_vector_index_async(
        self,
        request: main_models.CreateVectorIndexRequest,
    ) -> main_models.CreateVectorIndexResponse:
        runtime = RuntimeOptions()
        return await self.create_vector_index_with_options_async(request, runtime)

    def delete_ainode_with_options(
        self,
        request: main_models.DeleteAINodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAINodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_num):
            query['AINodeNum'] = request.ainode_num
        if not DaraCore.is_null(request.ainode_pool_id):
            query['AINodePoolId'] = request.ainode_pool_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAINode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAINodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ainode_with_options_async(
        self,
        request: main_models.DeleteAINodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAINodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ainode_num):
            query['AINodeNum'] = request.ainode_num
        if not DaraCore.is_null(request.ainode_pool_id):
            query['AINodePoolId'] = request.ainode_pool_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAINode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAINodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ainode(
        self,
        request: main_models.DeleteAINodeRequest,
    ) -> main_models.DeleteAINodeResponse:
        runtime = RuntimeOptions()
        return self.delete_ainode_with_options(request, runtime)

    async def delete_ainode_async(
        self,
        request: main_models.DeleteAINodeRequest,
    ) -> main_models.DeleteAINodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_ainode_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_collection_with_options(
        self,
        request: main_models.DeleteCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_collection_with_options_async(
        self,
        request: main_models.DeleteCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_collection(
        self,
        request: main_models.DeleteCollectionRequest,
    ) -> main_models.DeleteCollectionResponse:
        runtime = RuntimeOptions()
        return self.delete_collection_with_options(request, runtime)

    async def delete_collection_async(
        self,
        request: main_models.DeleteCollectionRequest,
    ) -> main_models.DeleteCollectionResponse:
        runtime = RuntimeOptions()
        return await self.delete_collection_with_options_async(request, runtime)

    def delete_collection_data_with_options(
        self,
        request: main_models.DeleteCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.collection_data):
            query['CollectionData'] = request.collection_data
        if not DaraCore.is_null(request.collection_data_filter):
            query['CollectionDataFilter'] = request.collection_data_filter
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_collection_data_with_options_async(
        self,
        request: main_models.DeleteCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.collection_data):
            query['CollectionData'] = request.collection_data
        if not DaraCore.is_null(request.collection_data_filter):
            query['CollectionDataFilter'] = request.collection_data_filter
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_collection_data(
        self,
        request: main_models.DeleteCollectionDataRequest,
    ) -> main_models.DeleteCollectionDataResponse:
        runtime = RuntimeOptions()
        return self.delete_collection_data_with_options(request, runtime)

    async def delete_collection_data_async(
        self,
        request: main_models.DeleteCollectionDataRequest,
    ) -> main_models.DeleteCollectionDataResponse:
        runtime = RuntimeOptions()
        return await self.delete_collection_data_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: main_models.DeleteDBInstanceRequest,
    ) -> main_models.DeleteDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: main_models.DeleteDBInstanceRequest,
    ) -> main_models.DeleteDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_dbinstance_iparray_with_options(
        self,
        request: main_models.DeleteDBInstanceIPArrayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceIPArrayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.iparray_name):
            query['IPArrayName'] = request.iparray_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstanceIPArray',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceIPArrayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_iparray_with_options_async(
        self,
        request: main_models.DeleteDBInstanceIPArrayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceIPArrayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.iparray_name):
            query['IPArrayName'] = request.iparray_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstanceIPArray',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceIPArrayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance_iparray(
        self,
        request: main_models.DeleteDBInstanceIPArrayRequest,
    ) -> main_models.DeleteDBInstanceIPArrayResponse:
        runtime = RuntimeOptions()
        return self.delete_dbinstance_iparray_with_options(request, runtime)

    async def delete_dbinstance_iparray_async(
        self,
        request: main_models.DeleteDBInstanceIPArrayRequest,
    ) -> main_models.DeleteDBInstanceIPArrayResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbinstance_iparray_with_options_async(request, runtime)

    def delete_dbinstance_plan_with_options(
        self,
        request: main_models.DeleteDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_plan_with_options_async(
        self,
        request: main_models.DeleteDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance_plan(
        self,
        request: main_models.DeleteDBInstancePlanRequest,
    ) -> main_models.DeleteDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return self.delete_dbinstance_plan_with_options(request, runtime)

    async def delete_dbinstance_plan_async(
        self,
        request: main_models.DeleteDBInstancePlanRequest,
    ) -> main_models.DeleteDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbinstance_plan_with_options_async(request, runtime)

    def delete_dbresource_group_with_options(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_group_with_options_async(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_group(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
    ) -> main_models.DeleteDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    async def delete_dbresource_group_async(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
    ) -> main_models.DeleteDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbresource_group_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: main_models.DeleteDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: main_models.DeleteDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: main_models.DeleteDatabaseRequest,
    ) -> main_models.DeleteDatabaseResponse:
        runtime = RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: main_models.DeleteDatabaseRequest,
    ) -> main_models.DeleteDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_document_with_options(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    async def delete_document_async(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return await self.delete_document_with_options_async(request, runtime)

    def delete_document_collection_with_options(
        self,
        request: main_models.DeleteDocumentCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocumentCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_collection_with_options_async(
        self,
        request: main_models.DeleteDocumentCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocumentCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document_collection(
        self,
        request: main_models.DeleteDocumentCollectionRequest,
    ) -> main_models.DeleteDocumentCollectionResponse:
        runtime = RuntimeOptions()
        return self.delete_document_collection_with_options(request, runtime)

    async def delete_document_collection_async(
        self,
        request: main_models.DeleteDocumentCollectionRequest,
    ) -> main_models.DeleteDocumentCollectionResponse:
        runtime = RuntimeOptions()
        return await self.delete_document_collection_with_options_async(request, runtime)

    def delete_extension_with_options(
        self,
        request: main_models.DeleteExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbnames):
            query['DBNames'] = request.dbnames
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExtension',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_extension_with_options_async(
        self,
        request: main_models.DeleteExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbnames):
            query['DBNames'] = request.dbnames
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExtension',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_extension(
        self,
        request: main_models.DeleteExtensionRequest,
    ) -> main_models.DeleteExtensionResponse:
        runtime = RuntimeOptions()
        return self.delete_extension_with_options(request, runtime)

    async def delete_extension_async(
        self,
        request: main_models.DeleteExtensionRequest,
    ) -> main_models.DeleteExtensionResponse:
        runtime = RuntimeOptions()
        return await self.delete_extension_with_options_async(request, runtime)

    def delete_external_data_service_with_options(
        self,
        request: main_models.DeleteExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_external_data_service_with_options_async(
        self,
        request: main_models.DeleteExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExternalDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_external_data_service(
        self,
        request: main_models.DeleteExternalDataServiceRequest,
    ) -> main_models.DeleteExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_external_data_service_with_options(request, runtime)

    async def delete_external_data_service_async(
        self,
        request: main_models.DeleteExternalDataServiceRequest,
    ) -> main_models.DeleteExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_external_data_service_with_options_async(request, runtime)

    def delete_hadoop_data_source_with_options(
        self,
        request: main_models.DeleteHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hadoop_data_source_with_options_async(
        self,
        request: main_models.DeleteHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHadoopDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hadoop_data_source(
        self,
        request: main_models.DeleteHadoopDataSourceRequest,
    ) -> main_models.DeleteHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_hadoop_data_source_with_options(request, runtime)

    async def delete_hadoop_data_source_async(
        self,
        request: main_models.DeleteHadoopDataSourceRequest,
    ) -> main_models.DeleteHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_hadoop_data_source_with_options_async(request, runtime)

    def delete_index_with_options(
        self,
        request: main_models.DeleteIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        request: main_models.DeleteIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index(
        self,
        request: main_models.DeleteIndexRequest,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        return self.delete_index_with_options(request, runtime)

    async def delete_index_async(
        self,
        request: main_models.DeleteIndexRequest,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        return await self.delete_index_with_options_async(request, runtime)

    def delete_jdbcdata_source_with_options(
        self,
        request: main_models.DeleteJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jdbcdata_source_with_options_async(
        self,
        request: main_models.DeleteJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJDBCDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jdbcdata_source(
        self,
        request: main_models.DeleteJDBCDataSourceRequest,
    ) -> main_models.DeleteJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_jdbcdata_source_with_options(request, runtime)

    async def delete_jdbcdata_source_async(
        self,
        request: main_models.DeleteJDBCDataSourceRequest,
    ) -> main_models.DeleteJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_jdbcdata_source_with_options_async(request, runtime)

    def delete_model_service_with_options(
        self,
        request: main_models.DeleteModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.model_service_id):
            query['ModelServiceId'] = request.model_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_service_with_options_async(
        self,
        request: main_models.DeleteModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.model_service_id):
            query['ModelServiceId'] = request.model_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_service(
        self,
        request: main_models.DeleteModelServiceRequest,
    ) -> main_models.DeleteModelServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_model_service_with_options(request, runtime)

    async def delete_model_service_async(
        self,
        request: main_models.DeleteModelServiceRequest,
    ) -> main_models.DeleteModelServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_model_service_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_private_ragservice_with_options(
        self,
        request: main_models.DeletePrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateRAGServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_ragservice_with_options_async(
        self,
        request: main_models.DeletePrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateRAGServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_ragservice(
        self,
        request: main_models.DeletePrivateRAGServiceRequest,
    ) -> main_models.DeletePrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_private_ragservice_with_options(request, runtime)

    async def delete_private_ragservice_async(
        self,
        request: main_models.DeletePrivateRAGServiceRequest,
    ) -> main_models.DeletePrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_ragservice_with_options_async(request, runtime)

    def delete_remote_adbdata_source_with_options(
        self,
        request: main_models.DeleteRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRemoteADBDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_remote_adbdata_source_with_options_async(
        self,
        request: main_models.DeleteRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRemoteADBDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_remote_adbdata_source(
        self,
        request: main_models.DeleteRemoteADBDataSourceRequest,
    ) -> main_models.DeleteRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_remote_adbdata_source_with_options(request, runtime)

    async def delete_remote_adbdata_source_async(
        self,
        request: main_models.DeleteRemoteADBDataSourceRequest,
    ) -> main_models.DeleteRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_remote_adbdata_source_with_options_async(request, runtime)

    def delete_secret_with_options(
        self,
        request: main_models.DeleteSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: main_models.DeleteSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    async def delete_secret_async(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        return await self.delete_secret_with_options_async(request, runtime)

    def delete_streaming_data_service_with_options(
        self,
        request: main_models.DeleteStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_streaming_data_service_with_options_async(
        self,
        request: main_models.DeleteStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_streaming_data_service(
        self,
        request: main_models.DeleteStreamingDataServiceRequest,
    ) -> main_models.DeleteStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_streaming_data_service_with_options(request, runtime)

    async def delete_streaming_data_service_async(
        self,
        request: main_models.DeleteStreamingDataServiceRequest,
    ) -> main_models.DeleteStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_streaming_data_service_with_options_async(request, runtime)

    def delete_streaming_data_source_with_options(
        self,
        request: main_models.DeleteStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_streaming_data_source_with_options_async(
        self,
        request: main_models.DeleteStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_streaming_data_source(
        self,
        request: main_models.DeleteStreamingDataSourceRequest,
    ) -> main_models.DeleteStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_streaming_data_source_with_options(request, runtime)

    async def delete_streaming_data_source_async(
        self,
        request: main_models.DeleteStreamingDataSourceRequest,
    ) -> main_models.DeleteStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_streaming_data_source_with_options_async(request, runtime)

    def delete_streaming_job_with_options(
        self,
        request: main_models.DeleteStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_streaming_job_with_options_async(
        self,
        request: main_models.DeleteStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_streaming_job(
        self,
        request: main_models.DeleteStreamingJobRequest,
    ) -> main_models.DeleteStreamingJobResponse:
        runtime = RuntimeOptions()
        return self.delete_streaming_job_with_options(request, runtime)

    async def delete_streaming_job_async(
        self,
        request: main_models.DeleteStreamingJobRequest,
    ) -> main_models.DeleteStreamingJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_streaming_job_with_options_async(request, runtime)

    def delete_supabase_project_with_options(
        self,
        request: main_models.DeleteSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSupabaseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_supabase_project_with_options_async(
        self,
        request: main_models.DeleteSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSupabaseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_supabase_project(
        self,
        request: main_models.DeleteSupabaseProjectRequest,
    ) -> main_models.DeleteSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_supabase_project_with_options(request, runtime)

    async def delete_supabase_project_async(
        self,
        request: main_models.DeleteSupabaseProjectRequest,
    ) -> main_models.DeleteSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_supabase_project_with_options_async(request, runtime)

    def delete_vector_index_with_options(
        self,
        request: main_models.DeleteVectorIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVectorIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVectorIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vector_index_with_options_async(
        self,
        request: main_models.DeleteVectorIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVectorIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVectorIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVectorIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vector_index(
        self,
        request: main_models.DeleteVectorIndexRequest,
    ) -> main_models.DeleteVectorIndexResponse:
        runtime = RuntimeOptions()
        return self.delete_vector_index_with_options(request, runtime)

    async def delete_vector_index_async(
        self,
        request: main_models.DeleteVectorIndexRequest,
    ) -> main_models.DeleteVectorIndexResponse:
        runtime = RuntimeOptions()
        return await self.delete_vector_index_with_options_async(request, runtime)

    def deploy_private_ragservice_with_options(
        self,
        request: main_models.DeployPrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployPrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployPrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployPrivateRAGServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_private_ragservice_with_options_async(
        self,
        request: main_models.DeployPrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployPrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployPrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployPrivateRAGServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_private_ragservice(
        self,
        request: main_models.DeployPrivateRAGServiceRequest,
    ) -> main_models.DeployPrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return self.deploy_private_ragservice_with_options(request, runtime)

    async def deploy_private_ragservice_async(
        self,
        request: main_models.DeployPrivateRAGServiceRequest,
    ) -> main_models.DeployPrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return await self.deploy_private_ragservice_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_sqlrecords_with_options(
        self,
        request: main_models.DescribeActiveSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_sqlrecords_with_options_async(
        self,
        request: main_models.DescribeActiveSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveSQLRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_sqlrecords(
        self,
        request: main_models.DescribeActiveSQLRecordsRequest,
    ) -> main_models.DescribeActiveSQLRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_active_sqlrecords_with_options(request, runtime)

    async def describe_active_sqlrecords_async(
        self,
        request: main_models.DescribeActiveSQLRecordsRequest,
    ) -> main_models.DescribeActiveSQLRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_sqlrecords_with_options_async(request, runtime)

    def describe_available_resources_with_options(
        self,
        request: main_models.DescribeAvailableResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resources_with_options_async(
        self,
        request: main_models.DescribeAvailableResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resources(
        self,
        request: main_models.DescribeAvailableResourcesRequest,
    ) -> main_models.DescribeAvailableResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_available_resources_with_options(request, runtime)

    async def describe_available_resources_async(
        self,
        request: main_models.DescribeAvailableResourcesRequest,
    ) -> main_models.DescribeAvailableResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_resources_with_options_async(request, runtime)

    def describe_backup_job_with_options(
        self,
        request: main_models.DescribeBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_job_with_options_async(
        self,
        request: main_models.DescribeBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_job(
        self,
        request: main_models.DescribeBackupJobRequest,
    ) -> main_models.DescribeBackupJobResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_job_with_options(request, runtime)

    async def describe_backup_job_async(
        self,
        request: main_models.DescribeBackupJobRequest,
    ) -> main_models.DescribeBackupJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_job_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_collection_with_options(
        self,
        request: main_models.DescribeCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_collection_with_options_async(
        self,
        request: main_models.DescribeCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_collection(
        self,
        request: main_models.DescribeCollectionRequest,
    ) -> main_models.DescribeCollectionResponse:
        runtime = RuntimeOptions()
        return self.describe_collection_with_options(request, runtime)

    async def describe_collection_async(
        self,
        request: main_models.DescribeCollectionRequest,
    ) -> main_models.DescribeCollectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_collection_with_options_async(request, runtime)

    def describe_create_index_job_with_options(
        self,
        request: main_models.DescribeCreateIndexJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCreateIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCreateIndexJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCreateIndexJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_create_index_job_with_options_async(
        self,
        request: main_models.DescribeCreateIndexJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCreateIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCreateIndexJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCreateIndexJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_create_index_job(
        self,
        request: main_models.DescribeCreateIndexJobRequest,
    ) -> main_models.DescribeCreateIndexJobResponse:
        runtime = RuntimeOptions()
        return self.describe_create_index_job_with_options(request, runtime)

    async def describe_create_index_job_async(
        self,
        request: main_models.DescribeCreateIndexJobRequest,
    ) -> main_models.DescribeCreateIndexJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_create_index_job_with_options_async(request, runtime)

    def describe_dbcluster_node_with_options(
        self,
        request: main_models.DescribeDBClusterNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_node_with_options_async(
        self,
        request: main_models.DescribeDBClusterNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_node(
        self,
        request: main_models.DescribeDBClusterNodeRequest,
    ) -> main_models.DescribeDBClusterNodeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_node_with_options(request, runtime)

    async def describe_dbcluster_node_async(
        self,
        request: main_models.DescribeDBClusterNodeRequest,
    ) -> main_models.DescribeDBClusterNodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_node_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.nodes):
            query['Nodes'] = request.nodes
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.nodes):
            query['Nodes'] = request.nodes
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_data_bloat_with_options(
        self,
        request: main_models.DescribeDBInstanceDataBloatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDataBloatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDataBloat',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDataBloatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_bloat_with_options_async(
        self,
        request: main_models.DescribeDBInstanceDataBloatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDataBloatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDataBloat',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDataBloatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_bloat(
        self,
        request: main_models.DescribeDBInstanceDataBloatRequest,
    ) -> main_models.DescribeDBInstanceDataBloatResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_data_bloat_with_options(request, runtime)

    async def describe_dbinstance_data_bloat_async(
        self,
        request: main_models.DescribeDBInstanceDataBloatRequest,
    ) -> main_models.DescribeDBInstanceDataBloatResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_data_bloat_with_options_async(request, runtime)

    def describe_dbinstance_data_skew_with_options(
        self,
        request: main_models.DescribeDBInstanceDataSkewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDataSkewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDataSkew',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDataSkewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_skew_with_options_async(
        self,
        request: main_models.DescribeDBInstanceDataSkewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDataSkewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDataSkew',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDataSkewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_skew(
        self,
        request: main_models.DescribeDBInstanceDataSkewRequest,
    ) -> main_models.DescribeDBInstanceDataSkewResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_data_skew_with_options(request, runtime)

    async def describe_dbinstance_data_skew_async(
        self,
        request: main_models.DescribeDBInstanceDataSkewRequest,
    ) -> main_models.DescribeDBInstanceDataSkewResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_data_skew_with_options_async(request, runtime)

    def describe_dbinstance_diagnosis_summary_with_options(
        self,
        request: main_models.DescribeDBInstanceDiagnosisSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDiagnosisSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_preferd):
            query['RolePreferd'] = request.role_preferd
        if not DaraCore.is_null(request.start_status):
            query['StartStatus'] = request.start_status
        if not DaraCore.is_null(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDiagnosisSummary',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDiagnosisSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_diagnosis_summary_with_options_async(
        self,
        request: main_models.DescribeDBInstanceDiagnosisSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceDiagnosisSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_preferd):
            query['RolePreferd'] = request.role_preferd
        if not DaraCore.is_null(request.start_status):
            query['StartStatus'] = request.start_status
        if not DaraCore.is_null(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceDiagnosisSummary',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceDiagnosisSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_diagnosis_summary(
        self,
        request: main_models.DescribeDBInstanceDiagnosisSummaryRequest,
    ) -> main_models.DescribeDBInstanceDiagnosisSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_diagnosis_summary_with_options(request, runtime)

    async def describe_dbinstance_diagnosis_summary_async(
        self,
        request: main_models.DescribeDBInstanceDiagnosisSummaryRequest,
    ) -> main_models.DescribeDBInstanceDiagnosisSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_diagnosis_summary_with_options_async(request, runtime)

    def describe_dbinstance_error_log_with_options(
        self,
        request: main_models.DescribeDBInstanceErrorLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceErrorLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceErrorLog',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceErrorLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_error_log_with_options_async(
        self,
        request: main_models.DescribeDBInstanceErrorLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceErrorLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceErrorLog',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceErrorLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_error_log(
        self,
        request: main_models.DescribeDBInstanceErrorLogRequest,
    ) -> main_models.DescribeDBInstanceErrorLogResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_error_log_with_options(request, runtime)

    async def describe_dbinstance_error_log_async(
        self,
        request: main_models.DescribeDBInstanceErrorLogRequest,
    ) -> main_models.DescribeDBInstanceErrorLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_error_log_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: main_models.DescribeDBInstanceIPArrayListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceIPArrayListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceIPArrayList',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_iparray_list_with_options_async(
        self,
        request: main_models.DescribeDBInstanceIPArrayListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceIPArrayListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceIPArrayList',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceIPArrayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(
        self,
        request: main_models.DescribeDBInstanceIPArrayListRequest,
    ) -> main_models.DescribeDBInstanceIPArrayListResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: main_models.DescribeDBInstanceIPArrayListRequest,
    ) -> main_models.DescribeDBInstanceIPArrayListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_index_usage_with_options(
        self,
        request: main_models.DescribeDBInstanceIndexUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceIndexUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceIndexUsage',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceIndexUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_index_usage_with_options_async(
        self,
        request: main_models.DescribeDBInstanceIndexUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceIndexUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceIndexUsage',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceIndexUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_index_usage(
        self,
        request: main_models.DescribeDBInstanceIndexUsageRequest,
    ) -> main_models.DescribeDBInstanceIndexUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_index_usage_with_options(request, runtime)

    async def describe_dbinstance_index_usage_async(
        self,
        request: main_models.DescribeDBInstanceIndexUsageRequest,
    ) -> main_models.DescribeDBInstanceIndexUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_index_usage_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceNetInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceNetInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_plans_with_options(
        self,
        request: main_models.DescribeDBInstancePlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_create_date):
            query['PlanCreateDate'] = request.plan_create_date
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePlans',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_plans_with_options_async(
        self,
        request: main_models.DescribeDBInstancePlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_create_date):
            query['PlanCreateDate'] = request.plan_create_date
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePlans',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_plans(
        self,
        request: main_models.DescribeDBInstancePlansRequest,
    ) -> main_models.DescribeDBInstancePlansResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_plans_with_options(request, runtime)

    async def describe_dbinstance_plans_async(
        self,
        request: main_models.DescribeDBInstancePlansRequest,
    ) -> main_models.DescribeDBInstancePlansResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_plans_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSSL',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSSL',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_support_max_performance_with_options(
        self,
        request: main_models.DescribeDBInstanceSupportMaxPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSupportMaxPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSupportMaxPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_support_max_performance_with_options_async(
        self,
        request: main_models.DescribeDBInstanceSupportMaxPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSupportMaxPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSupportMaxPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_support_max_performance(
        self,
        request: main_models.DescribeDBInstanceSupportMaxPerformanceRequest,
    ) -> main_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_support_max_performance_with_options(request, runtime)

    async def describe_dbinstance_support_max_performance_async(
        self,
        request: main_models.DescribeDBInstanceSupportMaxPerformanceRequest,
    ) -> main_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_support_max_performance_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        tmp_req: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeDBInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbinstance_categories):
            request.dbinstance_categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_categories, 'DBInstanceCategories', 'simple')
        if not DaraCore.is_null(tmp_req.dbinstance_modes):
            request.dbinstance_modes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_modes, 'DBInstanceModes', 'simple')
        if not DaraCore.is_null(tmp_req.dbinstance_statuses):
            request.dbinstance_statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_statuses, 'DBInstanceStatuses', 'simple')
        if not DaraCore.is_null(tmp_req.instance_deploy_types):
            request.instance_deploy_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_deploy_types, 'InstanceDeployTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_categories_shrink):
            query['DBInstanceCategories'] = request.dbinstance_categories_shrink
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstance_modes_shrink):
            query['DBInstanceModes'] = request.dbinstance_modes_shrink
        if not DaraCore.is_null(request.dbinstance_statuses_shrink):
            query['DBInstanceStatuses'] = request.dbinstance_statuses_shrink
        if not DaraCore.is_null(request.instance_deploy_types_shrink):
            query['InstanceDeployTypes'] = request.instance_deploy_types_shrink
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        tmp_req: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeDBInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbinstance_categories):
            request.dbinstance_categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_categories, 'DBInstanceCategories', 'simple')
        if not DaraCore.is_null(tmp_req.dbinstance_modes):
            request.dbinstance_modes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_modes, 'DBInstanceModes', 'simple')
        if not DaraCore.is_null(tmp_req.dbinstance_statuses):
            request.dbinstance_statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbinstance_statuses, 'DBInstanceStatuses', 'simple')
        if not DaraCore.is_null(tmp_req.instance_deploy_types):
            request.instance_deploy_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_deploy_types, 'InstanceDeployTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_categories_shrink):
            query['DBInstanceCategories'] = request.dbinstance_categories_shrink
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstance_modes_shrink):
            query['DBInstanceModes'] = request.dbinstance_modes_shrink
        if not DaraCore.is_null(request.dbinstance_statuses_shrink):
            query['DBInstanceStatuses'] = request.dbinstance_statuses_shrink
        if not DaraCore.is_null(request.instance_deploy_types_shrink):
            query['InstanceDeployTypes'] = request.instance_deploy_types_shrink
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: main_models.DescribeDBInstancesRequest,
    ) -> main_models.DescribeDBInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: main_models.DescribeDBInstancesRequest,
    ) -> main_models.DescribeDBInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_group_with_options_async(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_group(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
    ) -> main_models.DescribeDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
    ) -> main_models.DescribeDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_dbresource_management_mode_with_options(
        self,
        request: main_models.DescribeDBResourceManagementModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceManagementModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceManagementMode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceManagementModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_management_mode_with_options_async(
        self,
        request: main_models.DescribeDBResourceManagementModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceManagementModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceManagementMode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceManagementModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_management_mode(
        self,
        request: main_models.DescribeDBResourceManagementModeRequest,
    ) -> main_models.DescribeDBResourceManagementModeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbresource_management_mode_with_options(request, runtime)

    async def describe_dbresource_management_mode_async(
        self,
        request: main_models.DescribeDBResourceManagementModeRequest,
    ) -> main_models.DescribeDBResourceManagementModeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbresource_management_mode_with_options_async(request, runtime)

    def describe_dbversion_infos_with_options(
        self,
        request: main_models.DescribeDBVersionInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBVersionInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBVersionInfos',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBVersionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbversion_infos_with_options_async(
        self,
        request: main_models.DescribeDBVersionInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBVersionInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBVersionInfos',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBVersionInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbversion_infos(
        self,
        request: main_models.DescribeDBVersionInfosRequest,
    ) -> main_models.DescribeDBVersionInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_dbversion_infos_with_options(request, runtime)

    async def describe_dbversion_infos_async(
        self,
        request: main_models.DescribeDBVersionInfosRequest,
    ) -> main_models.DescribeDBVersionInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbversion_infos_with_options_async(request, runtime)

    def describe_data_backups_with_options(
        self,
        request: main_models.DescribeDataBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataBackups',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_backups_with_options_async(
        self,
        request: main_models.DescribeDataBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataBackups',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_backups(
        self,
        request: main_models.DescribeDataBackupsRequest,
    ) -> main_models.DescribeDataBackupsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_backups_with_options(request, runtime)

    async def describe_data_backups_async(
        self,
        request: main_models.DescribeDataBackupsRequest,
    ) -> main_models.DescribeDataBackupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_backups_with_options_async(request, runtime)

    def describe_data_re_distribute_info_with_options(
        self,
        request: main_models.DescribeDataReDistributeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataReDistributeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataReDistributeInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataReDistributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_re_distribute_info_with_options_async(
        self,
        request: main_models.DescribeDataReDistributeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataReDistributeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataReDistributeInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataReDistributeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_re_distribute_info(
        self,
        request: main_models.DescribeDataReDistributeInfoRequest,
    ) -> main_models.DescribeDataReDistributeInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_data_re_distribute_info_with_options(request, runtime)

    async def describe_data_re_distribute_info_async(
        self,
        request: main_models.DescribeDataReDistributeInfoRequest,
    ) -> main_models.DescribeDataReDistributeInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_re_distribute_info_with_options_async(request, runtime)

    def describe_data_share_instances_with_options(
        self,
        request: main_models.DescribeDataShareInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataShareInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataShareInstances',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataShareInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_share_instances_with_options_async(
        self,
        request: main_models.DescribeDataShareInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataShareInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataShareInstances',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataShareInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_share_instances(
        self,
        request: main_models.DescribeDataShareInstancesRequest,
    ) -> main_models.DescribeDataShareInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_data_share_instances_with_options(request, runtime)

    async def describe_data_share_instances_async(
        self,
        request: main_models.DescribeDataShareInstancesRequest,
    ) -> main_models.DescribeDataShareInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_share_instances_with_options_async(request, runtime)

    def describe_data_share_performance_with_options(
        self,
        request: main_models.DescribeDataSharePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSharePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSharePerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSharePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_share_performance_with_options_async(
        self,
        request: main_models.DescribeDataSharePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSharePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSharePerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSharePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_share_performance(
        self,
        request: main_models.DescribeDataSharePerformanceRequest,
    ) -> main_models.DescribeDataSharePerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_data_share_performance_with_options(request, runtime)

    async def describe_data_share_performance_async(
        self,
        request: main_models.DescribeDataSharePerformanceRequest,
    ) -> main_models.DescribeDataSharePerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_share_performance_with_options_async(request, runtime)

    def describe_database_with_options(
        self,
        request: main_models.DescribeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_with_options_async(
        self,
        request: main_models.DescribeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database(
        self,
        request: main_models.DescribeDatabaseRequest,
    ) -> main_models.DescribeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.describe_database_with_options(request, runtime)

    async def describe_database_async(
        self,
        request: main_models.DescribeDatabaseRequest,
    ) -> main_models.DescribeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisDimensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisDimensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisMonitorPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisMonitorPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_monitor_performance_with_options_async(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisMonitorPerformance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisMonitorPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_monitor_performance(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    async def describe_diagnosis_monitor_performance_async(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_monitor_performance_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.query_id):
            query['QueryID'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.query_id):
            query['QueryID'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_document_with_options(
        self,
        request: main_models.DescribeDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_document_with_options_async(
        self,
        request: main_models.DescribeDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_document(
        self,
        request: main_models.DescribeDocumentRequest,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        return self.describe_document_with_options(request, runtime)

    async def describe_document_async(
        self,
        request: main_models.DescribeDocumentRequest,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        return await self.describe_document_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.download_task_type):
            query['DownloadTaskType'] = request.download_task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.download_task_type):
            query['DownloadTaskType'] = request.download_task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
    ) -> main_models.DescribeDownloadRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
    ) -> main_models.DescribeDownloadRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_download_sqllogs_with_options(
        self,
        request: main_models.DescribeDownloadSQLLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadSQLLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadSQLLogs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_sqllogs_with_options_async(
        self,
        request: main_models.DescribeDownloadSQLLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadSQLLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadSQLLogs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadSQLLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_sqllogs(
        self,
        request: main_models.DescribeDownloadSQLLogsRequest,
    ) -> main_models.DescribeDownloadSQLLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_download_sqllogs_with_options(request, runtime)

    async def describe_download_sqllogs_async(
        self,
        request: main_models.DescribeDownloadSQLLogsRequest,
    ) -> main_models.DescribeDownloadSQLLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_sqllogs_with_options_async(request, runtime)

    def describe_extension_with_options(
        self,
        request: main_models.DescribeExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.extension_name):
            query['ExtensionName'] = request.extension_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExtension',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_extension_with_options_async(
        self,
        request: main_models.DescribeExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.extension_name):
            query['ExtensionName'] = request.extension_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExtension',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_extension(
        self,
        request: main_models.DescribeExtensionRequest,
    ) -> main_models.DescribeExtensionResponse:
        runtime = RuntimeOptions()
        return self.describe_extension_with_options(request, runtime)

    async def describe_extension_async(
        self,
        request: main_models.DescribeExtensionRequest,
    ) -> main_models.DescribeExtensionResponse:
        runtime = RuntimeOptions()
        return await self.describe_extension_with_options_async(request, runtime)

    def describe_external_data_service_with_options(
        self,
        request: main_models.DescribeExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_external_data_service_with_options_async(
        self,
        request: main_models.DescribeExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExternalDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_external_data_service(
        self,
        request: main_models.DescribeExternalDataServiceRequest,
    ) -> main_models.DescribeExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_external_data_service_with_options(request, runtime)

    async def describe_external_data_service_async(
        self,
        request: main_models.DescribeExternalDataServiceRequest,
    ) -> main_models.DescribeExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_external_data_service_with_options_async(request, runtime)

    def describe_hadoop_clusters_in_same_net_with_options(
        self,
        request: main_models.DescribeHadoopClustersInSameNetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopClustersInSameNetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopClustersInSameNet',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopClustersInSameNetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hadoop_clusters_in_same_net_with_options_async(
        self,
        request: main_models.DescribeHadoopClustersInSameNetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopClustersInSameNetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopClustersInSameNet',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopClustersInSameNetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hadoop_clusters_in_same_net(
        self,
        request: main_models.DescribeHadoopClustersInSameNetRequest,
    ) -> main_models.DescribeHadoopClustersInSameNetResponse:
        runtime = RuntimeOptions()
        return self.describe_hadoop_clusters_in_same_net_with_options(request, runtime)

    async def describe_hadoop_clusters_in_same_net_async(
        self,
        request: main_models.DescribeHadoopClustersInSameNetRequest,
    ) -> main_models.DescribeHadoopClustersInSameNetResponse:
        runtime = RuntimeOptions()
        return await self.describe_hadoop_clusters_in_same_net_with_options_async(request, runtime)

    def describe_hadoop_configs_with_options(
        self,
        request: main_models.DescribeHadoopConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopConfigs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hadoop_configs_with_options_async(
        self,
        request: main_models.DescribeHadoopConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopConfigs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hadoop_configs(
        self,
        request: main_models.DescribeHadoopConfigsRequest,
    ) -> main_models.DescribeHadoopConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_hadoop_configs_with_options(request, runtime)

    async def describe_hadoop_configs_async(
        self,
        request: main_models.DescribeHadoopConfigsRequest,
    ) -> main_models.DescribeHadoopConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_hadoop_configs_with_options_async(request, runtime)

    def describe_hadoop_data_source_with_options(
        self,
        request: main_models.DescribeHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hadoop_data_source_with_options_async(
        self,
        request: main_models.DescribeHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHadoopDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hadoop_data_source(
        self,
        request: main_models.DescribeHadoopDataSourceRequest,
    ) -> main_models.DescribeHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_hadoop_data_source_with_options(request, runtime)

    async def describe_hadoop_data_source_async(
        self,
        request: main_models.DescribeHadoopDataSourceRequest,
    ) -> main_models.DescribeHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_hadoop_data_source_with_options_async(request, runtime)

    def describe_health_status_with_options(
        self,
        request: main_models.DescribeHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_status_with_options_async(
        self,
        request: main_models.DescribeHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_status(
        self,
        request: main_models.DescribeHealthStatusRequest,
    ) -> main_models.DescribeHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    async def describe_health_status_async(
        self,
        request: main_models.DescribeHealthStatusRequest,
    ) -> main_models.DescribeHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_status_with_options_async(request, runtime)

    def describe_imvinfos_with_options(
        self,
        request: main_models.DescribeIMVInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIMVInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.mvname):
            query['MVName'] = request.mvname
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIMVInfos',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIMVInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imvinfos_with_options_async(
        self,
        request: main_models.DescribeIMVInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIMVInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.mvname):
            query['MVName'] = request.mvname
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIMVInfos',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIMVInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imvinfos(
        self,
        request: main_models.DescribeIMVInfosRequest,
    ) -> main_models.DescribeIMVInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_imvinfos_with_options(request, runtime)

    async def describe_imvinfos_async(
        self,
        request: main_models.DescribeIMVInfosRequest,
    ) -> main_models.DescribeIMVInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_imvinfos_with_options_async(request, runtime)

    def describe_index_with_options(
        self,
        request: main_models.DescribeIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_index_with_options_async(
        self,
        request: main_models.DescribeIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIndex',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_index(
        self,
        request: main_models.DescribeIndexRequest,
    ) -> main_models.DescribeIndexResponse:
        runtime = RuntimeOptions()
        return self.describe_index_with_options(request, runtime)

    async def describe_index_async(
        self,
        request: main_models.DescribeIndexRequest,
    ) -> main_models.DescribeIndexResponse:
        runtime = RuntimeOptions()
        return await self.describe_index_with_options_async(request, runtime)

    def describe_jdbcdata_source_with_options(
        self,
        request: main_models.DescribeJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_jdbcdata_source_with_options_async(
        self,
        request: main_models.DescribeJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJDBCDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_jdbcdata_source(
        self,
        request: main_models.DescribeJDBCDataSourceRequest,
    ) -> main_models.DescribeJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_jdbcdata_source_with_options(request, runtime)

    async def describe_jdbcdata_source_async(
        self,
        request: main_models.DescribeJDBCDataSourceRequest,
    ) -> main_models.DescribeJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_jdbcdata_source_with_options_async(request, runtime)

    def describe_log_backups_with_options(
        self,
        request: main_models.DescribeLogBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogBackups',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_backups_with_options_async(
        self,
        request: main_models.DescribeLogBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogBackups',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_backups(
        self,
        request: main_models.DescribeLogBackupsRequest,
    ) -> main_models.DescribeLogBackupsResponse:
        runtime = RuntimeOptions()
        return self.describe_log_backups_with_options(request, runtime)

    async def describe_log_backups_async(
        self,
        request: main_models.DescribeLogBackupsRequest,
    ) -> main_models.DescribeLogBackupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_backups_with_options_async(request, runtime)

    def describe_model_service_with_options(
        self,
        request: main_models.DescribeModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.model_service_id):
            query['ModelServiceId'] = request.model_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_service_with_options_async(
        self,
        request: main_models.DescribeModelServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.model_service_id):
            query['ModelServiceId'] = request.model_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_service(
        self,
        request: main_models.DescribeModelServiceRequest,
    ) -> main_models.DescribeModelServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_model_service_with_options(request, runtime)

    async def describe_model_service_async(
        self,
        request: main_models.DescribeModelServiceRequest,
    ) -> main_models.DescribeModelServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_service_with_options_async(request, runtime)

    def describe_modify_parameter_log_with_options(
        self,
        request: main_models.DescribeModifyParameterLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModifyParameterLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModifyParameterLog',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_modify_parameter_log_with_options_async(
        self,
        request: main_models.DescribeModifyParameterLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModifyParameterLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModifyParameterLog',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModifyParameterLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_modify_parameter_log(
        self,
        request: main_models.DescribeModifyParameterLogRequest,
    ) -> main_models.DescribeModifyParameterLogResponse:
        runtime = RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    async def describe_modify_parameter_log_async(
        self,
        request: main_models.DescribeModifyParameterLogRequest,
    ) -> main_models.DescribeModifyParameterLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_modify_parameter_log_with_options_async(request, runtime)

    def describe_namespace_with_options(
        self,
        request: main_models.DescribeNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: main_models.DescribeNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespace',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: main_models.DescribeNamespaceRequest,
    ) -> main_models.DescribeNamespaceResponse:
        runtime = RuntimeOptions()
        return self.describe_namespace_with_options(request, runtime)

    async def describe_namespace_async(
        self,
        request: main_models.DescribeNamespaceRequest,
    ) -> main_models.DescribeNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.describe_namespace_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: main_models.DescribeParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameters',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: main_models.DescribeParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameters',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: main_models.DescribeParametersRequest,
    ) -> main_models.DescribeParametersResponse:
        runtime = RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: main_models.DescribeParametersRequest,
    ) -> main_models.DescribeParametersResponse:
        runtime = RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_private_ragservice_with_options(
        self,
        request: main_models.DescribePrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateRAGServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_ragservice_with_options_async(
        self,
        request: main_models.DescribePrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateRAGServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_ragservice(
        self,
        request: main_models.DescribePrivateRAGServiceRequest,
    ) -> main_models.DescribePrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_private_ragservice_with_options(request, runtime)

    async def describe_private_ragservice_async(
        self,
        request: main_models.DescribePrivateRAGServiceRequest,
    ) -> main_models.DescribePrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_ragservice_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVSwitchs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitchs_with_options_async(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVSwitchs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitchs(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: main_models.DescribeRdsVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVpcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vpcs_with_options_async(
        self,
        request: main_models.DescribeRdsVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVpcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vpcs(
        self,
        request: main_models.DescribeRdsVpcsRequest,
    ) -> main_models.DescribeRdsVpcsResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: main_models.DescribeRdsVpcsRequest,
    ) -> main_models.DescribeRdsVpcsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_rebalance_status_with_options(
        self,
        request: main_models.DescribeRebalanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRebalanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRebalanceStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRebalanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rebalance_status_with_options_async(
        self,
        request: main_models.DescribeRebalanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRebalanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRebalanceStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRebalanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rebalance_status(
        self,
        request: main_models.DescribeRebalanceStatusRequest,
    ) -> main_models.DescribeRebalanceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_rebalance_status_with_options(request, runtime)

    async def describe_rebalance_status_async(
        self,
        request: main_models.DescribeRebalanceStatusRequest,
    ) -> main_models.DescribeRebalanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_rebalance_status_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_roles_with_options(
        self,
        request: main_models.DescribeRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoles',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_roles_with_options_async(
        self,
        request: main_models.DescribeRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoles',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_roles(
        self,
        request: main_models.DescribeRolesRequest,
    ) -> main_models.DescribeRolesResponse:
        runtime = RuntimeOptions()
        return self.describe_roles_with_options(request, runtime)

    async def describe_roles_async(
        self,
        request: main_models.DescribeRolesRequest,
    ) -> main_models.DescribeRolesResponse:
        runtime = RuntimeOptions()
        return await self.describe_roles_with_options_async(request, runtime)

    def describe_sqllog_count_with_options(
        self,
        request: main_models.DescribeSQLLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogCount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_count_with_options_async(
        self,
        request: main_models.DescribeSQLLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogCount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_count(
        self,
        request: main_models.DescribeSQLLogCountRequest,
    ) -> main_models.DescribeSQLLogCountResponse:
        runtime = RuntimeOptions()
        return self.describe_sqllog_count_with_options(request, runtime)

    async def describe_sqllog_count_async(
        self,
        request: main_models.DescribeSQLLogCountRequest,
    ) -> main_models.DescribeSQLLogCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqllog_count_with_options_async(request, runtime)

    def describe_sqllogs_with_options(
        self,
        request: main_models.DescribeSQLLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllogs_with_options_async(
        self,
        request: main_models.DescribeSQLLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllogs(
        self,
        request: main_models.DescribeSQLLogsRequest,
    ) -> main_models.DescribeSQLLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_sqllogs_with_options(request, runtime)

    async def describe_sqllogs_async(
        self,
        request: main_models.DescribeSQLLogsRequest,
    ) -> main_models.DescribeSQLLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqllogs_with_options_async(request, runtime)

    def describe_sqllogs_v2with_options(
        self,
        request: main_models.DescribeSQLLogsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogsV2',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllogs_v2with_options_async(
        self,
        request: main_models.DescribeSQLLogsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLLogsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLLogsV2',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLLogsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllogs_v2(
        self,
        request: main_models.DescribeSQLLogsV2Request,
    ) -> main_models.DescribeSQLLogsV2Response:
        runtime = RuntimeOptions()
        return self.describe_sqllogs_v2with_options(request, runtime)

    async def describe_sqllogs_v2_async(
        self,
        request: main_models.DescribeSQLLogsV2Request,
    ) -> main_models.DescribeSQLLogsV2Response:
        runtime = RuntimeOptions()
        return await self.describe_sqllogs_v2with_options_async(request, runtime)

    def describe_sample_data_with_options(
        self,
        request: main_models.DescribeSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_data_with_options_async(
        self,
        request: main_models.DescribeSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_data(
        self,
        request: main_models.DescribeSampleDataRequest,
    ) -> main_models.DescribeSampleDataResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_data_with_options(request, runtime)

    async def describe_sample_data_async(
        self,
        request: main_models.DescribeSampleDataRequest,
    ) -> main_models.DescribeSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_data_with_options_async(request, runtime)

    def describe_streaming_data_service_with_options(
        self,
        request: main_models.DescribeStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streaming_data_service_with_options_async(
        self,
        request: main_models.DescribeStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streaming_data_service(
        self,
        request: main_models.DescribeStreamingDataServiceRequest,
    ) -> main_models.DescribeStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_streaming_data_service_with_options(request, runtime)

    async def describe_streaming_data_service_async(
        self,
        request: main_models.DescribeStreamingDataServiceRequest,
    ) -> main_models.DescribeStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_streaming_data_service_with_options_async(request, runtime)

    def describe_streaming_data_source_with_options(
        self,
        request: main_models.DescribeStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streaming_data_source_with_options_async(
        self,
        request: main_models.DescribeStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streaming_data_source(
        self,
        request: main_models.DescribeStreamingDataSourceRequest,
    ) -> main_models.DescribeStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_streaming_data_source_with_options(request, runtime)

    async def describe_streaming_data_source_async(
        self,
        request: main_models.DescribeStreamingDataSourceRequest,
    ) -> main_models.DescribeStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_streaming_data_source_with_options_async(request, runtime)

    def describe_streaming_job_with_options(
        self,
        request: main_models.DescribeStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streaming_job_with_options_async(
        self,
        request: main_models.DescribeStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streaming_job(
        self,
        request: main_models.DescribeStreamingJobRequest,
    ) -> main_models.DescribeStreamingJobResponse:
        runtime = RuntimeOptions()
        return self.describe_streaming_job_with_options(request, runtime)

    async def describe_streaming_job_async(
        self,
        request: main_models.DescribeStreamingJobRequest,
    ) -> main_models.DescribeStreamingJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_streaming_job_with_options_async(request, runtime)

    def describe_support_features_with_options(
        self,
        request: main_models.DescribeSupportFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportFeatures',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_features_with_options_async(
        self,
        request: main_models.DescribeSupportFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportFeatures',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_features(
        self,
        request: main_models.DescribeSupportFeaturesRequest,
    ) -> main_models.DescribeSupportFeaturesResponse:
        runtime = RuntimeOptions()
        return self.describe_support_features_with_options(request, runtime)

    async def describe_support_features_async(
        self,
        request: main_models.DescribeSupportFeaturesRequest,
    ) -> main_models.DescribeSupportFeaturesResponse:
        runtime = RuntimeOptions()
        return await self.describe_support_features_with_options_async(request, runtime)

    def describe_table_with_options(
        self,
        request: main_models.DescribeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTable',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_with_options_async(
        self,
        request: main_models.DescribeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTable',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table(
        self,
        request: main_models.DescribeTableRequest,
    ) -> main_models.DescribeTableResponse:
        runtime = RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    async def describe_table_async(
        self,
        request: main_models.DescribeTableRequest,
    ) -> main_models.DescribeTableResponse:
        runtime = RuntimeOptions()
        return await self.describe_table_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        runtime = RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def describe_waiting_sqlinfo_with_options(
        self,
        request: main_models.DescribeWaitingSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWaitingSQLInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.pid):
            query['PID'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWaitingSQLInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWaitingSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waiting_sqlinfo_with_options_async(
        self,
        request: main_models.DescribeWaitingSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWaitingSQLInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.pid):
            query['PID'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWaitingSQLInfo',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWaitingSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waiting_sqlinfo(
        self,
        request: main_models.DescribeWaitingSQLInfoRequest,
    ) -> main_models.DescribeWaitingSQLInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_waiting_sqlinfo_with_options(request, runtime)

    async def describe_waiting_sqlinfo_async(
        self,
        request: main_models.DescribeWaitingSQLInfoRequest,
    ) -> main_models.DescribeWaitingSQLInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_waiting_sqlinfo_with_options_async(request, runtime)

    def describe_waiting_sqlrecords_with_options(
        self,
        request: main_models.DescribeWaitingSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWaitingSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWaitingSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWaitingSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waiting_sqlrecords_with_options_async(
        self,
        request: main_models.DescribeWaitingSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWaitingSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWaitingSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWaitingSQLRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waiting_sqlrecords(
        self,
        request: main_models.DescribeWaitingSQLRecordsRequest,
    ) -> main_models.DescribeWaitingSQLRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_waiting_sqlrecords_with_options(request, runtime)

    async def describe_waiting_sqlrecords_async(
        self,
        request: main_models.DescribeWaitingSQLRecordsRequest,
    ) -> main_models.DescribeWaitingSQLRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_waiting_sqlrecords_with_options_async(request, runtime)

    def describe_zones_private_ragservice_with_options(
        self,
        request: main_models.DescribeZonesPrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesPrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZonesPrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesPrivateRAGServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_private_ragservice_with_options_async(
        self,
        request: main_models.DescribeZonesPrivateRAGServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesPrivateRAGServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZonesPrivateRAGService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesPrivateRAGServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones_private_ragservice(
        self,
        request: main_models.DescribeZonesPrivateRAGServiceRequest,
    ) -> main_models.DescribeZonesPrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_private_ragservice_with_options(request, runtime)

    async def describe_zones_private_ragservice_async(
        self,
        request: main_models.DescribeZonesPrivateRAGServiceRequest,
    ) -> main_models.DescribeZonesPrivateRAGServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_private_ragservice_with_options_async(request, runtime)

    def disable_dbresource_group_with_options(
        self,
        request: main_models.DisableDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_dbresource_group_with_options_async(
        self,
        request: main_models.DisableDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_dbresource_group(
        self,
        request: main_models.DisableDBResourceGroupRequest,
    ) -> main_models.DisableDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.disable_dbresource_group_with_options(request, runtime)

    async def disable_dbresource_group_async(
        self,
        request: main_models.DisableDBResourceGroupRequest,
    ) -> main_models.DisableDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.disable_dbresource_group_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadDiagnosisRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadDiagnosisRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def download_sqllogs_records_with_options(
        self,
        request: main_models.DownloadSQLLogsRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSQLLogsRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSQLLogsRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSQLLogsRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_sqllogs_records_with_options_async(
        self,
        request: main_models.DownloadSQLLogsRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSQLLogsRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not DaraCore.is_null(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not DaraCore.is_null(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not DaraCore.is_null(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSQLLogsRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSQLLogsRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_sqllogs_records(
        self,
        request: main_models.DownloadSQLLogsRecordsRequest,
    ) -> main_models.DownloadSQLLogsRecordsResponse:
        runtime = RuntimeOptions()
        return self.download_sqllogs_records_with_options(request, runtime)

    async def download_sqllogs_records_async(
        self,
        request: main_models.DownloadSQLLogsRecordsRequest,
    ) -> main_models.DownloadSQLLogsRecordsResponse:
        runtime = RuntimeOptions()
        return await self.download_sqllogs_records_with_options_async(request, runtime)

    def download_slow_sqlrecords_with_options(
        self,
        request: main_models.DownloadSlowSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSlowSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSlowSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSlowSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_slow_sqlrecords_with_options_async(
        self,
        request: main_models.DownloadSlowSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSlowSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSlowSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSlowSQLRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_slow_sqlrecords(
        self,
        request: main_models.DownloadSlowSQLRecordsRequest,
    ) -> main_models.DownloadSlowSQLRecordsResponse:
        runtime = RuntimeOptions()
        return self.download_slow_sqlrecords_with_options(request, runtime)

    async def download_slow_sqlrecords_async(
        self,
        request: main_models.DownloadSlowSQLRecordsRequest,
    ) -> main_models.DownloadSlowSQLRecordsResponse:
        runtime = RuntimeOptions()
        return await self.download_slow_sqlrecords_with_options_async(request, runtime)

    def enable_collection_graph_ragwith_options(
        self,
        tmp_req: main_models.EnableCollectionGraphRAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCollectionGraphRAGResponse:
        tmp_req.validate()
        request = main_models.EnableCollectionGraphRAGShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.entity_types):
            request.entity_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.entity_types, 'EntityTypes', 'json')
        if not DaraCore.is_null(tmp_req.relationship_types):
            request.relationship_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.relationship_types, 'RelationshipTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.entity_types_shrink):
            query['EntityTypes'] = request.entity_types_shrink
        if not DaraCore.is_null(request.llmmodel):
            query['LLMModel'] = request.llmmodel
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relationship_types_shrink):
            query['RelationshipTypes'] = request.relationship_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCollectionGraphRAG',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCollectionGraphRAGResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_collection_graph_ragwith_options_async(
        self,
        tmp_req: main_models.EnableCollectionGraphRAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCollectionGraphRAGResponse:
        tmp_req.validate()
        request = main_models.EnableCollectionGraphRAGShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.entity_types):
            request.entity_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.entity_types, 'EntityTypes', 'json')
        if not DaraCore.is_null(tmp_req.relationship_types):
            request.relationship_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.relationship_types, 'RelationshipTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.entity_types_shrink):
            query['EntityTypes'] = request.entity_types_shrink
        if not DaraCore.is_null(request.llmmodel):
            query['LLMModel'] = request.llmmodel
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relationship_types_shrink):
            query['RelationshipTypes'] = request.relationship_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCollectionGraphRAG',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCollectionGraphRAGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_collection_graph_rag(
        self,
        request: main_models.EnableCollectionGraphRAGRequest,
    ) -> main_models.EnableCollectionGraphRAGResponse:
        runtime = RuntimeOptions()
        return self.enable_collection_graph_ragwith_options(request, runtime)

    async def enable_collection_graph_rag_async(
        self,
        request: main_models.EnableCollectionGraphRAGRequest,
    ) -> main_models.EnableCollectionGraphRAGResponse:
        runtime = RuntimeOptions()
        return await self.enable_collection_graph_ragwith_options_async(request, runtime)

    def enable_dbresource_group_with_options(
        self,
        request: main_models.EnableDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_dbresource_group_with_options_async(
        self,
        request: main_models.EnableDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_dbresource_group(
        self,
        request: main_models.EnableDBResourceGroupRequest,
    ) -> main_models.EnableDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.enable_dbresource_group_with_options(request, runtime)

    async def enable_dbresource_group_async(
        self,
        request: main_models.EnableDBResourceGroupRequest,
    ) -> main_models.EnableDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.enable_dbresource_group_with_options_async(request, runtime)

    def execute_statement_with_options(
        self,
        tmp_req: main_models.ExecuteStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteStatementResponse:
        tmp_req.validate()
        request = main_models.ExecuteStatementShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.rag_workspace_collection):
            request.rag_workspace_collection_shrink = Utils.array_to_string_with_specified_style(tmp_req.rag_workspace_collection, 'RagWorkspaceCollection', 'json')
        if not DaraCore.is_null(tmp_req.sqls):
            request.sqls_shrink = Utils.array_to_string_with_specified_style(tmp_req.sqls, 'Sqls', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rag_workspace_collection_shrink):
            query['RagWorkspaceCollection'] = request.rag_workspace_collection_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.run_type):
            query['RunType'] = request.run_type
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.statement_name):
            query['StatementName'] = request.statement_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.sql):
            body['Sql'] = request.sql
        if not DaraCore.is_null(request.sqls_shrink):
            body['Sqls'] = request.sqls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteStatement',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_statement_with_options_async(
        self,
        tmp_req: main_models.ExecuteStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteStatementResponse:
        tmp_req.validate()
        request = main_models.ExecuteStatementShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.rag_workspace_collection):
            request.rag_workspace_collection_shrink = Utils.array_to_string_with_specified_style(tmp_req.rag_workspace_collection, 'RagWorkspaceCollection', 'json')
        if not DaraCore.is_null(tmp_req.sqls):
            request.sqls_shrink = Utils.array_to_string_with_specified_style(tmp_req.sqls, 'Sqls', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rag_workspace_collection_shrink):
            query['RagWorkspaceCollection'] = request.rag_workspace_collection_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.run_type):
            query['RunType'] = request.run_type
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.statement_name):
            query['StatementName'] = request.statement_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.sql):
            body['Sql'] = request.sql
        if not DaraCore.is_null(request.sqls_shrink):
            body['Sqls'] = request.sqls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteStatement',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_statement(
        self,
        request: main_models.ExecuteStatementRequest,
    ) -> main_models.ExecuteStatementResponse:
        runtime = RuntimeOptions()
        return self.execute_statement_with_options(request, runtime)

    async def execute_statement_async(
        self,
        request: main_models.ExecuteStatementRequest,
    ) -> main_models.ExecuteStatementResponse:
        runtime = RuntimeOptions()
        return await self.execute_statement_with_options_async(request, runtime)

    def get_account_with_options(
        self,
        request: main_models.GetAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_with_options_async(
        self,
        request: main_models.GetAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account(
        self,
        request: main_models.GetAccountRequest,
    ) -> main_models.GetAccountResponse:
        runtime = RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    async def get_account_async(
        self,
        request: main_models.GetAccountRequest,
    ) -> main_models.GetAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_account_with_options_async(request, runtime)

    def get_graph_ragjob_with_options(
        self,
        request: main_models.GetGraphRAGJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGraphRAGJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGraphRAGJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGraphRAGJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_graph_ragjob_with_options_async(
        self,
        request: main_models.GetGraphRAGJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGraphRAGJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGraphRAGJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGraphRAGJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_graph_ragjob(
        self,
        request: main_models.GetGraphRAGJobRequest,
    ) -> main_models.GetGraphRAGJobResponse:
        runtime = RuntimeOptions()
        return self.get_graph_ragjob_with_options(request, runtime)

    async def get_graph_ragjob_async(
        self,
        request: main_models.GetGraphRAGJobRequest,
    ) -> main_models.GetGraphRAGJobResponse:
        runtime = RuntimeOptions()
        return await self.get_graph_ragjob_with_options_async(request, runtime)

    def get_secret_value_with_options(
        self,
        request: main_models.GetSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_value_with_options_async(
        self,
        request: main_models.GetSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_value(
        self,
        request: main_models.GetSecretValueRequest,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    async def get_secret_value_async(
        self,
        request: main_models.GetSecretValueRequest,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_value_with_options_async(request, runtime)

    def get_statement_result_with_options(
        self,
        request: main_models.GetStatementResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStatementResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStatementResult',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStatementResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_statement_result_with_options_async(
        self,
        request: main_models.GetStatementResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStatementResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStatementResult',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStatementResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_statement_result(
        self,
        request: main_models.GetStatementResultRequest,
    ) -> main_models.GetStatementResultResponse:
        runtime = RuntimeOptions()
        return self.get_statement_result_with_options(request, runtime)

    async def get_statement_result_async(
        self,
        request: main_models.GetStatementResultRequest,
    ) -> main_models.GetStatementResultResponse:
        runtime = RuntimeOptions()
        return await self.get_statement_result_with_options_async(request, runtime)

    def get_supabase_project_with_options(
        self,
        request: main_models.GetSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supabase_project_with_options_async(
        self,
        request: main_models.GetSupabaseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProject',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supabase_project(
        self,
        request: main_models.GetSupabaseProjectRequest,
    ) -> main_models.GetSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return self.get_supabase_project_with_options(request, runtime)

    async def get_supabase_project_async(
        self,
        request: main_models.GetSupabaseProjectRequest,
    ) -> main_models.GetSupabaseProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_supabase_project_with_options_async(request, runtime)

    def get_supabase_project_api_keys_with_options(
        self,
        request: main_models.GetSupabaseProjectApiKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProjectApiKeys',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectApiKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supabase_project_api_keys_with_options_async(
        self,
        request: main_models.GetSupabaseProjectApiKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProjectApiKeys',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectApiKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supabase_project_api_keys(
        self,
        request: main_models.GetSupabaseProjectApiKeysRequest,
    ) -> main_models.GetSupabaseProjectApiKeysResponse:
        runtime = RuntimeOptions()
        return self.get_supabase_project_api_keys_with_options(request, runtime)

    async def get_supabase_project_api_keys_async(
        self,
        request: main_models.GetSupabaseProjectApiKeysRequest,
    ) -> main_models.GetSupabaseProjectApiKeysResponse:
        runtime = RuntimeOptions()
        return await self.get_supabase_project_api_keys_with_options_async(request, runtime)

    def get_supabase_project_dashboard_account_with_options(
        self,
        request: main_models.GetSupabaseProjectDashboardAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectDashboardAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProjectDashboardAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectDashboardAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supabase_project_dashboard_account_with_options_async(
        self,
        request: main_models.GetSupabaseProjectDashboardAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupabaseProjectDashboardAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupabaseProjectDashboardAccount',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupabaseProjectDashboardAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supabase_project_dashboard_account(
        self,
        request: main_models.GetSupabaseProjectDashboardAccountRequest,
    ) -> main_models.GetSupabaseProjectDashboardAccountResponse:
        runtime = RuntimeOptions()
        return self.get_supabase_project_dashboard_account_with_options(request, runtime)

    async def get_supabase_project_dashboard_account_async(
        self,
        request: main_models.GetSupabaseProjectDashboardAccountRequest,
    ) -> main_models.GetSupabaseProjectDashboardAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_supabase_project_dashboard_account_with_options_async(request, runtime)

    def get_upload_document_job_with_options(
        self,
        request: main_models.GetUploadDocumentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadDocumentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadDocumentJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadDocumentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_document_job_with_options_async(
        self,
        request: main_models.GetUploadDocumentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadDocumentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadDocumentJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadDocumentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_document_job(
        self,
        request: main_models.GetUploadDocumentJobRequest,
    ) -> main_models.GetUploadDocumentJobResponse:
        runtime = RuntimeOptions()
        return self.get_upload_document_job_with_options(request, runtime)

    async def get_upload_document_job_async(
        self,
        request: main_models.GetUploadDocumentJobRequest,
    ) -> main_models.GetUploadDocumentJobResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_document_job_with_options_async(request, runtime)

    def get_upsert_collection_data_job_with_options(
        self,
        request: main_models.GetUpsertCollectionDataJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUpsertCollectionDataJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUpsertCollectionDataJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUpsertCollectionDataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upsert_collection_data_job_with_options_async(
        self,
        request: main_models.GetUpsertCollectionDataJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUpsertCollectionDataJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUpsertCollectionDataJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUpsertCollectionDataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upsert_collection_data_job(
        self,
        request: main_models.GetUpsertCollectionDataJobRequest,
    ) -> main_models.GetUpsertCollectionDataJobResponse:
        runtime = RuntimeOptions()
        return self.get_upsert_collection_data_job_with_options(request, runtime)

    async def get_upsert_collection_data_job_async(
        self,
        request: main_models.GetUpsertCollectionDataJobRequest,
    ) -> main_models.GetUpsertCollectionDataJobResponse:
        runtime = RuntimeOptions()
        return await self.get_upsert_collection_data_job_with_options_async(request, runtime)

    def grant_collection_with_options(
        self,
        request: main_models.GrantCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.grant_to_namespace):
            query['GrantToNamespace'] = request.grant_to_namespace
        if not DaraCore.is_null(request.grant_type):
            query['GrantType'] = request.grant_type
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_collection_with_options_async(
        self,
        request: main_models.GrantCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.grant_to_namespace):
            query['GrantToNamespace'] = request.grant_to_namespace
        if not DaraCore.is_null(request.grant_type):
            query['GrantType'] = request.grant_type
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_collection(
        self,
        request: main_models.GrantCollectionRequest,
    ) -> main_models.GrantCollectionResponse:
        runtime = RuntimeOptions()
        return self.grant_collection_with_options(request, runtime)

    async def grant_collection_async(
        self,
        request: main_models.GrantCollectionRequest,
    ) -> main_models.GrantCollectionResponse:
        runtime = RuntimeOptions()
        return await self.grant_collection_with_options_async(request, runtime)

    def handle_active_sqlrecord_with_options(
        self,
        request: main_models.HandleActiveSQLRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleActiveSQLRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleActiveSQLRecord',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleActiveSQLRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_active_sqlrecord_with_options_async(
        self,
        request: main_models.HandleActiveSQLRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleActiveSQLRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleActiveSQLRecord',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleActiveSQLRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_active_sqlrecord(
        self,
        request: main_models.HandleActiveSQLRecordRequest,
    ) -> main_models.HandleActiveSQLRecordResponse:
        runtime = RuntimeOptions()
        return self.handle_active_sqlrecord_with_options(request, runtime)

    async def handle_active_sqlrecord_async(
        self,
        request: main_models.HandleActiveSQLRecordRequest,
    ) -> main_models.HandleActiveSQLRecordResponse:
        runtime = RuntimeOptions()
        return await self.handle_active_sqlrecord_with_options_async(request, runtime)

    def init_vector_database_with_options(
        self,
        request: main_models.InitVectorDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitVectorDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitVectorDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitVectorDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_vector_database_with_options_async(
        self,
        request: main_models.InitVectorDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitVectorDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitVectorDatabase',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitVectorDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_vector_database(
        self,
        request: main_models.InitVectorDatabaseRequest,
    ) -> main_models.InitVectorDatabaseResponse:
        runtime = RuntimeOptions()
        return self.init_vector_database_with_options(request, runtime)

    async def init_vector_database_async(
        self,
        request: main_models.InitVectorDatabaseRequest,
    ) -> main_models.InitVectorDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.init_vector_database_with_options_async(request, runtime)

    def list_ainode_pools_with_options(
        self,
        request: main_models.ListAINodePoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAINodePoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAINodePools',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAINodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ainode_pools_with_options_async(
        self,
        request: main_models.ListAINodePoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAINodePoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAINodePools',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAINodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ainode_pools(
        self,
        request: main_models.ListAINodePoolsRequest,
    ) -> main_models.ListAINodePoolsResponse:
        runtime = RuntimeOptions()
        return self.list_ainode_pools_with_options(request, runtime)

    async def list_ainode_pools_async(
        self,
        request: main_models.ListAINodePoolsRequest,
    ) -> main_models.ListAINodePoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_ainode_pools_with_options_async(request, runtime)

    def list_backup_jobs_with_options(
        self,
        request: main_models.ListBackupJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackupJobs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backup_jobs_with_options_async(
        self,
        request: main_models.ListBackupJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackupJobs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_backup_jobs(
        self,
        request: main_models.ListBackupJobsRequest,
    ) -> main_models.ListBackupJobsResponse:
        runtime = RuntimeOptions()
        return self.list_backup_jobs_with_options(request, runtime)

    async def list_backup_jobs_async(
        self,
        request: main_models.ListBackupJobsRequest,
    ) -> main_models.ListBackupJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_backup_jobs_with_options_async(request, runtime)

    def list_collections_with_options(
        self,
        request: main_models.ListCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollections',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_collections_with_options_async(
        self,
        request: main_models.ListCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollections',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_collections(
        self,
        request: main_models.ListCollectionsRequest,
    ) -> main_models.ListCollectionsResponse:
        runtime = RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    async def list_collections_async(
        self,
        request: main_models.ListCollectionsRequest,
    ) -> main_models.ListCollectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_collections_with_options_async(request, runtime)

    def list_database_extensions_with_options(
        self,
        request: main_models.ListDatabaseExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_extensions_with_options_async(
        self,
        request: main_models.ListDatabaseExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_extensions(
        self,
        request: main_models.ListDatabaseExtensionsRequest,
    ) -> main_models.ListDatabaseExtensionsResponse:
        runtime = RuntimeOptions()
        return self.list_database_extensions_with_options(request, runtime)

    async def list_database_extensions_async(
        self,
        request: main_models.ListDatabaseExtensionsRequest,
    ) -> main_models.ListDatabaseExtensionsResponse:
        runtime = RuntimeOptions()
        return await self.list_database_extensions_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: main_models.ListDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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

    def list_document_collections_with_options(
        self,
        request: main_models.ListDocumentCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentCollections',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_document_collections_with_options_async(
        self,
        request: main_models.ListDocumentCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentCollections',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_document_collections(
        self,
        request: main_models.ListDocumentCollectionsRequest,
    ) -> main_models.ListDocumentCollectionsResponse:
        runtime = RuntimeOptions()
        return self.list_document_collections_with_options(request, runtime)

    async def list_document_collections_async(
        self,
        request: main_models.ListDocumentCollectionsRequest,
    ) -> main_models.ListDocumentCollectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_document_collections_with_options_async(request, runtime)

    def list_documents_with_options(
        self,
        request: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_documents_with_options_async(
        self,
        request: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_documents(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    async def list_documents_async(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.list_documents_with_options_async(request, runtime)

    def list_external_data_services_with_options(
        self,
        request: main_models.ListExternalDataServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalDataServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalDataServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalDataServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_data_services_with_options_async(
        self,
        request: main_models.ListExternalDataServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalDataServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalDataServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalDataServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_data_services(
        self,
        request: main_models.ListExternalDataServicesRequest,
    ) -> main_models.ListExternalDataServicesResponse:
        runtime = RuntimeOptions()
        return self.list_external_data_services_with_options(request, runtime)

    async def list_external_data_services_async(
        self,
        request: main_models.ListExternalDataServicesRequest,
    ) -> main_models.ListExternalDataServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_external_data_services_with_options_async(request, runtime)

    def list_external_data_sources_with_options(
        self,
        request: main_models.ListExternalDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_data_sources_with_options_async(
        self,
        request: main_models.ListExternalDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_data_sources(
        self,
        request: main_models.ListExternalDataSourcesRequest,
    ) -> main_models.ListExternalDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_external_data_sources_with_options(request, runtime)

    async def list_external_data_sources_async(
        self,
        request: main_models.ListExternalDataSourcesRequest,
    ) -> main_models.ListExternalDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_external_data_sources_with_options_async(request, runtime)

    def list_indices_with_options(
        self,
        request: main_models.ListIndicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_indices_with_options_async(
        self,
        request: main_models.ListIndicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_indices(
        self,
        request: main_models.ListIndicesRequest,
    ) -> main_models.ListIndicesResponse:
        runtime = RuntimeOptions()
        return self.list_indices_with_options(request, runtime)

    async def list_indices_async(
        self,
        request: main_models.ListIndicesRequest,
    ) -> main_models.ListIndicesResponse:
        runtime = RuntimeOptions()
        return await self.list_indices_with_options_async(request, runtime)

    def list_instance_databases_with_options(
        self,
        request: main_models.ListInstanceDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceDatabases',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_databases_with_options_async(
        self,
        request: main_models.ListInstanceDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceDatabases',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_databases(
        self,
        request: main_models.ListInstanceDatabasesRequest,
    ) -> main_models.ListInstanceDatabasesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_databases_with_options(request, runtime)

    async def list_instance_databases_async(
        self,
        request: main_models.ListInstanceDatabasesRequest,
    ) -> main_models.ListInstanceDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_databases_with_options_async(request, runtime)

    def list_instance_extensions_with_options(
        self,
        request: main_models.ListInstanceExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.install_status):
            query['InstallStatus'] = request.install_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_extensions_with_options_async(
        self,
        request: main_models.ListInstanceExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.install_status):
            query['InstallStatus'] = request.install_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_extensions(
        self,
        request: main_models.ListInstanceExtensionsRequest,
    ) -> main_models.ListInstanceExtensionsResponse:
        runtime = RuntimeOptions()
        return self.list_instance_extensions_with_options(request, runtime)

    async def list_instance_extensions_async(
        self,
        request: main_models.ListInstanceExtensionsRequest,
    ) -> main_models.ListInstanceExtensionsResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_extensions_with_options_async(request, runtime)

    def list_model_services_with_options(
        self,
        request: main_models.ListModelServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_services_with_options_async(
        self,
        request: main_models.ListModelServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_services(
        self,
        request: main_models.ListModelServicesRequest,
    ) -> main_models.ListModelServicesResponse:
        runtime = RuntimeOptions()
        return self.list_model_services_with_options(request, runtime)

    async def list_model_services_async(
        self,
        request: main_models.ListModelServicesRequest,
    ) -> main_models.ListModelServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_model_services_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not DaraCore.is_null(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_remote_adbdata_sources_with_options(
        self,
        request: main_models.ListRemoteADBDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemoteADBDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemoteADBDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemoteADBDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remote_adbdata_sources_with_options_async(
        self,
        request: main_models.ListRemoteADBDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemoteADBDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemoteADBDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemoteADBDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remote_adbdata_sources(
        self,
        request: main_models.ListRemoteADBDataSourcesRequest,
    ) -> main_models.ListRemoteADBDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_remote_adbdata_sources_with_options(request, runtime)

    async def list_remote_adbdata_sources_async(
        self,
        request: main_models.ListRemoteADBDataSourcesRequest,
    ) -> main_models.ListRemoteADBDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_remote_adbdata_sources_with_options_async(request, runtime)

    def list_schemas_with_options(
        self,
        request: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_pattern):
            query['SchemaPattern'] = request.schema_pattern
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        request: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_pattern):
            query['SchemaPattern'] = request.schema_pattern
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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

    def list_secrets_with_options(
        self,
        request: main_models.ListSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: main_models.ListSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    async def list_secrets_async(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        return await self.list_secrets_with_options_async(request, runtime)

    def list_slow_sqlrecords_with_options(
        self,
        request: main_models.ListSlowSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlowSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slow_sqlrecords_with_options_async(
        self,
        request: main_models.ListSlowSQLRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowSQLRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlowSQLRecords',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowSQLRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slow_sqlrecords(
        self,
        request: main_models.ListSlowSQLRecordsRequest,
    ) -> main_models.ListSlowSQLRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_slow_sqlrecords_with_options(request, runtime)

    async def list_slow_sqlrecords_async(
        self,
        request: main_models.ListSlowSQLRecordsRequest,
    ) -> main_models.ListSlowSQLRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_slow_sqlrecords_with_options_async(request, runtime)

    def list_streaming_data_services_with_options(
        self,
        request: main_models.ListStreamingDataServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingDataServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingDataServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingDataServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_streaming_data_services_with_options_async(
        self,
        request: main_models.ListStreamingDataServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingDataServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingDataServices',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingDataServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_streaming_data_services(
        self,
        request: main_models.ListStreamingDataServicesRequest,
    ) -> main_models.ListStreamingDataServicesResponse:
        runtime = RuntimeOptions()
        return self.list_streaming_data_services_with_options(request, runtime)

    async def list_streaming_data_services_async(
        self,
        request: main_models.ListStreamingDataServicesRequest,
    ) -> main_models.ListStreamingDataServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_streaming_data_services_with_options_async(request, runtime)

    def list_streaming_data_sources_with_options(
        self,
        request: main_models.ListStreamingDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_streaming_data_sources_with_options_async(
        self,
        request: main_models.ListStreamingDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingDataSources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_streaming_data_sources(
        self,
        request: main_models.ListStreamingDataSourcesRequest,
    ) -> main_models.ListStreamingDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_streaming_data_sources_with_options(request, runtime)

    async def list_streaming_data_sources_async(
        self,
        request: main_models.ListStreamingDataSourcesRequest,
    ) -> main_models.ListStreamingDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_streaming_data_sources_with_options_async(request, runtime)

    def list_streaming_jobs_with_options(
        self,
        request: main_models.ListStreamingJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingJobs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_streaming_jobs_with_options_async(
        self,
        request: main_models.ListStreamingJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStreamingJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStreamingJobs',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStreamingJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_streaming_jobs(
        self,
        request: main_models.ListStreamingJobsRequest,
    ) -> main_models.ListStreamingJobsResponse:
        runtime = RuntimeOptions()
        return self.list_streaming_jobs_with_options(request, runtime)

    async def list_streaming_jobs_async(
        self,
        request: main_models.ListStreamingJobsRequest,
    ) -> main_models.ListStreamingJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_streaming_jobs_with_options_async(request, runtime)

    def list_supabase_projects_with_options(
        self,
        request: main_models.ListSupabaseProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupabaseProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupabaseProjects',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupabaseProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supabase_projects_with_options_async(
        self,
        request: main_models.ListSupabaseProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupabaseProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupabaseProjects',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupabaseProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supabase_projects(
        self,
        request: main_models.ListSupabaseProjectsRequest,
    ) -> main_models.ListSupabaseProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_supabase_projects_with_options(request, runtime)

    async def list_supabase_projects_async(
        self,
        request: main_models.ListSupabaseProjectsRequest,
    ) -> main_models.ListSupabaseProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_supabase_projects_with_options_async(request, runtime)

    def list_support_models_with_options(
        self,
        request: main_models.ListSupportModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportModels',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_support_models_with_options_async(
        self,
        request: main_models.ListSupportModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportModels',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_support_models(
        self,
        request: main_models.ListSupportModelsRequest,
    ) -> main_models.ListSupportModelsResponse:
        runtime = RuntimeOptions()
        return self.list_support_models_with_options(request, runtime)

    async def list_support_models_async(
        self,
        request: main_models.ListSupportModelsRequest,
    ) -> main_models.ListSupportModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_support_models_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.table_pattern):
            query['TablePattern'] = request.table_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not DaraCore.is_null(request.table_pattern):
            query['TablePattern'] = request.table_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.enable_recovery_point):
            query['EnableRecoveryPoint'] = request.enable_recovery_point
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.recovery_point_period):
            query['RecoveryPointPeriod'] = request.recovery_point_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.enable_recovery_point):
            query['EnableRecoveryPoint'] = request.enable_recovery_point
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.recovery_point_period):
            query['RecoveryPointPeriod'] = request.recovery_point_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_collection_with_options(
        self,
        request: main_models.ModifyCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_collection_with_options_async(
        self,
        request: main_models.ModifyCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.metadata):
            query['Metadata'] = request.metadata
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCollection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_collection(
        self,
        request: main_models.ModifyCollectionRequest,
    ) -> main_models.ModifyCollectionResponse:
        runtime = RuntimeOptions()
        return self.modify_collection_with_options(request, runtime)

    async def modify_collection_async(
        self,
        request: main_models.ModifyCollectionRequest,
    ) -> main_models.ModifyCollectionResponse:
        runtime = RuntimeOptions()
        return await self.modify_collection_with_options_async(request, runtime)

    def modify_dbinstance_config_with_options(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConfig',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConfig',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConnectionString',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConnectionString',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_deployment_mode_with_options(
        self,
        request: main_models.ModifyDBInstanceDeploymentModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDeploymentModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDeploymentMode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDeploymentModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_deployment_mode_with_options_async(
        self,
        request: main_models.ModifyDBInstanceDeploymentModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDeploymentModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDeploymentMode',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDeploymentModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_deployment_mode(
        self,
        request: main_models.ModifyDBInstanceDeploymentModeRequest,
    ) -> main_models.ModifyDBInstanceDeploymentModeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_deployment_mode_with_options(request, runtime)

    async def modify_dbinstance_deployment_mode_async(
        self,
        request: main_models.ModifyDBInstanceDeploymentModeRequest,
    ) -> main_models.ModifyDBInstanceDeploymentModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_deployment_mode_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDescription',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDescription',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceNetworkType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceNetworkType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_pay_type_with_options(
        self,
        request: main_models.ModifyDBInstancePayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstancePayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstancePayType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_pay_type_with_options_async(
        self,
        request: main_models.ModifyDBInstancePayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstancePayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstancePayType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstancePayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_pay_type(
        self,
        request: main_models.ModifyDBInstancePayTypeRequest,
    ) -> main_models.ModifyDBInstancePayTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    async def modify_dbinstance_pay_type_async(
        self,
        request: main_models.ModifyDBInstancePayTypeRequest,
    ) -> main_models.ModifyDBInstancePayTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_pay_type_with_options_async(request, runtime)

    def modify_dbinstance_resource_group_with_options(
        self,
        request: main_models.ModifyDBInstanceResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_resource_group_with_options_async(
        self,
        request: main_models.ModifyDBInstanceResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_resource_group(
        self,
        request: main_models.ModifyDBInstanceResourceGroupRequest,
    ) -> main_models.ModifyDBInstanceResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_resource_group_with_options(request, runtime)

    async def modify_dbinstance_resource_group_async(
        self,
        request: main_models.ModifyDBInstanceResourceGroupRequest,
    ) -> main_models.ModifyDBInstanceResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_resource_group_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSSL',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSSL',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbresource_group_with_options(
        self,
        tmp_req: main_models.ModifyDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_group_items):
            request.resource_group_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_items, 'ResourceGroupItems', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_items_shrink):
            query['ResourceGroupItems'] = request.resource_group_items_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_group_with_options_async(
        self,
        tmp_req: main_models.ModifyDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_group_items):
            request.resource_group_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_items, 'ResourceGroupItems', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_items_shrink):
            query['ResourceGroupItems'] = request.resource_group_items_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_group(
        self,
        request: main_models.ModifyDBResourceGroupRequest,
    ) -> main_models.ModifyDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    async def modify_dbresource_group_async(
        self,
        request: main_models.ModifyDBResourceGroupRequest,
    ) -> main_models.ModifyDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbresource_group_with_options_async(request, runtime)

    def modify_external_data_service_with_options(
        self,
        request: main_models.ModifyExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_external_data_service_with_options_async(
        self,
        request: main_models.ModifyExternalDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExternalDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExternalDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExternalDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_external_data_service(
        self,
        request: main_models.ModifyExternalDataServiceRequest,
    ) -> main_models.ModifyExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return self.modify_external_data_service_with_options(request, runtime)

    async def modify_external_data_service_async(
        self,
        request: main_models.ModifyExternalDataServiceRequest,
    ) -> main_models.ModifyExternalDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.modify_external_data_service_with_options_async(request, runtime)

    def modify_hadoop_data_source_with_options(
        self,
        request: main_models.ModifyHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not DaraCore.is_null(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not DaraCore.is_null(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not DaraCore.is_null(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not DaraCore.is_null(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not DaraCore.is_null(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hadoop_data_source_with_options_async(
        self,
        request: main_models.ModifyHadoopDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHadoopDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not DaraCore.is_null(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not DaraCore.is_null(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not DaraCore.is_null(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not DaraCore.is_null(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not DaraCore.is_null(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not DaraCore.is_null(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHadoopDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHadoopDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hadoop_data_source(
        self,
        request: main_models.ModifyHadoopDataSourceRequest,
    ) -> main_models.ModifyHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return self.modify_hadoop_data_source_with_options(request, runtime)

    async def modify_hadoop_data_source_async(
        self,
        request: main_models.ModifyHadoopDataSourceRequest,
    ) -> main_models.ModifyHadoopDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_hadoop_data_source_with_options_async(request, runtime)

    def modify_jdbcdata_source_with_options(
        self,
        request: main_models.ModifyJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not DaraCore.is_null(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not DaraCore.is_null(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_jdbcdata_source_with_options_async(
        self,
        request: main_models.ModifyJDBCDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJDBCDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not DaraCore.is_null(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not DaraCore.is_null(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJDBCDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJDBCDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_jdbcdata_source(
        self,
        request: main_models.ModifyJDBCDataSourceRequest,
    ) -> main_models.ModifyJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return self.modify_jdbcdata_source_with_options(request, runtime)

    async def modify_jdbcdata_source_async(
        self,
        request: main_models.ModifyJDBCDataSourceRequest,
    ) -> main_models.ModifyJDBCDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_jdbcdata_source_with_options_async(request, runtime)

    def modify_master_spec_with_options(
        self,
        request: main_models.ModifyMasterSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMasterSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.master_aispec):
            query['MasterAISpec'] = request.master_aispec
        if not DaraCore.is_null(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMasterSpec',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMasterSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_master_spec_with_options_async(
        self,
        request: main_models.ModifyMasterSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMasterSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.master_aispec):
            query['MasterAISpec'] = request.master_aispec
        if not DaraCore.is_null(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMasterSpec',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMasterSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_master_spec(
        self,
        request: main_models.ModifyMasterSpecRequest,
    ) -> main_models.ModifyMasterSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_master_spec_with_options(request, runtime)

    async def modify_master_spec_async(
        self,
        request: main_models.ModifyMasterSpecRequest,
    ) -> main_models.ModifyMasterSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_master_spec_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: main_models.ModifyParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.force_restart_instance):
            query['ForceRestartInstance'] = request.force_restart_instance
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameters',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: main_models.ModifyParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.force_restart_instance):
            query['ForceRestartInstance'] = request.force_restart_instance
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameters',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameters(
        self,
        request: main_models.ModifyParametersRequest,
    ) -> main_models.ModifyParametersResponse:
        runtime = RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: main_models.ModifyParametersRequest,
    ) -> main_models.ModifyParametersResponse:
        runtime = RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_remote_adbdata_source_with_options(
        self,
        request: main_models.ModifyRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_password):
            query['UserPassword'] = request.user_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRemoteADBDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_remote_adbdata_source_with_options_async(
        self,
        request: main_models.ModifyRemoteADBDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRemoteADBDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.local_dbinstance_id):
            query['LocalDBInstanceId'] = request.local_dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_password):
            query['UserPassword'] = request.user_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRemoteADBDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRemoteADBDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_remote_adbdata_source(
        self,
        request: main_models.ModifyRemoteADBDataSourceRequest,
    ) -> main_models.ModifyRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return self.modify_remote_adbdata_source_with_options(request, runtime)

    async def modify_remote_adbdata_source_async(
        self,
        request: main_models.ModifyRemoteADBDataSourceRequest,
    ) -> main_models.ModifyRemoteADBDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_remote_adbdata_source_with_options_async(request, runtime)

    def modify_sqlcollector_policy_with_options(
        self,
        request: main_models.ModifySQLCollectorPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySQLCollectorPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySQLCollectorPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqlcollector_policy_with_options_async(
        self,
        request: main_models.ModifySQLCollectorPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySQLCollectorPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySQLCollectorPolicy',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sqlcollector_policy(
        self,
        request: main_models.ModifySQLCollectorPolicyRequest,
    ) -> main_models.ModifySQLCollectorPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    async def modify_sqlcollector_policy_async(
        self,
        request: main_models.ModifySQLCollectorPolicyRequest,
    ) -> main_models.ModifySQLCollectorPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_sqlcollector_policy_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: main_models.ModifySecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not DaraCore.is_null(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: main_models.ModifySecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not DaraCore.is_null(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: main_models.ModifySecurityIpsRequest,
    ) -> main_models.ModifySecurityIpsResponse:
        runtime = RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: main_models.ModifySecurityIpsRequest,
    ) -> main_models.ModifySecurityIpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_streaming_data_service_with_options(
        self,
        request: main_models.ModifyStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_streaming_data_service_with_options_async(
        self,
        request: main_models.ModifyStreamingDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingDataService',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_streaming_data_service(
        self,
        request: main_models.ModifyStreamingDataServiceRequest,
    ) -> main_models.ModifyStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return self.modify_streaming_data_service_with_options(request, runtime)

    async def modify_streaming_data_service_async(
        self,
        request: main_models.ModifyStreamingDataServiceRequest,
    ) -> main_models.ModifyStreamingDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.modify_streaming_data_service_with_options_async(request, runtime)

    def modify_streaming_data_source_with_options(
        self,
        request: main_models.ModifyStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_streaming_data_source_with_options_async(
        self,
        request: main_models.ModifyStreamingDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingDataSource',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_streaming_data_source(
        self,
        request: main_models.ModifyStreamingDataSourceRequest,
    ) -> main_models.ModifyStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return self.modify_streaming_data_source_with_options(request, runtime)

    async def modify_streaming_data_source_async(
        self,
        request: main_models.ModifyStreamingDataSourceRequest,
    ) -> main_models.ModifyStreamingDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_streaming_data_source_with_options_async(request, runtime)

    def modify_streaming_job_with_options(
        self,
        tmp_req: main_models.ModifyStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingJobResponse:
        tmp_req.validate()
        request = main_models.ModifyStreamingJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_columns):
            request.dest_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not DaraCore.is_null(tmp_req.match_columns):
            request.match_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not DaraCore.is_null(tmp_req.src_columns):
            request.src_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not DaraCore.is_null(tmp_req.update_columns):
            request.update_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.consistency):
            query['Consistency'] = request.consistency
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not DaraCore.is_null(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not DaraCore.is_null(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not DaraCore.is_null(request.dest_table):
            query['DestTable'] = request.dest_table
        if not DaraCore.is_null(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not DaraCore.is_null(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not DaraCore.is_null(request.try_run):
            query['TryRun'] = request.try_run
        if not DaraCore.is_null(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not DaraCore.is_null(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_streaming_job_with_options_async(
        self,
        tmp_req: main_models.ModifyStreamingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingJobResponse:
        tmp_req.validate()
        request = main_models.ModifyStreamingJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_columns):
            request.dest_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not DaraCore.is_null(tmp_req.match_columns):
            request.match_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not DaraCore.is_null(tmp_req.src_columns):
            request.src_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not DaraCore.is_null(tmp_req.update_columns):
            request.update_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.consistency):
            query['Consistency'] = request.consistency
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not DaraCore.is_null(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not DaraCore.is_null(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not DaraCore.is_null(request.dest_table):
            query['DestTable'] = request.dest_table
        if not DaraCore.is_null(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not DaraCore.is_null(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not DaraCore.is_null(request.try_run):
            query['TryRun'] = request.try_run
        if not DaraCore.is_null(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not DaraCore.is_null(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingJob',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_streaming_job(
        self,
        request: main_models.ModifyStreamingJobRequest,
    ) -> main_models.ModifyStreamingJobResponse:
        runtime = RuntimeOptions()
        return self.modify_streaming_job_with_options(request, runtime)

    async def modify_streaming_job_async(
        self,
        request: main_models.ModifyStreamingJobRequest,
    ) -> main_models.ModifyStreamingJobResponse:
        runtime = RuntimeOptions()
        return await self.modify_streaming_job_with_options_async(request, runtime)

    def modify_supabase_project_security_ips_with_options(
        self,
        request: main_models.ModifySupabaseProjectSecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySupabaseProjectSecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySupabaseProjectSecurityIps',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySupabaseProjectSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_supabase_project_security_ips_with_options_async(
        self,
        request: main_models.ModifySupabaseProjectSecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySupabaseProjectSecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySupabaseProjectSecurityIps',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySupabaseProjectSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_supabase_project_security_ips(
        self,
        request: main_models.ModifySupabaseProjectSecurityIpsRequest,
    ) -> main_models.ModifySupabaseProjectSecurityIpsResponse:
        runtime = RuntimeOptions()
        return self.modify_supabase_project_security_ips_with_options(request, runtime)

    async def modify_supabase_project_security_ips_async(
        self,
        request: main_models.ModifySupabaseProjectSecurityIpsRequest,
    ) -> main_models.ModifySupabaseProjectSecurityIpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_supabase_project_security_ips_with_options_async(request, runtime)

    def modify_vector_configuration_with_options(
        self,
        request: main_models.ModifyVectorConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVectorConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVectorConfiguration',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVectorConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vector_configuration_with_options_async(
        self,
        request: main_models.ModifyVectorConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVectorConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVectorConfiguration',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVectorConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vector_configuration(
        self,
        request: main_models.ModifyVectorConfigurationRequest,
    ) -> main_models.ModifyVectorConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_vector_configuration_with_options(request, runtime)

    async def modify_vector_configuration_async(
        self,
        request: main_models.ModifyVectorConfigurationRequest,
    ) -> main_models.ModifyVectorConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_vector_configuration_with_options_async(request, runtime)

    def pause_data_redistribute_with_options(
        self,
        request: main_models.PauseDataRedistributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseDataRedistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseDataRedistribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseDataRedistributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_data_redistribute_with_options_async(
        self,
        request: main_models.PauseDataRedistributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseDataRedistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseDataRedistribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseDataRedistributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_data_redistribute(
        self,
        request: main_models.PauseDataRedistributeRequest,
    ) -> main_models.PauseDataRedistributeResponse:
        runtime = RuntimeOptions()
        return self.pause_data_redistribute_with_options(request, runtime)

    async def pause_data_redistribute_async(
        self,
        request: main_models.PauseDataRedistributeRequest,
    ) -> main_models.PauseDataRedistributeResponse:
        runtime = RuntimeOptions()
        return await self.pause_data_redistribute_with_options_async(request, runtime)

    def pause_instance_with_options(
        self,
        request: main_models.PauseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_instance_with_options_async(
        self,
        request: main_models.PauseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_instance(
        self,
        request: main_models.PauseInstanceRequest,
    ) -> main_models.PauseInstanceResponse:
        runtime = RuntimeOptions()
        return self.pause_instance_with_options(request, runtime)

    async def pause_instance_async(
        self,
        request: main_models.PauseInstanceRequest,
    ) -> main_models.PauseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.pause_instance_with_options_async(request, runtime)

    def query_collection_data_with_options(
        self,
        tmp_req: main_models.QueryCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCollectionDataResponse:
        tmp_req.validate()
        request = main_models.QueryCollectionDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.relational_table_filter):
            request.relational_table_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.relational_table_filter, 'RelationalTableFilter', 'json')
        if not DaraCore.is_null(tmp_req.sparse_vector):
            request.sparse_vector_shrink = Utils.array_to_string_with_specified_style(tmp_req.sparse_vector, 'SparseVector', 'json')
        if not DaraCore.is_null(tmp_req.vector):
            request.vector_shrink = Utils.array_to_string_with_specified_style(tmp_req.vector, 'Vector', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not DaraCore.is_null(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_sparse_values):
            query['IncludeSparseValues'] = request.include_sparse_values
        if not DaraCore.is_null(request.include_values):
            query['IncludeValues'] = request.include_values
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relational_table_filter_shrink):
            query['RelationalTableFilter'] = request.relational_table_filter_shrink
        if not DaraCore.is_null(request.sparse_vector_shrink):
            query['SparseVector'] = request.sparse_vector_shrink
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.vector_shrink):
            query['Vector'] = request.vector_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_collection_data_with_options_async(
        self,
        tmp_req: main_models.QueryCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCollectionDataResponse:
        tmp_req.validate()
        request = main_models.QueryCollectionDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.relational_table_filter):
            request.relational_table_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.relational_table_filter, 'RelationalTableFilter', 'json')
        if not DaraCore.is_null(tmp_req.sparse_vector):
            request.sparse_vector_shrink = Utils.array_to_string_with_specified_style(tmp_req.sparse_vector, 'SparseVector', 'json')
        if not DaraCore.is_null(tmp_req.vector):
            request.vector_shrink = Utils.array_to_string_with_specified_style(tmp_req.vector, 'Vector', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not DaraCore.is_null(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_sparse_values):
            query['IncludeSparseValues'] = request.include_sparse_values
        if not DaraCore.is_null(request.include_values):
            query['IncludeValues'] = request.include_values
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relational_table_filter_shrink):
            query['RelationalTableFilter'] = request.relational_table_filter_shrink
        if not DaraCore.is_null(request.sparse_vector_shrink):
            query['SparseVector'] = request.sparse_vector_shrink
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.vector_shrink):
            query['Vector'] = request.vector_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_collection_data(
        self,
        request: main_models.QueryCollectionDataRequest,
    ) -> main_models.QueryCollectionDataResponse:
        runtime = RuntimeOptions()
        return self.query_collection_data_with_options(request, runtime)

    async def query_collection_data_async(
        self,
        request: main_models.QueryCollectionDataRequest,
    ) -> main_models.QueryCollectionDataResponse:
        runtime = RuntimeOptions()
        return await self.query_collection_data_with_options_async(request, runtime)

    def query_content_with_options(
        self,
        tmp_req: main_models.QueryContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentResponse:
        tmp_req.validate()
        request = main_models.QueryContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.graph_search_args):
            request.graph_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.graph_search_args, 'GraphSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.recall_window):
            request.recall_window_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_window, 'RecallWindow', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.graph_enhance):
            query['GraphEnhance'] = request.graph_enhance
        if not DaraCore.is_null(request.graph_search_args_shrink):
            query['GraphSearchArgs'] = request.graph_search_args_shrink
        if not DaraCore.is_null(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not DaraCore.is_null(request.include_file_url):
            query['IncludeFileUrl'] = request.include_file_url
        if not DaraCore.is_null(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_vector):
            query['IncludeVector'] = request.include_vector
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recall_window_shrink):
            query['RecallWindow'] = request.recall_window_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rerank_factor):
            query['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.url_expiration):
            query['UrlExpiration'] = request.url_expiration
        if not DaraCore.is_null(request.use_full_text_retrieval):
            query['UseFullTextRetrieval'] = request.use_full_text_retrieval
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryContent',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_content_with_options_async(
        self,
        tmp_req: main_models.QueryContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentResponse:
        tmp_req.validate()
        request = main_models.QueryContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.graph_search_args):
            request.graph_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.graph_search_args, 'GraphSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not DaraCore.is_null(tmp_req.recall_window):
            request.recall_window_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_window, 'RecallWindow', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.graph_enhance):
            query['GraphEnhance'] = request.graph_enhance
        if not DaraCore.is_null(request.graph_search_args_shrink):
            query['GraphSearchArgs'] = request.graph_search_args_shrink
        if not DaraCore.is_null(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not DaraCore.is_null(request.include_file_url):
            query['IncludeFileUrl'] = request.include_file_url
        if not DaraCore.is_null(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_vector):
            query['IncludeVector'] = request.include_vector
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recall_window_shrink):
            query['RecallWindow'] = request.recall_window_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rerank_factor):
            query['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.url_expiration):
            query['UrlExpiration'] = request.url_expiration
        if not DaraCore.is_null(request.use_full_text_retrieval):
            query['UseFullTextRetrieval'] = request.use_full_text_retrieval
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryContent',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_content(
        self,
        request: main_models.QueryContentRequest,
    ) -> main_models.QueryContentResponse:
        runtime = RuntimeOptions()
        return self.query_content_with_options(request, runtime)

    async def query_content_async(
        self,
        request: main_models.QueryContentRequest,
    ) -> main_models.QueryContentResponse:
        runtime = RuntimeOptions()
        return await self.query_content_with_options_async(request, runtime)

    def query_content_advance(
        self,
        request: main_models.QueryContentAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentResponse:
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
            'Product': 'gpdb',
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
        query_content_req = main_models.QueryContentRequest()
        Utils.convert(request, query_content_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            query_content_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        query_content_resp = self.query_content_with_options(query_content_req, runtime)
        return query_content_resp

    async def query_content_advance_async(
        self,
        request: main_models.QueryContentAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentResponse:
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
            'Product': 'gpdb',
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
        query_content_req = main_models.QueryContentRequest()
        Utils.convert(request, query_content_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            query_content_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        query_content_resp = await self.query_content_with_options_async(query_content_req, runtime)
        return query_content_resp

    def query_knowledge_bases_content_with_options(
        self,
        tmp_req: main_models.QueryKnowledgeBasesContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryKnowledgeBasesContentResponse:
        tmp_req.validate()
        request = main_models.QueryKnowledgeBasesContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merge_method_args):
            request.merge_method_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.merge_method_args, 'MergeMethodArgs', 'json')
        if not DaraCore.is_null(tmp_req.source_collection):
            request.source_collection_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_collection, 'SourceCollection', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.merge_method):
            query['MergeMethod'] = request.merge_method
        if not DaraCore.is_null(request.merge_method_args_shrink):
            query['MergeMethodArgs'] = request.merge_method_args_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rerank_factor):
            query['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.source_collection_shrink):
            query['SourceCollection'] = request.source_collection_shrink
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryKnowledgeBasesContent',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryKnowledgeBasesContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_knowledge_bases_content_with_options_async(
        self,
        tmp_req: main_models.QueryKnowledgeBasesContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryKnowledgeBasesContentResponse:
        tmp_req.validate()
        request = main_models.QueryKnowledgeBasesContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merge_method_args):
            request.merge_method_args_shrink = Utils.array_to_string_with_specified_style(tmp_req.merge_method_args, 'MergeMethodArgs', 'json')
        if not DaraCore.is_null(tmp_req.source_collection):
            request.source_collection_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_collection, 'SourceCollection', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.merge_method):
            query['MergeMethod'] = request.merge_method
        if not DaraCore.is_null(request.merge_method_args_shrink):
            query['MergeMethodArgs'] = request.merge_method_args_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rerank_factor):
            query['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.source_collection_shrink):
            query['SourceCollection'] = request.source_collection_shrink
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryKnowledgeBasesContent',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryKnowledgeBasesContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_knowledge_bases_content(
        self,
        request: main_models.QueryKnowledgeBasesContentRequest,
    ) -> main_models.QueryKnowledgeBasesContentResponse:
        runtime = RuntimeOptions()
        return self.query_knowledge_bases_content_with_options(request, runtime)

    async def query_knowledge_bases_content_async(
        self,
        request: main_models.QueryKnowledgeBasesContentRequest,
    ) -> main_models.QueryKnowledgeBasesContentResponse:
        runtime = RuntimeOptions()
        return await self.query_knowledge_bases_content_with_options_async(request, runtime)

    def rebalance_dbinstance_with_options(
        self,
        request: main_models.RebalanceDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_dbinstance_with_options_async(
        self,
        request: main_models.RebalanceDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_dbinstance(
        self,
        request: main_models.RebalanceDBInstanceRequest,
    ) -> main_models.RebalanceDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.rebalance_dbinstance_with_options(request, runtime)

    async def rebalance_dbinstance_async(
        self,
        request: main_models.RebalanceDBInstanceRequest,
    ) -> main_models.RebalanceDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.rebalance_dbinstance_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def rerank_with_options(
        self,
        tmp_req: main_models.RerankRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerankResponse:
        tmp_req.validate()
        request = main_models.RerankShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.max_chunks_per_doc):
            body['MaxChunksPerDoc'] = request.max_chunks_per_doc
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.return_documents):
            body['ReturnDocuments'] = request.return_documents
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Rerank',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerankResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerank_with_options_async(
        self,
        tmp_req: main_models.RerankRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerankResponse:
        tmp_req.validate()
        request = main_models.RerankShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.max_chunks_per_doc):
            body['MaxChunksPerDoc'] = request.max_chunks_per_doc
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.return_documents):
            body['ReturnDocuments'] = request.return_documents
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Rerank',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerank(
        self,
        request: main_models.RerankRequest,
    ) -> main_models.RerankResponse:
        runtime = RuntimeOptions()
        return self.rerank_with_options(request, runtime)

    async def rerank_async(
        self,
        request: main_models.RerankRequest,
    ) -> main_models.RerankResponse:
        runtime = RuntimeOptions()
        return await self.rerank_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def reset_imvmonitor_data_with_options(
        self,
        request: main_models.ResetIMVMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetIMVMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetIMVMonitorData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetIMVMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_imvmonitor_data_with_options_async(
        self,
        request: main_models.ResetIMVMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetIMVMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetIMVMonitorData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetIMVMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_imvmonitor_data(
        self,
        request: main_models.ResetIMVMonitorDataRequest,
    ) -> main_models.ResetIMVMonitorDataResponse:
        runtime = RuntimeOptions()
        return self.reset_imvmonitor_data_with_options(request, runtime)

    async def reset_imvmonitor_data_async(
        self,
        request: main_models.ResetIMVMonitorDataRequest,
    ) -> main_models.ResetIMVMonitorDataResponse:
        runtime = RuntimeOptions()
        return await self.reset_imvmonitor_data_with_options_async(request, runtime)

    def reset_supabase_project_password_with_options(
        self,
        request: main_models.ResetSupabaseProjectPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSupabaseProjectPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSupabaseProjectPassword',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSupabaseProjectPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_supabase_project_password_with_options_async(
        self,
        request: main_models.ResetSupabaseProjectPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSupabaseProjectPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSupabaseProjectPassword',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSupabaseProjectPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_supabase_project_password(
        self,
        request: main_models.ResetSupabaseProjectPasswordRequest,
    ) -> main_models.ResetSupabaseProjectPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_supabase_project_password_with_options(request, runtime)

    async def reset_supabase_project_password_async(
        self,
        request: main_models.ResetSupabaseProjectPasswordRequest,
    ) -> main_models.ResetSupabaseProjectPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_supabase_project_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: main_models.RestartDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: main_models.RestartDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: main_models.RestartDBInstanceRequest,
    ) -> main_models.RestartDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: main_models.RestartDBInstanceRequest,
    ) -> main_models.RestartDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def resume_data_redistribute_with_options(
        self,
        request: main_models.ResumeDataRedistributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeDataRedistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeDataRedistribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeDataRedistributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_data_redistribute_with_options_async(
        self,
        request: main_models.ResumeDataRedistributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeDataRedistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeDataRedistribute',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeDataRedistributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_data_redistribute(
        self,
        request: main_models.ResumeDataRedistributeRequest,
    ) -> main_models.ResumeDataRedistributeResponse:
        runtime = RuntimeOptions()
        return self.resume_data_redistribute_with_options(request, runtime)

    async def resume_data_redistribute_async(
        self,
        request: main_models.ResumeDataRedistributeRequest,
    ) -> main_models.ResumeDataRedistributeResponse:
        runtime = RuntimeOptions()
        return await self.resume_data_redistribute_with_options_async(request, runtime)

    def resume_instance_with_options(
        self,
        request: main_models.ResumeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        request: main_models.ResumeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        request: main_models.ResumeInstanceRequest,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    async def resume_instance_async(
        self,
        request: main_models.ResumeInstanceRequest,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.resume_instance_with_options_async(request, runtime)

    def set_dbinstance_plan_status_with_options(
        self,
        request: main_models.SetDBInstancePlanStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDBInstancePlanStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_status):
            query['PlanStatus'] = request.plan_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDBInstancePlanStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDBInstancePlanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dbinstance_plan_status_with_options_async(
        self,
        request: main_models.SetDBInstancePlanStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDBInstancePlanStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_status):
            query['PlanStatus'] = request.plan_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDBInstancePlanStatus',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDBInstancePlanStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dbinstance_plan_status(
        self,
        request: main_models.SetDBInstancePlanStatusRequest,
    ) -> main_models.SetDBInstancePlanStatusResponse:
        runtime = RuntimeOptions()
        return self.set_dbinstance_plan_status_with_options(request, runtime)

    async def set_dbinstance_plan_status_async(
        self,
        request: main_models.SetDBInstancePlanStatusRequest,
    ) -> main_models.SetDBInstancePlanStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_dbinstance_plan_status_with_options_async(request, runtime)

    def set_data_share_instance_with_options(
        self,
        tmp_req: main_models.SetDataShareInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataShareInstanceResponse:
        tmp_req.validate()
        request = main_models.SetDataShareInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_list):
            request.instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataShareInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataShareInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_share_instance_with_options_async(
        self,
        tmp_req: main_models.SetDataShareInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataShareInstanceResponse:
        tmp_req.validate()
        request = main_models.SetDataShareInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_list):
            request.instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataShareInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataShareInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_share_instance(
        self,
        request: main_models.SetDataShareInstanceRequest,
    ) -> main_models.SetDataShareInstanceResponse:
        runtime = RuntimeOptions()
        return self.set_data_share_instance_with_options(request, runtime)

    async def set_data_share_instance_async(
        self,
        request: main_models.SetDataShareInstanceRequest,
    ) -> main_models.SetDataShareInstanceResponse:
        runtime = RuntimeOptions()
        return await self.set_data_share_instance_with_options_async(request, runtime)

    def switch_dbinstance_net_type_with_options(
        self,
        request: main_models.SwitchDBInstanceNetTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDBInstanceNetTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceNetType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_net_type_with_options_async(
        self,
        request: main_models.SwitchDBInstanceNetTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDBInstanceNetTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceNetType',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDBInstanceNetTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_net_type(
        self,
        request: main_models.SwitchDBInstanceNetTypeRequest,
    ) -> main_models.SwitchDBInstanceNetTypeResponse:
        runtime = RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    async def switch_dbinstance_net_type_async(
        self,
        request: main_models.SwitchDBInstanceNetTypeRequest,
    ) -> main_models.SwitchDBInstanceNetTypeResponse:
        runtime = RuntimeOptions()
        return await self.switch_dbinstance_net_type_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def text_embedding_with_options(
        self,
        tmp_req: main_models.TextEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextEmbeddingResponse:
        tmp_req.validate()
        request = main_models.TextEmbeddingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextEmbedding',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextEmbeddingResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_embedding_with_options_async(
        self,
        tmp_req: main_models.TextEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextEmbeddingResponse:
        tmp_req.validate()
        request = main_models.TextEmbeddingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextEmbedding',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextEmbeddingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_embedding(
        self,
        request: main_models.TextEmbeddingRequest,
    ) -> main_models.TextEmbeddingResponse:
        runtime = RuntimeOptions()
        return self.text_embedding_with_options(request, runtime)

    async def text_embedding_async(
        self,
        request: main_models.TextEmbeddingRequest,
    ) -> main_models.TextEmbeddingResponse:
        runtime = RuntimeOptions()
        return await self.text_embedding_with_options_async(request, runtime)

    def unbind_dbresource_group_with_role_with_options(
        self,
        tmp_req: main_models.UnbindDBResourceGroupWithRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourceGroupWithRoleResponse:
        tmp_req.validate()
        request = main_models.UnbindDBResourceGroupWithRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_list):
            request.role_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourceGroupWithRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_group_with_role_with_options_async(
        self,
        tmp_req: main_models.UnbindDBResourceGroupWithRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourceGroupWithRoleResponse:
        tmp_req.validate()
        request = main_models.UnbindDBResourceGroupWithRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_list):
            request.role_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithRole',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourceGroupWithRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_group_with_role(
        self,
        request: main_models.UnbindDBResourceGroupWithRoleRequest,
    ) -> main_models.UnbindDBResourceGroupWithRoleResponse:
        runtime = RuntimeOptions()
        return self.unbind_dbresource_group_with_role_with_options(request, runtime)

    async def unbind_dbresource_group_with_role_async(
        self,
        request: main_models.UnbindDBResourceGroupWithRoleRequest,
    ) -> main_models.UnbindDBResourceGroupWithRoleResponse:
        runtime = RuntimeOptions()
        return await self.unbind_dbresource_group_with_role_with_options_async(request, runtime)

    def unload_sample_data_with_options(
        self,
        request: main_models.UnloadSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnloadSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnloadSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnloadSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def unload_sample_data_with_options_async(
        self,
        request: main_models.UnloadSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnloadSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnloadSampleData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnloadSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unload_sample_data(
        self,
        request: main_models.UnloadSampleDataRequest,
    ) -> main_models.UnloadSampleDataResponse:
        runtime = RuntimeOptions()
        return self.unload_sample_data_with_options(request, runtime)

    async def unload_sample_data_async(
        self,
        request: main_models.UnloadSampleDataRequest,
    ) -> main_models.UnloadSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.unload_sample_data_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_collection_data_metadata_with_options(
        self,
        tmp_req: main_models.UpdateCollectionDataMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectionDataMetadataResponse:
        tmp_req.validate()
        request = main_models.UpdateCollectionDataMetadataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.metadata_shrink):
            query['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollectionDataMetadata',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectionDataMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_collection_data_metadata_with_options_async(
        self,
        tmp_req: main_models.UpdateCollectionDataMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectionDataMetadataResponse:
        tmp_req.validate()
        request = main_models.UpdateCollectionDataMetadataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.metadata_shrink):
            query['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollectionDataMetadata',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectionDataMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_collection_data_metadata(
        self,
        request: main_models.UpdateCollectionDataMetadataRequest,
    ) -> main_models.UpdateCollectionDataMetadataResponse:
        runtime = RuntimeOptions()
        return self.update_collection_data_metadata_with_options(request, runtime)

    async def update_collection_data_metadata_async(
        self,
        request: main_models.UpdateCollectionDataMetadataRequest,
    ) -> main_models.UpdateCollectionDataMetadataResponse:
        runtime = RuntimeOptions()
        return await self.update_collection_data_metadata_with_options_async(request, runtime)

    def update_dbinstance_plan_with_options(
        self,
        request: main_models.UpdateDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_plan_with_options_async(
        self,
        request: main_models.UpdateDBInstancePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstancePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not DaraCore.is_null(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstancePlan',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_plan(
        self,
        request: main_models.UpdateDBInstancePlanRequest,
    ) -> main_models.UpdateDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return self.update_dbinstance_plan_with_options(request, runtime)

    async def update_dbinstance_plan_async(
        self,
        request: main_models.UpdateDBInstancePlanRequest,
    ) -> main_models.UpdateDBInstancePlanResponse:
        runtime = RuntimeOptions()
        return await self.update_dbinstance_plan_with_options_async(request, runtime)

    def upgrade_dbinstance_with_options(
        self,
        request: main_models.UpgradeDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_storage_size):
            query['CacheStorageSize'] = request.cache_storage_size
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not DaraCore.is_null(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not DaraCore.is_null(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_with_options_async(
        self,
        request: main_models.UpgradeDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_storage_size):
            query['CacheStorageSize'] = request.cache_storage_size
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not DaraCore.is_null(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not DaraCore.is_null(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not DaraCore.is_null(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstance',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance(
        self,
        request: main_models.UpgradeDBInstanceRequest,
    ) -> main_models.UpgradeDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.upgrade_dbinstance_with_options(request, runtime)

    async def upgrade_dbinstance_async(
        self,
        request: main_models.UpgradeDBInstanceRequest,
    ) -> main_models.UpgradeDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_dbinstance_with_options_async(request, runtime)

    def upgrade_dbversion_with_options(
        self,
        request: main_models.UpgradeDBVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.major_version):
            query['MajorVersion'] = request.major_version
        if not DaraCore.is_null(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBVersion',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbversion_with_options_async(
        self,
        request: main_models.UpgradeDBVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.major_version):
            query['MajorVersion'] = request.major_version
        if not DaraCore.is_null(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBVersion',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbversion(
        self,
        request: main_models.UpgradeDBVersionRequest,
    ) -> main_models.UpgradeDBVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_dbversion_with_options(request, runtime)

    async def upgrade_dbversion_async(
        self,
        request: main_models.UpgradeDBVersionRequest,
    ) -> main_models.UpgradeDBVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_dbversion_with_options_async(request, runtime)

    def upgrade_extensions_with_options(
        self,
        request: main_models.UpgradeExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.extensions):
            query['Extensions'] = request.extensions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_extensions_with_options_async(
        self,
        request: main_models.UpgradeExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.extensions):
            query['Extensions'] = request.extensions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeExtensions',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_extensions(
        self,
        request: main_models.UpgradeExtensionsRequest,
    ) -> main_models.UpgradeExtensionsResponse:
        runtime = RuntimeOptions()
        return self.upgrade_extensions_with_options(request, runtime)

    async def upgrade_extensions_async(
        self,
        request: main_models.UpgradeExtensionsRequest,
    ) -> main_models.UpgradeExtensionsResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_extensions_with_options_async(request, runtime)

    def upload_document_async_with_options(
        self,
        tmp_req: main_models.UploadDocumentAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentAsyncResponse:
        tmp_req.validate()
        request = main_models.UploadDocumentAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        if not DaraCore.is_null(tmp_req.separators):
            request.separators_shrink = Utils.array_to_string_with_specified_style(tmp_req.separators, 'Separators', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.chunk_overlap):
            body['ChunkOverlap'] = request.chunk_overlap
        if not DaraCore.is_null(request.chunk_size):
            body['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.document_loader_name):
            body['DocumentLoaderName'] = request.document_loader_name
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.separators_shrink):
            body['Separators'] = request.separators_shrink
        if not DaraCore.is_null(request.splitter_model):
            body['SplitterModel'] = request.splitter_model
        if not DaraCore.is_null(request.text_splitter_name):
            body['TextSplitterName'] = request.text_splitter_name
        if not DaraCore.is_null(request.vl_enhance):
            body['VlEnhance'] = request.vl_enhance
        if not DaraCore.is_null(request.zh_title_enhance):
            body['ZhTitleEnhance'] = request.zh_title_enhance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocumentAsync',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_document_async_with_options_async(
        self,
        tmp_req: main_models.UploadDocumentAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentAsyncResponse:
        tmp_req.validate()
        request = main_models.UploadDocumentAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        if not DaraCore.is_null(tmp_req.separators):
            request.separators_shrink = Utils.array_to_string_with_specified_style(tmp_req.separators, 'Separators', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.chunk_overlap):
            body['ChunkOverlap'] = request.chunk_overlap
        if not DaraCore.is_null(request.chunk_size):
            body['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.document_loader_name):
            body['DocumentLoaderName'] = request.document_loader_name
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.separators_shrink):
            body['Separators'] = request.separators_shrink
        if not DaraCore.is_null(request.splitter_model):
            body['SplitterModel'] = request.splitter_model
        if not DaraCore.is_null(request.text_splitter_name):
            body['TextSplitterName'] = request.text_splitter_name
        if not DaraCore.is_null(request.vl_enhance):
            body['VlEnhance'] = request.vl_enhance
        if not DaraCore.is_null(request.zh_title_enhance):
            body['ZhTitleEnhance'] = request.zh_title_enhance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocumentAsync',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_document_async(
        self,
        request: main_models.UploadDocumentAsyncRequest,
    ) -> main_models.UploadDocumentAsyncResponse:
        runtime = RuntimeOptions()
        return self.upload_document_async_with_options(request, runtime)

    async def upload_document_async_async(
        self,
        request: main_models.UploadDocumentAsyncRequest,
    ) -> main_models.UploadDocumentAsyncResponse:
        runtime = RuntimeOptions()
        return await self.upload_document_async_with_options_async(request, runtime)

    def upload_document_async_advance(
        self,
        request: main_models.UploadDocumentAsyncAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentAsyncResponse:
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
            'Product': 'gpdb',
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
        upload_document_async_req = main_models.UploadDocumentAsyncRequest()
        Utils.convert(request, upload_document_async_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            upload_document_async_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_document_async_resp = self.upload_document_async_with_options(upload_document_async_req, runtime)
        return upload_document_async_resp

    async def upload_document_async_advance_async(
        self,
        request: main_models.UploadDocumentAsyncAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentAsyncResponse:
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
            'Product': 'gpdb',
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
        upload_document_async_req = main_models.UploadDocumentAsyncRequest()
        Utils.convert(request, upload_document_async_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            upload_document_async_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_document_async_resp = await self.upload_document_async_with_options_async(upload_document_async_req, runtime)
        return upload_document_async_resp

    def upsert_chunks_with_options(
        self,
        tmp_req: main_models.UpsertChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertChunksResponse:
        tmp_req.validate()
        request = main_models.UpsertChunksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.text_chunks):
            request.text_chunks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_chunks, 'TextChunks', 'json')
        query = {}
        if not DaraCore.is_null(request.allow_insert_with_filter):
            query['AllowInsertWithFilter'] = request.allow_insert_with_filter
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.should_replace_file):
            query['ShouldReplaceFile'] = request.should_replace_file
        body = {}
        if not DaraCore.is_null(request.text_chunks_shrink):
            body['TextChunks'] = request.text_chunks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertChunks',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_chunks_with_options_async(
        self,
        tmp_req: main_models.UpsertChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertChunksResponse:
        tmp_req.validate()
        request = main_models.UpsertChunksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.text_chunks):
            request.text_chunks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_chunks, 'TextChunks', 'json')
        query = {}
        if not DaraCore.is_null(request.allow_insert_with_filter):
            query['AllowInsertWithFilter'] = request.allow_insert_with_filter
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.should_replace_file):
            query['ShouldReplaceFile'] = request.should_replace_file
        body = {}
        if not DaraCore.is_null(request.text_chunks_shrink):
            body['TextChunks'] = request.text_chunks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertChunks',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_chunks(
        self,
        request: main_models.UpsertChunksRequest,
    ) -> main_models.UpsertChunksResponse:
        runtime = RuntimeOptions()
        return self.upsert_chunks_with_options(request, runtime)

    async def upsert_chunks_async(
        self,
        request: main_models.UpsertChunksRequest,
    ) -> main_models.UpsertChunksResponse:
        runtime = RuntimeOptions()
        return await self.upsert_chunks_with_options_async(request, runtime)

    def upsert_collection_data_with_options(
        self,
        tmp_req: main_models.UpsertCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataResponse:
        tmp_req.validate()
        request = main_models.UpsertCollectionDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rows):
            request.rows_shrink = Utils.array_to_string_with_specified_style(tmp_req.rows, 'Rows', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.rows_shrink):
            body['Rows'] = request.rows_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_collection_data_with_options_async(
        self,
        tmp_req: main_models.UpsertCollectionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataResponse:
        tmp_req.validate()
        request = main_models.UpsertCollectionDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rows):
            request.rows_shrink = Utils.array_to_string_with_specified_style(tmp_req.rows, 'Rows', 'json')
        query = {}
        if not DaraCore.is_null(request.collection):
            query['Collection'] = request.collection
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.rows_shrink):
            body['Rows'] = request.rows_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionData',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_collection_data(
        self,
        request: main_models.UpsertCollectionDataRequest,
    ) -> main_models.UpsertCollectionDataResponse:
        runtime = RuntimeOptions()
        return self.upsert_collection_data_with_options(request, runtime)

    async def upsert_collection_data_async(
        self,
        request: main_models.UpsertCollectionDataRequest,
    ) -> main_models.UpsertCollectionDataResponse:
        runtime = RuntimeOptions()
        return await self.upsert_collection_data_with_options_async(request, runtime)

    def upsert_collection_data_async_with_options(
        self,
        request: main_models.UpsertCollectionDataAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionDataAsync',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionDataAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_collection_data_async_with_options_async(
        self,
        request: main_models.UpsertCollectionDataAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.collection):
            body['Collection'] = request.collection
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionDataAsync',
            version = '2016-05-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionDataAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_collection_data_async(
        self,
        request: main_models.UpsertCollectionDataAsyncRequest,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
        runtime = RuntimeOptions()
        return self.upsert_collection_data_async_with_options(request, runtime)

    async def upsert_collection_data_async_async(
        self,
        request: main_models.UpsertCollectionDataAsyncRequest,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
        runtime = RuntimeOptions()
        return await self.upsert_collection_data_async_with_options_async(request, runtime)

    def upsert_collection_data_async_advance(
        self,
        request: main_models.UpsertCollectionDataAsyncAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
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
            'Product': 'gpdb',
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
        upsert_collection_data_async_req = main_models.UpsertCollectionDataAsyncRequest()
        Utils.convert(request, upsert_collection_data_async_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            upsert_collection_data_async_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upsert_collection_data_async_resp = self.upsert_collection_data_async_with_options(upsert_collection_data_async_req, runtime)
        return upsert_collection_data_async_resp

    async def upsert_collection_data_async_advance_async(
        self,
        request: main_models.UpsertCollectionDataAsyncAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionDataAsyncResponse:
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
            'Product': 'gpdb',
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
        upsert_collection_data_async_req = main_models.UpsertCollectionDataAsyncRequest()
        Utils.convert(request, upsert_collection_data_async_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
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
            upsert_collection_data_async_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upsert_collection_data_async_resp = await self.upsert_collection_data_async_with_options_async(upsert_collection_data_async_req, runtime)
        return upsert_collection_data_async_resp
