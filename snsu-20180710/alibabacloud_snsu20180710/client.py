# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_snsu20180710 import models as snsu_20180710_models
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
        self._endpoint = self.get_endpoint('snsu', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cidr_in_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.AddCidrInVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddCidrInVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCidrInVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddCidrInVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cidr_in_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.AddCidrInVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddCidrInVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCidrInVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddCidrInVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cidr_in_vtune_instance(
        self,
        request: snsu_20180710_models.AddCidrInVtuneInstanceRequest,
    ) -> snsu_20180710_models.AddCidrInVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cidr_in_vtune_instance_with_options(request, runtime)

    async def add_cidr_in_vtune_instance_async(
        self,
        request: snsu_20180710_models.AddCidrInVtuneInstanceRequest,
    ) -> snsu_20180710_models.AddCidrInVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cidr_in_vtune_instance_with_options_async(request, runtime)

    def add_epninstance_with_options(
        self,
        request: snsu_20180710_models.AddEPNInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEPNInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accelerate):
            body['Accelerate'] = request.accelerate
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.dscp):
            body['Dscp'] = request.dscp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.epn_name):
            body['EpnName'] = request.epn_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security):
            body['Security'] = request.security
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEPNInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEPNInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_epninstance_with_options_async(
        self,
        request: snsu_20180710_models.AddEPNInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEPNInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accelerate):
            body['Accelerate'] = request.accelerate
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.dscp):
            body['Dscp'] = request.dscp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.epn_name):
            body['EpnName'] = request.epn_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security):
            body['Security'] = request.security
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEPNInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEPNInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_epninstance(
        self,
        request: snsu_20180710_models.AddEPNInstanceRequest,
    ) -> snsu_20180710_models.AddEPNInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_epninstance_with_options(request, runtime)

    async def add_epninstance_async(
        self,
        request: snsu_20180710_models.AddEPNInstanceRequest,
    ) -> snsu_20180710_models.AddEPNInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_epninstance_with_options_async(request, runtime)

    def add_evgw_in_epn_with_options(
        self,
        request: snsu_20180710_models.AddEvgwInEpnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEvgwInEpnResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.evgw_region):
            body['EvgwRegion'] = request.evgw_region
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEvgwInEpn',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEvgwInEpnResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_evgw_in_epn_with_options_async(
        self,
        request: snsu_20180710_models.AddEvgwInEpnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEvgwInEpnResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.evgw_region):
            body['EvgwRegion'] = request.evgw_region
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEvgwInEpn',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEvgwInEpnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_evgw_in_epn(
        self,
        request: snsu_20180710_models.AddEvgwInEpnRequest,
    ) -> snsu_20180710_models.AddEvgwInEpnResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_evgw_in_epn_with_options(request, runtime)

    async def add_evgw_in_epn_async(
        self,
        request: snsu_20180710_models.AddEvgwInEpnRequest,
    ) -> snsu_20180710_models.AddEvgwInEpnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_evgw_in_epn_with_options_async(request, runtime)

    def add_evgw_instance_with_options(
        self,
        request: snsu_20180710_models.AddEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_name):
            body['EvgwName'] = request.evgw_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.ipsec_psk):
            body['IpsecPsk'] = request.ipsec_psk
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEvgwInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_evgw_instance_with_options_async(
        self,
        request: snsu_20180710_models.AddEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_name):
            body['EvgwName'] = request.evgw_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.ipsec_psk):
            body['IpsecPsk'] = request.ipsec_psk
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddEvgwInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_evgw_instance(
        self,
        request: snsu_20180710_models.AddEvgwInstanceRequest,
    ) -> snsu_20180710_models.AddEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_evgw_instance_with_options(request, runtime)

    async def add_evgw_instance_async(
        self,
        request: snsu_20180710_models.AddEvgwInstanceRequest,
    ) -> snsu_20180710_models.AddEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_evgw_instance_with_options_async(request, runtime)

    def add_vtune_in_evgw_with_options(
        self,
        request: snsu_20180710_models.AddVtuneInEvgwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddVtuneInEvgwResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddVtuneInEvgw',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddVtuneInEvgwResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vtune_in_evgw_with_options_async(
        self,
        request: snsu_20180710_models.AddVtuneInEvgwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddVtuneInEvgwResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddVtuneInEvgw',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddVtuneInEvgwResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vtune_in_evgw(
        self,
        request: snsu_20180710_models.AddVtuneInEvgwRequest,
    ) -> snsu_20180710_models.AddVtuneInEvgwResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vtune_in_evgw_with_options(request, runtime)

    async def add_vtune_in_evgw_async(
        self,
        request: snsu_20180710_models.AddVtuneInEvgwRequest,
    ) -> snsu_20180710_models.AddVtuneInEvgwResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vtune_in_evgw_with_options_async(request, runtime)

    def add_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.AddVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.cpe_id):
            body['CpeId'] = request.cpe_id
        if not UtilClient.is_unset(request.dhcp):
            body['Dhcp'] = request.dhcp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.enable_bgp):
            body['EnableBgp'] = request.enable_bgp
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.partner):
            body['Partner'] = request.partner
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.pt_uuid):
            body['PtUuid'] = request.pt_uuid
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.AddVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.AddVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.cpe_id):
            body['CpeId'] = request.cpe_id
        if not UtilClient.is_unset(request.dhcp):
            body['Dhcp'] = request.dhcp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.enable_bgp):
            body['EnableBgp'] = request.enable_bgp
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.partner):
            body['Partner'] = request.partner
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.pt_uuid):
            body['PtUuid'] = request.pt_uuid
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.AddVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vtune_instance(
        self,
        request: snsu_20180710_models.AddVtuneInstanceRequest,
    ) -> snsu_20180710_models.AddVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vtune_instance_with_options(request, runtime)

    async def add_vtune_instance_async(
        self,
        request: snsu_20180710_models.AddVtuneInstanceRequest,
    ) -> snsu_20180710_models.AddVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vtune_instance_with_options_async(request, runtime)

    def complete_commodity_info_with_options(
        self,
        request: snsu_20180710_models.CompleteCommodityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CompleteCommodityInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteCommodityInfo',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CompleteCommodityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_commodity_info_with_options_async(
        self,
        request: snsu_20180710_models.CompleteCommodityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CompleteCommodityInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteCommodityInfo',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CompleteCommodityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_commodity_info(
        self,
        request: snsu_20180710_models.CompleteCommodityInfoRequest,
    ) -> snsu_20180710_models.CompleteCommodityInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_commodity_info_with_options(request, runtime)

    async def complete_commodity_info_async(
        self,
        request: snsu_20180710_models.CompleteCommodityInfoRequest,
    ) -> snsu_20180710_models.CompleteCommodityInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_commodity_info_with_options_async(request, runtime)

    def create_ebiwith_options(
        self,
        request: snsu_20180710_models.CreateEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CreateEBIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.exp_info):
            body['ExpInfo'] = request.exp_info
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.gateway):
            body['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip_info):
            body['IpInfo'] = request.ip_info
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CreateEBIResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ebiwith_options_async(
        self,
        request: snsu_20180710_models.CreateEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CreateEBIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.exp_info):
            body['ExpInfo'] = request.exp_info
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.gateway):
            body['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip_info):
            body['IpInfo'] = request.ip_info
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CreateEBIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ebi(
        self,
        request: snsu_20180710_models.CreateEBIRequest,
    ) -> snsu_20180710_models.CreateEBIResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ebiwith_options(request, runtime)

    async def create_ebi_async(
        self,
        request: snsu_20180710_models.CreateEBIRequest,
    ) -> snsu_20180710_models.CreateEBIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ebiwith_options_async(request, runtime)

    def create_order_call_back_with_options(
        self,
        request: snsu_20180710_models.CreateOrderCallBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CreateOrderCallBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderCallBack',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CreateOrderCallBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_call_back_with_options_async(
        self,
        request: snsu_20180710_models.CreateOrderCallBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.CreateOrderCallBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderCallBack',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.CreateOrderCallBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_call_back(
        self,
        request: snsu_20180710_models.CreateOrderCallBackRequest,
    ) -> snsu_20180710_models.CreateOrderCallBackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_call_back_with_options(request, runtime)

    async def create_order_call_back_async(
        self,
        request: snsu_20180710_models.CreateOrderCallBackRequest,
    ) -> snsu_20180710_models.CreateOrderCallBackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_call_back_with_options_async(request, runtime)

    def delete_cidr_in_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.DeleteCidrInVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteCidrInVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCidrInVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteCidrInVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cidr_in_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.DeleteCidrInVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteCidrInVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.cidrs):
            body['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCidrInVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteCidrInVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cidr_in_vtune_instance(
        self,
        request: snsu_20180710_models.DeleteCidrInVtuneInstanceRequest,
    ) -> snsu_20180710_models.DeleteCidrInVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cidr_in_vtune_instance_with_options(request, runtime)

    async def delete_cidr_in_vtune_instance_async(
        self,
        request: snsu_20180710_models.DeleteCidrInVtuneInstanceRequest,
    ) -> snsu_20180710_models.DeleteCidrInVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cidr_in_vtune_instance_with_options_async(request, runtime)

    def delete_ebiwith_options(
        self,
        request: snsu_20180710_models.DeleteEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEBIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.ebi_id):
            body['EbiId'] = request.ebi_id
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEBIResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ebiwith_options_async(
        self,
        request: snsu_20180710_models.DeleteEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEBIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.ebi_id):
            body['EbiId'] = request.ebi_id
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEBIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ebi(
        self,
        request: snsu_20180710_models.DeleteEBIRequest,
    ) -> snsu_20180710_models.DeleteEBIResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ebiwith_options(request, runtime)

    async def delete_ebi_async(
        self,
        request: snsu_20180710_models.DeleteEBIRequest,
    ) -> snsu_20180710_models.DeleteEBIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ebiwith_options_async(request, runtime)

    def delete_epn_instance_with_options(
        self,
        request: snsu_20180710_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_epn_instance_with_options_async(
        self,
        request: snsu_20180710_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_epn_instance(
        self,
        request: snsu_20180710_models.DeleteEpnInstanceRequest,
    ) -> snsu_20180710_models.DeleteEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_epn_instance_with_options(request, runtime)

    async def delete_epn_instance_async(
        self,
        request: snsu_20180710_models.DeleteEpnInstanceRequest,
    ) -> snsu_20180710_models.DeleteEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_epn_instance_with_options_async(request, runtime)

    def delete_evgw_in_epn_with_options(
        self,
        request: snsu_20180710_models.DeleteEvgwInEpnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEvgwInEpnResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.evgw_region):
            body['EvgwRegion'] = request.evgw_region
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEvgwInEpn',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEvgwInEpnResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evgw_in_epn_with_options_async(
        self,
        request: snsu_20180710_models.DeleteEvgwInEpnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEvgwInEpnResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.evgw_region):
            body['EvgwRegion'] = request.evgw_region
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEvgwInEpn',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEvgwInEpnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evgw_in_epn(
        self,
        request: snsu_20180710_models.DeleteEvgwInEpnRequest,
    ) -> snsu_20180710_models.DeleteEvgwInEpnResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_evgw_in_epn_with_options(request, runtime)

    async def delete_evgw_in_epn_async(
        self,
        request: snsu_20180710_models.DeleteEvgwInEpnRequest,
    ) -> snsu_20180710_models.DeleteEvgwInEpnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_evgw_in_epn_with_options_async(request, runtime)

    def delete_evgw_instance_with_options(
        self,
        request: snsu_20180710_models.DeleteEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEvgwInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evgw_instance_with_options_async(
        self,
        request: snsu_20180710_models.DeleteEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteEvgwInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evgw_instance(
        self,
        request: snsu_20180710_models.DeleteEvgwInstanceRequest,
    ) -> snsu_20180710_models.DeleteEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_evgw_instance_with_options(request, runtime)

    async def delete_evgw_instance_async(
        self,
        request: snsu_20180710_models.DeleteEvgwInstanceRequest,
    ) -> snsu_20180710_models.DeleteEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_evgw_instance_with_options_async(request, runtime)

    def delete_vtune_in_evgw_with_options(
        self,
        request: snsu_20180710_models.DeleteVtuneInEvgwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteVtuneInEvgwResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVtuneInEvgw',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteVtuneInEvgwResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vtune_in_evgw_with_options_async(
        self,
        request: snsu_20180710_models.DeleteVtuneInEvgwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteVtuneInEvgwResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVtuneInEvgw',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteVtuneInEvgwResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vtune_in_evgw(
        self,
        request: snsu_20180710_models.DeleteVtuneInEvgwRequest,
    ) -> snsu_20180710_models.DeleteVtuneInEvgwResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vtune_in_evgw_with_options(request, runtime)

    async def delete_vtune_in_evgw_async(
        self,
        request: snsu_20180710_models.DeleteVtuneInEvgwRequest,
    ) -> snsu_20180710_models.DeleteVtuneInEvgwResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vtune_in_evgw_with_options_async(request, runtime)

    def delete_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.DeleteVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.DeleteVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.DeleteVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.DeleteVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vtune_instance(
        self,
        request: snsu_20180710_models.DeleteVtuneInstanceRequest,
    ) -> snsu_20180710_models.DeleteVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vtune_instance_with_options(request, runtime)

    async def delete_vtune_instance_async(
        self,
        request: snsu_20180710_models.DeleteVtuneInstanceRequest,
    ) -> snsu_20180710_models.DeleteVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vtune_instance_with_options_async(request, runtime)

    def get_evltraffic_data_with_options(
        self,
        request: snsu_20180710_models.GetEVLTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEVLTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.group_method):
            body['GroupMethod'] = request.group_method
        if not UtilClient.is_unset(request.group_type):
            body['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEVLTrafficData',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEVLTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evltraffic_data_with_options_async(
        self,
        request: snsu_20180710_models.GetEVLTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEVLTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.group_method):
            body['GroupMethod'] = request.group_method
        if not UtilClient.is_unset(request.group_type):
            body['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEVLTrafficData',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEVLTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evltraffic_data(
        self,
        request: snsu_20180710_models.GetEVLTrafficDataRequest,
    ) -> snsu_20180710_models.GetEVLTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_evltraffic_data_with_options(request, runtime)

    async def get_evltraffic_data_async(
        self,
        request: snsu_20180710_models.GetEVLTrafficDataRequest,
    ) -> snsu_20180710_models.GetEVLTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_evltraffic_data_with_options_async(request, runtime)

    def get_epn_instance_with_options(
        self,
        request: snsu_20180710_models.GetEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_epn_instance_with_options_async(
        self,
        request: snsu_20180710_models.GetEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_epn_instance(
        self,
        request: snsu_20180710_models.GetEpnInstanceRequest,
    ) -> snsu_20180710_models.GetEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_epn_instance_with_options(request, runtime)

    async def get_epn_instance_async(
        self,
        request: snsu_20180710_models.GetEpnInstanceRequest,
    ) -> snsu_20180710_models.GetEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_epn_instance_with_options_async(request, runtime)

    def get_evgw_instance_with_options(
        self,
        request: snsu_20180710_models.GetEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEvgwInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evgw_instance_with_options_async(
        self,
        request: snsu_20180710_models.GetEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEvgwInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evgw_instance(
        self,
        request: snsu_20180710_models.GetEvgwInstanceRequest,
    ) -> snsu_20180710_models.GetEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_evgw_instance_with_options(request, runtime)

    async def get_evgw_instance_async(
        self,
        request: snsu_20180710_models.GetEvgwInstanceRequest,
    ) -> snsu_20180710_models.GetEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_evgw_instance_with_options_async(request, runtime)

    def get_evgw_regions_with_options(
        self,
        request: snsu_20180710_models.GetEvgwRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEvgwRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvgwRegions',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEvgwRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evgw_regions_with_options_async(
        self,
        request: snsu_20180710_models.GetEvgwRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetEvgwRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvgwRegions',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetEvgwRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evgw_regions(
        self,
        request: snsu_20180710_models.GetEvgwRegionsRequest,
    ) -> snsu_20180710_models.GetEvgwRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_evgw_regions_with_options(request, runtime)

    async def get_evgw_regions_async(
        self,
        request: snsu_20180710_models.GetEvgwRegionsRequest,
    ) -> snsu_20180710_models.GetEvgwRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_evgw_regions_with_options_async(request, runtime)

    def get_llbztraffic_data_with_options(
        self,
        request: snsu_20180710_models.GetLLBZTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetLLBZTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.group_method):
            body['GroupMethod'] = request.group_method
        if not UtilClient.is_unset(request.group_type):
            body['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLLBZTrafficData',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetLLBZTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_llbztraffic_data_with_options_async(
        self,
        request: snsu_20180710_models.GetLLBZTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetLLBZTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.group_method):
            body['GroupMethod'] = request.group_method
        if not UtilClient.is_unset(request.group_type):
            body['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLLBZTrafficData',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetLLBZTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_llbztraffic_data(
        self,
        request: snsu_20180710_models.GetLLBZTrafficDataRequest,
    ) -> snsu_20180710_models.GetLLBZTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_llbztraffic_data_with_options(request, runtime)

    async def get_llbztraffic_data_async(
        self,
        request: snsu_20180710_models.GetLLBZTrafficDataRequest,
    ) -> snsu_20180710_models.GetLLBZTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_llbztraffic_data_with_options_async(request, runtime)

    def get_vtune_config_with_options(
        self,
        request: snsu_20180710_models.GetVtuneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetVtuneConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVtuneConfig',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetVtuneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vtune_config_with_options_async(
        self,
        request: snsu_20180710_models.GetVtuneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetVtuneConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVtuneConfig',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetVtuneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vtune_config(
        self,
        request: snsu_20180710_models.GetVtuneConfigRequest,
    ) -> snsu_20180710_models.GetVtuneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vtune_config_with_options(request, runtime)

    async def get_vtune_config_async(
        self,
        request: snsu_20180710_models.GetVtuneConfigRequest,
    ) -> snsu_20180710_models.GetVtuneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vtune_config_with_options_async(request, runtime)

    def get_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.GetVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.GetVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.GetVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.GetVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vtune_instance(
        self,
        request: snsu_20180710_models.GetVtuneInstanceRequest,
    ) -> snsu_20180710_models.GetVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vtune_instance_with_options(request, runtime)

    async def get_vtune_instance_async(
        self,
        request: snsu_20180710_models.GetVtuneInstanceRequest,
    ) -> snsu_20180710_models.GetVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vtune_instance_with_options_async(request, runtime)

    def list_ebiwith_options(
        self,
        request: snsu_20180710_models.ListEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ListEBIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ListEBIResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ebiwith_options_async(
        self,
        request: snsu_20180710_models.ListEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ListEBIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ListEBIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ebi(
        self,
        request: snsu_20180710_models.ListEBIRequest,
    ) -> snsu_20180710_models.ListEBIResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ebiwith_options(request, runtime)

    async def list_ebi_async(
        self,
        request: snsu_20180710_models.ListEBIRequest,
    ) -> snsu_20180710_models.ListEBIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ebiwith_options_async(request, runtime)

    def open_api_test_with_options(
        self,
        request: snsu_20180710_models.OpenApiTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.OpenApiTestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenApiTest',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.OpenApiTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_api_test_with_options_async(
        self,
        request: snsu_20180710_models.OpenApiTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.OpenApiTestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenApiTest',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.OpenApiTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_api_test(
        self,
        request: snsu_20180710_models.OpenApiTestRequest,
    ) -> snsu_20180710_models.OpenApiTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_api_test_with_options(request, runtime)

    async def open_api_test_async(
        self,
        request: snsu_20180710_models.OpenApiTestRequest,
    ) -> snsu_20180710_models.OpenApiTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_api_test_with_options_async(request, runtime)

    def query_accelerate_seller_shop_with_options(
        self,
        request: snsu_20180710_models.QueryAccelerateSellerShopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryAccelerateSellerShopResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccelerateSellerShop',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryAccelerateSellerShopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accelerate_seller_shop_with_options_async(
        self,
        request: snsu_20180710_models.QueryAccelerateSellerShopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryAccelerateSellerShopResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccelerateSellerShop',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryAccelerateSellerShopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accelerate_seller_shop(
        self,
        request: snsu_20180710_models.QueryAccelerateSellerShopRequest,
    ) -> snsu_20180710_models.QueryAccelerateSellerShopResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_accelerate_seller_shop_with_options(request, runtime)

    async def query_accelerate_seller_shop_async(
        self,
        request: snsu_20180710_models.QueryAccelerateSellerShopRequest,
    ) -> snsu_20180710_models.QueryAccelerateSellerShopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_accelerate_seller_shop_with_options_async(request, runtime)

    def query_accelerate_statistics_with_options(
        self,
        request: snsu_20180710_models.QueryAccelerateStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryAccelerateStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccelerateStatistics',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryAccelerateStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accelerate_statistics_with_options_async(
        self,
        request: snsu_20180710_models.QueryAccelerateStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryAccelerateStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccelerateStatistics',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryAccelerateStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accelerate_statistics(
        self,
        request: snsu_20180710_models.QueryAccelerateStatisticsRequest,
    ) -> snsu_20180710_models.QueryAccelerateStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_accelerate_statistics_with_options(request, runtime)

    async def query_accelerate_statistics_async(
        self,
        request: snsu_20180710_models.QueryAccelerateStatisticsRequest,
    ) -> snsu_20180710_models.QueryAccelerateStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_accelerate_statistics_with_options_async(request, runtime)

    def query_ebiwith_options(
        self,
        request: snsu_20180710_models.QueryEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEBIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.ebi_id):
            body['Ebi_id'] = request.ebi_id
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEBIResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ebiwith_options_async(
        self,
        request: snsu_20180710_models.QueryEBIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEBIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.ebi_id):
            body['Ebi_id'] = request.ebi_id
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEBI',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEBIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ebi(
        self,
        request: snsu_20180710_models.QueryEBIRequest,
    ) -> snsu_20180710_models.QueryEBIResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ebiwith_options(request, runtime)

    async def query_ebi_async(
        self,
        request: snsu_20180710_models.QueryEBIRequest,
    ) -> snsu_20180710_models.QueryEBIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ebiwith_options_async(request, runtime)

    def query_ent_private_net_addresses_with_options(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEntPrivateNetAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntPrivateNetAddresses',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEntPrivateNetAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ent_private_net_addresses_with_options_async(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEntPrivateNetAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntPrivateNetAddresses',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEntPrivateNetAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ent_private_net_addresses(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetAddressesRequest,
    ) -> snsu_20180710_models.QueryEntPrivateNetAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ent_private_net_addresses_with_options(request, runtime)

    async def query_ent_private_net_addresses_async(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetAddressesRequest,
    ) -> snsu_20180710_models.QueryEntPrivateNetAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ent_private_net_addresses_with_options_async(request, runtime)

    def query_ent_private_net_orders_with_options(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEntPrivateNetOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_address):
            query['FilterAddress'] = request.filter_address
        if not UtilClient.is_unset(request.filter_intention_id):
            query['FilterIntentionId'] = request.filter_intention_id
        if not UtilClient.is_unset(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntPrivateNetOrders',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEntPrivateNetOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ent_private_net_orders_with_options_async(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEntPrivateNetOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_address):
            query['FilterAddress'] = request.filter_address
        if not UtilClient.is_unset(request.filter_intention_id):
            query['FilterIntentionId'] = request.filter_intention_id
        if not UtilClient.is_unset(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntPrivateNetOrders',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEntPrivateNetOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ent_private_net_orders(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetOrdersRequest,
    ) -> snsu_20180710_models.QueryEntPrivateNetOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ent_private_net_orders_with_options(request, runtime)

    async def query_ent_private_net_orders_async(
        self,
        request: snsu_20180710_models.QueryEntPrivateNetOrdersRequest,
    ) -> snsu_20180710_models.QueryEntPrivateNetOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ent_private_net_orders_with_options_async(request, runtime)

    def query_epn_instances_with_options(
        self,
        request: snsu_20180710_models.QueryEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEpnInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEpnInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEpnInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_epn_instances_with_options_async(
        self,
        request: snsu_20180710_models.QueryEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEpnInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEpnInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEpnInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_epn_instances(
        self,
        request: snsu_20180710_models.QueryEpnInstancesRequest,
    ) -> snsu_20180710_models.QueryEpnInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_epn_instances_with_options(request, runtime)

    async def query_epn_instances_async(
        self,
        request: snsu_20180710_models.QueryEpnInstancesRequest,
    ) -> snsu_20180710_models.QueryEpnInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_epn_instances_with_options_async(request, runtime)

    def query_evgw_instances_with_options(
        self,
        request: snsu_20180710_models.QueryEvgwInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEvgwInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEvgwInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEvgwInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_evgw_instances_with_options_async(
        self,
        request: snsu_20180710_models.QueryEvgwInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryEvgwInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEvgwInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryEvgwInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_evgw_instances(
        self,
        request: snsu_20180710_models.QueryEvgwInstancesRequest,
    ) -> snsu_20180710_models.QueryEvgwInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_evgw_instances_with_options(request, runtime)

    async def query_evgw_instances_async(
        self,
        request: snsu_20180710_models.QueryEvgwInstancesRequest,
    ) -> snsu_20180710_models.QueryEvgwInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_evgw_instances_with_options_async(request, runtime)

    def query_open_status_with_options(
        self,
        request: snsu_20180710_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpenStatus',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_open_status_with_options_async(
        self,
        request: snsu_20180710_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpenStatus',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_open_status(
        self,
        request: snsu_20180710_models.QueryOpenStatusRequest,
    ) -> snsu_20180710_models.QueryOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_open_status_with_options(request, runtime)

    async def query_open_status_async(
        self,
        request: snsu_20180710_models.QueryOpenStatusRequest,
    ) -> snsu_20180710_models.QueryOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_open_status_with_options_async(request, runtime)

    def query_test_period_detail_with_options(
        self,
        request: snsu_20180710_models.QueryTestPeriodDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryTestPeriodDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTestPeriodDetail',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryTestPeriodDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_test_period_detail_with_options_async(
        self,
        request: snsu_20180710_models.QueryTestPeriodDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryTestPeriodDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTestPeriodDetail',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryTestPeriodDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_test_period_detail(
        self,
        request: snsu_20180710_models.QueryTestPeriodDetailRequest,
    ) -> snsu_20180710_models.QueryTestPeriodDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_test_period_detail_with_options(request, runtime)

    async def query_test_period_detail_async(
        self,
        request: snsu_20180710_models.QueryTestPeriodDetailRequest,
    ) -> snsu_20180710_models.QueryTestPeriodDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_test_period_detail_with_options_async(request, runtime)

    def query_vtune_instances_with_options(
        self,
        request: snsu_20180710_models.QueryVtuneInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryVtuneInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryVtuneInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryVtuneInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_vtune_instances_with_options_async(
        self,
        request: snsu_20180710_models.QueryVtuneInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.QueryVtuneInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryVtuneInstances',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.QueryVtuneInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_vtune_instances(
        self,
        request: snsu_20180710_models.QueryVtuneInstancesRequest,
    ) -> snsu_20180710_models.QueryVtuneInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_vtune_instances_with_options(request, runtime)

    async def query_vtune_instances_async(
        self,
        request: snsu_20180710_models.QueryVtuneInstancesRequest,
    ) -> snsu_20180710_models.QueryVtuneInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_vtune_instances_with_options_async(request, runtime)

    def resume_epn_instance_with_options(
        self,
        request: snsu_20180710_models.ResumeEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ResumeEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ResumeEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_epn_instance_with_options_async(
        self,
        request: snsu_20180710_models.ResumeEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ResumeEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ResumeEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_epn_instance(
        self,
        request: snsu_20180710_models.ResumeEpnInstanceRequest,
    ) -> snsu_20180710_models.ResumeEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_epn_instance_with_options(request, runtime)

    async def resume_epn_instance_async(
        self,
        request: snsu_20180710_models.ResumeEpnInstanceRequest,
    ) -> snsu_20180710_models.ResumeEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_epn_instance_with_options_async(request, runtime)

    def stop_epn_instance_with_options(
        self,
        request: snsu_20180710_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.StopEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_epn_instance_with_options_async(
        self,
        request: snsu_20180710_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.StopEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_epn_instance(
        self,
        request: snsu_20180710_models.StopEpnInstanceRequest,
    ) -> snsu_20180710_models.StopEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_epn_instance_with_options(request, runtime)

    async def stop_epn_instance_async(
        self,
        request: snsu_20180710_models.StopEpnInstanceRequest,
    ) -> snsu_20180710_models.StopEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_epn_instance_with_options_async(request, runtime)

    def update_epn_instance_with_options(
        self,
        request: snsu_20180710_models.UpdateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accelerate):
            body['Accelerate'] = request.accelerate
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.aliuid):
            body['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.dscp):
            body['Dscp'] = request.dscp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.epn_name):
            body['EpnName'] = request.epn_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security):
            body['Security'] = request.security
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_epn_instance_with_options_async(
        self,
        request: snsu_20180710_models.UpdateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateEpnInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accelerate):
            body['Accelerate'] = request.accelerate
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.aliuid):
            body['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.dscp):
            body['Dscp'] = request.dscp
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.epn_id):
            body['EpnId'] = request.epn_id
        if not UtilClient.is_unset(request.epn_name):
            body['EpnName'] = request.epn_name
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security):
            body['Security'] = request.security
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEpnInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_epn_instance(
        self,
        request: snsu_20180710_models.UpdateEpnInstanceRequest,
    ) -> snsu_20180710_models.UpdateEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_epn_instance_with_options(request, runtime)

    async def update_epn_instance_async(
        self,
        request: snsu_20180710_models.UpdateEpnInstanceRequest,
    ) -> snsu_20180710_models.UpdateEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_epn_instance_with_options_async(request, runtime)

    def update_evgw_instance_with_options(
        self,
        request: snsu_20180710_models.UpdateEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.ipsec_psk):
            body['IpsecPsk'] = request.ipsec_psk
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateEvgwInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_evgw_instance_with_options_async(
        self,
        request: snsu_20180710_models.UpdateEvgwInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateEvgwInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.evgw_id):
            body['EvgwId'] = request.evgw_id
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.ipsec_psk):
            body['IpsecPsk'] = request.ipsec_psk
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEvgwInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateEvgwInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_evgw_instance(
        self,
        request: snsu_20180710_models.UpdateEvgwInstanceRequest,
    ) -> snsu_20180710_models.UpdateEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_evgw_instance_with_options(request, runtime)

    async def update_evgw_instance_async(
        self,
        request: snsu_20180710_models.UpdateEvgwInstanceRequest,
    ) -> snsu_20180710_models.UpdateEvgwInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_evgw_instance_with_options_async(request, runtime)

    def update_vtune_instance_with_options(
        self,
        request: snsu_20180710_models.UpdateVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.enable_bgp):
            body['EnableBgp'] = request.enable_bgp
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateVtuneInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vtune_instance_with_options_async(
        self,
        request: snsu_20180710_models.UpdateVtuneInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.UpdateVtuneInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['AkProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_security_transport):
            body['CallerSecurityTransport'] = request.caller_security_transport
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.enable_bgp):
            body['EnableBgp'] = request.enable_bgp
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.limit_rx):
            body['LimitRx'] = request.limit_rx
        if not UtilClient.is_unset(request.limit_tx):
            body['LimitTx'] = request.limit_tx
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_caller_ip):
            body['ProxyCallerIp'] = request.proxy_caller_ip
        if not UtilClient.is_unset(request.proxy_caller_security_transport):
            body['ProxyCallerSecurityTransport'] = request.proxy_caller_security_transport
        if not UtilClient.is_unset(request.proxy_id):
            body['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            body['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sms_resource_owner_id):
            body['SmsResourceOwnerId'] = request.sms_resource_owner_id
        if not UtilClient.is_unset(request.tag_key_1):
            body['TagKey1'] = request.tag_key_1
        if not UtilClient.is_unset(request.tag_key_2):
            body['TagKey2'] = request.tag_key_2
        if not UtilClient.is_unset(request.tag_key_3):
            body['TagKey3'] = request.tag_key_3
        if not UtilClient.is_unset(request.tag_key_4):
            body['TagKey4'] = request.tag_key_4
        if not UtilClient.is_unset(request.tag_key_5):
            body['TagKey5'] = request.tag_key_5
        if not UtilClient.is_unset(request.tag_key_value_models):
            body['TagKeyValueModels'] = request.tag_key_value_models
        if not UtilClient.is_unset(request.tag_value_1):
            body['TagValue1'] = request.tag_value_1
        if not UtilClient.is_unset(request.tag_value_2):
            body['TagValue2'] = request.tag_value_2
        if not UtilClient.is_unset(request.tag_value_3):
            body['TagValue3'] = request.tag_value_3
        if not UtilClient.is_unset(request.tag_value_4):
            body['TagValue4'] = request.tag_value_4
        if not UtilClient.is_unset(request.tag_value_5):
            body['TagValue5'] = request.tag_value_5
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vtune_id):
            body['VtuneId'] = request.vtune_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVtuneInstance',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.UpdateVtuneInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vtune_instance(
        self,
        request: snsu_20180710_models.UpdateVtuneInstanceRequest,
    ) -> snsu_20180710_models.UpdateVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vtune_instance_with_options(request, runtime)

    async def update_vtune_instance_async(
        self,
        request: snsu_20180710_models.UpdateVtuneInstanceRequest,
    ) -> snsu_20180710_models.UpdateVtuneInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vtune_instance_with_options_async(request, runtime)

    def validat_yun_snsu_buy_with_options(
        self,
        request: snsu_20180710_models.ValidatYunSnsuBuyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ValidatYunSnsuBuyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatYunSnsuBuy',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ValidatYunSnsuBuyResponse(),
            self.call_api(params, req, runtime)
        )

    async def validat_yun_snsu_buy_with_options_async(
        self,
        request: snsu_20180710_models.ValidatYunSnsuBuyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsu_20180710_models.ValidatYunSnsuBuyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatYunSnsuBuy',
            version='2018-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            snsu_20180710_models.ValidatYunSnsuBuyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validat_yun_snsu_buy(
        self,
        request: snsu_20180710_models.ValidatYunSnsuBuyRequest,
    ) -> snsu_20180710_models.ValidatYunSnsuBuyResponse:
        runtime = util_models.RuntimeOptions()
        return self.validat_yun_snsu_buy_with_options(request, runtime)

    async def validat_yun_snsu_buy_async(
        self,
        request: snsu_20180710_models.ValidatYunSnsuBuyRequest,
    ) -> snsu_20180710_models.ValidatYunSnsuBuyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validat_yun_snsu_buy_with_options_async(request, runtime)
