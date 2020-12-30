# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dm20151123 import models as dm_20151123_models
from alibabacloud_tea_util import models as util_models


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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.AddIpfilterResponse().from_map(
            self.do_rpcrequest('AddIpfilter', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_ipfilter_with_options_async(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.AddIpfilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.AddIpfilterResponse().from_map(
            await self.do_rpcrequest_async('AddIpfilter', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_ipfilter(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
    ) -> dm_20151123_models.AddIpfilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ipfilter_with_options(request, runtime)

    async def add_ipfilter_async(
        self,
        request: dm_20151123_models.AddIpfilterRequest,
    ) -> dm_20151123_models.AddIpfilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ipfilter_with_options_async(request, runtime)

    def approve_mail_template_with_options(
        self,
        request: dm_20151123_models.ApproveMailTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveMailTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveMailTemplateResponse().from_map(
            self.do_rpcrequest('ApproveMailTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_mail_template_with_options_async(
        self,
        request: dm_20151123_models.ApproveMailTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveMailTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveMailTemplateResponse().from_map(
            await self.do_rpcrequest_async('ApproveMailTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_mail_template(
        self,
        request: dm_20151123_models.ApproveMailTemplateRequest,
    ) -> dm_20151123_models.ApproveMailTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_mail_template_with_options(request, runtime)

    async def approve_mail_template_async(
        self,
        request: dm_20151123_models.ApproveMailTemplateRequest,
    ) -> dm_20151123_models.ApproveMailTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_mail_template_with_options_async(request, runtime)

    def approve_reply_mail_address_with_options(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveReplyMailAddressResponse().from_map(
            self.do_rpcrequest('ApproveReplyMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_reply_mail_address_with_options_async(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveReplyMailAddressResponse().from_map(
            await self.do_rpcrequest_async('ApproveReplyMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_reply_mail_address(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_reply_mail_address_with_options(request, runtime)

    async def approve_reply_mail_address_async(
        self,
        request: dm_20151123_models.ApproveReplyMailAddressRequest,
    ) -> dm_20151123_models.ApproveReplyMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_reply_mail_address_with_options_async(request, runtime)

    def approve_sms_template_with_options(
        self,
        request: dm_20151123_models.ApproveSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveSmsTemplateResponse().from_map(
            self.do_rpcrequest('ApproveSmsTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_sms_template_with_options_async(
        self,
        request: dm_20151123_models.ApproveSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveSmsTemplateResponse().from_map(
            await self.do_rpcrequest_async('ApproveSmsTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_sms_template(
        self,
        request: dm_20151123_models.ApproveSmsTemplateRequest,
    ) -> dm_20151123_models.ApproveSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_sms_template_with_options(request, runtime)

    async def approve_sms_template_async(
        self,
        request: dm_20151123_models.ApproveSmsTemplateRequest,
    ) -> dm_20151123_models.ApproveSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_sms_template_with_options_async(request, runtime)

    def approve_template_with_options(
        self,
        request: dm_20151123_models.ApproveTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveTemplateResponse().from_map(
            self.do_rpcrequest('ApproveTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_template_with_options_async(
        self,
        request: dm_20151123_models.ApproveTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ApproveTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ApproveTemplateResponse().from_map(
            await self.do_rpcrequest_async('ApproveTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_template(
        self,
        request: dm_20151123_models.ApproveTemplateRequest,
    ) -> dm_20151123_models.ApproveTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_template_with_options(request, runtime)

    async def approve_template_async(
        self,
        request: dm_20151123_models.ApproveTemplateRequest,
    ) -> dm_20151123_models.ApproveTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_template_with_options_async(request, runtime)

    def batch_send_mail_with_options(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.BatchSendMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.BatchSendMailResponse().from_map(
            self.do_rpcrequest('BatchSendMail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_send_mail_with_options_async(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.BatchSendMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.BatchSendMailResponse().from_map(
            await self.do_rpcrequest_async('BatchSendMail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_send_mail(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
    ) -> dm_20151123_models.BatchSendMailResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_send_mail_with_options(request, runtime)

    async def batch_send_mail_async(
        self,
        request: dm_20151123_models.BatchSendMailRequest,
    ) -> dm_20151123_models.BatchSendMailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_send_mail_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: dm_20151123_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckDomainResponse().from_map(
            self.do_rpcrequest('CheckDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: dm_20151123_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckDomainResponse().from_map(
            await self.do_rpcrequest_async('CheckDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_domain(
        self,
        request: dm_20151123_models.CheckDomainRequest,
    ) -> dm_20151123_models.CheckDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: dm_20151123_models.CheckDomainRequest,
    ) -> dm_20151123_models.CheckDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_invalid_address_with_options(
        self,
        request: dm_20151123_models.CheckInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckInvalidAddressResponse().from_map(
            self.do_rpcrequest('CheckInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_invalid_address_with_options_async(
        self,
        request: dm_20151123_models.CheckInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckInvalidAddressResponse().from_map(
            await self.do_rpcrequest_async('CheckInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_invalid_address(
        self,
        request: dm_20151123_models.CheckInvalidAddressRequest,
    ) -> dm_20151123_models.CheckInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_invalid_address_with_options(request, runtime)

    async def check_invalid_address_async(
        self,
        request: dm_20151123_models.CheckInvalidAddressRequest,
    ) -> dm_20151123_models.CheckInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_invalid_address_with_options_async(request, runtime)

    def check_reply_to_mail_address_with_options(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckReplyToMailAddressResponse().from_map(
            self.do_rpcrequest('CheckReplyToMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_reply_to_mail_address_with_options_async(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CheckReplyToMailAddressResponse().from_map(
            await self.do_rpcrequest_async('CheckReplyToMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_reply_to_mail_address(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_reply_to_mail_address_with_options(request, runtime)

    async def check_reply_to_mail_address_async(
        self,
        request: dm_20151123_models.CheckReplyToMailAddressRequest,
    ) -> dm_20151123_models.CheckReplyToMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_reply_to_mail_address_with_options_async(request, runtime)

    def create_dayu_with_options(
        self,
        request: dm_20151123_models.CreateDayuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDayuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateDayuResponse().from_map(
            self.do_rpcrequest('CreateDayu', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dayu_with_options_async(
        self,
        request: dm_20151123_models.CreateDayuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDayuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateDayuResponse().from_map(
            await self.do_rpcrequest_async('CreateDayu', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dayu(
        self,
        request: dm_20151123_models.CreateDayuRequest,
    ) -> dm_20151123_models.CreateDayuResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dayu_with_options(request, runtime)

    async def create_dayu_async(
        self,
        request: dm_20151123_models.CreateDayuRequest,
    ) -> dm_20151123_models.CreateDayuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dayu_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: dm_20151123_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateDomainResponse().from_map(
            self.do_rpcrequest('CreateDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: dm_20151123_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateDomainResponse().from_map(
            await self.do_rpcrequest_async('CreateDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain(
        self,
        request: dm_20151123_models.CreateDomainRequest,
    ) -> dm_20151123_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: dm_20151123_models.CreateDomainRequest,
    ) -> dm_20151123_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_mail_address_with_options(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateMailAddressResponse().from_map(
            self.do_rpcrequest('CreateMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mail_address_with_options_async(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateMailAddressResponse().from_map(
            await self.do_rpcrequest_async('CreateMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mail_address(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mail_address_with_options(request, runtime)

    async def create_mail_address_async(
        self,
        request: dm_20151123_models.CreateMailAddressRequest,
    ) -> dm_20151123_models.CreateMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mail_address_with_options_async(request, runtime)

    def create_receiver_with_options(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateReceiverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateReceiverResponse().from_map(
            self.do_rpcrequest('CreateReceiver', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_receiver_with_options_async(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateReceiverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateReceiverResponse().from_map(
            await self.do_rpcrequest_async('CreateReceiver', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_receiver(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
    ) -> dm_20151123_models.CreateReceiverResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_receiver_with_options(request, runtime)

    async def create_receiver_async(
        self,
        request: dm_20151123_models.CreateReceiverRequest,
    ) -> dm_20151123_models.CreateReceiverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_receiver_with_options_async(request, runtime)

    def create_sign_with_options(
        self,
        request: dm_20151123_models.CreateSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateSignResponse().from_map(
            self.do_rpcrequest('CreateSign', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sign_with_options_async(
        self,
        request: dm_20151123_models.CreateSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateSignResponse().from_map(
            await self.do_rpcrequest_async('CreateSign', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sign(
        self,
        request: dm_20151123_models.CreateSignRequest,
    ) -> dm_20151123_models.CreateSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sign_with_options(request, runtime)

    async def create_sign_async(
        self,
        request: dm_20151123_models.CreateSignRequest,
    ) -> dm_20151123_models.CreateSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sign_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: dm_20151123_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateTagResponse().from_map(
            self.do_rpcrequest('CreateTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: dm_20151123_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateTagResponse().from_map(
            await self.do_rpcrequest_async('CreateTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tag(
        self,
        request: dm_20151123_models.CreateTagRequest,
    ) -> dm_20151123_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: dm_20151123_models.CreateTagRequest,
    ) -> dm_20151123_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: dm_20151123_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateTemplateResponse().from_map(
            self.do_rpcrequest('CreateTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: dm_20151123_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.CreateTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(
        self,
        request: dm_20151123_models.CreateTemplateRequest,
    ) -> dm_20151123_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: dm_20151123_models.CreateTemplateRequest,
    ) -> dm_20151123_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteDomainResponse().from_map(
            self.do_rpcrequest('DeleteDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
    ) -> dm_20151123_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: dm_20151123_models.DeleteDomainRequest,
    ) -> dm_20151123_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_invalid_address_with_options(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteInvalidAddressResponse().from_map(
            self.do_rpcrequest('DeleteInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_invalid_address_with_options_async(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteInvalidAddressResponse().from_map(
            await self.do_rpcrequest_async('DeleteInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_invalid_address(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_invalid_address_with_options(request, runtime)

    async def delete_invalid_address_async(
        self,
        request: dm_20151123_models.DeleteInvalidAddressRequest,
    ) -> dm_20151123_models.DeleteInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_invalid_address_with_options_async(request, runtime)

    def delete_ipfilter_by_edm_id_with_options(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteIpfilterByEdmIdResponse().from_map(
            self.do_rpcrequest('DeleteIpfilterByEdmId', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipfilter_by_edm_id_with_options_async(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteIpfilterByEdmIdResponse().from_map(
            await self.do_rpcrequest_async('DeleteIpfilterByEdmId', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipfilter_by_edm_id(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipfilter_by_edm_id_with_options(request, runtime)

    async def delete_ipfilter_by_edm_id_async(
        self,
        request: dm_20151123_models.DeleteIpfilterByEdmIdRequest,
    ) -> dm_20151123_models.DeleteIpfilterByEdmIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipfilter_by_edm_id_with_options_async(request, runtime)

    def delete_mail_address_with_options(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteMailAddressResponse().from_map(
            self.do_rpcrequest('DeleteMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mail_address_with_options_async(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteMailAddressResponse().from_map(
            await self.do_rpcrequest_async('DeleteMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mail_address(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mail_address_with_options(request, runtime)

    async def delete_mail_address_async(
        self,
        request: dm_20151123_models.DeleteMailAddressRequest,
    ) -> dm_20151123_models.DeleteMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mail_address_with_options_async(request, runtime)

    def delete_receiver_with_options(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteReceiverResponse().from_map(
            self.do_rpcrequest('DeleteReceiver', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_receiver_with_options_async(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteReceiverResponse().from_map(
            await self.do_rpcrequest_async('DeleteReceiver', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_receiver(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_with_options(request, runtime)

    async def delete_receiver_async(
        self,
        request: dm_20151123_models.DeleteReceiverRequest,
    ) -> dm_20151123_models.DeleteReceiverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_receiver_with_options_async(request, runtime)

    def delete_receiver_detail_with_options(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteReceiverDetailResponse().from_map(
            self.do_rpcrequest('DeleteReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteReceiverDetailResponse().from_map(
            await self.do_rpcrequest_async('DeleteReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_receiver_detail(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_detail_with_options(request, runtime)

    async def delete_receiver_detail_async(
        self,
        request: dm_20151123_models.DeleteReceiverDetailRequest,
    ) -> dm_20151123_models.DeleteReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_receiver_detail_with_options_async(request, runtime)

    def delete_sign_with_options(
        self,
        request: dm_20151123_models.DeleteSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteSignResponse().from_map(
            self.do_rpcrequest('DeleteSign', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sign_with_options_async(
        self,
        request: dm_20151123_models.DeleteSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteSignResponse().from_map(
            await self.do_rpcrequest_async('DeleteSign', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sign(
        self,
        request: dm_20151123_models.DeleteSignRequest,
    ) -> dm_20151123_models.DeleteSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sign_with_options(request, runtime)

    async def delete_sign_async(
        self,
        request: dm_20151123_models.DeleteSignRequest,
    ) -> dm_20151123_models.DeleteSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sign_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: dm_20151123_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteTagResponse().from_map(
            self.do_rpcrequest('DeleteTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: dm_20151123_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteTagResponse().from_map(
            await self.do_rpcrequest_async('DeleteTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tag(
        self,
        request: dm_20151123_models.DeleteTagRequest,
    ) -> dm_20151123_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: dm_20151123_models.DeleteTagRequest,
    ) -> dm_20151123_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: dm_20151123_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteTemplateResponse().from_map(
            self.do_rpcrequest('DeleteTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: dm_20151123_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DeleteTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: dm_20151123_models.DeleteTemplateRequest,
    ) -> dm_20151123_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: dm_20151123_models.DeleteTemplateRequest,
    ) -> dm_20151123_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def desc_account_summary_with_options(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescAccountSummaryResponse().from_map(
            self.do_rpcrequest('DescAccountSummary', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def desc_account_summary_with_options_async(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescAccountSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescAccountSummary', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def desc_account_summary(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.desc_account_summary_with_options(request, runtime)

    async def desc_account_summary_async(
        self,
        request: dm_20151123_models.DescAccountSummaryRequest,
    ) -> dm_20151123_models.DescAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.desc_account_summary_with_options_async(request, runtime)

    def desc_account_summary_2with_options(
        self,
        request: dm_20151123_models.DescAccountSummary2Request,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummary2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescAccountSummary2Response().from_map(
            self.do_rpcrequest('DescAccountSummary2', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def desc_account_summary_2with_options_async(
        self,
        request: dm_20151123_models.DescAccountSummary2Request,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescAccountSummary2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescAccountSummary2Response().from_map(
            await self.do_rpcrequest_async('DescAccountSummary2', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def desc_account_summary_2(
        self,
        request: dm_20151123_models.DescAccountSummary2Request,
    ) -> dm_20151123_models.DescAccountSummary2Response:
        runtime = util_models.RuntimeOptions()
        return self.desc_account_summary_2with_options(request, runtime)

    async def desc_account_summary_2_async(
        self,
        request: dm_20151123_models.DescAccountSummary2Request,
    ) -> dm_20151123_models.DescAccountSummary2Response:
        runtime = util_models.RuntimeOptions()
        return await self.desc_account_summary_2with_options_async(request, runtime)

    def desc_domain_with_options(
        self,
        request: dm_20151123_models.DescDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescDomainResponse().from_map(
            self.do_rpcrequest('DescDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def desc_domain_with_options_async(
        self,
        request: dm_20151123_models.DescDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescDomainResponse().from_map(
            await self.do_rpcrequest_async('DescDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def desc_domain(
        self,
        request: dm_20151123_models.DescDomainRequest,
    ) -> dm_20151123_models.DescDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.desc_domain_with_options(request, runtime)

    async def desc_domain_async(
        self,
        request: dm_20151123_models.DescDomainRequest,
    ) -> dm_20151123_models.DescDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.desc_domain_with_options_async(request, runtime)

    def desc_template_with_options(
        self,
        request: dm_20151123_models.DescTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescTemplateResponse().from_map(
            self.do_rpcrequest('DescTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def desc_template_with_options_async(
        self,
        request: dm_20151123_models.DescTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.DescTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.DescTemplateResponse().from_map(
            await self.do_rpcrequest_async('DescTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def desc_template(
        self,
        request: dm_20151123_models.DescTemplateRequest,
    ) -> dm_20151123_models.DescTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.desc_template_with_options(request, runtime)

    async def desc_template_async(
        self,
        request: dm_20151123_models.DescTemplateRequest,
    ) -> dm_20151123_models.DescTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.desc_template_with_options_async(request, runtime)

    def enable_account_with_options(
        self,
        request: dm_20151123_models.EnableAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.EnableAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.EnableAccountResponse().from_map(
            self.do_rpcrequest('EnableAccount', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_account_with_options_async(
        self,
        request: dm_20151123_models.EnableAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.EnableAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.EnableAccountResponse().from_map(
            await self.do_rpcrequest_async('EnableAccount', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_account(
        self,
        request: dm_20151123_models.EnableAccountRequest,
    ) -> dm_20151123_models.EnableAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_account_with_options(request, runtime)

    async def enable_account_async(
        self,
        request: dm_20151123_models.EnableAccountRequest,
    ) -> dm_20151123_models.EnableAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_account_with_options_async(request, runtime)

    def get_account_list_with_options(
        self,
        request: dm_20151123_models.GetAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetAccountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetAccountListResponse().from_map(
            self.do_rpcrequest('GetAccountList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_list_with_options_async(
        self,
        request: dm_20151123_models.GetAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetAccountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetAccountListResponse().from_map(
            await self.do_rpcrequest_async('GetAccountList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_list(
        self,
        request: dm_20151123_models.GetAccountListRequest,
    ) -> dm_20151123_models.GetAccountListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_list_with_options(request, runtime)

    async def get_account_list_async(
        self,
        request: dm_20151123_models.GetAccountListRequest,
    ) -> dm_20151123_models.GetAccountListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_list_with_options_async(request, runtime)

    def get_ipfilter_list_with_options(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetIpfilterListResponse().from_map(
            self.do_rpcrequest('GetIpfilterList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ipfilter_list_with_options_async(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetIpfilterListResponse().from_map(
            await self.do_rpcrequest_async('GetIpfilterList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ipfilter_list(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ipfilter_list_with_options(request, runtime)

    async def get_ipfilter_list_async(
        self,
        request: dm_20151123_models.GetIpfilterListRequest,
    ) -> dm_20151123_models.GetIpfilterListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ipfilter_list_with_options_async(request, runtime)

    def get_ip_protection_with_options(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetIpProtectionResponse().from_map(
            self.do_rpcrequest('GetIpProtection', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ip_protection_with_options_async(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetIpProtectionResponse().from_map(
            await self.do_rpcrequest_async('GetIpProtection', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ip_protection(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ip_protection_with_options(request, runtime)

    async def get_ip_protection_async(
        self,
        request: dm_20151123_models.GetIpProtectionRequest,
    ) -> dm_20151123_models.GetIpProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_protection_with_options_async(request, runtime)

    def get_mail_address_msg_call_back_url_with_options(
        self,
        request: dm_20151123_models.GetMailAddressMsgCallBackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetMailAddressMsgCallBackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetMailAddressMsgCallBackUrlResponse().from_map(
            self.do_rpcrequest('GetMailAddressMsgCallBackUrl', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mail_address_msg_call_back_url_with_options_async(
        self,
        request: dm_20151123_models.GetMailAddressMsgCallBackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetMailAddressMsgCallBackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetMailAddressMsgCallBackUrlResponse().from_map(
            await self.do_rpcrequest_async('GetMailAddressMsgCallBackUrl', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mail_address_msg_call_back_url(
        self,
        request: dm_20151123_models.GetMailAddressMsgCallBackUrlRequest,
    ) -> dm_20151123_models.GetMailAddressMsgCallBackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mail_address_msg_call_back_url_with_options(request, runtime)

    async def get_mail_address_msg_call_back_url_async(
        self,
        request: dm_20151123_models.GetMailAddressMsgCallBackUrlRequest,
    ) -> dm_20151123_models.GetMailAddressMsgCallBackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mail_address_msg_call_back_url_with_options_async(request, runtime)

    def get_region_list_with_options(
        self,
        request: dm_20151123_models.GetRegionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetRegionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetRegionListResponse().from_map(
            self.do_rpcrequest('GetRegionList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_region_list_with_options_async(
        self,
        request: dm_20151123_models.GetRegionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetRegionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetRegionListResponse().from_map(
            await self.do_rpcrequest_async('GetRegionList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_region_list(
        self,
        request: dm_20151123_models.GetRegionListRequest,
    ) -> dm_20151123_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_region_list_with_options(request, runtime)

    async def get_region_list_async(
        self,
        request: dm_20151123_models.GetRegionListRequest,
    ) -> dm_20151123_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_region_list_with_options_async(request, runtime)

    def get_sender_address_list_with_options(
        self,
        request: dm_20151123_models.GetSenderAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetSenderAddressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetSenderAddressListResponse().from_map(
            self.do_rpcrequest('GetSenderAddressList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sender_address_list_with_options_async(
        self,
        request: dm_20151123_models.GetSenderAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetSenderAddressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetSenderAddressListResponse().from_map(
            await self.do_rpcrequest_async('GetSenderAddressList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sender_address_list(
        self,
        request: dm_20151123_models.GetSenderAddressListRequest,
    ) -> dm_20151123_models.GetSenderAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sender_address_list_with_options(request, runtime)

    async def get_sender_address_list_async(
        self,
        request: dm_20151123_models.GetSenderAddressListRequest,
    ) -> dm_20151123_models.GetSenderAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sender_address_list_with_options_async(request, runtime)

    def get_track_list_with_options(
        self,
        request: dm_20151123_models.GetTrackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetTrackListResponse().from_map(
            self.do_rpcrequest('GetTrackList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_track_list_with_options_async(
        self,
        request: dm_20151123_models.GetTrackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetTrackListResponse().from_map(
            await self.do_rpcrequest_async('GetTrackList', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_track_list(
        self,
        request: dm_20151123_models.GetTrackListRequest,
    ) -> dm_20151123_models.GetTrackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_track_list_with_options(request, runtime)

    async def get_track_list_async(
        self,
        request: dm_20151123_models.GetTrackListRequest,
    ) -> dm_20151123_models.GetTrackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_track_list_with_options_async(request, runtime)

    def get_track_list_by_mail_from_and_tag_name_with_options(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetTrackListByMailFromAndTagNameResponse().from_map(
            self.do_rpcrequest('GetTrackListByMailFromAndTagName', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_track_list_by_mail_from_and_tag_name_with_options_async(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.GetTrackListByMailFromAndTagNameResponse().from_map(
            await self.do_rpcrequest_async('GetTrackListByMailFromAndTagName', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_track_list_by_mail_from_and_tag_name(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_track_list_by_mail_from_and_tag_name_with_options(request, runtime)

    async def get_track_list_by_mail_from_and_tag_name_async(
        self,
        request: dm_20151123_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> dm_20151123_models.GetTrackListByMailFromAndTagNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_track_list_by_mail_from_and_tag_name_with_options_async(request, runtime)

    def migrate_market_with_options(
        self,
        request: dm_20151123_models.MigrateMarketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.MigrateMarketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.MigrateMarketResponse().from_map(
            self.do_rpcrequest('MigrateMarket', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_market_with_options_async(
        self,
        request: dm_20151123_models.MigrateMarketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.MigrateMarketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.MigrateMarketResponse().from_map(
            await self.do_rpcrequest_async('MigrateMarket', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_market(
        self,
        request: dm_20151123_models.MigrateMarketRequest,
    ) -> dm_20151123_models.MigrateMarketResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_market_with_options(request, runtime)

    async def migrate_market_async(
        self,
        request: dm_20151123_models.MigrateMarketRequest,
    ) -> dm_20151123_models.MigrateMarketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_market_with_options_async(request, runtime)

    def modify_account_notification_with_options(
        self,
        request: dm_20151123_models.ModifyAccountNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyAccountNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyAccountNotificationResponse().from_map(
            self.do_rpcrequest('ModifyAccountNotification', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_notification_with_options_async(
        self,
        request: dm_20151123_models.ModifyAccountNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyAccountNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyAccountNotificationResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountNotification', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_notification(
        self,
        request: dm_20151123_models.ModifyAccountNotificationRequest,
    ) -> dm_20151123_models.ModifyAccountNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_notification_with_options(request, runtime)

    async def modify_account_notification_async(
        self,
        request: dm_20151123_models.ModifyAccountNotificationRequest,
    ) -> dm_20151123_models.ModifyAccountNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_notification_with_options_async(request, runtime)

    def modify_mail_address_with_options(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyMailAddressResponse().from_map(
            self.do_rpcrequest('ModifyMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_mail_address_with_options_async(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyMailAddressResponse().from_map(
            await self.do_rpcrequest_async('ModifyMailAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_mail_address(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_mail_address_with_options(request, runtime)

    async def modify_mail_address_async(
        self,
        request: dm_20151123_models.ModifyMailAddressRequest,
    ) -> dm_20151123_models.ModifyMailAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_mail_address_with_options_async(request, runtime)

    def modify_pwby_domain_with_options(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyPWByDomainResponse().from_map(
            self.do_rpcrequest('ModifyPWByDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_pwby_domain_with_options_async(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyPWByDomainResponse().from_map(
            await self.do_rpcrequest_async('ModifyPWByDomain', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_pwby_domain(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_pwby_domain_with_options(request, runtime)

    async def modify_pwby_domain_async(
        self,
        request: dm_20151123_models.ModifyPWByDomainRequest,
    ) -> dm_20151123_models.ModifyPWByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_pwby_domain_with_options_async(request, runtime)

    def modify_sender_address_notification_with_options(
        self,
        request: dm_20151123_models.ModifySenderAddressNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifySenderAddressNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifySenderAddressNotificationResponse().from_map(
            self.do_rpcrequest('ModifySenderAddressNotification', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sender_address_notification_with_options_async(
        self,
        request: dm_20151123_models.ModifySenderAddressNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifySenderAddressNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifySenderAddressNotificationResponse().from_map(
            await self.do_rpcrequest_async('ModifySenderAddressNotification', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sender_address_notification(
        self,
        request: dm_20151123_models.ModifySenderAddressNotificationRequest,
    ) -> dm_20151123_models.ModifySenderAddressNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sender_address_notification_with_options(request, runtime)

    async def modify_sender_address_notification_async(
        self,
        request: dm_20151123_models.ModifySenderAddressNotificationRequest,
    ) -> dm_20151123_models.ModifySenderAddressNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sender_address_notification_with_options_async(request, runtime)

    def modify_tag_with_options(
        self,
        request: dm_20151123_models.ModifyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyTagResponse().from_map(
            self.do_rpcrequest('ModifyTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_tag_with_options_async(
        self,
        request: dm_20151123_models.ModifyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyTagResponse().from_map(
            await self.do_rpcrequest_async('ModifyTag', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_tag(
        self,
        request: dm_20151123_models.ModifyTagRequest,
    ) -> dm_20151123_models.ModifyTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_options(request, runtime)

    async def modify_tag_async(
        self,
        request: dm_20151123_models.ModifyTagRequest,
    ) -> dm_20151123_models.ModifyTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_with_options_async(request, runtime)

    def modify_template_with_options(
        self,
        request: dm_20151123_models.ModifyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyTemplateResponse().from_map(
            self.do_rpcrequest('ModifyTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_template_with_options_async(
        self,
        request: dm_20151123_models.ModifyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.ModifyTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.ModifyTemplateResponse().from_map(
            await self.do_rpcrequest_async('ModifyTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_template(
        self,
        request: dm_20151123_models.ModifyTemplateRequest,
    ) -> dm_20151123_models.ModifyTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    async def modify_template_async(
        self,
        request: dm_20151123_models.ModifyTemplateRequest,
    ) -> dm_20151123_models.ModifyTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_with_options_async(request, runtime)

    def query_domain_by_param_with_options(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryDomainByParamResponse().from_map(
            self.do_rpcrequest('QueryDomainByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryDomainByParamResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_domain_by_param(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_param_with_options(request, runtime)

    async def query_domain_by_param_async(
        self,
        request: dm_20151123_models.QueryDomainByParamRequest,
    ) -> dm_20151123_models.QueryDomainByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_param_with_options_async(request, runtime)

    def query_invalid_address_with_options(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryInvalidAddressResponse().from_map(
            self.do_rpcrequest('QueryInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_invalid_address_with_options_async(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryInvalidAddressResponse().from_map(
            await self.do_rpcrequest_async('QueryInvalidAddress', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_invalid_address(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_invalid_address_with_options(request, runtime)

    async def query_invalid_address_async(
        self,
        request: dm_20151123_models.QueryInvalidAddressRequest,
    ) -> dm_20151123_models.QueryInvalidAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_invalid_address_with_options_async(request, runtime)

    def query_receiver_by_param_with_options(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryReceiverByParamResponse().from_map(
            self.do_rpcrequest('QueryReceiverByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_receiver_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryReceiverByParamResponse().from_map(
            await self.do_rpcrequest_async('QueryReceiverByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_receiver_by_param(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_by_param_with_options(request, runtime)

    async def query_receiver_by_param_async(
        self,
        request: dm_20151123_models.QueryReceiverByParamRequest,
    ) -> dm_20151123_models.QueryReceiverByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_receiver_by_param_with_options_async(request, runtime)

    def query_receiver_detail_with_options(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryReceiverDetailResponse().from_map(
            self.do_rpcrequest('QueryReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryReceiverDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_receiver_detail(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_detail_with_options(request, runtime)

    async def query_receiver_detail_async(
        self,
        request: dm_20151123_models.QueryReceiverDetailRequest,
    ) -> dm_20151123_models.QueryReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_receiver_detail_with_options_async(request, runtime)

    def query_sign_by_param_with_options(
        self,
        request: dm_20151123_models.QuerySignByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QuerySignByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QuerySignByParamResponse().from_map(
            self.do_rpcrequest('QuerySignByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_sign_by_param_with_options_async(
        self,
        request: dm_20151123_models.QuerySignByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QuerySignByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QuerySignByParamResponse().from_map(
            await self.do_rpcrequest_async('QuerySignByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sign_by_param(
        self,
        request: dm_20151123_models.QuerySignByParamRequest,
    ) -> dm_20151123_models.QuerySignByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sign_by_param_with_options(request, runtime)

    async def query_sign_by_param_async(
        self,
        request: dm_20151123_models.QuerySignByParamRequest,
    ) -> dm_20151123_models.QuerySignByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sign_by_param_with_options_async(request, runtime)

    def query_sms_statistics_with_options(
        self,
        request: dm_20151123_models.QuerySmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QuerySmsStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QuerySmsStatisticsResponse().from_map(
            self.do_rpcrequest('QuerySmsStatistics', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_sms_statistics_with_options_async(
        self,
        request: dm_20151123_models.QuerySmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QuerySmsStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QuerySmsStatisticsResponse().from_map(
            await self.do_rpcrequest_async('QuerySmsStatistics', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sms_statistics(
        self,
        request: dm_20151123_models.QuerySmsStatisticsRequest,
    ) -> dm_20151123_models.QuerySmsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_with_options(request, runtime)

    async def query_sms_statistics_async(
        self,
        request: dm_20151123_models.QuerySmsStatisticsRequest,
    ) -> dm_20151123_models.QuerySmsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_with_options_async(request, runtime)

    def query_tag_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTagByParamResponse().from_map(
            self.do_rpcrequest('QueryTagByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tag_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTagByParamResponse().from_map(
            await self.do_rpcrequest_async('QueryTagByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tag_by_param(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tag_by_param_with_options(request, runtime)

    async def query_tag_by_param_async(
        self,
        request: dm_20151123_models.QueryTagByParamRequest,
    ) -> dm_20151123_models.QueryTagByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_by_param_with_options_async(request, runtime)

    def query_task_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTaskByParamResponse().from_map(
            self.do_rpcrequest('QueryTaskByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTaskByParamResponse().from_map(
            await self.do_rpcrequest_async('QueryTaskByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_task_by_param(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_task_by_param_with_options(request, runtime)

    async def query_task_by_param_async(
        self,
        request: dm_20151123_models.QueryTaskByParamRequest,
    ) -> dm_20151123_models.QueryTaskByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_by_param_with_options_async(request, runtime)

    def query_template_by_param_with_options(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTemplateByParamResponse().from_map(
            self.do_rpcrequest('QueryTemplateByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_template_by_param_with_options_async(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.QueryTemplateByParamResponse().from_map(
            await self.do_rpcrequest_async('QueryTemplateByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_template_by_param(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_template_by_param_with_options(request, runtime)

    async def query_template_by_param_async(
        self,
        request: dm_20151123_models.QueryTemplateByParamRequest,
    ) -> dm_20151123_models.QueryTemplateByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_template_by_param_with_options_async(request, runtime)

    def save_receiver_detail_with_options(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SaveReceiverDetailResponse().from_map(
            self.do_rpcrequest('SaveReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_receiver_detail_with_options_async(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SaveReceiverDetailResponse().from_map(
            await self.do_rpcrequest_async('SaveReceiverDetail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_receiver_detail(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_receiver_detail_with_options(request, runtime)

    async def save_receiver_detail_async(
        self,
        request: dm_20151123_models.SaveReceiverDetailRequest,
    ) -> dm_20151123_models.SaveReceiverDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_receiver_detail_with_options_async(request, runtime)

    def sender_statistics_by_tag_name_and_batch_idwith_options(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse().from_map(
            self.do_rpcrequest('SenderStatisticsByTagNameAndBatchID', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sender_statistics_by_tag_name_and_batch_idwith_options_async(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse().from_map(
            await self.do_rpcrequest_async('SenderStatisticsByTagNameAndBatchID', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sender_statistics_by_tag_name_and_batch_id(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_by_tag_name_and_batch_idwith_options(request, runtime)

    async def sender_statistics_by_tag_name_and_batch_id_async(
        self,
        request: dm_20151123_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> dm_20151123_models.SenderStatisticsByTagNameAndBatchIDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sender_statistics_by_tag_name_and_batch_idwith_options_async(request, runtime)

    def sender_statistics_detail_by_param_with_options(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SenderStatisticsDetailByParamResponse().from_map(
            self.do_rpcrequest('SenderStatisticsDetailByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sender_statistics_detail_by_param_with_options_async(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SenderStatisticsDetailByParamResponse().from_map(
            await self.do_rpcrequest_async('SenderStatisticsDetailByParam', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sender_statistics_detail_by_param(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_detail_by_param_with_options(request, runtime)

    async def sender_statistics_detail_by_param_async(
        self,
        request: dm_20151123_models.SenderStatisticsDetailByParamRequest,
    ) -> dm_20151123_models.SenderStatisticsDetailByParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sender_statistics_detail_by_param_with_options_async(request, runtime)

    def send_test_by_template_with_options(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SendTestByTemplateResponse().from_map(
            self.do_rpcrequest('SendTestByTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_test_by_template_with_options_async(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SendTestByTemplateResponse().from_map(
            await self.do_rpcrequest_async('SendTestByTemplate', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_test_by_template(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_test_by_template_with_options(request, runtime)

    async def send_test_by_template_async(
        self,
        request: dm_20151123_models.SendTestByTemplateRequest,
    ) -> dm_20151123_models.SendTestByTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_test_by_template_with_options_async(request, runtime)

    def single_send_mail_with_options(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SingleSendMailResponse().from_map(
            self.do_rpcrequest('SingleSendMail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def single_send_mail_with_options_async(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendMailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SingleSendMailResponse().from_map(
            await self.do_rpcrequest_async('SingleSendMail', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_send_mail(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
    ) -> dm_20151123_models.SingleSendMailResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_send_mail_with_options(request, runtime)

    async def single_send_mail_async(
        self,
        request: dm_20151123_models.SingleSendMailRequest,
    ) -> dm_20151123_models.SingleSendMailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_send_mail_with_options_async(request, runtime)

    def single_send_sms_with_options(
        self,
        request: dm_20151123_models.SingleSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SingleSendSmsResponse().from_map(
            self.do_rpcrequest('SingleSendSms', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def single_send_sms_with_options_async(
        self,
        request: dm_20151123_models.SingleSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.SingleSendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.SingleSendSmsResponse().from_map(
            await self.do_rpcrequest_async('SingleSendSms', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_send_sms(
        self,
        request: dm_20151123_models.SingleSendSmsRequest,
    ) -> dm_20151123_models.SingleSendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_send_sms_with_options(request, runtime)

    async def single_send_sms_async(
        self,
        request: dm_20151123_models.SingleSendSmsRequest,
    ) -> dm_20151123_models.SingleSendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_send_sms_with_options_async(request, runtime)

    def update_domain_track_name_with_options(
        self,
        request: dm_20151123_models.UpdateDomainTrackNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateDomainTrackNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateDomainTrackNameResponse().from_map(
            self.do_rpcrequest('UpdateDomainTrackName', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_track_name_with_options_async(
        self,
        request: dm_20151123_models.UpdateDomainTrackNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateDomainTrackNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateDomainTrackNameResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainTrackName', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_domain_track_name(
        self,
        request: dm_20151123_models.UpdateDomainTrackNameRequest,
    ) -> dm_20151123_models.UpdateDomainTrackNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_domain_track_name_with_options(request, runtime)

    async def update_domain_track_name_async(
        self,
        request: dm_20151123_models.UpdateDomainTrackNameRequest,
    ) -> dm_20151123_models.UpdateDomainTrackNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_track_name_with_options_async(request, runtime)

    def update_ip_protection_with_options(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateIpProtectionResponse().from_map(
            self.do_rpcrequest('UpdateIpProtection', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ip_protection_with_options_async(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateIpProtectionResponse().from_map(
            await self.do_rpcrequest_async('UpdateIpProtection', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_protection(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ip_protection_with_options(request, runtime)

    async def update_ip_protection_async(
        self,
        request: dm_20151123_models.UpdateIpProtectionRequest,
    ) -> dm_20151123_models.UpdateIpProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_protection_with_options_async(request, runtime)

    def update_mail_address_msg_call_back_url_with_options(
        self,
        request: dm_20151123_models.UpdateMailAddressMsgCallBackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse().from_map(
            self.do_rpcrequest('UpdateMailAddressMsgCallBackUrl', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mail_address_msg_call_back_url_with_options_async(
        self,
        request: dm_20151123_models.UpdateMailAddressMsgCallBackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse().from_map(
            await self.do_rpcrequest_async('UpdateMailAddressMsgCallBackUrl', '2015-11-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mail_address_msg_call_back_url(
        self,
        request: dm_20151123_models.UpdateMailAddressMsgCallBackUrlRequest,
    ) -> dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mail_address_msg_call_back_url_with_options(request, runtime)

    async def update_mail_address_msg_call_back_url_async(
        self,
        request: dm_20151123_models.UpdateMailAddressMsgCallBackUrlRequest,
    ) -> dm_20151123_models.UpdateMailAddressMsgCallBackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mail_address_msg_call_back_url_with_options_async(request, runtime)
