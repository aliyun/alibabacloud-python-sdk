# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dts20200101 import models as main_models
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
            'cn-qingdao': 'dts.aliyuncs.com',
            'cn-beijing': 'dts.aliyuncs.com',
            'cn-zhangjiakou': 'dts.aliyuncs.com',
            'cn-huhehaote': 'dts.aliyuncs.com',
            'cn-hangzhou': 'dts.aliyuncs.com',
            'cn-shanghai': 'dts.aliyuncs.com',
            'cn-shenzhen': 'dts.aliyuncs.com',
            'cn-hongkong': 'dts.aliyuncs.com',
            'ap-southeast-1': 'dts.aliyuncs.com',
            'ap-southeast-2': 'dts.aliyuncs.com',
            'ap-southeast-3': 'dts.aliyuncs.com',
            'ap-southeast-5': 'dts.aliyuncs.com',
            'eu-west-1': 'dts.aliyuncs.com',
            'us-west-1': 'dts.aliyuncs.com',
            'us-east-1': 'dts.aliyuncs.com',
            'eu-central-1': 'dts.aliyuncs.com',
            'me-east-1': 'dts.aliyuncs.com',
            'ap-south-1': 'dts.aliyuncs.com',
            'cn-hangzhou-finance': 'dts.aliyuncs.com',
            'cn-shanghai-finance-1': 'dts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dts.aliyuncs.com',
            'cn-north-2-gov-1': 'dts.aliyuncs.com',
            'ap-northeast-2-pop': 'dts.aliyuncs.com',
            'cn-beijing-finance-1': 'dts.aliyuncs.com',
            'cn-beijing-finance-pop': 'dts.aliyuncs.com',
            'cn-beijing-gov-1': 'dts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dts.aliyuncs.com',
            'cn-chengdu': 'dts.aliyuncs.com',
            'cn-edge-1': 'dts.aliyuncs.com',
            'cn-fujian': 'dts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dts.aliyuncs.com',
            'cn-hangzhou-test-306': 'dts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dts.aliyuncs.com',
            'cn-qingdao-nebula': 'dts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dts.aliyuncs.com',
            'cn-shanghai-inner': 'dts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dts.aliyuncs.com',
            'cn-shenzhen-inner': 'dts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dts.aliyuncs.com',
            'cn-wuhan': 'dts.aliyuncs.com',
            'cn-wulanchabu': 'dts.aliyuncs.com',
            'cn-yushanfang': 'dts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dts.aliyuncs.com',
            'eu-west-1-oxs': 'dts.aliyuncs.com',
            'rus-west-1-pop': 'dts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
                tmp = str(form.get("host"))
                host = f'{bucket_name}.{tmp}'
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
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
                tmp = str(form.get("host"))
                host = f'{bucket_name}.{tmp}'
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
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

    def configure_dts_job_with_options(
        self,
        request: main_models.ConfigureDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.data_check_configure):
            query['DataCheckConfigure'] = request.data_check_configure
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not DaraCore.is_null(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dest_ca_certificate_oss_url):
            query['DestCaCertificateOssUrl'] = request.dest_ca_certificate_oss_url
        if not DaraCore.is_null(request.dest_ca_certificate_password):
            query['DestCaCertificatePassword'] = request.dest_ca_certificate_password
        if not DaraCore.is_null(request.dest_client_cert_oss_url):
            query['DestClientCertOssUrl'] = request.dest_client_cert_oss_url
        if not DaraCore.is_null(request.dest_client_key_oss_url):
            query['DestClientKeyOssUrl'] = request.dest_client_key_oss_url
        if not DaraCore.is_null(request.dest_client_password):
            query['DestClientPassword'] = request.dest_client_password
        if not DaraCore.is_null(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not DaraCore.is_null(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not DaraCore.is_null(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_owner_id):
            query['DestinationEndpointOwnerID'] = request.destination_endpoint_owner_id
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_role):
            query['DestinationEndpointRole'] = request.destination_endpoint_role
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.disaster_recovery_job):
            query['DisasterRecoveryJob'] = request.disaster_recovery_job
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not DaraCore.is_null(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not DaraCore.is_null(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.source_endpoint_vswitch_id):
            query['SourceEndpointVSwitchID'] = request.source_endpoint_vswitch_id
        if not DaraCore.is_null(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not DaraCore.is_null(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not DaraCore.is_null(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not DaraCore.is_null(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not DaraCore.is_null(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not DaraCore.is_null(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not DaraCore.is_null(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_dts_job_with_options_async(
        self,
        request: main_models.ConfigureDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.data_check_configure):
            query['DataCheckConfigure'] = request.data_check_configure
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not DaraCore.is_null(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dest_ca_certificate_oss_url):
            query['DestCaCertificateOssUrl'] = request.dest_ca_certificate_oss_url
        if not DaraCore.is_null(request.dest_ca_certificate_password):
            query['DestCaCertificatePassword'] = request.dest_ca_certificate_password
        if not DaraCore.is_null(request.dest_client_cert_oss_url):
            query['DestClientCertOssUrl'] = request.dest_client_cert_oss_url
        if not DaraCore.is_null(request.dest_client_key_oss_url):
            query['DestClientKeyOssUrl'] = request.dest_client_key_oss_url
        if not DaraCore.is_null(request.dest_client_password):
            query['DestClientPassword'] = request.dest_client_password
        if not DaraCore.is_null(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not DaraCore.is_null(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not DaraCore.is_null(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_owner_id):
            query['DestinationEndpointOwnerID'] = request.destination_endpoint_owner_id
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_role):
            query['DestinationEndpointRole'] = request.destination_endpoint_role
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.disaster_recovery_job):
            query['DisasterRecoveryJob'] = request.disaster_recovery_job
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not DaraCore.is_null(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not DaraCore.is_null(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.source_endpoint_vswitch_id):
            query['SourceEndpointVSwitchID'] = request.source_endpoint_vswitch_id
        if not DaraCore.is_null(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not DaraCore.is_null(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not DaraCore.is_null(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not DaraCore.is_null(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not DaraCore.is_null(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not DaraCore.is_null(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not DaraCore.is_null(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_dts_job(
        self,
        request: main_models.ConfigureDtsJobRequest,
    ) -> main_models.ConfigureDtsJobResponse:
        runtime = RuntimeOptions()
        return self.configure_dts_job_with_options(request, runtime)

    async def configure_dts_job_async(
        self,
        request: main_models.ConfigureDtsJobRequest,
    ) -> main_models.ConfigureDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.configure_dts_job_with_options_async(request, runtime)

    def configure_dts_job_advance(
        self,
        request: main_models.ConfigureDtsJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureDtsJobResponse:
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
            'Product': 'Dts',
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
        configure_dts_job_req = main_models.ConfigureDtsJobRequest()
        Utils.convert(request, configure_dts_job_req)
        if not DaraCore.is_null(request.file_oss_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_oss_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            configure_dts_job_req.file_oss_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        configure_dts_job_resp = self.configure_dts_job_with_options(configure_dts_job_req, runtime)
        return configure_dts_job_resp

    async def configure_dts_job_advance_async(
        self,
        request: main_models.ConfigureDtsJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureDtsJobResponse:
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
            'Product': 'Dts',
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
        configure_dts_job_req = main_models.ConfigureDtsJobRequest()
        Utils.convert(request, configure_dts_job_req)
        if not DaraCore.is_null(request.file_oss_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_oss_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            configure_dts_job_req.file_oss_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        configure_dts_job_resp = await self.configure_dts_job_with_options_async(configure_dts_job_req, runtime)
        return configure_dts_job_resp

    def configure_migration_job_with_options(
        self,
        request: main_models.ConfigureMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not DaraCore.is_null(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not DaraCore.is_null(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not DaraCore.is_null(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_migration_job_with_options_async(
        self,
        request: main_models.ConfigureMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not DaraCore.is_null(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not DaraCore.is_null(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not DaraCore.is_null(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_migration_job(
        self,
        request: main_models.ConfigureMigrationJobRequest,
    ) -> main_models.ConfigureMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    async def configure_migration_job_async(
        self,
        request: main_models.ConfigureMigrationJobRequest,
    ) -> main_models.ConfigureMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.configure_migration_job_with_options_async(request, runtime)

    def configure_migration_job_alert_with_options(
        self,
        request: main_models.ConfigureMigrationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureMigrationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'ConfigureMigrationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_migration_job_alert_with_options_async(
        self,
        request: main_models.ConfigureMigrationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureMigrationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'ConfigureMigrationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureMigrationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_migration_job_alert(
        self,
        request: main_models.ConfigureMigrationJobAlertRequest,
    ) -> main_models.ConfigureMigrationJobAlertResponse:
        runtime = RuntimeOptions()
        return self.configure_migration_job_alert_with_options(request, runtime)

    async def configure_migration_job_alert_async(
        self,
        request: main_models.ConfigureMigrationJobAlertRequest,
    ) -> main_models.ConfigureMigrationJobAlertResponse:
        runtime = RuntimeOptions()
        return await self.configure_migration_job_alert_with_options_async(request, runtime)

    def configure_subscription_with_options(
        self,
        request: main_models.ConfigureSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.db_list):
            query['DbList'] = request.db_list
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not DaraCore.is_null(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not DaraCore.is_null(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserve):
            query['Reserve'] = request.reserve
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not DaraCore.is_null(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not DaraCore.is_null(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not DaraCore.is_null(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not DaraCore.is_null(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not DaraCore.is_null(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not DaraCore.is_null(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not DaraCore.is_null(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not DaraCore.is_null(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not DaraCore.is_null(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscription',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_with_options_async(
        self,
        request: main_models.ConfigureSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.db_list):
            query['DbList'] = request.db_list
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not DaraCore.is_null(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not DaraCore.is_null(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserve):
            query['Reserve'] = request.reserve
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not DaraCore.is_null(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not DaraCore.is_null(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not DaraCore.is_null(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not DaraCore.is_null(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not DaraCore.is_null(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not DaraCore.is_null(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not DaraCore.is_null(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not DaraCore.is_null(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not DaraCore.is_null(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscription',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription(
        self,
        request: main_models.ConfigureSubscriptionRequest,
    ) -> main_models.ConfigureSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.configure_subscription_with_options(request, runtime)

    async def configure_subscription_async(
        self,
        request: main_models.ConfigureSubscriptionRequest,
    ) -> main_models.ConfigureSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.configure_subscription_with_options_async(request, runtime)

    def configure_subscription_instance_with_options(
        self,
        request: main_models.ConfigureSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not DaraCore.is_null(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not DaraCore.is_null(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not DaraCore.is_null(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not DaraCore.is_null(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_instance_with_options_async(
        self,
        request: main_models.ConfigureSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not DaraCore.is_null(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not DaraCore.is_null(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not DaraCore.is_null(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not DaraCore.is_null(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription_instance(
        self,
        request: main_models.ConfigureSubscriptionInstanceRequest,
    ) -> main_models.ConfigureSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    async def configure_subscription_instance_async(
        self,
        request: main_models.ConfigureSubscriptionInstanceRequest,
    ) -> main_models.ConfigureSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return await self.configure_subscription_instance_with_options_async(request, runtime)

    def configure_subscription_instance_alert_with_options(
        self,
        request: main_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionInstanceAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscriptionInstanceAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_instance_alert_with_options_async(
        self,
        request: main_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSubscriptionInstanceAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSubscriptionInstanceAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSubscriptionInstanceAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription_instance_alert(
        self,
        request: main_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> main_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = RuntimeOptions()
        return self.configure_subscription_instance_alert_with_options(request, runtime)

    async def configure_subscription_instance_alert_async(
        self,
        request: main_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> main_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = RuntimeOptions()
        return await self.configure_subscription_instance_alert_with_options_async(request, runtime)

    def configure_synchronization_job_with_options(
        self,
        request: main_models.ConfigureSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not DaraCore.is_null(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_with_options_async(
        self,
        request: main_models.ConfigureSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not DaraCore.is_null(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job(
        self,
        request: main_models.ConfigureSynchronizationJobRequest,
    ) -> main_models.ConfigureSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    async def configure_synchronization_job_async(
        self,
        request: main_models.ConfigureSynchronizationJobRequest,
    ) -> main_models.ConfigureSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.configure_synchronization_job_with_options_async(request, runtime)

    def configure_synchronization_job_alert_with_options(
        self,
        request: main_models.ConfigureSynchronizationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_alert_with_options_async(
        self,
        request: main_models.ConfigureSynchronizationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not DaraCore.is_null(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not DaraCore.is_null(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not DaraCore.is_null(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not DaraCore.is_null(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job_alert(
        self,
        request: main_models.ConfigureSynchronizationJobAlertRequest,
    ) -> main_models.ConfigureSynchronizationJobAlertResponse:
        runtime = RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

    async def configure_synchronization_job_alert_async(
        self,
        request: main_models.ConfigureSynchronizationJobAlertRequest,
    ) -> main_models.ConfigureSynchronizationJobAlertResponse:
        runtime = RuntimeOptions()
        return await self.configure_synchronization_job_alert_with_options_async(request, runtime)

    def configure_synchronization_job_replicator_compare_with_options(
        self,
        request: main_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJobReplicatorCompare',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_replicator_compare_with_options_async(
        self,
        request: main_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureSynchronizationJobReplicatorCompare',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job_replicator_compare(
        self,
        request: main_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> main_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = RuntimeOptions()
        return self.configure_synchronization_job_replicator_compare_with_options(request, runtime)

    async def configure_synchronization_job_replicator_compare_async(
        self,
        request: main_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> main_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = RuntimeOptions()
        return await self.configure_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def convert_instance_resource_group_with_options(
        self,
        request: main_models.ConvertInstanceResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstanceResourceGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_instance_resource_group_with_options_async(
        self,
        request: main_models.ConvertInstanceResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstanceResourceGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_instance_resource_group(
        self,
        request: main_models.ConvertInstanceResourceGroupRequest,
    ) -> main_models.ConvertInstanceResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.convert_instance_resource_group_with_options(request, runtime)

    async def convert_instance_resource_group_async(
        self,
        request: main_models.ConvertInstanceResourceGroupRequest,
    ) -> main_models.ConvertInstanceResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.convert_instance_resource_group_with_options_async(request, runtime)

    def count_job_by_condition_with_options(
        self,
        request: main_models.CountJobByConditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CountJobByConditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CountJobByCondition',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountJobByConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_job_by_condition_with_options_async(
        self,
        request: main_models.CountJobByConditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CountJobByConditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CountJobByCondition',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountJobByConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_job_by_condition(
        self,
        request: main_models.CountJobByConditionRequest,
    ) -> main_models.CountJobByConditionResponse:
        runtime = RuntimeOptions()
        return self.count_job_by_condition_with_options(request, runtime)

    async def count_job_by_condition_async(
        self,
        request: main_models.CountJobByConditionRequest,
    ) -> main_models.CountJobByConditionResponse:
        runtime = RuntimeOptions()
        return await self.count_job_by_condition_with_options_async(request, runtime)

    def create_consumer_channel_with_options(
        self,
        request: main_models.CreateConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_channel_with_options_async(
        self,
        request: main_models.CreateConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_channel(
        self,
        request: main_models.CreateConsumerChannelRequest,
    ) -> main_models.CreateConsumerChannelResponse:
        runtime = RuntimeOptions()
        return self.create_consumer_channel_with_options(request, runtime)

    async def create_consumer_channel_async(
        self,
        request: main_models.CreateConsumerChannelRequest,
    ) -> main_models.CreateConsumerChannelResponse:
        runtime = RuntimeOptions()
        return await self.create_consumer_channel_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: main_models.CreateConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_dedicated_cluster_monitor_rule_with_options(
        self,
        request: main_models.CreateDedicatedClusterMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDedicatedClusterMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_alarm_threshold):
            query['CpuAlarmThreshold'] = request.cpu_alarm_threshold
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.disk_alarm_threshold):
            query['DiskAlarmThreshold'] = request.disk_alarm_threshold
        if not DaraCore.is_null(request.du_alarm_threshold):
            query['DuAlarmThreshold'] = request.du_alarm_threshold
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mem_alarm_threshold):
            query['MemAlarmThreshold'] = request.mem_alarm_threshold
        if not DaraCore.is_null(request.notice_switch):
            query['NoticeSwitch'] = request.notice_switch
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phones):
            query['Phones'] = request.phones
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDedicatedClusterMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDedicatedClusterMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_cluster_monitor_rule_with_options_async(
        self,
        request: main_models.CreateDedicatedClusterMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDedicatedClusterMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_alarm_threshold):
            query['CpuAlarmThreshold'] = request.cpu_alarm_threshold
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.disk_alarm_threshold):
            query['DiskAlarmThreshold'] = request.disk_alarm_threshold
        if not DaraCore.is_null(request.du_alarm_threshold):
            query['DuAlarmThreshold'] = request.du_alarm_threshold
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mem_alarm_threshold):
            query['MemAlarmThreshold'] = request.mem_alarm_threshold
        if not DaraCore.is_null(request.notice_switch):
            query['NoticeSwitch'] = request.notice_switch
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phones):
            query['Phones'] = request.phones
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDedicatedClusterMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDedicatedClusterMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_cluster_monitor_rule(
        self,
        request: main_models.CreateDedicatedClusterMonitorRuleRequest,
    ) -> main_models.CreateDedicatedClusterMonitorRuleResponse:
        runtime = RuntimeOptions()
        return self.create_dedicated_cluster_monitor_rule_with_options(request, runtime)

    async def create_dedicated_cluster_monitor_rule_async(
        self,
        request: main_models.CreateDedicatedClusterMonitorRuleRequest,
    ) -> main_models.CreateDedicatedClusterMonitorRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_dedicated_cluster_monitor_rule_with_options_async(request, runtime)

    def create_doc_parser_job_with_options(
        self,
        request: main_models.CreateDocParserJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocParserJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocParserJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocParserJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_doc_parser_job_with_options_async(
        self,
        request: main_models.CreateDocParserJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocParserJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocParserJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocParserJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_doc_parser_job(
        self,
        request: main_models.CreateDocParserJobRequest,
    ) -> main_models.CreateDocParserJobResponse:
        runtime = RuntimeOptions()
        return self.create_doc_parser_job_with_options(request, runtime)

    async def create_doc_parser_job_async(
        self,
        request: main_models.CreateDocParserJobRequest,
    ) -> main_models.CreateDocParserJobResponse:
        runtime = RuntimeOptions()
        return await self.create_doc_parser_job_with_options_async(request, runtime)

    def create_doc_parser_job_advance(
        self,
        request: main_models.CreateDocParserJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocParserJobResponse:
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
            'Product': 'Dts',
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
        create_doc_parser_job_req = main_models.CreateDocParserJobRequest()
        Utils.convert(request, create_doc_parser_job_req)
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
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            create_doc_parser_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_doc_parser_job_resp = self.create_doc_parser_job_with_options(create_doc_parser_job_req, runtime)
        return create_doc_parser_job_resp

    async def create_doc_parser_job_advance_async(
        self,
        request: main_models.CreateDocParserJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocParserJobResponse:
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
            'Product': 'Dts',
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
        create_doc_parser_job_req = main_models.CreateDocParserJobRequest()
        Utils.convert(request, create_doc_parser_job_req)
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
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            create_doc_parser_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_doc_parser_job_resp = await self.create_doc_parser_job_with_options_async(create_doc_parser_job_req, runtime)
        return create_doc_parser_job_resp

    def create_dts_instance_with_options(
        self,
        request: main_models.CreateDtsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDtsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not DaraCore.is_null(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.dts_region):
            query['DtsRegion'] = request.dts_region
        if not DaraCore.is_null(request.du):
            query['Du'] = request.du
        if not DaraCore.is_null(request.fee_type):
            query['FeeType'] = request.fee_type
        if not DaraCore.is_null(request.insight_module):
            query['InsightModule'] = request.insight_module
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_region):
            query['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDtsInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDtsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dts_instance_with_options_async(
        self,
        request: main_models.CreateDtsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDtsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not DaraCore.is_null(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.dts_region):
            query['DtsRegion'] = request.dts_region
        if not DaraCore.is_null(request.du):
            query['Du'] = request.du
        if not DaraCore.is_null(request.fee_type):
            query['FeeType'] = request.fee_type
        if not DaraCore.is_null(request.insight_module):
            query['InsightModule'] = request.insight_module
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_region):
            query['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDtsInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDtsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dts_instance(
        self,
        request: main_models.CreateDtsInstanceRequest,
    ) -> main_models.CreateDtsInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_dts_instance_with_options(request, runtime)

    async def create_dts_instance_async(
        self,
        request: main_models.CreateDtsInstanceRequest,
    ) -> main_models.CreateDtsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_dts_instance_with_options_async(request, runtime)

    def create_job_monitor_rule_with_options(
        self,
        request: main_models.CreateJobMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.notice_value):
            query['NoticeValue'] = request.notice_value
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.times):
            query['Times'] = request.times
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_monitor_rule_with_options_async(
        self,
        request: main_models.CreateJobMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.notice_value):
            query['NoticeValue'] = request.notice_value
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.times):
            query['Times'] = request.times
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_monitor_rule(
        self,
        request: main_models.CreateJobMonitorRuleRequest,
    ) -> main_models.CreateJobMonitorRuleResponse:
        runtime = RuntimeOptions()
        return self.create_job_monitor_rule_with_options(request, runtime)

    async def create_job_monitor_rule_async(
        self,
        request: main_models.CreateJobMonitorRuleRequest,
    ) -> main_models.CreateJobMonitorRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_job_monitor_rule_with_options_async(request, runtime)

    def create_migration_job_with_options(
        self,
        request: main_models.CreateMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_job_with_options_async(
        self,
        request: main_models.CreateMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_job(
        self,
        request: main_models.CreateMigrationJobRequest,
    ) -> main_models.CreateMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    async def create_migration_job_async(
        self,
        request: main_models.CreateMigrationJobRequest,
    ) -> main_models.CreateMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.create_migration_job_with_options_async(request, runtime)

    def create_reverse_dts_job_with_options(
        self,
        request: main_models.CreateReverseDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReverseDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not DaraCore.is_null(request.shard_username):
            query['ShardUsername'] = request.shard_username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReverseDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReverseDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reverse_dts_job_with_options_async(
        self,
        request: main_models.CreateReverseDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReverseDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not DaraCore.is_null(request.shard_username):
            query['ShardUsername'] = request.shard_username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReverseDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReverseDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reverse_dts_job(
        self,
        request: main_models.CreateReverseDtsJobRequest,
    ) -> main_models.CreateReverseDtsJobResponse:
        runtime = RuntimeOptions()
        return self.create_reverse_dts_job_with_options(request, runtime)

    async def create_reverse_dts_job_async(
        self,
        request: main_models.CreateReverseDtsJobRequest,
    ) -> main_models.CreateReverseDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.create_reverse_dts_job_with_options_async(request, runtime)

    def create_subscription_instance_with_options(
        self,
        request: main_models.CreateSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscription_instance_with_options_async(
        self,
        request: main_models.CreateSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscription_instance(
        self,
        request: main_models.CreateSubscriptionInstanceRequest,
    ) -> main_models.CreateSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    async def create_subscription_instance_async(
        self,
        request: main_models.CreateSubscriptionInstanceRequest,
    ) -> main_models.CreateSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_subscription_instance_with_options_async(request, runtime)

    def create_synchronization_job_with_options(
        self,
        request: main_models.CreateSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_region):
            query['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.network_type):
            query['networkType'] = request.network_type
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_synchronization_job_with_options_async(
        self,
        request: main_models.CreateSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_region):
            query['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.network_type):
            query['networkType'] = request.network_type
        if not DaraCore.is_null(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_synchronization_job(
        self,
        request: main_models.CreateSynchronizationJobRequest,
    ) -> main_models.CreateSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    async def create_synchronization_job_async(
        self,
        request: main_models.CreateSynchronizationJobRequest,
    ) -> main_models.CreateSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.create_synchronization_job_with_options_async(request, runtime)

    def delete_consumer_channel_with_options(
        self,
        request: main_models.DeleteConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_channel_with_options_async(
        self,
        request: main_models.DeleteConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_channel(
        self,
        request: main_models.DeleteConsumerChannelRequest,
    ) -> main_models.DeleteConsumerChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_consumer_channel_with_options(request, runtime)

    async def delete_consumer_channel_async(
        self,
        request: main_models.DeleteConsumerChannelRequest,
    ) -> main_models.DeleteConsumerChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_consumer_channel_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: main_models.DeleteConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: main_models.DeleteConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_dts_job_with_options(
        self,
        request: main_models.DeleteDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dts_job_with_options_async(
        self,
        request: main_models.DeleteDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dts_job(
        self,
        request: main_models.DeleteDtsJobRequest,
    ) -> main_models.DeleteDtsJobResponse:
        runtime = RuntimeOptions()
        return self.delete_dts_job_with_options(request, runtime)

    async def delete_dts_job_async(
        self,
        request: main_models.DeleteDtsJobRequest,
    ) -> main_models.DeleteDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_dts_job_with_options_async(request, runtime)

    def delete_dts_jobs_with_options(
        self,
        request: main_models.DeleteDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dts_jobs_with_options_async(
        self,
        request: main_models.DeleteDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dts_jobs(
        self,
        request: main_models.DeleteDtsJobsRequest,
    ) -> main_models.DeleteDtsJobsResponse:
        runtime = RuntimeOptions()
        return self.delete_dts_jobs_with_options(request, runtime)

    async def delete_dts_jobs_async(
        self,
        request: main_models.DeleteDtsJobsRequest,
    ) -> main_models.DeleteDtsJobsResponse:
        runtime = RuntimeOptions()
        return await self.delete_dts_jobs_with_options_async(request, runtime)

    def delete_migration_job_with_options(
        self,
        request: main_models.DeleteMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DeleteMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_job_with_options_async(
        self,
        request: main_models.DeleteMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DeleteMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_job(
        self,
        request: main_models.DeleteMigrationJobRequest,
    ) -> main_models.DeleteMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    async def delete_migration_job_async(
        self,
        request: main_models.DeleteMigrationJobRequest,
    ) -> main_models.DeleteMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_migration_job_with_options_async(request, runtime)

    def delete_subscription_instance_with_options(
        self,
        request: main_models.DeleteSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subscription_instance_with_options_async(
        self,
        request: main_models.DeleteSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subscription_instance(
        self,
        request: main_models.DeleteSubscriptionInstanceRequest,
    ) -> main_models.DeleteSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    async def delete_subscription_instance_async(
        self,
        request: main_models.DeleteSubscriptionInstanceRequest,
    ) -> main_models.DeleteSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_subscription_instance_with_options_async(request, runtime)

    def delete_synchronization_job_with_options(
        self,
        request: main_models.DeleteSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_synchronization_job_with_options_async(
        self,
        request: main_models.DeleteSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_synchronization_job(
        self,
        request: main_models.DeleteSynchronizationJobRequest,
    ) -> main_models.DeleteSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    async def delete_synchronization_job_async(
        self,
        request: main_models.DeleteSynchronizationJobRequest,
    ) -> main_models.DeleteSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_synchronization_job_with_options_async(request, runtime)

    def describe_channel_account_with_options(
        self,
        request: main_models.DescribeChannelAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAccount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_account_with_options_async(
        self,
        request: main_models.DescribeChannelAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAccount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_account(
        self,
        request: main_models.DescribeChannelAccountRequest,
    ) -> main_models.DescribeChannelAccountResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_account_with_options(request, runtime)

    async def describe_channel_account_async(
        self,
        request: main_models.DescribeChannelAccountRequest,
    ) -> main_models.DescribeChannelAccountResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_account_with_options_async(request, runtime)

    def describe_check_jobs_with_options(
        self,
        request: main_models.DescribeCheckJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCheckJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_job_id):
            query['CheckJobId'] = request.check_job_id
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCheckJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCheckJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_jobs_with_options_async(
        self,
        request: main_models.DescribeCheckJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCheckJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_job_id):
            query['CheckJobId'] = request.check_job_id
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCheckJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCheckJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_jobs(
        self,
        request: main_models.DescribeCheckJobsRequest,
    ) -> main_models.DescribeCheckJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_check_jobs_with_options(request, runtime)

    async def describe_check_jobs_async(
        self,
        request: main_models.DescribeCheckJobsRequest,
    ) -> main_models.DescribeCheckJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_check_jobs_with_options_async(request, runtime)

    def describe_cluster_operate_logs_with_options(
        self,
        request: main_models.DescribeClusterOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterOperateLogs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_operate_logs_with_options_async(
        self,
        request: main_models.DescribeClusterOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterOperateLogs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_operate_logs(
        self,
        request: main_models.DescribeClusterOperateLogsRequest,
    ) -> main_models.DescribeClusterOperateLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_operate_logs_with_options(request, runtime)

    async def describe_cluster_operate_logs_async(
        self,
        request: main_models.DescribeClusterOperateLogsRequest,
    ) -> main_models.DescribeClusterOperateLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_operate_logs_with_options_async(request, runtime)

    def describe_cluster_used_utilization_with_options(
        self,
        request: main_models.DescribeClusterUsedUtilizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterUsedUtilizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.env):
            body['Env'] = request.env
        if not DaraCore.is_null(request.metric_type):
            body['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterUsedUtilization',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterUsedUtilizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_used_utilization_with_options_async(
        self,
        request: main_models.DescribeClusterUsedUtilizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterUsedUtilizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.env):
            body['Env'] = request.env
        if not DaraCore.is_null(request.metric_type):
            body['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterUsedUtilization',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterUsedUtilizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_used_utilization(
        self,
        request: main_models.DescribeClusterUsedUtilizationRequest,
    ) -> main_models.DescribeClusterUsedUtilizationResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_used_utilization_with_options(request, runtime)

    async def describe_cluster_used_utilization_async(
        self,
        request: main_models.DescribeClusterUsedUtilizationRequest,
    ) -> main_models.DescribeClusterUsedUtilizationResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_used_utilization_with_options_async(request, runtime)

    def describe_connection_status_with_options(
        self,
        request: main_models.DescribeConnectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not DaraCore.is_null(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConnectionStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_connection_status_with_options_async(
        self,
        request: main_models.DescribeConnectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not DaraCore.is_null(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not DaraCore.is_null(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConnectionStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_connection_status(
        self,
        request: main_models.DescribeConnectionStatusRequest,
    ) -> main_models.DescribeConnectionStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_connection_status_with_options(request, runtime)

    async def describe_connection_status_async(
        self,
        request: main_models.DescribeConnectionStatusRequest,
    ) -> main_models.DescribeConnectionStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_connection_status_with_options_async(request, runtime)

    def describe_consumer_channel_with_options(
        self,
        request: main_models.DescribeConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consumer_channel_with_options_async(
        self,
        request: main_models.DescribeConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consumer_channel(
        self,
        request: main_models.DescribeConsumerChannelRequest,
    ) -> main_models.DescribeConsumerChannelResponse:
        runtime = RuntimeOptions()
        return self.describe_consumer_channel_with_options(request, runtime)

    async def describe_consumer_channel_async(
        self,
        request: main_models.DescribeConsumerChannelRequest,
    ) -> main_models.DescribeConsumerChannelResponse:
        runtime = RuntimeOptions()
        return await self.describe_consumer_channel_with_options_async(request, runtime)

    def describe_consumer_group_with_options(
        self,
        request: main_models.DescribeConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consumer_group_with_options_async(
        self,
        request: main_models.DescribeConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConsumerGroup',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consumer_group(
        self,
        request: main_models.DescribeConsumerGroupRequest,
    ) -> main_models.DescribeConsumerGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_consumer_group_with_options(request, runtime)

    async def describe_consumer_group_async(
        self,
        request: main_models.DescribeConsumerGroupRequest,
    ) -> main_models.DescribeConsumerGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_consumer_group_with_options_async(request, runtime)

    def describe_dtsipwith_options(
        self,
        request: main_models.DescribeDTSIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDTSIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDTSIP',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDTSIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dtsipwith_options_async(
        self,
        request: main_models.DescribeDTSIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDTSIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDTSIP',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDTSIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dtsip(
        self,
        request: main_models.DescribeDTSIPRequest,
    ) -> main_models.DescribeDTSIPResponse:
        runtime = RuntimeOptions()
        return self.describe_dtsipwith_options(request, runtime)

    async def describe_dtsip_async(
        self,
        request: main_models.DescribeDTSIPRequest,
    ) -> main_models.DescribeDTSIPResponse:
        runtime = RuntimeOptions()
        return await self.describe_dtsipwith_options_async(request, runtime)

    def describe_data_check_report_url_with_options(
        self,
        request: main_models.DescribeDataCheckReportUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckReportUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckReportUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_check_report_url_with_options_async(
        self,
        request: main_models.DescribeDataCheckReportUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckReportUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckReportUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckReportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_check_report_url(
        self,
        request: main_models.DescribeDataCheckReportUrlRequest,
    ) -> main_models.DescribeDataCheckReportUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_data_check_report_url_with_options(request, runtime)

    async def describe_data_check_report_url_async(
        self,
        request: main_models.DescribeDataCheckReportUrlRequest,
    ) -> main_models.DescribeDataCheckReportUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_check_report_url_with_options_async(request, runtime)

    def describe_data_check_table_details_with_options(
        self,
        request: main_models.DescribeDataCheckTableDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckTableDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckTableDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_check_table_details_with_options_async(
        self,
        request: main_models.DescribeDataCheckTableDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckTableDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckTableDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_check_table_details(
        self,
        request: main_models.DescribeDataCheckTableDetailsRequest,
    ) -> main_models.DescribeDataCheckTableDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_check_table_details_with_options(request, runtime)

    async def describe_data_check_table_details_async(
        self,
        request: main_models.DescribeDataCheckTableDetailsRequest,
    ) -> main_models.DescribeDataCheckTableDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_check_table_details_with_options_async(request, runtime)

    def describe_data_check_table_diff_details_with_options(
        self,
        request: main_models.DescribeDataCheckTableDiffDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckTableDiffDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckTableDiffDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckTableDiffDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_check_table_diff_details_with_options_async(
        self,
        request: main_models.DescribeDataCheckTableDiffDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCheckTableDiffDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['CheckType'] = request.check_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCheckTableDiffDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCheckTableDiffDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_check_table_diff_details(
        self,
        request: main_models.DescribeDataCheckTableDiffDetailsRequest,
    ) -> main_models.DescribeDataCheckTableDiffDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_check_table_diff_details_with_options(request, runtime)

    async def describe_data_check_table_diff_details_async(
        self,
        request: main_models.DescribeDataCheckTableDiffDetailsRequest,
    ) -> main_models.DescribeDataCheckTableDiffDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_check_table_diff_details_with_options_async(request, runtime)

    def describe_dedicated_cluster_with_options(
        self,
        request: main_models.DescribeDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
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
            action = 'DescribeDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_cluster_with_options_async(
        self,
        request: main_models.DescribeDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
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
            action = 'DescribeDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_cluster(
        self,
        request: main_models.DescribeDedicatedClusterRequest,
    ) -> main_models.DescribeDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return self.describe_dedicated_cluster_with_options(request, runtime)

    async def describe_dedicated_cluster_async(
        self,
        request: main_models.DescribeDedicatedClusterRequest,
    ) -> main_models.DescribeDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return await self.describe_dedicated_cluster_with_options_async(request, runtime)

    def describe_dedicated_cluster_monitor_rule_with_options(
        self,
        request: main_models.DescribeDedicatedClusterMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedClusterMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
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
            action = 'DescribeDedicatedClusterMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedClusterMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_cluster_monitor_rule_with_options_async(
        self,
        request: main_models.DescribeDedicatedClusterMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedClusterMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
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
            action = 'DescribeDedicatedClusterMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedClusterMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_cluster_monitor_rule(
        self,
        request: main_models.DescribeDedicatedClusterMonitorRuleRequest,
    ) -> main_models.DescribeDedicatedClusterMonitorRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_dedicated_cluster_monitor_rule_with_options(request, runtime)

    async def describe_dedicated_cluster_monitor_rule_async(
        self,
        request: main_models.DescribeDedicatedClusterMonitorRuleRequest,
    ) -> main_models.DescribeDedicatedClusterMonitorRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_dedicated_cluster_monitor_rule_with_options_async(request, runtime)

    def describe_doc_parser_job_result_with_options(
        self,
        request: main_models.DescribeDocParserJobResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocParserJobResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocParserJobResult',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocParserJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doc_parser_job_result_with_options_async(
        self,
        request: main_models.DescribeDocParserJobResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocParserJobResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocParserJobResult',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocParserJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doc_parser_job_result(
        self,
        request: main_models.DescribeDocParserJobResultRequest,
    ) -> main_models.DescribeDocParserJobResultResponse:
        runtime = RuntimeOptions()
        return self.describe_doc_parser_job_result_with_options(request, runtime)

    async def describe_doc_parser_job_result_async(
        self,
        request: main_models.DescribeDocParserJobResultRequest,
    ) -> main_models.DescribeDocParserJobResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_doc_parser_job_result_with_options_async(request, runtime)

    def describe_doc_parser_job_status_with_options(
        self,
        request: main_models.DescribeDocParserJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocParserJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocParserJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocParserJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doc_parser_job_status_with_options_async(
        self,
        request: main_models.DescribeDocParserJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocParserJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.rag_instance_id):
            query['RagInstanceId'] = request.rag_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocParserJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocParserJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doc_parser_job_status(
        self,
        request: main_models.DescribeDocParserJobStatusRequest,
    ) -> main_models.DescribeDocParserJobStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_doc_parser_job_status_with_options(request, runtime)

    async def describe_doc_parser_job_status_async(
        self,
        request: main_models.DescribeDocParserJobStatusRequest,
    ) -> main_models.DescribeDocParserJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_doc_parser_job_status_with_options_async(request, runtime)

    def describe_dts_etl_job_version_info_with_options(
        self,
        request: main_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsEtlJobVersionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsEtlJobVersionInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsEtlJobVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_etl_job_version_info_with_options_async(
        self,
        request: main_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsEtlJobVersionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsEtlJobVersionInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsEtlJobVersionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_etl_job_version_info(
        self,
        request: main_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> main_models.DescribeDtsEtlJobVersionInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dts_etl_job_version_info_with_options(request, runtime)

    async def describe_dts_etl_job_version_info_async(
        self,
        request: main_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> main_models.DescribeDtsEtlJobVersionInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dts_etl_job_version_info_with_options_async(request, runtime)

    def describe_dts_job_config_with_options(
        self,
        request: main_models.DescribeDtsJobConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.for_acceleration):
            query['ForAcceleration'] = request.for_acceleration
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
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
            action = 'DescribeDtsJobConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_job_config_with_options_async(
        self,
        request: main_models.DescribeDtsJobConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.for_acceleration):
            query['ForAcceleration'] = request.for_acceleration
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
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
            action = 'DescribeDtsJobConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_job_config(
        self,
        request: main_models.DescribeDtsJobConfigRequest,
    ) -> main_models.DescribeDtsJobConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dts_job_config_with_options(request, runtime)

    async def describe_dts_job_config_async(
        self,
        request: main_models.DescribeDtsJobConfigRequest,
    ) -> main_models.DescribeDtsJobConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dts_job_config_with_options_async(request, runtime)

    def describe_dts_job_detail_with_options(
        self,
        request: main_models.DescribeDtsJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_job_detail_with_options_async(
        self,
        request: main_models.DescribeDtsJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_job_detail(
        self,
        request: main_models.DescribeDtsJobDetailRequest,
    ) -> main_models.DescribeDtsJobDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dts_job_detail_with_options(request, runtime)

    async def describe_dts_job_detail_async(
        self,
        request: main_models.DescribeDtsJobDetailRequest,
    ) -> main_models.DescribeDtsJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dts_job_detail_with_options_async(request, runtime)

    def describe_dts_jobs_with_options(
        self,
        request: main_models.DescribeDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dest_product_type):
            query['DestProductType'] = request.dest_product_type
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_product_type):
            query['SrcProductType'] = request.src_product_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.without_db_list):
            query['WithoutDbList'] = request.without_db_list
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_jobs_with_options_async(
        self,
        request: main_models.DescribeDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dest_product_type):
            query['DestProductType'] = request.dest_product_type
        if not DaraCore.is_null(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_product_type):
            query['SrcProductType'] = request.src_product_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.without_db_list):
            query['WithoutDbList'] = request.without_db_list
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_jobs(
        self,
        request: main_models.DescribeDtsJobsRequest,
    ) -> main_models.DescribeDtsJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_dts_jobs_with_options(request, runtime)

    async def describe_dts_jobs_async(
        self,
        request: main_models.DescribeDtsJobsRequest,
    ) -> main_models.DescribeDtsJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dts_jobs_with_options_async(request, runtime)

    def describe_dts_service_log_with_options(
        self,
        request: main_models.DescribeDtsServiceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsServiceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsServiceLog',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_service_log_with_options_async(
        self,
        request: main_models.DescribeDtsServiceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDtsServiceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDtsServiceLog',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDtsServiceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_service_log(
        self,
        request: main_models.DescribeDtsServiceLogRequest,
    ) -> main_models.DescribeDtsServiceLogResponse:
        runtime = RuntimeOptions()
        return self.describe_dts_service_log_with_options(request, runtime)

    async def describe_dts_service_log_async(
        self,
        request: main_models.DescribeDtsServiceLogRequest,
    ) -> main_models.DescribeDtsServiceLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_dts_service_log_with_options_async(request, runtime)

    def describe_endpoint_switch_status_with_options(
        self,
        request: main_models.DescribeEndpointSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpointSwitchStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoint_switch_status_with_options_async(
        self,
        request: main_models.DescribeEndpointSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpointSwitchStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoint_switch_status(
        self,
        request: main_models.DescribeEndpointSwitchStatusRequest,
    ) -> main_models.DescribeEndpointSwitchStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    async def describe_endpoint_switch_status_async(
        self,
        request: main_models.DescribeEndpointSwitchStatusRequest,
    ) -> main_models.DescribeEndpointSwitchStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_endpoint_switch_status_with_options_async(request, runtime)

    def describe_etl_job_logs_with_options(
        self,
        request: main_models.DescribeEtlJobLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEtlJobLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEtlJobLogs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEtlJobLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_etl_job_logs_with_options_async(
        self,
        request: main_models.DescribeEtlJobLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEtlJobLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEtlJobLogs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEtlJobLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_etl_job_logs(
        self,
        request: main_models.DescribeEtlJobLogsRequest,
    ) -> main_models.DescribeEtlJobLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_etl_job_logs_with_options(request, runtime)

    async def describe_etl_job_logs_async(
        self,
        request: main_models.DescribeEtlJobLogsRequest,
    ) -> main_models.DescribeEtlJobLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_etl_job_logs_with_options_async(request, runtime)

    def describe_full_process_list_with_options(
        self,
        request: main_models.DescribeFullProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFullProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFullProcessList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFullProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_full_process_list_with_options_async(
        self,
        request: main_models.DescribeFullProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFullProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFullProcessList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFullProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_full_process_list(
        self,
        request: main_models.DescribeFullProcessListRequest,
    ) -> main_models.DescribeFullProcessListResponse:
        runtime = RuntimeOptions()
        return self.describe_full_process_list_with_options(request, runtime)

    async def describe_full_process_list_async(
        self,
        request: main_models.DescribeFullProcessListRequest,
    ) -> main_models.DescribeFullProcessListResponse:
        runtime = RuntimeOptions()
        return await self.describe_full_process_list_with_options_async(request, runtime)

    def describe_gad_instances_with_options(
        self,
        request: main_models.DescribeGadInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGadInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_engine_types):
            query['DbEngineTypes'] = request.db_engine_types
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
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
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGadInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGadInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gad_instances_with_options_async(
        self,
        request: main_models.DescribeGadInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGadInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_engine_types):
            query['DbEngineTypes'] = request.db_engine_types
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
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
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGadInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGadInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gad_instances(
        self,
        request: main_models.DescribeGadInstancesRequest,
    ) -> main_models.DescribeGadInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_gad_instances_with_options(request, runtime)

    async def describe_gad_instances_async(
        self,
        request: main_models.DescribeGadInstancesRequest,
    ) -> main_models.DescribeGadInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_gad_instances_with_options_async(request, runtime)

    def describe_initialization_status_with_options(
        self,
        request: main_models.DescribeInitializationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInitializationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInitializationStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInitializationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_initialization_status_with_options_async(
        self,
        request: main_models.DescribeInitializationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInitializationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInitializationStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInitializationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_initialization_status(
        self,
        request: main_models.DescribeInitializationStatusRequest,
    ) -> main_models.DescribeInitializationStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    async def describe_initialization_status_async(
        self,
        request: main_models.DescribeInitializationStatusRequest,
    ) -> main_models.DescribeInitializationStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_initialization_status_with_options_async(request, runtime)

    def describe_job_monitor_rule_with_options(
        self,
        request: main_models.DescribeJobMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_monitor_rule_with_options_async(
        self,
        request: main_models.DescribeJobMonitorRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMonitorRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMonitorRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_monitor_rule(
        self,
        request: main_models.DescribeJobMonitorRuleRequest,
    ) -> main_models.DescribeJobMonitorRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_job_monitor_rule_with_options(request, runtime)

    async def describe_job_monitor_rule_async(
        self,
        request: main_models.DescribeJobMonitorRuleRequest,
    ) -> main_models.DescribeJobMonitorRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_monitor_rule_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            body['Env'] = request.env
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            body['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            body['Env'] = request.env
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            body['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_list(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_migration_job_alert_with_options(
        self,
        request: main_models.DescribeMigrationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DescribeMigrationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_alert_with_options_async(
        self,
        request: main_models.DescribeMigrationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DescribeMigrationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_alert(
        self,
        request: main_models.DescribeMigrationJobAlertRequest,
    ) -> main_models.DescribeMigrationJobAlertResponse:
        runtime = RuntimeOptions()
        return self.describe_migration_job_alert_with_options(request, runtime)

    async def describe_migration_job_alert_async(
        self,
        request: main_models.DescribeMigrationJobAlertRequest,
    ) -> main_models.DescribeMigrationJobAlertResponse:
        runtime = RuntimeOptions()
        return await self.describe_migration_job_alert_with_options_async(request, runtime)

    def describe_migration_job_detail_with_options(
        self,
        request: main_models.DescribeMigrationJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMigrationJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_detail_with_options_async(
        self,
        request: main_models.DescribeMigrationJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMigrationJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_detail(
        self,
        request: main_models.DescribeMigrationJobDetailRequest,
    ) -> main_models.DescribeMigrationJobDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    async def describe_migration_job_detail_async(
        self,
        request: main_models.DescribeMigrationJobDetailRequest,
    ) -> main_models.DescribeMigrationJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_migration_job_detail_with_options_async(request, runtime)

    def describe_migration_job_status_with_options(
        self,
        request: main_models.DescribeMigrationJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DescribeMigrationJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_status_with_options_async(
        self,
        request: main_models.DescribeMigrationJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'DescribeMigrationJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_status(
        self,
        request: main_models.DescribeMigrationJobStatusRequest,
    ) -> main_models.DescribeMigrationJobStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    async def describe_migration_job_status_async(
        self,
        request: main_models.DescribeMigrationJobStatusRequest,
    ) -> main_models.DescribeMigrationJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_migration_job_status_with_options_async(request, runtime)

    def describe_migration_jobs_with_options(
        self,
        request: main_models.DescribeMigrationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMigrationJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_jobs_with_options_async(
        self,
        request: main_models.DescribeMigrationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMigrationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMigrationJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMigrationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_jobs(
        self,
        request: main_models.DescribeMigrationJobsRequest,
    ) -> main_models.DescribeMigrationJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    async def describe_migration_jobs_async(
        self,
        request: main_models.DescribeMigrationJobsRequest,
    ) -> main_models.DescribeMigrationJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_migration_jobs_with_options_async(request, runtime)

    def describe_pre_check_create_gad_order_result_with_options(
        self,
        request: main_models.DescribePreCheckCreateGadOrderResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckCreateGadOrderResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckCreateGadOrderResult',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckCreateGadOrderResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_create_gad_order_result_with_options_async(
        self,
        request: main_models.DescribePreCheckCreateGadOrderResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckCreateGadOrderResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckCreateGadOrderResult',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckCreateGadOrderResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_create_gad_order_result(
        self,
        request: main_models.DescribePreCheckCreateGadOrderResultRequest,
    ) -> main_models.DescribePreCheckCreateGadOrderResultResponse:
        runtime = RuntimeOptions()
        return self.describe_pre_check_create_gad_order_result_with_options(request, runtime)

    async def describe_pre_check_create_gad_order_result_async(
        self,
        request: main_models.DescribePreCheckCreateGadOrderResultRequest,
    ) -> main_models.DescribePreCheckCreateGadOrderResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_pre_check_create_gad_order_result_with_options_async(request, runtime)

    def describe_pre_check_status_with_options(
        self,
        request: main_models.DescribePreCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not DaraCore.is_null(request.struct_type):
            query['StructType'] = request.struct_type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_status_with_options_async(
        self,
        request: main_models.DescribePreCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not DaraCore.is_null(request.struct_type):
            query['StructType'] = request.struct_type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_status(
        self,
        request: main_models.DescribePreCheckStatusRequest,
    ) -> main_models.DescribePreCheckStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_pre_check_status_with_options(request, runtime)

    async def describe_pre_check_status_async(
        self,
        request: main_models.DescribePreCheckStatusRequest,
    ) -> main_models.DescribePreCheckStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_pre_check_status_with_options_async(request, runtime)

    def describe_subscription_instance_alert_with_options(
        self,
        request: main_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstanceAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstanceAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instance_alert_with_options_async(
        self,
        request: main_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstanceAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstanceAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstanceAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instance_alert(
        self,
        request: main_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> main_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = RuntimeOptions()
        return self.describe_subscription_instance_alert_with_options(request, runtime)

    async def describe_subscription_instance_alert_async(
        self,
        request: main_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> main_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = RuntimeOptions()
        return await self.describe_subscription_instance_alert_with_options_async(request, runtime)

    def describe_subscription_instance_status_with_options(
        self,
        request: main_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstanceStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instance_status_with_options_async(
        self,
        request: main_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstanceStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instance_status(
        self,
        request: main_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> main_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    async def describe_subscription_instance_status_async(
        self,
        request: main_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> main_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_subscription_instance_status_with_options_async(request, runtime)

    def describe_subscription_instances_with_options(
        self,
        request: main_models.DescribeSubscriptionInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instances_with_options_async(
        self,
        request: main_models.DescribeSubscriptionInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instances(
        self,
        request: main_models.DescribeSubscriptionInstancesRequest,
    ) -> main_models.DescribeSubscriptionInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    async def describe_subscription_instances_async(
        self,
        request: main_models.DescribeSubscriptionInstancesRequest,
    ) -> main_models.DescribeSubscriptionInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_subscription_instances_with_options_async(request, runtime)

    def describe_subscription_meta_with_options(
        self,
        tmp_req: main_models.DescribeSubscriptionMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionMetaResponse:
        tmp_req.validate()
        request = main_models.DescribeSubscriptionMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not DaraCore.is_null(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionMeta',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_meta_with_options_async(
        self,
        tmp_req: main_models.DescribeSubscriptionMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubscriptionMetaResponse:
        tmp_req.validate()
        request = main_models.DescribeSubscriptionMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not DaraCore.is_null(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubscriptionMeta',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubscriptionMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_meta(
        self,
        request: main_models.DescribeSubscriptionMetaRequest,
    ) -> main_models.DescribeSubscriptionMetaResponse:
        runtime = RuntimeOptions()
        return self.describe_subscription_meta_with_options(request, runtime)

    async def describe_subscription_meta_async(
        self,
        request: main_models.DescribeSubscriptionMetaRequest,
    ) -> main_models.DescribeSubscriptionMetaResponse:
        runtime = RuntimeOptions()
        return await self.describe_subscription_meta_with_options_async(request, runtime)

    def describe_sync_status_with_options(
        self,
        request: main_models.DescribeSyncStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_status_with_options_async(
        self,
        request: main_models.DescribeSyncStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_status(
        self,
        request: main_models.DescribeSyncStatusRequest,
    ) -> main_models.DescribeSyncStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sync_status_with_options(request, runtime)

    async def describe_sync_status_async(
        self,
        request: main_models.DescribeSyncStatusRequest,
    ) -> main_models.DescribeSyncStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sync_status_with_options_async(request, runtime)

    def describe_synchronization_job_alert_with_options(
        self,
        request: main_models.DescribeSynchronizationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_alert_with_options_async(
        self,
        request: main_models.DescribeSynchronizationJobAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobAlert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_alert(
        self,
        request: main_models.DescribeSynchronizationJobAlertRequest,
    ) -> main_models.DescribeSynchronizationJobAlertResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    async def describe_synchronization_job_alert_async(
        self,
        request: main_models.DescribeSynchronizationJobAlertRequest,
    ) -> main_models.DescribeSynchronizationJobAlertResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_job_alert_with_options_async(request, runtime)

    def describe_synchronization_job_replicator_compare_with_options(
        self,
        request: main_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobReplicatorCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobReplicatorCompare',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_replicator_compare_with_options_async(
        self,
        request: main_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobReplicatorCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobReplicatorCompare',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobReplicatorCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_replicator_compare(
        self,
        request: main_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> main_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_job_replicator_compare_with_options(request, runtime)

    async def describe_synchronization_job_replicator_compare_async(
        self,
        request: main_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> main_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def describe_synchronization_job_status_with_options(
        self,
        request: main_models.DescribeSynchronizationJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_status_with_options_async(
        self,
        request: main_models.DescribeSynchronizationJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_status(
        self,
        request: main_models.DescribeSynchronizationJobStatusRequest,
    ) -> main_models.DescribeSynchronizationJobStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    async def describe_synchronization_job_status_async(
        self,
        request: main_models.DescribeSynchronizationJobStatusRequest,
    ) -> main_models.DescribeSynchronizationJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_job_status_with_options_async(request, runtime)

    def describe_synchronization_job_status_list_with_options(
        self,
        request: main_models.DescribeSynchronizationJobStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobStatusList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_status_list_with_options_async(
        self,
        request: main_models.DescribeSynchronizationJobStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobStatusList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobStatusListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_status_list(
        self,
        request: main_models.DescribeSynchronizationJobStatusListRequest,
    ) -> main_models.DescribeSynchronizationJobStatusListResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_job_status_list_with_options(request, runtime)

    async def describe_synchronization_job_status_list_async(
        self,
        request: main_models.DescribeSynchronizationJobStatusListRequest,
    ) -> main_models.DescribeSynchronizationJobStatusListResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_job_status_list_with_options_async(request, runtime)

    def describe_synchronization_jobs_with_options(
        self,
        request: main_models.DescribeSynchronizationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_jobs_with_options_async(
        self,
        request: main_models.DescribeSynchronizationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_jobs(
        self,
        request: main_models.DescribeSynchronizationJobsRequest,
    ) -> main_models.DescribeSynchronizationJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    async def describe_synchronization_jobs_async(
        self,
        request: main_models.DescribeSynchronizationJobsRequest,
    ) -> main_models.DescribeSynchronizationJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_jobs_with_options_async(request, runtime)

    def describe_synchronization_object_modify_status_with_options(
        self,
        request: main_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationObjectModifyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationObjectModifyStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_object_modify_status_with_options_async(
        self,
        request: main_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynchronizationObjectModifyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynchronizationObjectModifyStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynchronizationObjectModifyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_object_modify_status(
        self,
        request: main_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> main_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    async def describe_synchronization_object_modify_status_async(
        self,
        request: main_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> main_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_synchronization_object_modify_status_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: main_models.DescribeTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeys',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_keys_with_options_async(
        self,
        request: main_models.DescribeTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeys',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_keys(
        self,
        request: main_models.DescribeTagKeysRequest,
    ) -> main_models.DescribeTagKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: main_models.DescribeTagKeysRequest,
    ) -> main_models.DescribeTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_values_with_options(
        self,
        request: main_models.DescribeTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagValues',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_values_with_options_async(
        self,
        request: main_models.DescribeTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagValues',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_values(
        self,
        request: main_models.DescribeTagValuesRequest,
    ) -> main_models.DescribeTagValuesResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_values_with_options(request, runtime)

    async def describe_tag_values_async(
        self,
        request: main_models.DescribeTagValuesRequest,
    ) -> main_models.DescribeTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_values_with_options_async(request, runtime)

    def detach_gad_instance_db_member_with_options(
        self,
        request: main_models.DetachGadInstanceDbMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachGadInstanceDbMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGadInstanceDbMember',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGadInstanceDbMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_gad_instance_db_member_with_options_async(
        self,
        request: main_models.DetachGadInstanceDbMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachGadInstanceDbMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGadInstanceDbMember',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGadInstanceDbMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_gad_instance_db_member(
        self,
        request: main_models.DetachGadInstanceDbMemberRequest,
    ) -> main_models.DetachGadInstanceDbMemberResponse:
        runtime = RuntimeOptions()
        return self.detach_gad_instance_db_member_with_options(request, runtime)

    async def detach_gad_instance_db_member_async(
        self,
        request: main_models.DetachGadInstanceDbMemberRequest,
    ) -> main_models.DetachGadInstanceDbMemberResponse:
        runtime = RuntimeOptions()
        return await self.detach_gad_instance_db_member_with_options_async(request, runtime)

    def init_dts_rds_instance_with_options(
        self,
        request: main_models.InitDtsRdsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitDtsRdsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not DaraCore.is_null(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not DaraCore.is_null(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not DaraCore.is_null(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitDtsRdsInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitDtsRdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_dts_rds_instance_with_options_async(
        self,
        request: main_models.InitDtsRdsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitDtsRdsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not DaraCore.is_null(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not DaraCore.is_null(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not DaraCore.is_null(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitDtsRdsInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitDtsRdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_dts_rds_instance(
        self,
        request: main_models.InitDtsRdsInstanceRequest,
    ) -> main_models.InitDtsRdsInstanceResponse:
        runtime = RuntimeOptions()
        return self.init_dts_rds_instance_with_options(request, runtime)

    async def init_dts_rds_instance_async(
        self,
        request: main_models.InitDtsRdsInstanceRequest,
    ) -> main_models.InitDtsRdsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.init_dts_rds_instance_with_options_async(request, runtime)

    def list_dedicated_cluster_with_options(
        self,
        request: main_models.ListDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dedicated_cluster_with_options_async(
        self,
        request: main_models.ListDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDedicatedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dedicated_cluster(
        self,
        request: main_models.ListDedicatedClusterRequest,
    ) -> main_models.ListDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return self.list_dedicated_cluster_with_options(request, runtime)

    async def list_dedicated_cluster_async(
        self,
        request: main_models.ListDedicatedClusterRequest,
    ) -> main_models.ListDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return await self.list_dedicated_cluster_with_options_async(request, runtime)

    def list_job_step_with_options(
        self,
        request: main_models.ListJobStepRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobStep',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_step_with_options_async(
        self,
        request: main_models.ListJobStepRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobStep',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_step(
        self,
        request: main_models.ListJobStepRequest,
    ) -> main_models.ListJobStepResponse:
        runtime = RuntimeOptions()
        return self.list_job_step_with_options(request, runtime)

    async def list_job_step_async(
        self,
        request: main_models.ListJobStepRequest,
    ) -> main_models.ListJobStepResponse:
        runtime = RuntimeOptions()
        return await self.list_job_step_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-01-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-01-01',
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

    def modify_consumer_channel_with_options(
        self,
        request: main_models.ModifyConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumer_channel_with_options_async(
        self,
        request: main_models.ModifyConsumerChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumerChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumerChannel',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumer_channel(
        self,
        request: main_models.ModifyConsumerChannelRequest,
    ) -> main_models.ModifyConsumerChannelResponse:
        runtime = RuntimeOptions()
        return self.modify_consumer_channel_with_options(request, runtime)

    async def modify_consumer_channel_async(
        self,
        request: main_models.ModifyConsumerChannelRequest,
    ) -> main_models.ModifyConsumerChannelResponse:
        runtime = RuntimeOptions()
        return await self.modify_consumer_channel_with_options_async(request, runtime)

    def modify_consumer_group_password_with_options(
        self,
        request: main_models.ModifyConsumerGroupPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumerGroupPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumerGroupPassword',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumerGroupPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumer_group_password_with_options_async(
        self,
        request: main_models.ModifyConsumerGroupPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumerGroupPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not DaraCore.is_null(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not DaraCore.is_null(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumerGroupPassword',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumerGroupPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumer_group_password(
        self,
        request: main_models.ModifyConsumerGroupPasswordRequest,
    ) -> main_models.ModifyConsumerGroupPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_consumer_group_password_with_options(request, runtime)

    async def modify_consumer_group_password_async(
        self,
        request: main_models.ModifyConsumerGroupPasswordRequest,
    ) -> main_models.ModifyConsumerGroupPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_consumer_group_password_with_options_async(request, runtime)

    def modify_consumption_timestamp_with_options(
        self,
        request: main_models.ModifyConsumptionTimestampRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumptionTimestampResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumptionTimestamp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumptionTimestampResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumption_timestamp_with_options_async(
        self,
        request: main_models.ModifyConsumptionTimestampRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyConsumptionTimestampResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyConsumptionTimestamp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyConsumptionTimestampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumption_timestamp(
        self,
        request: main_models.ModifyConsumptionTimestampRequest,
    ) -> main_models.ModifyConsumptionTimestampResponse:
        runtime = RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    async def modify_consumption_timestamp_async(
        self,
        request: main_models.ModifyConsumptionTimestampRequest,
    ) -> main_models.ModifyConsumptionTimestampResponse:
        runtime = RuntimeOptions()
        return await self.modify_consumption_timestamp_with_options_async(request, runtime)

    def modify_dedicated_cluster_with_options(
        self,
        request: main_models.ModifyDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversold_ratio):
            query['OversoldRatio'] = request.oversold_ratio
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
            action = 'ModifyDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_cluster_with_options_async(
        self,
        request: main_models.ModifyDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversold_ratio):
            query['OversoldRatio'] = request.oversold_ratio
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
            action = 'ModifyDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDedicatedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_cluster(
        self,
        request: main_models.ModifyDedicatedClusterRequest,
    ) -> main_models.ModifyDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_dedicated_cluster_with_options(request, runtime)

    async def modify_dedicated_cluster_async(
        self,
        request: main_models.ModifyDedicatedClusterRequest,
    ) -> main_models.ModifyDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_dedicated_cluster_with_options_async(request, runtime)

    def modify_dts_job_with_options(
        self,
        tmp_req: main_models.ModifyDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobResponse:
        tmp_req.validate()
        request = main_models.ModifyDtsJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.db_list):
            request.db_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        body = {}
        if not DaraCore.is_null(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not DaraCore.is_null(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not DaraCore.is_null(request.filter_table_name):
            body['FilterTableName'] = request.filter_table_name
        if not DaraCore.is_null(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not DaraCore.is_null(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_with_options_async(
        self,
        tmp_req: main_models.ModifyDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobResponse:
        tmp_req.validate()
        request = main_models.ModifyDtsJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.db_list):
            request.db_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not DaraCore.is_null(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        body = {}
        if not DaraCore.is_null(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not DaraCore.is_null(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not DaraCore.is_null(request.filter_table_name):
            body['FilterTableName'] = request.filter_table_name
        if not DaraCore.is_null(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not DaraCore.is_null(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job(
        self,
        request: main_models.ModifyDtsJobRequest,
    ) -> main_models.ModifyDtsJobResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_with_options(request, runtime)

    async def modify_dts_job_async(
        self,
        request: main_models.ModifyDtsJobRequest,
    ) -> main_models.ModifyDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_with_options_async(request, runtime)

    def modify_dts_job_advance(
        self,
        request: main_models.ModifyDtsJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobResponse:
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
            'Product': 'Dts',
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
        modify_dts_job_req = main_models.ModifyDtsJobRequest()
        Utils.convert(request, modify_dts_job_req)
        if not DaraCore.is_null(request.file_oss_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_oss_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            modify_dts_job_req.file_oss_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        modify_dts_job_resp = self.modify_dts_job_with_options(modify_dts_job_req, runtime)
        return modify_dts_job_resp

    async def modify_dts_job_advance_async(
        self,
        request: main_models.ModifyDtsJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobResponse:
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
            'Product': 'Dts',
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
        modify_dts_job_req = main_models.ModifyDtsJobRequest()
        Utils.convert(request, modify_dts_job_req)
        if not DaraCore.is_null(request.file_oss_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_oss_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            modify_dts_job_req.file_oss_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        modify_dts_job_resp = await self.modify_dts_job_with_options_async(modify_dts_job_req, runtime)
        return modify_dts_job_resp

    def modify_dts_job_config_with_options(
        self,
        request: main_models.ModifyDtsJobConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_config_with_options_async(
        self,
        request: main_models.ModifyDtsJobConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_config(
        self,
        request: main_models.ModifyDtsJobConfigRequest,
    ) -> main_models.ModifyDtsJobConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_config_with_options(request, runtime)

    async def modify_dts_job_config_async(
        self,
        request: main_models.ModifyDtsJobConfigRequest,
    ) -> main_models.ModifyDtsJobConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_config_with_options_async(request, runtime)

    def modify_dts_job_dedicated_cluster_with_options(
        self,
        request: main_models.ModifyDtsJobDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
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
            action = 'ModifyDtsJobDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_dedicated_cluster_with_options_async(
        self,
        request: main_models.ModifyDtsJobDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
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
            action = 'ModifyDtsJobDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobDedicatedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_dedicated_cluster(
        self,
        request: main_models.ModifyDtsJobDedicatedClusterRequest,
    ) -> main_models.ModifyDtsJobDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_dedicated_cluster_with_options(request, runtime)

    async def modify_dts_job_dedicated_cluster_async(
        self,
        request: main_models.ModifyDtsJobDedicatedClusterRequest,
    ) -> main_models.ModifyDtsJobDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_dedicated_cluster_with_options_async(request, runtime)

    def modify_dts_job_du_limit_with_options(
        self,
        request: main_models.ModifyDtsJobDuLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobDuLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.du_limit):
            query['DuLimit'] = request.du_limit
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
            action = 'ModifyDtsJobDuLimit',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobDuLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_du_limit_with_options_async(
        self,
        request: main_models.ModifyDtsJobDuLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobDuLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.du_limit):
            query['DuLimit'] = request.du_limit
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
            action = 'ModifyDtsJobDuLimit',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobDuLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_du_limit(
        self,
        request: main_models.ModifyDtsJobDuLimitRequest,
    ) -> main_models.ModifyDtsJobDuLimitResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_du_limit_with_options(request, runtime)

    async def modify_dts_job_du_limit_async(
        self,
        request: main_models.ModifyDtsJobDuLimitRequest,
    ) -> main_models.ModifyDtsJobDuLimitResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_du_limit_with_options_async(request, runtime)

    def modify_dts_job_endpoint_with_options(
        self,
        request: main_models.ModifyDtsJobEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not DaraCore.is_null(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not DaraCore.is_null(request.endpoint_ip):
            query['EndpointIp'] = request.endpoint_ip
        if not DaraCore.is_null(request.endpoint_port):
            query['EndpointPort'] = request.endpoint_port
        if not DaraCore.is_null(request.endpoint_region_id):
            query['EndpointRegionId'] = request.endpoint_region_id
        if not DaraCore.is_null(request.modify_account):
            query['ModifyAccount'] = request.modify_account
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not DaraCore.is_null(request.shard_username):
            query['ShardUsername'] = request.shard_username
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobEndpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_endpoint_with_options_async(
        self,
        request: main_models.ModifyDtsJobEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not DaraCore.is_null(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not DaraCore.is_null(request.endpoint_ip):
            query['EndpointIp'] = request.endpoint_ip
        if not DaraCore.is_null(request.endpoint_port):
            query['EndpointPort'] = request.endpoint_port
        if not DaraCore.is_null(request.endpoint_region_id):
            query['EndpointRegionId'] = request.endpoint_region_id
        if not DaraCore.is_null(request.modify_account):
            query['ModifyAccount'] = request.modify_account
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not DaraCore.is_null(request.shard_username):
            query['ShardUsername'] = request.shard_username
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobEndpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_endpoint(
        self,
        request: main_models.ModifyDtsJobEndpointRequest,
    ) -> main_models.ModifyDtsJobEndpointResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_endpoint_with_options(request, runtime)

    async def modify_dts_job_endpoint_async(
        self,
        request: main_models.ModifyDtsJobEndpointRequest,
    ) -> main_models.ModifyDtsJobEndpointResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_endpoint_with_options_async(request, runtime)

    def modify_dts_job_name_with_options(
        self,
        request: main_models.ModifyDtsJobNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobName',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_name_with_options_async(
        self,
        request: main_models.ModifyDtsJobNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobName',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_name(
        self,
        request: main_models.ModifyDtsJobNameRequest,
    ) -> main_models.ModifyDtsJobNameResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_name_with_options(request, runtime)

    async def modify_dts_job_name_async(
        self,
        request: main_models.ModifyDtsJobNameRequest,
    ) -> main_models.ModifyDtsJobNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_name_with_options_async(request, runtime)

    def modify_dts_job_password_with_options(
        self,
        request: main_models.ModifyDtsJobPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobPassword',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_password_with_options_async(
        self,
        request: main_models.ModifyDtsJobPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDtsJobPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDtsJobPassword',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDtsJobPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_password(
        self,
        request: main_models.ModifyDtsJobPasswordRequest,
    ) -> main_models.ModifyDtsJobPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_dts_job_password_with_options(request, runtime)

    async def modify_dts_job_password_async(
        self,
        request: main_models.ModifyDtsJobPasswordRequest,
    ) -> main_models.ModifyDtsJobPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_dts_job_password_with_options_async(request, runtime)

    def modify_dynamic_config_with_options(
        self,
        request: main_models.ModifyDynamicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDynamicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_list):
            query['ConfigList'] = request.config_list
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.enable_limit):
            query['EnableLimit'] = request.enable_limit
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDynamicConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDynamicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dynamic_config_with_options_async(
        self,
        request: main_models.ModifyDynamicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDynamicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_list):
            query['ConfigList'] = request.config_list
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.enable_limit):
            query['EnableLimit'] = request.enable_limit
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDynamicConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDynamicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dynamic_config(
        self,
        request: main_models.ModifyDynamicConfigRequest,
    ) -> main_models.ModifyDynamicConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dynamic_config_with_options(request, runtime)

    async def modify_dynamic_config_async(
        self,
        request: main_models.ModifyDynamicConfigRequest,
    ) -> main_models.ModifyDynamicConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dynamic_config_with_options_async(request, runtime)

    def modify_gad_instance_name_with_options(
        self,
        request: main_models.ModifyGadInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGadInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action = 'ModifyGadInstanceName',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGadInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gad_instance_name_with_options_async(
        self,
        request: main_models.ModifyGadInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGadInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action = 'ModifyGadInstanceName',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGadInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gad_instance_name(
        self,
        request: main_models.ModifyGadInstanceNameRequest,
    ) -> main_models.ModifyGadInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.modify_gad_instance_name_with_options(request, runtime)

    async def modify_gad_instance_name_async(
        self,
        request: main_models.ModifyGadInstanceNameRequest,
    ) -> main_models.ModifyGadInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_gad_instance_name_with_options_async(request, runtime)

    def modify_job_step_checkpoint_with_options(
        self,
        request: main_models.ModifyJobStepCheckpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJobStepCheckpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_step_id):
            query['JobStepId'] = request.job_step_id
        if not DaraCore.is_null(request.new_check_point):
            query['NewCheckPoint'] = request.new_check_point
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJobStepCheckpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJobStepCheckpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_job_step_checkpoint_with_options_async(
        self,
        request: main_models.ModifyJobStepCheckpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJobStepCheckpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_step_id):
            query['JobStepId'] = request.job_step_id
        if not DaraCore.is_null(request.new_check_point):
            query['NewCheckPoint'] = request.new_check_point
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJobStepCheckpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJobStepCheckpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_job_step_checkpoint(
        self,
        request: main_models.ModifyJobStepCheckpointRequest,
    ) -> main_models.ModifyJobStepCheckpointResponse:
        runtime = RuntimeOptions()
        return self.modify_job_step_checkpoint_with_options(request, runtime)

    async def modify_job_step_checkpoint_async(
        self,
        request: main_models.ModifyJobStepCheckpointRequest,
    ) -> main_models.ModifyJobStepCheckpointResponse:
        runtime = RuntimeOptions()
        return await self.modify_job_step_checkpoint_with_options_async(request, runtime)

    def modify_subscription_with_options(
        self,
        request: main_models.ModifySubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_list):
            query['DbList'] = request.db_list
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not DaraCore.is_null(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySubscription',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_with_options_async(
        self,
        request: main_models.ModifySubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_list):
            query['DbList'] = request.db_list
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not DaraCore.is_null(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySubscription',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription(
        self,
        request: main_models.ModifySubscriptionRequest,
    ) -> main_models.ModifySubscriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_subscription_with_options(request, runtime)

    async def modify_subscription_async(
        self,
        request: main_models.ModifySubscriptionRequest,
    ) -> main_models.ModifySubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_subscription_with_options_async(request, runtime)

    def modify_subscription_object_with_options(
        self,
        request: main_models.ModifySubscriptionObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySubscriptionObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySubscriptionObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySubscriptionObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_object_with_options_async(
        self,
        request: main_models.ModifySubscriptionObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySubscriptionObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not DaraCore.is_null(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySubscriptionObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySubscriptionObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription_object(
        self,
        request: main_models.ModifySubscriptionObjectRequest,
    ) -> main_models.ModifySubscriptionObjectResponse:
        runtime = RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    async def modify_subscription_object_async(
        self,
        request: main_models.ModifySubscriptionObjectRequest,
    ) -> main_models.ModifySubscriptionObjectResponse:
        runtime = RuntimeOptions()
        return await self.modify_subscription_object_with_options_async(request, runtime)

    def modify_synchronization_object_with_options(
        self,
        request: main_models.ModifySynchronizationObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySynchronizationObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not DaraCore.is_null(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySynchronizationObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySynchronizationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_synchronization_object_with_options_async(
        self,
        request: main_models.ModifySynchronizationObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySynchronizationObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not DaraCore.is_null(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySynchronizationObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySynchronizationObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_synchronization_object(
        self,
        request: main_models.ModifySynchronizationObjectRequest,
    ) -> main_models.ModifySynchronizationObjectResponse:
        runtime = RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    async def modify_synchronization_object_async(
        self,
        request: main_models.ModifySynchronizationObjectRequest,
    ) -> main_models.ModifySynchronizationObjectResponse:
        runtime = RuntimeOptions()
        return await self.modify_synchronization_object_with_options_async(request, runtime)

    def pre_check_create_gad_order_with_options(
        self,
        request: main_models.PreCheckCreateGadOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreCheckCreateGadOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_database_name):
            query['MasterDatabaseName'] = request.master_database_name
        if not DaraCore.is_null(request.master_engine_arch_type):
            query['MasterEngineArchType'] = request.master_engine_arch_type
        if not DaraCore.is_null(request.master_shard_account_name):
            query['MasterShardAccountName'] = request.master_shard_account_name
        if not DaraCore.is_null(request.master_shard_account_password):
            query['MasterShardAccountPassword'] = request.master_shard_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_database_name):
            query['SlaveDatabaseName'] = request.slave_database_name
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        if not DaraCore.is_null(request.slave_db_instance_region):
            query['SlaveDbInstanceRegion'] = request.slave_db_instance_region
        if not DaraCore.is_null(request.slave_engine_arch_type):
            query['SlaveEngineArchType'] = request.slave_engine_arch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreCheckCreateGadOrder',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreCheckCreateGadOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def pre_check_create_gad_order_with_options_async(
        self,
        request: main_models.PreCheckCreateGadOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreCheckCreateGadOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_database_name):
            query['MasterDatabaseName'] = request.master_database_name
        if not DaraCore.is_null(request.master_engine_arch_type):
            query['MasterEngineArchType'] = request.master_engine_arch_type
        if not DaraCore.is_null(request.master_shard_account_name):
            query['MasterShardAccountName'] = request.master_shard_account_name
        if not DaraCore.is_null(request.master_shard_account_password):
            query['MasterShardAccountPassword'] = request.master_shard_account_password
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_database_name):
            query['SlaveDatabaseName'] = request.slave_database_name
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        if not DaraCore.is_null(request.slave_db_instance_region):
            query['SlaveDbInstanceRegion'] = request.slave_db_instance_region
        if not DaraCore.is_null(request.slave_engine_arch_type):
            query['SlaveEngineArchType'] = request.slave_engine_arch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreCheckCreateGadOrder',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreCheckCreateGadOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pre_check_create_gad_order(
        self,
        request: main_models.PreCheckCreateGadOrderRequest,
    ) -> main_models.PreCheckCreateGadOrderResponse:
        runtime = RuntimeOptions()
        return self.pre_check_create_gad_order_with_options(request, runtime)

    async def pre_check_create_gad_order_async(
        self,
        request: main_models.PreCheckCreateGadOrderRequest,
    ) -> main_models.PreCheckCreateGadOrderResponse:
        runtime = RuntimeOptions()
        return await self.pre_check_create_gad_order_with_options_async(request, runtime)

    def promote_to_master_with_options(
        self,
        request: main_models.PromoteToMasterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromoteToMasterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PromoteToMaster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromoteToMasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def promote_to_master_with_options_async(
        self,
        request: main_models.PromoteToMasterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromoteToMasterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PromoteToMaster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromoteToMasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def promote_to_master(
        self,
        request: main_models.PromoteToMasterRequest,
    ) -> main_models.PromoteToMasterResponse:
        runtime = RuntimeOptions()
        return self.promote_to_master_with_options(request, runtime)

    async def promote_to_master_async(
        self,
        request: main_models.PromoteToMasterRequest,
    ) -> main_models.PromoteToMasterResponse:
        runtime = RuntimeOptions()
        return await self.promote_to_master_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_dts_job_with_options(
        self,
        request: main_models.ResetDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_dts_job_with_options_async(
        self,
        request: main_models.ResetDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_dts_job(
        self,
        request: main_models.ResetDtsJobRequest,
    ) -> main_models.ResetDtsJobResponse:
        runtime = RuntimeOptions()
        return self.reset_dts_job_with_options(request, runtime)

    async def reset_dts_job_async(
        self,
        request: main_models.ResetDtsJobRequest,
    ) -> main_models.ResetDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.reset_dts_job_with_options_async(request, runtime)

    def reset_synchronization_job_with_options(
        self,
        request: main_models.ResetSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_synchronization_job_with_options_async(
        self,
        request: main_models.ResetSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_synchronization_job(
        self,
        request: main_models.ResetSynchronizationJobRequest,
    ) -> main_models.ResetSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    async def reset_synchronization_job_async(
        self,
        request: main_models.ResetSynchronizationJobRequest,
    ) -> main_models.ResetSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.reset_synchronization_job_with_options_async(request, runtime)

    def reverse_two_way_direction_with_options(
        self,
        request: main_models.ReverseTwoWayDirectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReverseTwoWayDirectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.ignore_error_sub_job):
            query['IgnoreErrorSubJob'] = request.ignore_error_sub_job
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReverseTwoWayDirection',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReverseTwoWayDirectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reverse_two_way_direction_with_options_async(
        self,
        request: main_models.ReverseTwoWayDirectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReverseTwoWayDirectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.ignore_error_sub_job):
            query['IgnoreErrorSubJob'] = request.ignore_error_sub_job
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReverseTwoWayDirection',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReverseTwoWayDirectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reverse_two_way_direction(
        self,
        request: main_models.ReverseTwoWayDirectionRequest,
    ) -> main_models.ReverseTwoWayDirectionResponse:
        runtime = RuntimeOptions()
        return self.reverse_two_way_direction_with_options(request, runtime)

    async def reverse_two_way_direction_async(
        self,
        request: main_models.ReverseTwoWayDirectionRequest,
    ) -> main_models.ReverseTwoWayDirectionResponse:
        runtime = RuntimeOptions()
        return await self.reverse_two_way_direction_with_options_async(request, runtime)

    def shield_precheck_with_options(
        self,
        request: main_models.ShieldPrecheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ShieldPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ShieldPrecheck',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShieldPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def shield_precheck_with_options_async(
        self,
        request: main_models.ShieldPrecheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ShieldPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ShieldPrecheck',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShieldPrecheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def shield_precheck(
        self,
        request: main_models.ShieldPrecheckRequest,
    ) -> main_models.ShieldPrecheckResponse:
        runtime = RuntimeOptions()
        return self.shield_precheck_with_options(request, runtime)

    async def shield_precheck_async(
        self,
        request: main_models.ShieldPrecheckRequest,
    ) -> main_models.ShieldPrecheckResponse:
        runtime = RuntimeOptions()
        return await self.shield_precheck_with_options_async(request, runtime)

    def skip_full_job_table_with_options(
        self,
        request: main_models.SkipFullJobTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipFullJobTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_progress_id):
            query['JobProgressId'] = request.job_progress_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipFullJobTable',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipFullJobTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_full_job_table_with_options_async(
        self,
        request: main_models.SkipFullJobTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipFullJobTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_progress_id):
            query['JobProgressId'] = request.job_progress_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipFullJobTable',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipFullJobTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_full_job_table(
        self,
        request: main_models.SkipFullJobTableRequest,
    ) -> main_models.SkipFullJobTableResponse:
        runtime = RuntimeOptions()
        return self.skip_full_job_table_with_options(request, runtime)

    async def skip_full_job_table_async(
        self,
        request: main_models.SkipFullJobTableRequest,
    ) -> main_models.SkipFullJobTableResponse:
        runtime = RuntimeOptions()
        return await self.skip_full_job_table_with_options_async(request, runtime)

    def skip_pre_check_with_options(
        self,
        request: main_models.SkipPreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not DaraCore.is_null(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipPreCheck',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_pre_check_with_options_async(
        self,
        request: main_models.SkipPreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not DaraCore.is_null(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipPreCheck',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_pre_check(
        self,
        request: main_models.SkipPreCheckRequest,
    ) -> main_models.SkipPreCheckResponse:
        runtime = RuntimeOptions()
        return self.skip_pre_check_with_options(request, runtime)

    async def skip_pre_check_async(
        self,
        request: main_models.SkipPreCheckRequest,
    ) -> main_models.SkipPreCheckResponse:
        runtime = RuntimeOptions()
        return await self.skip_pre_check_with_options_async(request, runtime)

    def start_dts_job_with_options(
        self,
        request: main_models.StartDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dts_job_with_options_async(
        self,
        request: main_models.StartDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dts_job(
        self,
        request: main_models.StartDtsJobRequest,
    ) -> main_models.StartDtsJobResponse:
        runtime = RuntimeOptions()
        return self.start_dts_job_with_options(request, runtime)

    async def start_dts_job_async(
        self,
        request: main_models.StartDtsJobRequest,
    ) -> main_models.StartDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.start_dts_job_with_options_async(request, runtime)

    def start_dts_jobs_with_options(
        self,
        request: main_models.StartDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dts_jobs_with_options_async(
        self,
        request: main_models.StartDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dts_jobs(
        self,
        request: main_models.StartDtsJobsRequest,
    ) -> main_models.StartDtsJobsResponse:
        runtime = RuntimeOptions()
        return self.start_dts_jobs_with_options(request, runtime)

    async def start_dts_jobs_async(
        self,
        request: main_models.StartDtsJobsRequest,
    ) -> main_models.StartDtsJobsResponse:
        runtime = RuntimeOptions()
        return await self.start_dts_jobs_with_options_async(request, runtime)

    def start_migration_job_with_options(
        self,
        request: main_models.StartMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'StartMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_migration_job_with_options_async(
        self,
        request: main_models.StartMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'StartMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_migration_job(
        self,
        request: main_models.StartMigrationJobRequest,
    ) -> main_models.StartMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    async def start_migration_job_async(
        self,
        request: main_models.StartMigrationJobRequest,
    ) -> main_models.StartMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.start_migration_job_with_options_async(request, runtime)

    def start_reverse_writer_with_options(
        self,
        request: main_models.StartReverseWriterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartReverseWriterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_point):
            query['CheckPoint'] = request.check_point
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartReverseWriter',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartReverseWriterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_reverse_writer_with_options_async(
        self,
        request: main_models.StartReverseWriterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartReverseWriterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_point):
            query['CheckPoint'] = request.check_point
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartReverseWriter',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartReverseWriterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_reverse_writer(
        self,
        request: main_models.StartReverseWriterRequest,
    ) -> main_models.StartReverseWriterResponse:
        runtime = RuntimeOptions()
        return self.start_reverse_writer_with_options(request, runtime)

    async def start_reverse_writer_async(
        self,
        request: main_models.StartReverseWriterRequest,
    ) -> main_models.StartReverseWriterResponse:
        runtime = RuntimeOptions()
        return await self.start_reverse_writer_with_options_async(request, runtime)

    def start_subscription_instance_with_options(
        self,
        request: main_models.StartSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_subscription_instance_with_options_async(
        self,
        request: main_models.StartSubscriptionInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSubscriptionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSubscriptionInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_subscription_instance(
        self,
        request: main_models.StartSubscriptionInstanceRequest,
    ) -> main_models.StartSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    async def start_subscription_instance_async(
        self,
        request: main_models.StartSubscriptionInstanceRequest,
    ) -> main_models.StartSubscriptionInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_subscription_instance_with_options_async(request, runtime)

    def start_synchronization_job_with_options(
        self,
        request: main_models.StartSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_synchronization_job_with_options_async(
        self,
        request: main_models.StartSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_synchronization_job(
        self,
        request: main_models.StartSynchronizationJobRequest,
    ) -> main_models.StartSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    async def start_synchronization_job_async(
        self,
        request: main_models.StartSynchronizationJobRequest,
    ) -> main_models.StartSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.start_synchronization_job_with_options_async(request, runtime)

    def stop_dedicated_cluster_with_options(
        self,
        request: main_models.StopDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'StopDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dedicated_cluster_with_options_async(
        self,
        request: main_models.StopDedicatedClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDedicatedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'StopDedicatedCluster',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDedicatedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dedicated_cluster(
        self,
        request: main_models.StopDedicatedClusterRequest,
    ) -> main_models.StopDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return self.stop_dedicated_cluster_with_options(request, runtime)

    async def stop_dedicated_cluster_async(
        self,
        request: main_models.StopDedicatedClusterRequest,
    ) -> main_models.StopDedicatedClusterResponse:
        runtime = RuntimeOptions()
        return await self.stop_dedicated_cluster_with_options_async(request, runtime)

    def stop_dts_job_with_options(
        self,
        request: main_models.StopDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dts_job_with_options_async(
        self,
        request: main_models.StopDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dts_job(
        self,
        request: main_models.StopDtsJobRequest,
    ) -> main_models.StopDtsJobResponse:
        runtime = RuntimeOptions()
        return self.stop_dts_job_with_options(request, runtime)

    async def stop_dts_job_async(
        self,
        request: main_models.StopDtsJobRequest,
    ) -> main_models.StopDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.stop_dts_job_with_options_async(request, runtime)

    def stop_dts_jobs_with_options(
        self,
        request: main_models.StopDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dts_jobs_with_options_async(
        self,
        request: main_models.StopDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dts_jobs(
        self,
        request: main_models.StopDtsJobsRequest,
    ) -> main_models.StopDtsJobsResponse:
        runtime = RuntimeOptions()
        return self.stop_dts_jobs_with_options(request, runtime)

    async def stop_dts_jobs_async(
        self,
        request: main_models.StopDtsJobsRequest,
    ) -> main_models.StopDtsJobsResponse:
        runtime = RuntimeOptions()
        return await self.stop_dts_jobs_with_options_async(request, runtime)

    def stop_migration_job_with_options(
        self,
        request: main_models.StopMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'StopMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_migration_job_with_options_async(
        self,
        request: main_models.StopMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'StopMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_migration_job(
        self,
        request: main_models.StopMigrationJobRequest,
    ) -> main_models.StopMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    async def stop_migration_job_async(
        self,
        request: main_models.StopMigrationJobRequest,
    ) -> main_models.StopMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.stop_migration_job_with_options_async(request, runtime)

    def summary_job_detail_with_options(
        self,
        request: main_models.SummaryJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SummaryJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.struct_type):
            query['StructType'] = request.struct_type
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SummaryJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SummaryJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def summary_job_detail_with_options_async(
        self,
        request: main_models.SummaryJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SummaryJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.job_code):
            query['JobCode'] = request.job_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.struct_type):
            query['StructType'] = request.struct_type
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SummaryJobDetail',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SummaryJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def summary_job_detail(
        self,
        request: main_models.SummaryJobDetailRequest,
    ) -> main_models.SummaryJobDetailResponse:
        runtime = RuntimeOptions()
        return self.summary_job_detail_with_options(request, runtime)

    async def summary_job_detail_async(
        self,
        request: main_models.SummaryJobDetailRequest,
    ) -> main_models.SummaryJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.summary_job_detail_with_options_async(request, runtime)

    def suspend_dts_job_with_options(
        self,
        request: main_models.SuspendDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_dts_job_with_options_async(
        self,
        request: main_models.SuspendDtsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendDtsJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendDtsJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_dts_job(
        self,
        request: main_models.SuspendDtsJobRequest,
    ) -> main_models.SuspendDtsJobResponse:
        runtime = RuntimeOptions()
        return self.suspend_dts_job_with_options(request, runtime)

    async def suspend_dts_job_async(
        self,
        request: main_models.SuspendDtsJobRequest,
    ) -> main_models.SuspendDtsJobResponse:
        runtime = RuntimeOptions()
        return await self.suspend_dts_job_with_options_async(request, runtime)

    def suspend_dts_jobs_with_options(
        self,
        request: main_models.SuspendDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_dts_jobs_with_options_async(
        self,
        request: main_models.SuspendDtsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendDtsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendDtsJobs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_dts_jobs(
        self,
        request: main_models.SuspendDtsJobsRequest,
    ) -> main_models.SuspendDtsJobsResponse:
        runtime = RuntimeOptions()
        return self.suspend_dts_jobs_with_options(request, runtime)

    async def suspend_dts_jobs_async(
        self,
        request: main_models.SuspendDtsJobsRequest,
    ) -> main_models.SuspendDtsJobsResponse:
        runtime = RuntimeOptions()
        return await self.suspend_dts_jobs_with_options_async(request, runtime)

    def suspend_migration_job_with_options(
        self,
        request: main_models.SuspendMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'SuspendMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_migration_job_with_options_async(
        self,
        request: main_models.SuspendMigrationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendMigrationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
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
            action = 'SuspendMigrationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_migration_job(
        self,
        request: main_models.SuspendMigrationJobRequest,
    ) -> main_models.SuspendMigrationJobResponse:
        runtime = RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    async def suspend_migration_job_async(
        self,
        request: main_models.SuspendMigrationJobRequest,
    ) -> main_models.SuspendMigrationJobResponse:
        runtime = RuntimeOptions()
        return await self.suspend_migration_job_with_options_async(request, runtime)

    def suspend_synchronization_job_with_options(
        self,
        request: main_models.SuspendSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_synchronization_job_with_options_async(
        self,
        request: main_models.SuspendSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendSynchronizationJob',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_synchronization_job(
        self,
        request: main_models.SuspendSynchronizationJobRequest,
    ) -> main_models.SuspendSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    async def suspend_synchronization_job_async(
        self,
        request: main_models.SuspendSynchronizationJobRequest,
    ) -> main_models.SuspendSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.suspend_synchronization_job_with_options_async(request, runtime)

    def switch_physical_dts_job_to_cloud_with_options(
        self,
        request: main_models.SwitchPhysicalDtsJobToCloudRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchPhysicalDtsJobToCloudResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchPhysicalDtsJobToCloud',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchPhysicalDtsJobToCloudResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_physical_dts_job_to_cloud_with_options_async(
        self,
        request: main_models.SwitchPhysicalDtsJobToCloudRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchPhysicalDtsJobToCloudResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchPhysicalDtsJobToCloud',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchPhysicalDtsJobToCloudResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_physical_dts_job_to_cloud(
        self,
        request: main_models.SwitchPhysicalDtsJobToCloudRequest,
    ) -> main_models.SwitchPhysicalDtsJobToCloudResponse:
        runtime = RuntimeOptions()
        return self.switch_physical_dts_job_to_cloud_with_options(request, runtime)

    async def switch_physical_dts_job_to_cloud_async(
        self,
        request: main_models.SwitchPhysicalDtsJobToCloudRequest,
    ) -> main_models.SwitchPhysicalDtsJobToCloudResponse:
        runtime = RuntimeOptions()
        return await self.switch_physical_dts_job_to_cloud_with_options_async(request, runtime)

    def switch_synchronization_endpoint_with_options(
        self,
        request: main_models.SwitchSynchronizationEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSynchronizationEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSynchronizationEndpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSynchronizationEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_synchronization_endpoint_with_options_async(
        self,
        request: main_models.SwitchSynchronizationEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSynchronizationEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSynchronizationEndpoint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSynchronizationEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_synchronization_endpoint(
        self,
        request: main_models.SwitchSynchronizationEndpointRequest,
    ) -> main_models.SwitchSynchronizationEndpointResponse:
        runtime = RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)

    async def switch_synchronization_endpoint_async(
        self,
        request: main_models.SwitchSynchronizationEndpointRequest,
    ) -> main_models.SwitchSynchronizationEndpointResponse:
        runtime = RuntimeOptions()
        return await self.switch_synchronization_endpoint_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-01-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-01-01',
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

    def transfer_instance_class_with_options(
        self,
        request: main_models.TransferInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInstanceClass',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_instance_class_with_options_async(
        self,
        request: main_models.TransferInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInstanceClass',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_instance_class(
        self,
        request: main_models.TransferInstanceClassRequest,
    ) -> main_models.TransferInstanceClassResponse:
        runtime = RuntimeOptions()
        return self.transfer_instance_class_with_options(request, runtime)

    async def transfer_instance_class_async(
        self,
        request: main_models.TransferInstanceClassRequest,
    ) -> main_models.TransferInstanceClassResponse:
        runtime = RuntimeOptions()
        return await self.transfer_instance_class_with_options_async(request, runtime)

    def transfer_pay_type_with_options(
        self,
        request: main_models.TransferPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferPayType',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_pay_type_with_options_async(
        self,
        request: main_models.TransferPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.max_du):
            query['MaxDu'] = request.max_du
        if not DaraCore.is_null(request.min_du):
            query['MinDu'] = request.min_du
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferPayType',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_pay_type(
        self,
        request: main_models.TransferPayTypeRequest,
    ) -> main_models.TransferPayTypeResponse:
        runtime = RuntimeOptions()
        return self.transfer_pay_type_with_options(request, runtime)

    async def transfer_pay_type_async(
        self,
        request: main_models.TransferPayTypeRequest,
    ) -> main_models.TransferPayTypeResponse:
        runtime = RuntimeOptions()
        return await self.transfer_pay_type_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-01-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-01-01',
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

    def upgrade_two_way_with_options(
        self,
        request: main_models.UpgradeTwoWayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeTwoWayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeTwoWay',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeTwoWayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_two_way_with_options_async(
        self,
        request: main_models.UpgradeTwoWayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeTwoWayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeTwoWay',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeTwoWayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_two_way(
        self,
        request: main_models.UpgradeTwoWayRequest,
    ) -> main_models.UpgradeTwoWayResponse:
        runtime = RuntimeOptions()
        return self.upgrade_two_way_with_options(request, runtime)

    async def upgrade_two_way_async(
        self,
        request: main_models.UpgradeTwoWayRequest,
    ) -> main_models.UpgradeTwoWayResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_two_way_with_options_async(request, runtime)

    def white_ip_list_with_options(
        self,
        request: main_models.WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_aliyun_uid):
            query['DestAliyunUid'] = request.dest_aliyun_uid
        if not DaraCore.is_null(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not DaraCore.is_null(request.dest_role_name):
            query['DestRoleName'] = request.dest_role_name
        if not DaraCore.is_null(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not DaraCore.is_null(request.dest_vpc_id):
            query['DestVpcId'] = request.dest_vpc_id
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_aliyun_uid):
            query['SrcAliyunUid'] = request.src_aliyun_uid
        if not DaraCore.is_null(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not DaraCore.is_null(request.src_role_name):
            query['SrcRoleName'] = request.src_role_name
        if not DaraCore.is_null(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WhiteIpList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WhiteIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def white_ip_list_with_options_async(
        self,
        request: main_models.WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_aliyun_uid):
            query['DestAliyunUid'] = request.dest_aliyun_uid
        if not DaraCore.is_null(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not DaraCore.is_null(request.dest_role_name):
            query['DestRoleName'] = request.dest_role_name
        if not DaraCore.is_null(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not DaraCore.is_null(request.dest_vpc_id):
            query['DestVpcId'] = request.dest_vpc_id
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.src_aliyun_uid):
            query['SrcAliyunUid'] = request.src_aliyun_uid
        if not DaraCore.is_null(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not DaraCore.is_null(request.src_role_name):
            query['SrcRoleName'] = request.src_role_name
        if not DaraCore.is_null(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WhiteIpList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WhiteIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def white_ip_list(
        self,
        request: main_models.WhiteIpListRequest,
    ) -> main_models.WhiteIpListResponse:
        runtime = RuntimeOptions()
        return self.white_ip_list_with_options(request, runtime)

    async def white_ip_list_async(
        self,
        request: main_models.WhiteIpListRequest,
    ) -> main_models.WhiteIpListResponse:
        runtime = RuntimeOptions()
        return await self.white_ip_list_with_options_async(request, runtime)
