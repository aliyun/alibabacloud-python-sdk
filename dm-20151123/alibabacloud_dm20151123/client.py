# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.request import TeaRequest
from Tea.exceptions import TeaException
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_fileform.client import Client as FileFormClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dm20151123 import models as dm_20151123_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_darabonba_number.client import Client as NumberClient


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
        self._endpoint = self.get_endpoint('dm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = TeaCore.do_action(_request)
        resp_map = None
        body_str = UtilClient.read_as_string(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = await TeaCore.async_do_action(_request)
        resp_map = None
        body_str = await UtilClient.read_as_string_async(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

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

    def add_ipfilter_with_options(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.AddIpfilterResponse:
        """
        @summary Add IP Protection Information
        
        @param request: AddIpfilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpfilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_address):
            query['IpAddress'] = request.ip_address
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
            action='AddIpfilter',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.AddIpfilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ipfilter_with_options_async(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.AddIpfilterResponse:
        """
        @summary Add IP Protection Information
        
        @param request: AddIpfilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpfilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_address):
            query['IpAddress'] = request.ip_address
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
            action='AddIpfilter',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.AddIpfilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ipfilter(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
    ) -> dm_20151123_models.AddIpfilterResponse:
        """
        @summary Add IP Protection Information
        
        @param request: AddIpfilterRequest
        @return: AddIpfilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ipfilter_with_options(request, runtime)

    async def add_ipfilter_async(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
    ) -> dm_20151123_models.AddIpfilterResponse:
        """
        @summary Add IP Protection Information
        
        @param request: AddIpfilterRequest
        @return: AddIpfilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ipfilter_with_options_async(request, runtime)

    def approve_reply_mail_address_with_options(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        """
        @summary Verify Reply Address
        
        @param request: ApproveReplyMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveReplyMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveReplyMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ApproveReplyMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_reply_mail_address_with_options_async(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        """
        @summary Verify Reply Address
        
        @param request: ApproveReplyMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveReplyMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveReplyMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ApproveReplyMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_reply_mail_address(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        """
        @summary Verify Reply Address
        
        @param request: ApproveReplyMailAddressRequest
        @return: ApproveReplyMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_reply_mail_address_with_options(request, runtime)

    async def approve_reply_mail_address_async(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        """
        @summary Verify Reply Address
        
        @param request: ApproveReplyMailAddressRequest
        @return: ApproveReplyMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.approve_reply_mail_address_with_options_async(request, runtime)

    def batch_send_mail_with_options(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.BatchSendMailResponse:
        """
        @summary Batch Send Emails
        
        @param request: BatchSendMailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSendMailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.headers):
            query['Headers'] = request.headers
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.un_subscribe_filter_level):
            query['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not UtilClient.is_unset(request.un_subscribe_link_type):
            query['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSendMail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.BatchSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_send_mail_with_options_async(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.BatchSendMailResponse:
        """
        @summary Batch Send Emails
        
        @param request: BatchSendMailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSendMailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.headers):
            query['Headers'] = request.headers
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.un_subscribe_filter_level):
            query['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not UtilClient.is_unset(request.un_subscribe_link_type):
            query['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSendMail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.BatchSendMailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_send_mail(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
    ) -> dm_20151123_models.BatchSendMailResponse:
        """
        @summary Batch Send Emails
        
        @param request: BatchSendMailRequest
        @return: BatchSendMailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_send_mail_with_options(request, runtime)

    async def batch_send_mail_async(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
    ) -> dm_20151123_models.BatchSendMailResponse:
        """
        @summary Batch Send Emails
        
        @param request: BatchSendMailRequest
        @return: BatchSendMailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_send_mail_with_options_async(request, runtime)

    def change_domain_dkim_record_with_options(
        self,
        request: dm_20151123_models.ChangeDomainDkimRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ChangeDomainDkimRecordResponse:
        """
        @summary 修改域名DKIM记录
        
        @param request: ChangeDomainDkimRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainDkimRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dkim_rsa_length):
            query['DkimRsaLength'] = request.dkim_rsa_length
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
            action='ChangeDomainDkimRecord',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ChangeDomainDkimRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_dkim_record_with_options_async(
        self,
        request: dm_20151123_models.ChangeDomainDkimRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ChangeDomainDkimRecordResponse:
        """
        @summary 修改域名DKIM记录
        
        @param request: ChangeDomainDkimRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainDkimRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dkim_rsa_length):
            query['DkimRsaLength'] = request.dkim_rsa_length
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
            action='ChangeDomainDkimRecord',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ChangeDomainDkimRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_dkim_record(
        self,
        request: dm_20151123_models.ChangeDomainDkimRecordRequest,
    ) -> dm_20151123_models.ChangeDomainDkimRecordResponse:
        """
        @summary 修改域名DKIM记录
        
        @param request: ChangeDomainDkimRecordRequest
        @return: ChangeDomainDkimRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_domain_dkim_record_with_options(request, runtime)

    async def change_domain_dkim_record_async(
        self,
        request: dm_20151123_models.ChangeDomainDkimRecordRequest,
    ) -> dm_20151123_models.ChangeDomainDkimRecordResponse:
        """
        @summary 修改域名DKIM记录
        
        @param request: ChangeDomainDkimRecordRequest
        @return: ChangeDomainDkimRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_domain_dkim_record_with_options_async(request, runtime)

    def check_disposable_with_options(
        self,
        request: dm_20151123_models.CheckDisposableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDisposableResponse:
        """
        @summary 检查地址是否为一次性邮箱
        
        @param request: CheckDisposableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDisposableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDisposable',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckDisposableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_disposable_with_options_async(
        self,
        request: dm_20151123_models.CheckDisposableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDisposableResponse:
        """
        @summary 检查地址是否为一次性邮箱
        
        @param request: CheckDisposableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDisposableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDisposable',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckDisposableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_disposable(
        self,
        request: dm_20151123_models.CheckDisposableRequest,
    ) -> dm_20151123_models.CheckDisposableResponse:
        """
        @summary 检查地址是否为一次性邮箱
        
        @param request: CheckDisposableRequest
        @return: CheckDisposableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_disposable_with_options(request, runtime)

    async def check_disposable_async(
        self,
        request: dm_20151123_models.CheckDisposableRequest,
    ) -> dm_20151123_models.CheckDisposableResponse:
        """
        @summary 检查地址是否为一次性邮箱
        
        @param request: CheckDisposableRequest
        @return: CheckDisposableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_disposable_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: dm_20151123_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDomainResponse:
        """
        @summary Check Domain Status
        
        @param request: CheckDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
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
            action='CheckDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: dm_20151123_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDomainResponse:
        """
        @summary Check Domain Status
        
        @param request: CheckDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
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
            action='CheckDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: dm_20151123_models.CheckDomainRequest,
    ) -> dm_20151123_models.CheckDomainResponse:
        """
        @summary Check Domain Status
        
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: dm_20151123_models.CheckDomainRequest,
    ) -> dm_20151123_models.CheckDomainResponse:
        """
        @summary Check Domain Status
        
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_reply_to_mail_address_with_options(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        """
        @summary Validate Reply-To Address
        
        @param request: CheckReplyToMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckReplyToMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReplyToMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckReplyToMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_reply_to_mail_address_with_options_async(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        """
        @summary Validate Reply-To Address
        
        @param request: CheckReplyToMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckReplyToMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReplyToMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CheckReplyToMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_reply_to_mail_address(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        """
        @summary Validate Reply-To Address
        
        @param request: CheckReplyToMailAddressRequest
        @return: CheckReplyToMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_reply_to_mail_address_with_options(request, runtime)

    async def check_reply_to_mail_address_async(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        """
        @summary Validate Reply-To Address
        
        @param request: CheckReplyToMailAddressRequest
        @return: CheckReplyToMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_reply_to_mail_address_with_options_async(request, runtime)

    def config_set_cancel_relation_from_address_with_options(
        self,
        request: dm_20151123_models.ConfigSetCancelRelationFromAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetCancelRelationFromAddressResponse:
        """
        @summary 配置集取消关联发信地址
        
        @param request: ConfigSetCancelRelationFromAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetCancelRelationFromAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_address):
            query['FromAddress'] = request.from_address
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetCancelRelationFromAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetCancelRelationFromAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_cancel_relation_from_address_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetCancelRelationFromAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetCancelRelationFromAddressResponse:
        """
        @summary 配置集取消关联发信地址
        
        @param request: ConfigSetCancelRelationFromAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetCancelRelationFromAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_address):
            query['FromAddress'] = request.from_address
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetCancelRelationFromAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetCancelRelationFromAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_cancel_relation_from_address(
        self,
        request: dm_20151123_models.ConfigSetCancelRelationFromAddressRequest,
    ) -> dm_20151123_models.ConfigSetCancelRelationFromAddressResponse:
        """
        @summary 配置集取消关联发信地址
        
        @param request: ConfigSetCancelRelationFromAddressRequest
        @return: ConfigSetCancelRelationFromAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_cancel_relation_from_address_with_options(request, runtime)

    async def config_set_cancel_relation_from_address_async(
        self,
        request: dm_20151123_models.ConfigSetCancelRelationFromAddressRequest,
    ) -> dm_20151123_models.ConfigSetCancelRelationFromAddressResponse:
        """
        @summary 配置集取消关联发信地址
        
        @param request: ConfigSetCancelRelationFromAddressRequest
        @return: ConfigSetCancelRelationFromAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_cancel_relation_from_address_with_options_async(request, runtime)

    def config_set_create_with_options(
        self,
        request: dm_20151123_models.ConfigSetCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetCreateResponse:
        """
        @summary 配置集创建
        
        @param request: ConfigSetCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetCreate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_create_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetCreateResponse:
        """
        @summary 配置集创建
        
        @param request: ConfigSetCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetCreate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_create(
        self,
        request: dm_20151123_models.ConfigSetCreateRequest,
    ) -> dm_20151123_models.ConfigSetCreateResponse:
        """
        @summary 配置集创建
        
        @param request: ConfigSetCreateRequest
        @return: ConfigSetCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_create_with_options(request, runtime)

    async def config_set_create_async(
        self,
        request: dm_20151123_models.ConfigSetCreateRequest,
    ) -> dm_20151123_models.ConfigSetCreateResponse:
        """
        @summary 配置集创建
        
        @param request: ConfigSetCreateRequest
        @return: ConfigSetCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_create_with_options_async(request, runtime)

    def config_set_delete_with_options(
        self,
        request: dm_20151123_models.ConfigSetDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetDeleteResponse:
        """
        @summary 删除配置集
        
        @param request: ConfigSetDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.is_force):
            query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetDelete',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_delete_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetDeleteResponse:
        """
        @summary 删除配置集
        
        @param request: ConfigSetDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.is_force):
            query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetDelete',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_delete(
        self,
        request: dm_20151123_models.ConfigSetDeleteRequest,
    ) -> dm_20151123_models.ConfigSetDeleteResponse:
        """
        @summary 删除配置集
        
        @param request: ConfigSetDeleteRequest
        @return: ConfigSetDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_delete_with_options(request, runtime)

    async def config_set_delete_async(
        self,
        request: dm_20151123_models.ConfigSetDeleteRequest,
    ) -> dm_20151123_models.ConfigSetDeleteResponse:
        """
        @summary 删除配置集
        
        @param request: ConfigSetDeleteRequest
        @return: ConfigSetDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_delete_with_options_async(request, runtime)

    def config_set_detail_with_options(
        self,
        request: dm_20151123_models.ConfigSetDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetDetailResponse:
        """
        @summary 配置集详情
        
        @param request: ConfigSetDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_detail_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetDetailResponse:
        """
        @summary 配置集详情
        
        @param request: ConfigSetDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_detail(
        self,
        request: dm_20151123_models.ConfigSetDetailRequest,
    ) -> dm_20151123_models.ConfigSetDetailResponse:
        """
        @summary 配置集详情
        
        @param request: ConfigSetDetailRequest
        @return: ConfigSetDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_detail_with_options(request, runtime)

    async def config_set_detail_async(
        self,
        request: dm_20151123_models.ConfigSetDetailRequest,
    ) -> dm_20151123_models.ConfigSetDetailResponse:
        """
        @summary 配置集详情
        
        @param request: ConfigSetDetailRequest
        @return: ConfigSetDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_detail_with_options_async(request, runtime)

    def config_set_list_with_options(
        self,
        request: dm_20151123_models.ConfigSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetListResponse:
        """
        @summary 配置集列表
        
        @param request: ConfigSetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_list_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetListResponse:
        """
        @summary 配置集列表
        
        @param request: ConfigSetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_list(
        self,
        request: dm_20151123_models.ConfigSetListRequest,
    ) -> dm_20151123_models.ConfigSetListResponse:
        """
        @summary 配置集列表
        
        @param request: ConfigSetListRequest
        @return: ConfigSetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_list_with_options(request, runtime)

    async def config_set_list_async(
        self,
        request: dm_20151123_models.ConfigSetListRequest,
    ) -> dm_20151123_models.ConfigSetListResponse:
        """
        @summary 配置集列表
        
        @param request: ConfigSetListRequest
        @return: ConfigSetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_list_with_options_async(request, runtime)

    def config_set_relation_from_address_with_options(
        self,
        request: dm_20151123_models.ConfigSetRelationFromAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetRelationFromAddressResponse:
        """
        @summary 配置集关联发信地址
        
        @param request: ConfigSetRelationFromAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetRelationFromAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_address):
            query['FromAddress'] = request.from_address
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetRelationFromAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetRelationFromAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_relation_from_address_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetRelationFromAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetRelationFromAddressResponse:
        """
        @summary 配置集关联发信地址
        
        @param request: ConfigSetRelationFromAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetRelationFromAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_address):
            query['FromAddress'] = request.from_address
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetRelationFromAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetRelationFromAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_relation_from_address(
        self,
        request: dm_20151123_models.ConfigSetRelationFromAddressRequest,
    ) -> dm_20151123_models.ConfigSetRelationFromAddressResponse:
        """
        @summary 配置集关联发信地址
        
        @param request: ConfigSetRelationFromAddressRequest
        @return: ConfigSetRelationFromAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_relation_from_address_with_options(request, runtime)

    async def config_set_relation_from_address_async(
        self,
        request: dm_20151123_models.ConfigSetRelationFromAddressRequest,
    ) -> dm_20151123_models.ConfigSetRelationFromAddressResponse:
        """
        @summary 配置集关联发信地址
        
        @param request: ConfigSetRelationFromAddressRequest
        @return: ConfigSetRelationFromAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_relation_from_address_with_options_async(request, runtime)

    def config_set_update_with_options(
        self,
        request: dm_20151123_models.ConfigSetUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetUpdateResponse:
        """
        @summary 配置集更新
        
        @param request: ConfigSetUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetUpdate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_update_with_options_async(
        self,
        request: dm_20151123_models.ConfigSetUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ConfigSetUpdateResponse:
        """
        @summary 配置集更新
        
        @param request: ConfigSetUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSetUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSetUpdate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ConfigSetUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_update(
        self,
        request: dm_20151123_models.ConfigSetUpdateRequest,
    ) -> dm_20151123_models.ConfigSetUpdateResponse:
        """
        @summary 配置集更新
        
        @param request: ConfigSetUpdateRequest
        @return: ConfigSetUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_set_update_with_options(request, runtime)

    async def config_set_update_async(
        self,
        request: dm_20151123_models.ConfigSetUpdateRequest,
    ) -> dm_20151123_models.ConfigSetUpdateResponse:
        """
        @summary 配置集更新
        
        @param request: ConfigSetUpdateRequest
        @return: ConfigSetUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_set_update_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: dm_20151123_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDomainResponse:
        """
        @summary Create Domain
        
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.dkim_selector):
            query['dkimSelector'] = request.dkim_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: dm_20151123_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDomainResponse:
        """
        @summary Create Domain
        
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.dkim_selector):
            query['dkimSelector'] = request.dkim_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: dm_20151123_models.CreateDomainRequest,
    ) -> dm_20151123_models.CreateDomainResponse:
        """
        @summary Create Domain
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: dm_20151123_models.CreateDomainRequest,
    ) -> dm_20151123_models.CreateDomainResponse:
        """
        @summary Create Domain
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_mail_address_with_options(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        """
        @summary Create a mail address.
        
        @param request: CreateMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mail_address_with_options_async(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        """
        @summary Create a mail address.
        
        @param request: CreateMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mail_address(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        """
        @summary Create a mail address.
        
        @param request: CreateMailAddressRequest
        @return: CreateMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mail_address_with_options(request, runtime)

    async def create_mail_address_async(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        """
        @summary Create a mail address.
        
        @param request: CreateMailAddressRequest
        @return: CreateMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mail_address_with_options_async(request, runtime)

    def create_receiver_with_options(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateReceiverResponse:
        """
        @summary Create Receiver List
        
        @param request: CreateReceiverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReceiverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_alias):
            query['ReceiversAlias'] = request.receivers_alias
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReceiver',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_receiver_with_options_async(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateReceiverResponse:
        """
        @summary Create Receiver List
        
        @param request: CreateReceiverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReceiverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_alias):
            query['ReceiversAlias'] = request.receivers_alias
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReceiver',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_receiver(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
    ) -> dm_20151123_models.CreateReceiverResponse:
        """
        @summary Create Receiver List
        
        @param request: CreateReceiverRequest
        @return: CreateReceiverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_receiver_with_options(request, runtime)

    async def create_receiver_async(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
    ) -> dm_20151123_models.CreateReceiverResponse:
        """
        @summary Create Receiver List
        
        @param request: CreateReceiverRequest
        @return: CreateReceiverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_receiver_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: dm_20151123_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTagResponse:
        """
        @summary Create Tag
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: dm_20151123_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTagResponse:
        """
        @summary Create Tag
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: dm_20151123_models.CreateTagRequest,
    ) -> dm_20151123_models.CreateTagResponse:
        """
        @summary Create Tag
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: dm_20151123_models.CreateTagRequest,
    ) -> dm_20151123_models.CreateTagResponse:
        """
        @summary Create Tag
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_user_suppression_with_options(
        self,
        request: dm_20151123_models.CreateUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateUserSuppressionResponse:
        """
        @summary Create User\\"s Invalid Address
        
        @param request: CreateUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
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
            action='CreateUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_suppression_with_options_async(
        self,
        request: dm_20151123_models.CreateUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateUserSuppressionResponse:
        """
        @summary Create User\\"s Invalid Address
        
        @param request: CreateUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
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
            action='CreateUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.CreateUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_suppression(
        self,
        request: dm_20151123_models.CreateUserSuppressionRequest,
    ) -> dm_20151123_models.CreateUserSuppressionResponse:
        """
        @summary Create User\\"s Invalid Address
        
        @param request: CreateUserSuppressionRequest
        @return: CreateUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_suppression_with_options(request, runtime)

    async def create_user_suppression_async(
        self,
        request: dm_20151123_models.CreateUserSuppressionRequest,
    ) -> dm_20151123_models.CreateUserSuppressionResponse:
        """
        @summary Create User\\"s Invalid Address
        
        @param request: CreateUserSuppressionRequest
        @return: CreateUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_suppression_with_options_async(request, runtime)

    def dedicated_ip_auto_renewal_with_options(
        self,
        request: dm_20151123_models.DedicatedIpAutoRenewalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpAutoRenewalResponse:
        """
        @summary Set Dedicated IP Auto Renewal
        
        @param request: DedicatedIpAutoRenewalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpAutoRenewalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpAutoRenewal',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpAutoRenewalResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_auto_renewal_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpAutoRenewalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpAutoRenewalResponse:
        """
        @summary Set Dedicated IP Auto Renewal
        
        @param request: DedicatedIpAutoRenewalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpAutoRenewalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpAutoRenewal',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpAutoRenewalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_auto_renewal(
        self,
        request: dm_20151123_models.DedicatedIpAutoRenewalRequest,
    ) -> dm_20151123_models.DedicatedIpAutoRenewalResponse:
        """
        @summary Set Dedicated IP Auto Renewal
        
        @param request: DedicatedIpAutoRenewalRequest
        @return: DedicatedIpAutoRenewalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_auto_renewal_with_options(request, runtime)

    async def dedicated_ip_auto_renewal_async(
        self,
        request: dm_20151123_models.DedicatedIpAutoRenewalRequest,
    ) -> dm_20151123_models.DedicatedIpAutoRenewalResponse:
        """
        @summary Set Dedicated IP Auto Renewal
        
        @param request: DedicatedIpAutoRenewalRequest
        @return: DedicatedIpAutoRenewalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_auto_renewal_with_options_async(request, runtime)

    def dedicated_ip_change_warmup_type_with_options(
        self,
        request: dm_20151123_models.DedicatedIpChangeWarmupTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpChangeWarmupTypeResponse:
        """
        @summary Change the warmup method for a dedicated IP
        
        @param request: DedicatedIpChangeWarmupTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpChangeWarmupTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.warmup_type):
            query['WarmupType'] = request.warmup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpChangeWarmupType',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpChangeWarmupTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_change_warmup_type_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpChangeWarmupTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpChangeWarmupTypeResponse:
        """
        @summary Change the warmup method for a dedicated IP
        
        @param request: DedicatedIpChangeWarmupTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpChangeWarmupTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.warmup_type):
            query['WarmupType'] = request.warmup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpChangeWarmupType',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpChangeWarmupTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_change_warmup_type(
        self,
        request: dm_20151123_models.DedicatedIpChangeWarmupTypeRequest,
    ) -> dm_20151123_models.DedicatedIpChangeWarmupTypeResponse:
        """
        @summary Change the warmup method for a dedicated IP
        
        @param request: DedicatedIpChangeWarmupTypeRequest
        @return: DedicatedIpChangeWarmupTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_change_warmup_type_with_options(request, runtime)

    async def dedicated_ip_change_warmup_type_async(
        self,
        request: dm_20151123_models.DedicatedIpChangeWarmupTypeRequest,
    ) -> dm_20151123_models.DedicatedIpChangeWarmupTypeResponse:
        """
        @summary Change the warmup method for a dedicated IP
        
        @param request: DedicatedIpChangeWarmupTypeRequest
        @return: DedicatedIpChangeWarmupTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_change_warmup_type_with_options_async(request, runtime)

    def dedicated_ip_list_with_options(
        self,
        request: dm_20151123_models.DedicatedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpListResponse:
        """
        @summary Dedicated IP User IP List
        
        @param request: DedicatedIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_list_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpListResponse:
        """
        @summary Dedicated IP User IP List
        
        @param request: DedicatedIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_list(
        self,
        request: dm_20151123_models.DedicatedIpListRequest,
    ) -> dm_20151123_models.DedicatedIpListResponse:
        """
        @summary Dedicated IP User IP List
        
        @param request: DedicatedIpListRequest
        @return: DedicatedIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_list_with_options(request, runtime)

    async def dedicated_ip_list_async(
        self,
        request: dm_20151123_models.DedicatedIpListRequest,
    ) -> dm_20151123_models.DedicatedIpListResponse:
        """
        @summary Dedicated IP User IP List
        
        @param request: DedicatedIpListRequest
        @return: DedicatedIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_list_with_options_async(request, runtime)

    def dedicated_ip_none_pool_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpNonePoolListResponse:
        """
        @summary Purchased Independent IPs Not Added to Pool
        
        @param request: DedicatedIpNonePoolListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpNonePoolListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DedicatedIpNonePoolList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpNonePoolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_none_pool_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpNonePoolListResponse:
        """
        @summary Purchased Independent IPs Not Added to Pool
        
        @param request: DedicatedIpNonePoolListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpNonePoolListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DedicatedIpNonePoolList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpNonePoolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_none_pool_list(self) -> dm_20151123_models.DedicatedIpNonePoolListResponse:
        """
        @summary Purchased Independent IPs Not Added to Pool
        
        @return: DedicatedIpNonePoolListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_none_pool_list_with_options(runtime)

    async def dedicated_ip_none_pool_list_async(self) -> dm_20151123_models.DedicatedIpNonePoolListResponse:
        """
        @summary Purchased Independent IPs Not Added to Pool
        
        @return: DedicatedIpNonePoolListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_none_pool_list_with_options_async(runtime)

    def dedicated_ip_pool_create_with_options(
        self,
        request: dm_20151123_models.DedicatedIpPoolCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolCreateResponse:
        """
        @summary Creation of Independent IP Pool
        
        @param request: DedicatedIpPoolCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolCreate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_create_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolCreateResponse:
        """
        @summary Creation of Independent IP Pool
        
        @param request: DedicatedIpPoolCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolCreate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_create(
        self,
        request: dm_20151123_models.DedicatedIpPoolCreateRequest,
    ) -> dm_20151123_models.DedicatedIpPoolCreateResponse:
        """
        @summary Creation of Independent IP Pool
        
        @param request: DedicatedIpPoolCreateRequest
        @return: DedicatedIpPoolCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_pool_create_with_options(request, runtime)

    async def dedicated_ip_pool_create_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolCreateRequest,
    ) -> dm_20151123_models.DedicatedIpPoolCreateResponse:
        """
        @summary Creation of Independent IP Pool
        
        @param request: DedicatedIpPoolCreateRequest
        @return: DedicatedIpPoolCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_pool_create_with_options_async(request, runtime)

    def dedicated_ip_pool_delete_with_options(
        self,
        request: dm_20151123_models.DedicatedIpPoolDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolDeleteResponse:
        """
        @summary 独立IP池删除
        
        @param request: DedicatedIpPoolDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolDelete',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_delete_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolDeleteResponse:
        """
        @summary 独立IP池删除
        
        @param request: DedicatedIpPoolDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolDelete',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_delete(
        self,
        request: dm_20151123_models.DedicatedIpPoolDeleteRequest,
    ) -> dm_20151123_models.DedicatedIpPoolDeleteResponse:
        """
        @summary 独立IP池删除
        
        @param request: DedicatedIpPoolDeleteRequest
        @return: DedicatedIpPoolDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_pool_delete_with_options(request, runtime)

    async def dedicated_ip_pool_delete_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolDeleteRequest,
    ) -> dm_20151123_models.DedicatedIpPoolDeleteResponse:
        """
        @summary 独立IP池删除
        
        @param request: DedicatedIpPoolDeleteRequest
        @return: DedicatedIpPoolDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_pool_delete_with_options_async(request, runtime)

    def dedicated_ip_pool_list_with_options(
        self,
        request: dm_20151123_models.DedicatedIpPoolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolListResponse:
        """
        @summary Dedicated IP Pool List
        
        @param request: DedicatedIpPoolListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_list_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolListResponse:
        """
        @summary Dedicated IP Pool List
        
        @param request: DedicatedIpPoolListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_list(
        self,
        request: dm_20151123_models.DedicatedIpPoolListRequest,
    ) -> dm_20151123_models.DedicatedIpPoolListResponse:
        """
        @summary Dedicated IP Pool List
        
        @param request: DedicatedIpPoolListRequest
        @return: DedicatedIpPoolListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_pool_list_with_options(request, runtime)

    async def dedicated_ip_pool_list_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolListRequest,
    ) -> dm_20151123_models.DedicatedIpPoolListResponse:
        """
        @summary Dedicated IP Pool List
        
        @param request: DedicatedIpPoolListRequest
        @return: DedicatedIpPoolListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_pool_list_with_options_async(request, runtime)

    def dedicated_ip_pool_update_with_options(
        self,
        request: dm_20151123_models.DedicatedIpPoolUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolUpdateResponse:
        """
        @summary Update of dedicated IP Pool
        
        @param request: DedicatedIpPoolUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.update_resource):
            query['UpdateResource'] = request.update_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolUpdate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_update_with_options_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DedicatedIpPoolUpdateResponse:
        """
        @summary Update of dedicated IP Pool
        
        @param request: DedicatedIpPoolUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DedicatedIpPoolUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.update_resource):
            query['UpdateResource'] = request.update_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DedicatedIpPoolUpdate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DedicatedIpPoolUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_update(
        self,
        request: dm_20151123_models.DedicatedIpPoolUpdateRequest,
    ) -> dm_20151123_models.DedicatedIpPoolUpdateResponse:
        """
        @summary Update of dedicated IP Pool
        
        @param request: DedicatedIpPoolUpdateRequest
        @return: DedicatedIpPoolUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dedicated_ip_pool_update_with_options(request, runtime)

    async def dedicated_ip_pool_update_async(
        self,
        request: dm_20151123_models.DedicatedIpPoolUpdateRequest,
    ) -> dm_20151123_models.DedicatedIpPoolUpdateResponse:
        """
        @summary Update of dedicated IP Pool
        
        @param request: DedicatedIpPoolUpdateRequest
        @return: DedicatedIpPoolUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dedicated_ip_pool_update_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteDomainResponse:
        """
        @summary Delete Domain
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
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
            action='DeleteDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteDomainResponse:
        """
        @summary Delete Domain
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
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
            action='DeleteDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
    ) -> dm_20151123_models.DeleteDomainResponse:
        """
        @summary Delete Domain
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
    ) -> dm_20151123_models.DeleteDomainResponse:
        """
        @summary Delete Domain
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_invalid_address_with_options(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        """
        @summary Remove invalid addresses from the invalid address database
        
        @param request: DeleteInvalidAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInvalidAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvalidAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteInvalidAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_invalid_address_with_options_async(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        """
        @summary Remove invalid addresses from the invalid address database
        
        @param request: DeleteInvalidAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInvalidAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvalidAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteInvalidAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_invalid_address(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        """
        @summary Remove invalid addresses from the invalid address database
        
        @param request: DeleteInvalidAddressRequest
        @return: DeleteInvalidAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_invalid_address_with_options(request, runtime)

    async def delete_invalid_address_async(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        """
        @summary Remove invalid addresses from the invalid address database
        
        @param request: DeleteInvalidAddressRequest
        @return: DeleteInvalidAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_invalid_address_with_options_async(request, runtime)

    def delete_ipfilter_by_edm_id_with_options(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        """
        @summary Delete IP Protection Information
        
        @param request: DeleteIpfilterByEdmIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpfilterByEdmIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='DeleteIpfilterByEdmId',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteIpfilterByEdmIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipfilter_by_edm_id_with_options_async(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        """
        @summary Delete IP Protection Information
        
        @param request: DeleteIpfilterByEdmIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpfilterByEdmIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='DeleteIpfilterByEdmId',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteIpfilterByEdmIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipfilter_by_edm_id(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        """
        @summary Delete IP Protection Information
        
        @param request: DeleteIpfilterByEdmIdRequest
        @return: DeleteIpfilterByEdmIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipfilter_by_edm_id_with_options(request, runtime)

    async def delete_ipfilter_by_edm_id_async(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        """
        @summary Delete IP Protection Information
        
        @param request: DeleteIpfilterByEdmIdRequest
        @return: DeleteIpfilterByEdmIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipfilter_by_edm_id_with_options_async(request, runtime)

    def delete_mail_address_with_options(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        """
        @summary Delete Mail Address
        
        @param request: DeleteMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
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
            action='DeleteMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mail_address_with_options_async(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        """
        @summary Delete Mail Address
        
        @param request: DeleteMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
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
            action='DeleteMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mail_address(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        """
        @summary Delete Mail Address
        
        @param request: DeleteMailAddressRequest
        @return: DeleteMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mail_address_with_options(request, runtime)

    async def delete_mail_address_async(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        """
        @summary Delete Mail Address
        
        @param request: DeleteMailAddressRequest
        @return: DeleteMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mail_address_with_options_async(request, runtime)

    def delete_receiver_with_options(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        """
        @summary Delete Receiver List
        
        @param request: DeleteReceiverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReceiverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiver',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_receiver_with_options_async(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        """
        @summary Delete Receiver List
        
        @param request: DeleteReceiverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReceiverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiver',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_receiver(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        """
        @summary Delete Receiver List
        
        @param request: DeleteReceiverRequest
        @return: DeleteReceiverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_with_options(request, runtime)

    async def delete_receiver_async(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        """
        @summary Delete Receiver List
        
        @param request: DeleteReceiverRequest
        @return: DeleteReceiverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_receiver_with_options_async(request, runtime)

    def delete_receiver_detail_with_options(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        """
        @summary Delete a Single Recipient
        
        @param request: DeleteReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        """
        @summary Delete a Single Recipient
        
        @param request: DeleteReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_receiver_detail(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        """
        @summary Delete a Single Recipient
        
        @param request: DeleteReceiverDetailRequest
        @return: DeleteReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_detail_with_options(request, runtime)

    async def delete_receiver_detail_async(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        """
        @summary Delete a Single Recipient
        
        @param request: DeleteReceiverDetailRequest
        @return: DeleteReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_receiver_detail_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: dm_20151123_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTagResponse:
        """
        @summary Delete Tag
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: dm_20151123_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTagResponse:
        """
        @summary Delete Tag
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: dm_20151123_models.DeleteTagRequest,
    ) -> dm_20151123_models.DeleteTagResponse:
        """
        @summary Delete Tag
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: dm_20151123_models.DeleteTagRequest,
    ) -> dm_20151123_models.DeleteTagResponse:
        """
        @summary Delete Tag
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_validate_file_with_options(
        self,
        request: dm_20151123_models.DeleteValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteValidateFileResponse:
        """
        @summary 删除批量校验任务的结果文件
        
        @param request: DeleteValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_validate_file_with_options_async(
        self,
        request: dm_20151123_models.DeleteValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteValidateFileResponse:
        """
        @summary 删除批量校验任务的结果文件
        
        @param request: DeleteValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DeleteValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_validate_file(
        self,
        request: dm_20151123_models.DeleteValidateFileRequest,
    ) -> dm_20151123_models.DeleteValidateFileResponse:
        """
        @summary 删除批量校验任务的结果文件
        
        @param request: DeleteValidateFileRequest
        @return: DeleteValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_validate_file_with_options(request, runtime)

    async def delete_validate_file_async(
        self,
        request: dm_20151123_models.DeleteValidateFileRequest,
    ) -> dm_20151123_models.DeleteValidateFileResponse:
        """
        @summary 删除批量校验任务的结果文件
        
        @param request: DeleteValidateFileRequest
        @return: DeleteValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_validate_file_with_options_async(request, runtime)

    def desc_account_summary_with_options(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        """
        @summary Retrieve account information.
        
        @param request: DescAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescAccountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescAccountSummary',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_account_summary_with_options_async(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        """
        @summary Retrieve account information.
        
        @param request: DescAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescAccountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescAccountSummary',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_account_summary(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        """
        @summary Retrieve account information.
        
        @param request: DescAccountSummaryRequest
        @return: DescAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.desc_account_summary_with_options(request, runtime)

    async def desc_account_summary_async(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        """
        @summary Retrieve account information.
        
        @param request: DescAccountSummaryRequest
        @return: DescAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.desc_account_summary_with_options_async(request, runtime)

    def desc_domain_with_options(
        self,
        request: dm_20151123_models.DescDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescDomainResponse:
        """
        @summary Get Domain Details
        
        @param request: DescDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.require_real_time_dns_records):
            query['RequireRealTimeDnsRecords'] = request.require_real_time_dns_records
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_domain_with_options_async(
        self,
        request: dm_20151123_models.DescDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescDomainResponse:
        """
        @summary Get Domain Details
        
        @param request: DescDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.require_real_time_dns_records):
            query['RequireRealTimeDnsRecords'] = request.require_real_time_dns_records
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_domain(
        self,
        request: dm_20151123_models.DescDomainRequest,
    ) -> dm_20151123_models.DescDomainResponse:
        """
        @summary Get Domain Details
        
        @param request: DescDomainRequest
        @return: DescDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.desc_domain_with_options(request, runtime)

    async def desc_domain_async(
        self,
        request: dm_20151123_models.DescDomainRequest,
    ) -> dm_20151123_models.DescDomainResponse:
        """
        @summary Get Domain Details
        
        @param request: DescDomainRequest
        @return: DescDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.desc_domain_with_options_async(request, runtime)

    def desc_template_with_options(
        self,
        request: dm_20151123_models.DescTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescTemplateResponse:
        """
        @summary 查看模板信息
        
        @param request: DescTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescTemplate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_template_with_options_async(
        self,
        request: dm_20151123_models.DescTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescTemplateResponse:
        """
        @summary 查看模板信息
        
        @param request: DescTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescTemplate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.DescTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_template(
        self,
        request: dm_20151123_models.DescTemplateRequest,
    ) -> dm_20151123_models.DescTemplateResponse:
        """
        @summary 查看模板信息
        
        @param request: DescTemplateRequest
        @return: DescTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.desc_template_with_options(request, runtime)

    async def desc_template_async(
        self,
        request: dm_20151123_models.DescTemplateRequest,
    ) -> dm_20151123_models.DescTemplateResponse:
        """
        @summary 查看模板信息
        
        @param request: DescTemplateRequest
        @return: DescTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.desc_template_with_options_async(request, runtime)

    def get_dedicated_ip_warm_up_detail_with_options(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpDetailResponse:
        """
        @summary 获取专属ip的预热详情信息
        
        @param request: GetDedicatedIpWarmUpDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDedicatedIpWarmUpDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.end_day_mark):
            query['EndDayMark'] = request.end_day_mark
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.start_day_mark):
            query['StartDayMark'] = request.start_day_mark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedIpWarmUpDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetDedicatedIpWarmUpDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dedicated_ip_warm_up_detail_with_options_async(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpDetailResponse:
        """
        @summary 获取专属ip的预热详情信息
        
        @param request: GetDedicatedIpWarmUpDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDedicatedIpWarmUpDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.end_day_mark):
            query['EndDayMark'] = request.end_day_mark
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.start_day_mark):
            query['StartDayMark'] = request.start_day_mark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedIpWarmUpDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetDedicatedIpWarmUpDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dedicated_ip_warm_up_detail(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpDetailRequest,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpDetailResponse:
        """
        @summary 获取专属ip的预热详情信息
        
        @param request: GetDedicatedIpWarmUpDetailRequest
        @return: GetDedicatedIpWarmUpDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dedicated_ip_warm_up_detail_with_options(request, runtime)

    async def get_dedicated_ip_warm_up_detail_async(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpDetailRequest,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpDetailResponse:
        """
        @summary 获取专属ip的预热详情信息
        
        @param request: GetDedicatedIpWarmUpDetailRequest
        @return: GetDedicatedIpWarmUpDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dedicated_ip_warm_up_detail_with_options_async(request, runtime)

    def get_dedicated_ip_warm_up_info_with_options(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpInfoResponse:
        """
        @summary 获取专属ip的预热信息
        
        @param request: GetDedicatedIpWarmUpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDedicatedIpWarmUpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedIpWarmUpInfo',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetDedicatedIpWarmUpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dedicated_ip_warm_up_info_with_options_async(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpInfoResponse:
        """
        @summary 获取专属ip的预热信息
        
        @param request: GetDedicatedIpWarmUpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDedicatedIpWarmUpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedIpWarmUpInfo',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetDedicatedIpWarmUpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dedicated_ip_warm_up_info(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpInfoRequest,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpInfoResponse:
        """
        @summary 获取专属ip的预热信息
        
        @param request: GetDedicatedIpWarmUpInfoRequest
        @return: GetDedicatedIpWarmUpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dedicated_ip_warm_up_info_with_options(request, runtime)

    async def get_dedicated_ip_warm_up_info_async(
        self,
        request: dm_20151123_models.GetDedicatedIpWarmUpInfoRequest,
    ) -> dm_20151123_models.GetDedicatedIpWarmUpInfoResponse:
        """
        @summary 获取专属ip的预热信息
        
        @param request: GetDedicatedIpWarmUpInfoRequest
        @return: GetDedicatedIpWarmUpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dedicated_ip_warm_up_info_with_options_async(request, runtime)

    def get_ip_protection_with_options(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        """
        @summary Get IP Protection Information
        
        @param request: GetIpProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIpProtection',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetIpProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ip_protection_with_options_async(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        """
        @summary Get IP Protection Information
        
        @param request: GetIpProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIpProtection',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetIpProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ip_protection(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        """
        @summary Get IP Protection Information
        
        @param request: GetIpProtectionRequest
        @return: GetIpProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ip_protection_with_options(request, runtime)

    async def get_ip_protection_async(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        """
        @summary Get IP Protection Information
        
        @param request: GetIpProtectionRequest
        @return: GetIpProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_protection_with_options_async(request, runtime)

    def get_ipfilter_list_with_options(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        """
        @summary Retrieve IP Protection Information
        
        @param request: GetIpfilterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpfilterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIpfilterList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetIpfilterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipfilter_list_with_options_async(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        """
        @summary Retrieve IP Protection Information
        
        @param request: GetIpfilterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpfilterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIpfilterList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetIpfilterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipfilter_list(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        """
        @summary Retrieve IP Protection Information
        
        @param request: GetIpfilterListRequest
        @return: GetIpfilterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ipfilter_list_with_options(request, runtime)

    async def get_ipfilter_list_async(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        """
        @summary Retrieve IP Protection Information
        
        @param request: GetIpfilterListRequest
        @return: GetIpfilterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ipfilter_list_with_options_async(request, runtime)

    def get_suppression_list_level_with_options(
        self,
        request: dm_20151123_models.GetSuppressionListLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetSuppressionListLevelResponse:
        """
        @summary 获取用户无效地址级别配置
        
        @param request: GetSuppressionListLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuppressionListLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetSuppressionListLevel',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetSuppressionListLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_suppression_list_level_with_options_async(
        self,
        request: dm_20151123_models.GetSuppressionListLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetSuppressionListLevelResponse:
        """
        @summary 获取用户无效地址级别配置
        
        @param request: GetSuppressionListLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuppressionListLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='GetSuppressionListLevel',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetSuppressionListLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_suppression_list_level(
        self,
        request: dm_20151123_models.GetSuppressionListLevelRequest,
    ) -> dm_20151123_models.GetSuppressionListLevelResponse:
        """
        @summary 获取用户无效地址级别配置
        
        @param request: GetSuppressionListLevelRequest
        @return: GetSuppressionListLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_suppression_list_level_with_options(request, runtime)

    async def get_suppression_list_level_async(
        self,
        request: dm_20151123_models.GetSuppressionListLevelRequest,
    ) -> dm_20151123_models.GetSuppressionListLevelResponse:
        """
        @summary 获取用户无效地址级别配置
        
        @param request: GetSuppressionListLevelRequest
        @return: GetSuppressionListLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_suppression_list_level_with_options_async(request, runtime)

    def get_track_list_with_options(
        self,
        request: dm_20151123_models.GetTrackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListResponse:
        """
        @summary Get tracking information
        
        @param request: GetTrackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrackList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetTrackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_track_list_with_options_async(
        self,
        request: dm_20151123_models.GetTrackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListResponse:
        """
        @summary Get tracking information
        
        @param request: GetTrackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrackList',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetTrackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_track_list(
        self,
        request: dm_20151123_models.GetTrackListRequest,
    ) -> dm_20151123_models.GetTrackListResponse:
        """
        @summary Get tracking information
        
        @param request: GetTrackListRequest
        @return: GetTrackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_track_list_with_options(request, runtime)

    async def get_track_list_async(
        self,
        request: dm_20151123_models.GetTrackListRequest,
    ) -> dm_20151123_models.GetTrackListResponse:
        """
        @summary Get tracking information
        
        @param request: GetTrackListRequest
        @return: GetTrackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_track_list_with_options_async(request, runtime)

    def get_track_list_by_mail_from_and_tag_name_with_options(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        """
        @summary Get tracking information based on the sender address and tag name
        
        @param request: GetTrackListByMailFromAndTagNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrackListByMailFromAndTagNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrackListByMailFromAndTagName',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetTrackListByMailFromAndTagNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_track_list_by_mail_from_and_tag_name_with_options_async(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        """
        @summary Get tracking information based on the sender address and tag name
        
        @param request: GetTrackListByMailFromAndTagNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrackListByMailFromAndTagNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrackListByMailFromAndTagName',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetTrackListByMailFromAndTagNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_track_list_by_mail_from_and_tag_name(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        """
        @summary Get tracking information based on the sender address and tag name
        
        @param request: GetTrackListByMailFromAndTagNameRequest
        @return: GetTrackListByMailFromAndTagNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_track_list_by_mail_from_and_tag_name_with_options(request, runtime)

    async def get_track_list_by_mail_from_and_tag_name_async(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        """
        @summary Get tracking information based on the sender address and tag name
        
        @param request: GetTrackListByMailFromAndTagNameRequest
        @return: GetTrackListByMailFromAndTagNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_track_list_by_mail_from_and_tag_name_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetUserResponse:
        """
        @summary Get Account Details
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUser',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetUserResponse:
        """
        @summary Get Account Details
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUser',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(self) -> dm_20151123_models.GetUserResponse:
        """
        @summary Get Account Details
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(runtime)

    async def get_user_async(self) -> dm_20151123_models.GetUserResponse:
        """
        @summary Get Account Details
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(runtime)

    def get_validate_file_with_options(
        self,
        request: dm_20151123_models.GetValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidateFileResponse:
        """
        @summary 获取批量校验任务的结果文件
        
        @param request: GetValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validate_file_with_options_async(
        self,
        request: dm_20151123_models.GetValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidateFileResponse:
        """
        @summary 获取批量校验任务的结果文件
        
        @param request: GetValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validate_file(
        self,
        request: dm_20151123_models.GetValidateFileRequest,
    ) -> dm_20151123_models.GetValidateFileResponse:
        """
        @summary 获取批量校验任务的结果文件
        
        @param request: GetValidateFileRequest
        @return: GetValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_validate_file_with_options(request, runtime)

    async def get_validate_file_async(
        self,
        request: dm_20151123_models.GetValidateFileRequest,
    ) -> dm_20151123_models.GetValidateFileResponse:
        """
        @summary 获取批量校验任务的结果文件
        
        @param request: GetValidateFileRequest
        @return: GetValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_validate_file_with_options_async(request, runtime)

    def get_validate_file_status_with_options(
        self,
        request: dm_20151123_models.GetValidateFileStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidateFileStatusResponse:
        """
        @summary 获取批量校验任务的状态
        
        @param request: GetValidateFileStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidateFileStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidateFileStatus',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidateFileStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validate_file_status_with_options_async(
        self,
        request: dm_20151123_models.GetValidateFileStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidateFileStatusResponse:
        """
        @summary 获取批量校验任务的状态
        
        @param request: GetValidateFileStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidateFileStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidateFileStatus',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidateFileStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validate_file_status(
        self,
        request: dm_20151123_models.GetValidateFileStatusRequest,
    ) -> dm_20151123_models.GetValidateFileStatusResponse:
        """
        @summary 获取批量校验任务的状态
        
        @param request: GetValidateFileStatusRequest
        @return: GetValidateFileStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_validate_file_status_with_options(request, runtime)

    async def get_validate_file_status_async(
        self,
        request: dm_20151123_models.GetValidateFileStatusRequest,
    ) -> dm_20151123_models.GetValidateFileStatusResponse:
        """
        @summary 获取批量校验任务的状态
        
        @param request: GetValidateFileStatusRequest
        @return: GetValidateFileStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_validate_file_status_with_options_async(request, runtime)

    def get_validation_quota_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidationQuotaResponse:
        """
        @summary 获取电子邮件校验额度
        
        @param request: GetValidationQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidationQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetValidationQuota',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidationQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validation_quota_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetValidationQuotaResponse:
        """
        @summary 获取电子邮件校验额度
        
        @param request: GetValidationQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetValidationQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetValidationQuota',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.GetValidationQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validation_quota(self) -> dm_20151123_models.GetValidationQuotaResponse:
        """
        @summary 获取电子邮件校验额度
        
        @return: GetValidationQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_validation_quota_with_options(runtime)

    async def get_validation_quota_async(self) -> dm_20151123_models.GetValidationQuotaResponse:
        """
        @summary 获取电子邮件校验额度
        
        @return: GetValidationQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_validation_quota_with_options_async(runtime)

    def list_block_sending_with_options(
        self,
        request: dm_20151123_models.ListBlockSendingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ListBlockSendingResponse:
        """
        @summary 获取发信的黑名单列表
        
        @param request: ListBlockSendingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBlockSendingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.block_email):
            query['BlockEmail'] = request.block_email
        if not UtilClient.is_unset(request.block_type):
            query['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBlockSending',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ListBlockSendingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_block_sending_with_options_async(
        self,
        request: dm_20151123_models.ListBlockSendingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ListBlockSendingResponse:
        """
        @summary 获取发信的黑名单列表
        
        @param request: ListBlockSendingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBlockSendingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.block_email):
            query['BlockEmail'] = request.block_email
        if not UtilClient.is_unset(request.block_type):
            query['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBlockSending',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ListBlockSendingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_block_sending(
        self,
        request: dm_20151123_models.ListBlockSendingRequest,
    ) -> dm_20151123_models.ListBlockSendingResponse:
        """
        @summary 获取发信的黑名单列表
        
        @param request: ListBlockSendingRequest
        @return: ListBlockSendingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_block_sending_with_options(request, runtime)

    async def list_block_sending_async(
        self,
        request: dm_20151123_models.ListBlockSendingRequest,
    ) -> dm_20151123_models.ListBlockSendingResponse:
        """
        @summary 获取发信的黑名单列表
        
        @param request: ListBlockSendingRequest
        @return: ListBlockSendingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_block_sending_with_options_async(request, runtime)

    def list_user_suppression_with_options(
        self,
        request: dm_20151123_models.ListUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ListUserSuppressionResponse:
        """
        @summary List User Invalid Addresses.
        
        @param request: ListUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.end_bounce_time):
            query['EndBounceTime'] = request.end_bounce_time
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
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
        if not UtilClient.is_unset(request.start_bounce_time):
            query['StartBounceTime'] = request.start_bounce_time
        if not UtilClient.is_unset(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ListUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_suppression_with_options_async(
        self,
        request: dm_20151123_models.ListUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ListUserSuppressionResponse:
        """
        @summary List User Invalid Addresses.
        
        @param request: ListUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.end_bounce_time):
            query['EndBounceTime'] = request.end_bounce_time
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
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
        if not UtilClient.is_unset(request.start_bounce_time):
            query['StartBounceTime'] = request.start_bounce_time
        if not UtilClient.is_unset(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ListUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_suppression(
        self,
        request: dm_20151123_models.ListUserSuppressionRequest,
    ) -> dm_20151123_models.ListUserSuppressionResponse:
        """
        @summary List User Invalid Addresses.
        
        @param request: ListUserSuppressionRequest
        @return: ListUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_suppression_with_options(request, runtime)

    async def list_user_suppression_async(
        self,
        request: dm_20151123_models.ListUserSuppressionRequest,
    ) -> dm_20151123_models.ListUserSuppressionResponse:
        """
        @summary List User Invalid Addresses.
        
        @param request: ListUserSuppressionRequest
        @return: ListUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_suppression_with_options_async(request, runtime)

    def modify_mail_address_with_options(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        """
        @summary Modify the sending address
        
        @param request: ModifyMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mail_address_with_options_async(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        """
        @summary Modify the sending address
        
        @param request: ModifyMailAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMailAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMailAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mail_address(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        """
        @summary Modify the sending address
        
        @param request: ModifyMailAddressRequest
        @return: ModifyMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_mail_address_with_options(request, runtime)

    async def modify_mail_address_async(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        """
        @summary Modify the sending address
        
        @param request: ModifyMailAddressRequest
        @return: ModifyMailAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_mail_address_with_options_async(request, runtime)

    def modify_pwby_domain_with_options(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        """
        @summary Modify the domain-level password
        
        @param request: ModifyPWByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPWByDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPWByDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyPWByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pwby_domain_with_options_async(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        """
        @summary Modify the domain-level password
        
        @param request: ModifyPWByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPWByDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPWByDomain',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyPWByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pwby_domain(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        """
        @summary Modify the domain-level password
        
        @param request: ModifyPWByDomainRequest
        @return: ModifyPWByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_pwby_domain_with_options(request, runtime)

    async def modify_pwby_domain_async(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        """
        @summary Modify the domain-level password
        
        @param request: ModifyPWByDomainRequest
        @return: ModifyPWByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_pwby_domain_with_options_async(request, runtime)

    def modify_tag_with_options(
        self,
        request: dm_20151123_models.ModifyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTagResponse:
        """
        @summary Modify Tag
        
        @param request: ModifyTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tag_with_options_async(
        self,
        request: dm_20151123_models.ModifyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTagResponse:
        """
        @summary Modify Tag
        
        @param request: ModifyTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTag',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ModifyTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tag(
        self,
        request: dm_20151123_models.ModifyTagRequest,
    ) -> dm_20151123_models.ModifyTagResponse:
        """
        @summary Modify Tag
        
        @param request: ModifyTagRequest
        @return: ModifyTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_options(request, runtime)

    async def modify_tag_async(
        self,
        request: dm_20151123_models.ModifyTagRequest,
    ) -> dm_20151123_models.ModifyTagResponse:
        """
        @summary Modify Tag
        
        @param request: ModifyTagRequest
        @return: ModifyTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_with_options_async(request, runtime)

    def query_domain_by_param_with_options(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        """
        @summary Query domain information
        
        @param request: QueryDomainByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryDomainByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        """
        @summary Query domain information
        
        @param request: QueryDomainByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryDomainByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_param(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        """
        @summary Query domain information
        
        @param request: QueryDomainByParamRequest
        @return: QueryDomainByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_param_with_options(request, runtime)

    async def query_domain_by_param_async(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        """
        @summary Query domain information
        
        @param request: QueryDomainByParamRequest
        @return: QueryDomainByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_param_with_options_async(request, runtime)

    def query_invalid_address_with_options(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        """
        @summary NextStart changed to string
        
        @description Retrieve deduplicated invalid address information. If an email is sent to the same invalid address multiple times, only the first occurrence will be recorded. The query should be based on the time when the address was first classified as invalid.
        
        @param request: QueryInvalidAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInvalidAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvalidAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryInvalidAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_invalid_address_with_options_async(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        """
        @summary NextStart changed to string
        
        @description Retrieve deduplicated invalid address information. If an email is sent to the same invalid address multiple times, only the first occurrence will be recorded. The query should be based on the time when the address was first classified as invalid.
        
        @param request: QueryInvalidAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInvalidAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvalidAddress',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryInvalidAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_invalid_address(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        """
        @summary NextStart changed to string
        
        @description Retrieve deduplicated invalid address information. If an email is sent to the same invalid address multiple times, only the first occurrence will be recorded. The query should be based on the time when the address was first classified as invalid.
        
        @param request: QueryInvalidAddressRequest
        @return: QueryInvalidAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_invalid_address_with_options(request, runtime)

    async def query_invalid_address_async(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        """
        @summary NextStart changed to string
        
        @description Retrieve deduplicated invalid address information. If an email is sent to the same invalid address multiple times, only the first occurrence will be recorded. The query should be based on the time when the address was first classified as invalid.
        
        @param request: QueryInvalidAddressRequest
        @return: QueryInvalidAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_invalid_address_with_options_async(request, runtime)

    def query_mail_address_by_param_with_options(
        self,
        request: dm_20151123_models.QueryMailAddressByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryMailAddressByParamResponse:
        """
        @summary Query the list of sending addresses.
        
        @param request: QueryMailAddressByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMailAddressByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMailAddressByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryMailAddressByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mail_address_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryMailAddressByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryMailAddressByParamResponse:
        """
        @summary Query the list of sending addresses.
        
        @param request: QueryMailAddressByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMailAddressByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMailAddressByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryMailAddressByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mail_address_by_param(
        self,
        request: dm_20151123_models.QueryMailAddressByParamRequest,
    ) -> dm_20151123_models.QueryMailAddressByParamResponse:
        """
        @summary Query the list of sending addresses.
        
        @param request: QueryMailAddressByParamRequest
        @return: QueryMailAddressByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mail_address_by_param_with_options(request, runtime)

    async def query_mail_address_by_param_async(
        self,
        request: dm_20151123_models.QueryMailAddressByParamRequest,
    ) -> dm_20151123_models.QueryMailAddressByParamResponse:
        """
        @summary Query the list of sending addresses.
        
        @param request: QueryMailAddressByParamRequest
        @return: QueryMailAddressByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mail_address_by_param_with_options_async(request, runtime)

    def query_receiver_by_param_with_options(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        """
        @summary Query the details of the recipient list
        
        @param request: QueryReceiverByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReceiverByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryReceiverByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_receiver_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        """
        @summary Query the details of the recipient list
        
        @param request: QueryReceiverByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReceiverByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryReceiverByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_receiver_by_param(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        """
        @summary Query the details of the recipient list
        
        @param request: QueryReceiverByParamRequest
        @return: QueryReceiverByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_by_param_with_options(request, runtime)

    async def query_receiver_by_param_async(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        """
        @summary Query the details of the recipient list
        
        @param request: QueryReceiverByParamRequest
        @return: QueryReceiverByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_receiver_by_param_with_options_async(request, runtime)

    def query_receiver_detail_with_options(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        """
        @summary Retrieve detailed information about a recipient list
        
        @param request: QueryReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        """
        @summary Retrieve detailed information about a recipient list
        
        @param request: QueryReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_receiver_detail(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        """
        @summary Retrieve detailed information about a recipient list
        
        @param request: QueryReceiverDetailRequest
        @return: QueryReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_detail_with_options(request, runtime)

    async def query_receiver_detail_async(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        """
        @summary Retrieve detailed information about a recipient list
        
        @param request: QueryReceiverDetailRequest
        @return: QueryReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_receiver_detail_with_options_async(request, runtime)

    def query_tag_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        """
        @summary Call QueryTagByParam to retrieve tags.
        
        @param request: QueryTagByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
            action='QueryTagByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTagByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        """
        @summary Call QueryTagByParam to retrieve tags.
        
        @param request: QueryTagByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
            action='QueryTagByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTagByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_by_param(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        """
        @summary Call QueryTagByParam to retrieve tags.
        
        @param request: QueryTagByParamRequest
        @return: QueryTagByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tag_by_param_with_options(request, runtime)

    async def query_tag_by_param_async(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        """
        @summary Call QueryTagByParam to retrieve tags.
        
        @param request: QueryTagByParamRequest
        @return: QueryTagByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_by_param_with_options_async(request, runtime)

    def query_task_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        """
        @summary Query task list
        
        @param request: QueryTaskByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTaskByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        """
        @summary Query task list
        
        @param request: QueryTaskByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTaskByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_by_param(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        """
        @summary Query task list
        
        @param request: QueryTaskByParamRequest
        @return: QueryTaskByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_by_param_with_options(request, runtime)

    async def query_task_by_param_async(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        """
        @summary Query task list
        
        @param request: QueryTaskByParamRequest
        @return: QueryTaskByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_by_param_with_options_async(request, runtime)

    def query_template_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        """
        @summary 查询模板信息
        
        @param request: QueryTemplateByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTemplateByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTemplateByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_template_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        """
        @summary 查询模板信息
        
        @param request: QueryTemplateByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTemplateByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.QueryTemplateByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_template_by_param(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        """
        @summary 查询模板信息
        
        @param request: QueryTemplateByParamRequest
        @return: QueryTemplateByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_template_by_param_with_options(request, runtime)

    async def query_template_by_param_async(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        """
        @summary 查询模板信息
        
        @param request: QueryTemplateByParamRequest
        @return: QueryTemplateByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_template_by_param_with_options_async(request, runtime)

    def remove_user_suppression_with_options(
        self,
        request: dm_20151123_models.RemoveUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.RemoveUserSuppressionResponse:
        """
        @summary 删除用户无效地址
        
        @param request: RemoveUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suppression_ids):
            query['SuppressionIds'] = request.suppression_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.RemoveUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_suppression_with_options_async(
        self,
        request: dm_20151123_models.RemoveUserSuppressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.RemoveUserSuppressionResponse:
        """
        @summary 删除用户无效地址
        
        @param request: RemoveUserSuppressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserSuppressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suppression_ids):
            query['SuppressionIds'] = request.suppression_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserSuppression',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.RemoveUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_suppression(
        self,
        request: dm_20151123_models.RemoveUserSuppressionRequest,
    ) -> dm_20151123_models.RemoveUserSuppressionResponse:
        """
        @summary 删除用户无效地址
        
        @param request: RemoveUserSuppressionRequest
        @return: RemoveUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_user_suppression_with_options(request, runtime)

    async def remove_user_suppression_async(
        self,
        request: dm_20151123_models.RemoveUserSuppressionRequest,
    ) -> dm_20151123_models.RemoveUserSuppressionResponse:
        """
        @summary 删除用户无效地址
        
        @param request: RemoveUserSuppressionRequest
        @return: RemoveUserSuppressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_suppression_with_options_async(request, runtime)

    def save_receiver_detail_with_options(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        """
        @summary Create a Single Recipient
        
        @param request: SaveReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_detail):
            query['CustomDetail'] = request.custom_detail
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SaveReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        """
        @summary Create a Single Recipient
        
        @param request: SaveReceiverDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveReceiverDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_detail):
            query['CustomDetail'] = request.custom_detail
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveReceiverDetail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SaveReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_receiver_detail(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        """
        @summary Create a Single Recipient
        
        @param request: SaveReceiverDetailRequest
        @return: SaveReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_receiver_detail_with_options(request, runtime)

    async def save_receiver_detail_async(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        """
        @summary Create a Single Recipient
        
        @param request: SaveReceiverDetailRequest
        @return: SaveReceiverDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_receiver_detail_with_options_async(request, runtime)

    def send_test_by_template_with_options(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        """
        @summary Send Template Test Email
        
        @param request: SendTestByTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTestByTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.birthday):
            query['Birthday'] = request.birthday
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            query['TemplateParams'] = request.template_params
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendTestByTemplate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SendTestByTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_test_by_template_with_options_async(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        """
        @summary Send Template Test Email
        
        @param request: SendTestByTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTestByTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.birthday):
            query['Birthday'] = request.birthday
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            query['TemplateParams'] = request.template_params
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendTestByTemplate',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SendTestByTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_test_by_template(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        """
        @summary Send Template Test Email
        
        @param request: SendTestByTemplateRequest
        @return: SendTestByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_test_by_template_with_options(request, runtime)

    async def send_test_by_template_async(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        """
        @summary Send Template Test Email
        
        @param request: SendTestByTemplateRequest
        @return: SendTestByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_test_by_template_with_options_async(request, runtime)

    def send_validate_file_with_options(
        self,
        request: dm_20151123_models.SendValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendValidateFileResponse:
        """
        @summary 提交批量校验任务
        
        @param request: SendValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_column):
            query['AddressColumn'] = request.address_column
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.has_header_row):
            query['HasHeaderRow'] = request.has_header_row
        if not UtilClient.is_unset(request.remove_duplicate):
            query['RemoveDuplicate'] = request.remove_duplicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SendValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_validate_file_with_options_async(
        self,
        request: dm_20151123_models.SendValidateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendValidateFileResponse:
        """
        @summary 提交批量校验任务
        
        @param request: SendValidateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendValidateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_column):
            query['AddressColumn'] = request.address_column
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.has_header_row):
            query['HasHeaderRow'] = request.has_header_row
        if not UtilClient.is_unset(request.remove_duplicate):
            query['RemoveDuplicate'] = request.remove_duplicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendValidateFile',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SendValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_validate_file(
        self,
        request: dm_20151123_models.SendValidateFileRequest,
    ) -> dm_20151123_models.SendValidateFileResponse:
        """
        @summary 提交批量校验任务
        
        @param request: SendValidateFileRequest
        @return: SendValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_validate_file_with_options(request, runtime)

    async def send_validate_file_async(
        self,
        request: dm_20151123_models.SendValidateFileRequest,
    ) -> dm_20151123_models.SendValidateFileResponse:
        """
        @summary 提交批量校验任务
        
        @param request: SendValidateFileRequest
        @return: SendValidateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_validate_file_with_options_async(request, runtime)

    def send_validate_file_advance(
        self,
        request: dm_20151123_models.SendValidateFileAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendValidateFileResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        send_validate_file_req = dm_20151123_models.SendValidateFileRequest()
        OpenApiUtilClient.convert(request, send_validate_file_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            send_validate_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        send_validate_file_resp = self.send_validate_file_with_options(send_validate_file_req, runtime)
        return send_validate_file_resp

    async def send_validate_file_advance_async(
        self,
        request: dm_20151123_models.SendValidateFileAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendValidateFileResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        send_validate_file_req = dm_20151123_models.SendValidateFileRequest()
        OpenApiUtilClient.convert(request, send_validate_file_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            send_validate_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        send_validate_file_resp = await self.send_validate_file_with_options_async(send_validate_file_req, runtime)
        return send_validate_file_resp

    def sender_statistics_by_tag_name_and_batch_idwith_options(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        """
        @summary Retrieve Sending Data under Specified Conditions
        
        @param request: SenderStatisticsByTagNameAndBatchIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SenderStatisticsByTagNameAndBatchIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsByTagNameAndBatchID',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def sender_statistics_by_tag_name_and_batch_idwith_options_async(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        """
        @summary Retrieve Sending Data under Specified Conditions
        
        @param request: SenderStatisticsByTagNameAndBatchIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SenderStatisticsByTagNameAndBatchIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not UtilClient.is_unset(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.esp):
            query['Esp'] = request.esp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsByTagNameAndBatchID',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sender_statistics_by_tag_name_and_batch_id(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        """
        @summary Retrieve Sending Data under Specified Conditions
        
        @param request: SenderStatisticsByTagNameAndBatchIDRequest
        @return: SenderStatisticsByTagNameAndBatchIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_by_tag_name_and_batch_idwith_options(request, runtime)

    async def sender_statistics_by_tag_name_and_batch_id_async(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        """
        @summary Retrieve Sending Data under Specified Conditions
        
        @param request: SenderStatisticsByTagNameAndBatchIDRequest
        @return: SenderStatisticsByTagNameAndBatchIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sender_statistics_by_tag_name_and_batch_idwith_options_async(request, runtime)

    def sender_statistics_detail_by_param_with_options(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        """
        @summary Query Delivery Result Details
        
        @param request: SenderStatisticsDetailByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SenderStatisticsDetailByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsDetailByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SenderStatisticsDetailByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def sender_statistics_detail_by_param_with_options_async(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        """
        @summary Query Delivery Result Details
        
        @param request: SenderStatisticsDetailByParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SenderStatisticsDetailByParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsDetailByParam',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SenderStatisticsDetailByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sender_statistics_detail_by_param(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        """
        @summary Query Delivery Result Details
        
        @param request: SenderStatisticsDetailByParamRequest
        @return: SenderStatisticsDetailByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_detail_by_param_with_options(request, runtime)

    async def sender_statistics_detail_by_param_async(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        """
        @summary Query Delivery Result Details
        
        @param request: SenderStatisticsDetailByParamRequest
        @return: SenderStatisticsDetailByParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sender_statistics_detail_by_param_with_options_async(request, runtime)

    def set_suppression_list_level_with_options(
        self,
        request: dm_20151123_models.SetSuppressionListLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SetSuppressionListLevelResponse:
        """
        @summary 设置用户无效地址级别配置
        
        @param request: SetSuppressionListLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSuppressionListLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suppression_list_level):
            query['SuppressionListLevel'] = request.suppression_list_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSuppressionListLevel',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SetSuppressionListLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_suppression_list_level_with_options_async(
        self,
        request: dm_20151123_models.SetSuppressionListLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SetSuppressionListLevelResponse:
        """
        @summary 设置用户无效地址级别配置
        
        @param request: SetSuppressionListLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSuppressionListLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suppression_list_level):
            query['SuppressionListLevel'] = request.suppression_list_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSuppressionListLevel',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SetSuppressionListLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_suppression_list_level(
        self,
        request: dm_20151123_models.SetSuppressionListLevelRequest,
    ) -> dm_20151123_models.SetSuppressionListLevelResponse:
        """
        @summary 设置用户无效地址级别配置
        
        @param request: SetSuppressionListLevelRequest
        @return: SetSuppressionListLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_suppression_list_level_with_options(request, runtime)

    async def set_suppression_list_level_async(
        self,
        request: dm_20151123_models.SetSuppressionListLevelRequest,
    ) -> dm_20151123_models.SetSuppressionListLevelResponse:
        """
        @summary 设置用户无效地址级别配置
        
        @param request: SetSuppressionListLevelRequest
        @return: SetSuppressionListLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_suppression_list_level_with_options_async(request, runtime)

    def single_send_mail_with_options(
        self,
        tmp_req: dm_20151123_models.SingleSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        """
        @summary API for Sending Emails
        
        @param tmp_req: SingleSendMailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SingleSendMailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dm_20151123_models.SingleSendMailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.attachments):
            body['Attachments'] = request.attachments
        if not UtilClient.is_unset(request.click_trace):
            body['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.from_alias):
            body['FromAlias'] = request.from_alias
        if not UtilClient.is_unset(request.headers):
            body['Headers'] = request.headers
        if not UtilClient.is_unset(request.html_body):
            body['HtmlBody'] = request.html_body
        if not UtilClient.is_unset(request.ip_pool_id):
            body['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.reply_address):
            body['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            body['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.reply_to_address):
            body['ReplyToAddress'] = request.reply_to_address
        if not UtilClient.is_unset(request.subject):
            body['Subject'] = request.subject
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.template_shrink):
            body['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.text_body):
            body['TextBody'] = request.text_body
        if not UtilClient.is_unset(request.to_address):
            body['ToAddress'] = request.to_address
        if not UtilClient.is_unset(request.un_subscribe_filter_level):
            body['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not UtilClient.is_unset(request.un_subscribe_link_type):
            body['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SingleSendMail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SingleSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_send_mail_with_options_async(
        self,
        tmp_req: dm_20151123_models.SingleSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        """
        @summary API for Sending Emails
        
        @param tmp_req: SingleSendMailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SingleSendMailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dm_20151123_models.SingleSendMailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.attachments):
            body['Attachments'] = request.attachments
        if not UtilClient.is_unset(request.click_trace):
            body['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.from_alias):
            body['FromAlias'] = request.from_alias
        if not UtilClient.is_unset(request.headers):
            body['Headers'] = request.headers
        if not UtilClient.is_unset(request.html_body):
            body['HtmlBody'] = request.html_body
        if not UtilClient.is_unset(request.ip_pool_id):
            body['IpPoolId'] = request.ip_pool_id
        if not UtilClient.is_unset(request.reply_address):
            body['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            body['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.reply_to_address):
            body['ReplyToAddress'] = request.reply_to_address
        if not UtilClient.is_unset(request.subject):
            body['Subject'] = request.subject
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.template_shrink):
            body['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.text_body):
            body['TextBody'] = request.text_body
        if not UtilClient.is_unset(request.to_address):
            body['ToAddress'] = request.to_address
        if not UtilClient.is_unset(request.un_subscribe_filter_level):
            body['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not UtilClient.is_unset(request.un_subscribe_link_type):
            body['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SingleSendMail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.SingleSendMailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_send_mail(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
    ) -> dm_20151123_models.SingleSendMailResponse:
        """
        @summary API for Sending Emails
        
        @param request: SingleSendMailRequest
        @return: SingleSendMailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.single_send_mail_with_options(request, runtime)

    async def single_send_mail_async(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
    ) -> dm_20151123_models.SingleSendMailResponse:
        """
        @summary API for Sending Emails
        
        @param request: SingleSendMailRequest
        @return: SingleSendMailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.single_send_mail_with_options_async(request, runtime)

    def single_send_mail_advance(
        self,
        request: dm_20151123_models.SingleSendMailAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        single_send_mail_req = dm_20151123_models.SingleSendMailRequest()
        OpenApiUtilClient.convert(request, single_send_mail_req)
        if not UtilClient.is_unset(request.attachments):
            i_0 = 0
            for item_0 in request.attachments:
                if not UtilClient.is_unset(item_0.attachment_url_object):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.attachment_url_object,
                        content_type=''
                    )
                    oss_header = {
                        'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                        'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                        'policy': auth_response_body.get('EncodedPolicy'),
                        'Signature': auth_response_body.get('Signature'),
                        'key': auth_response_body.get('ObjectKey'),
                        'file': file_obj,
                        'success_action_status': '201'
                    }
                    self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
                    tmp = single_send_mail_req.attachments[i_0]
                    tmp.attachment_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        single_send_mail_resp = self.single_send_mail_with_options(single_send_mail_req, runtime)
        return single_send_mail_resp

    async def single_send_mail_advance_async(
        self,
        request: dm_20151123_models.SingleSendMailAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        single_send_mail_req = dm_20151123_models.SingleSendMailRequest()
        OpenApiUtilClient.convert(request, single_send_mail_req)
        if not UtilClient.is_unset(request.attachments):
            i_0 = 0
            for item_0 in request.attachments:
                if not UtilClient.is_unset(item_0.attachment_url_object):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.attachment_url_object,
                        content_type=''
                    )
                    oss_header = {
                        'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                        'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                        'policy': auth_response_body.get('EncodedPolicy'),
                        'Signature': auth_response_body.get('Signature'),
                        'key': auth_response_body.get('ObjectKey'),
                        'file': file_obj,
                        'success_action_status': '201'
                    }
                    await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
                    tmp = single_send_mail_req.attachments[i_0]
                    tmp.attachment_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        single_send_mail_resp = await self.single_send_mail_with_options_async(single_send_mail_req, runtime)
        return single_send_mail_resp

    def unblock_sending_with_options(
        self,
        request: dm_20151123_models.UnblockSendingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UnblockSendingResponse:
        """
        @summary Lift sending restrictions due to unsubscription, reporting, etc.
        
        @param request: UnblockSendingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnblockSendingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_email):
            query['BlockEmail'] = request.block_email
        if not UtilClient.is_unset(request.block_type):
            query['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnblockSending',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UnblockSendingResponse(),
            self.call_api(params, req, runtime)
        )

    async def unblock_sending_with_options_async(
        self,
        request: dm_20151123_models.UnblockSendingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UnblockSendingResponse:
        """
        @summary Lift sending restrictions due to unsubscription, reporting, etc.
        
        @param request: UnblockSendingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnblockSendingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_email):
            query['BlockEmail'] = request.block_email
        if not UtilClient.is_unset(request.block_type):
            query['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnblockSending',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UnblockSendingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unblock_sending(
        self,
        request: dm_20151123_models.UnblockSendingRequest,
    ) -> dm_20151123_models.UnblockSendingResponse:
        """
        @summary Lift sending restrictions due to unsubscription, reporting, etc.
        
        @param request: UnblockSendingRequest
        @return: UnblockSendingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unblock_sending_with_options(request, runtime)

    async def unblock_sending_async(
        self,
        request: dm_20151123_models.UnblockSendingRequest,
    ) -> dm_20151123_models.UnblockSendingResponse:
        """
        @summary Lift sending restrictions due to unsubscription, reporting, etc.
        
        @param request: UnblockSendingRequest
        @return: UnblockSendingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unblock_sending_with_options_async(request, runtime)

    def update_ip_protection_with_options(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        """
        @summary Update IP Protection API
        
        @param request: UpdateIpProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protection):
            query['IpProtection'] = request.ip_protection
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
            action='UpdateIpProtection',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UpdateIpProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ip_protection_with_options_async(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        """
        @summary Update IP Protection API
        
        @param request: UpdateIpProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protection):
            query['IpProtection'] = request.ip_protection
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
            action='UpdateIpProtection',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UpdateIpProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ip_protection(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        """
        @summary Update IP Protection API
        
        @param request: UpdateIpProtectionRequest
        @return: UpdateIpProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ip_protection_with_options(request, runtime)

    async def update_ip_protection_async(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        """
        @summary Update IP Protection API
        
        @param request: UpdateIpProtectionRequest
        @return: UpdateIpProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_protection_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        tmp_req: dm_20151123_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateUserResponse:
        """
        @summary Update account information
        
        @param tmp_req: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dm_20151123_models.UpdateUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        body = {}
        if not UtilClient.is_unset(request.user_shrink):
            body['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        tmp_req: dm_20151123_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateUserResponse:
        """
        @summary Update account information
        
        @param tmp_req: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dm_20151123_models.UpdateUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        body = {}
        if not UtilClient.is_unset(request.user_shrink):
            body['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: dm_20151123_models.UpdateUserRequest,
    ) -> dm_20151123_models.UpdateUserResponse:
        """
        @summary Update account information
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: dm_20151123_models.UpdateUserRequest,
    ) -> dm_20151123_models.UpdateUserResponse:
        """
        @summary Update account information
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def validate_email_with_options(
        self,
        request: dm_20151123_models.ValidateEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ValidateEmailResponse:
        """
        @summary 校验电子邮件地址
        
        @param request: ValidateEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateEmail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ValidateEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_email_with_options_async(
        self,
        request: dm_20151123_models.ValidateEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ValidateEmailResponse:
        """
        @summary 校验电子邮件地址
        
        @param request: ValidateEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateEmail',
            version='2015-11-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20151123_models.ValidateEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_email(
        self,
        request: dm_20151123_models.ValidateEmailRequest,
    ) -> dm_20151123_models.ValidateEmailResponse:
        """
        @summary 校验电子邮件地址
        
        @param request: ValidateEmailRequest
        @return: ValidateEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_email_with_options(request, runtime)

    async def validate_email_async(
        self,
        request: dm_20151123_models.ValidateEmailRequest,
    ) -> dm_20151123_models.ValidateEmailResponse:
        """
        @summary 校验电子邮件地址
        
        @param request: ValidateEmailRequest
        @return: ValidateEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_email_with_options_async(request, runtime)
