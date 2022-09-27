# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mscopensubscription20210713 import models as msc_open_subscription_20210713_models
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
        self._endpoint = self.get_endpoint('mscopensubscription', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_contact_with_options(
        self,
        request: msc_open_subscription_20210713_models.CreateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.position):
            body['Position'] = request.position
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_contact_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.CreateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.position):
            body['Position'] = request.position
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_contact(
        self,
        request: msc_open_subscription_20210713_models.CreateContactRequest,
    ) -> msc_open_subscription_20210713_models.CreateContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_contact_with_options(request, runtime)

    async def create_contact_async(
        self,
        request: msc_open_subscription_20210713_models.CreateContactRequest,
    ) -> msc_open_subscription_20210713_models.CreateContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_contact_with_options_async(request, runtime)

    def create_subscription_item_with_options(
        self,
        request: msc_open_subscription_20210713_models.CreateSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateSubscriptionItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.item_name):
            body['ItemName'] = request.item_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateSubscriptionItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscription_item_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.CreateSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateSubscriptionItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.item_name):
            body['ItemName'] = request.item_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateSubscriptionItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscription_item(
        self,
        request: msc_open_subscription_20210713_models.CreateSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.CreateSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_item_with_options(request, runtime)

    async def create_subscription_item_async(
        self,
        request: msc_open_subscription_20210713_models.CreateSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.CreateSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_item_with_options_async(request, runtime)

    def create_webhook_with_options(
        self,
        request: msc_open_subscription_20210713_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.server_url):
            body['ServerUrl'] = request.server_url
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_webhook_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.CreateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.server_url):
            body['ServerUrl'] = request.server_url
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.CreateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_webhook(
        self,
        request: msc_open_subscription_20210713_models.CreateWebhookRequest,
    ) -> msc_open_subscription_20210713_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_webhook_with_options(request, runtime)

    async def create_webhook_async(
        self,
        request: msc_open_subscription_20210713_models.CreateWebhookRequest,
    ) -> msc_open_subscription_20210713_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_webhook_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: msc_open_subscription_20210713_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.DeleteContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact(
        self,
        request: msc_open_subscription_20210713_models.DeleteContactRequest,
    ) -> msc_open_subscription_20210713_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    async def delete_contact_async(
        self,
        request: msc_open_subscription_20210713_models.DeleteContactRequest,
    ) -> msc_open_subscription_20210713_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_with_options_async(request, runtime)

    def delete_webhook_with_options(
        self,
        request: msc_open_subscription_20210713_models.DeleteWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.DeleteWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.DeleteWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_webhook_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.DeleteWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.DeleteWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.DeleteWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_webhook(
        self,
        request: msc_open_subscription_20210713_models.DeleteWebhookRequest,
    ) -> msc_open_subscription_20210713_models.DeleteWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_webhook_with_options(request, runtime)

    async def delete_webhook_async(
        self,
        request: msc_open_subscription_20210713_models.DeleteWebhookRequest,
    ) -> msc_open_subscription_20210713_models.DeleteWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_webhook_with_options_async(request, runtime)

    def get_contact_with_options(
        self,
        request: msc_open_subscription_20210713_models.GetContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetContactResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.GetContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetContactResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact(
        self,
        request: msc_open_subscription_20210713_models.GetContactRequest,
    ) -> msc_open_subscription_20210713_models.GetContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_contact_with_options(request, runtime)

    async def get_contact_async(
        self,
        request: msc_open_subscription_20210713_models.GetContactRequest,
    ) -> msc_open_subscription_20210713_models.GetContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_contact_with_options_async(request, runtime)

    def get_subscription_item_with_options(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetSubscriptionItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_item_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetSubscriptionItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_item(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_item_with_options(request, runtime)

    async def get_subscription_item_async(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_item_with_options_async(request, runtime)

    def get_subscription_item_detail_with_options(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionItemDetail',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_item_detail_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionItemDetail',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_item_detail(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemDetailRequest,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_item_detail_with_options(request, runtime)

    async def get_subscription_item_detail_async(
        self,
        request: msc_open_subscription_20210713_models.GetSubscriptionItemDetailRequest,
    ) -> msc_open_subscription_20210713_models.GetSubscriptionItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_item_detail_with_options_async(request, runtime)

    def get_webhook_with_options(
        self,
        request: msc_open_subscription_20210713_models.GetWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetWebhookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_webhook_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.GetWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.GetWebhookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.GetWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_webhook(
        self,
        request: msc_open_subscription_20210713_models.GetWebhookRequest,
    ) -> msc_open_subscription_20210713_models.GetWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_webhook_with_options(request, runtime)

    async def get_webhook_async(
        self,
        request: msc_open_subscription_20210713_models.GetWebhookRequest,
    ) -> msc_open_subscription_20210713_models.GetWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_webhook_with_options_async(request, runtime)

    def list_contacts_with_options(
        self,
        request: msc_open_subscription_20210713_models.ListContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListContactsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContacts',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contacts_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.ListContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListContactsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContacts',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contacts(
        self,
        request: msc_open_subscription_20210713_models.ListContactsRequest,
    ) -> msc_open_subscription_20210713_models.ListContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_contacts_with_options(request, runtime)

    async def list_contacts_async(
        self,
        request: msc_open_subscription_20210713_models.ListContactsRequest,
    ) -> msc_open_subscription_20210713_models.ListContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_contacts_with_options_async(request, runtime)

    def list_subscription_item_group_details_with_options(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionItemGroupDetails',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_item_group_details_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionItemGroupDetails',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_item_group_details(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsRequest,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_subscription_item_group_details_with_options(request, runtime)

    async def list_subscription_item_group_details_async(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsRequest,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemGroupDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_subscription_item_group_details_with_options_async(request, runtime)

    def list_subscription_items_with_options(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionItems',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListSubscriptionItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_items_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionItems',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListSubscriptionItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_items(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemsRequest,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_subscription_items_with_options(request, runtime)

    async def list_subscription_items_async(
        self,
        request: msc_open_subscription_20210713_models.ListSubscriptionItemsRequest,
    ) -> msc_open_subscription_20210713_models.ListSubscriptionItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_subscription_items_with_options_async(request, runtime)

    def list_webhooks_with_options(
        self,
        request: msc_open_subscription_20210713_models.ListWebhooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListWebhooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebhooks',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListWebhooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_webhooks_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.ListWebhooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.ListWebhooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebhooks',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.ListWebhooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_webhooks(
        self,
        request: msc_open_subscription_20210713_models.ListWebhooksRequest,
    ) -> msc_open_subscription_20210713_models.ListWebhooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_webhooks_with_options(request, runtime)

    async def list_webhooks_async(
        self,
        request: msc_open_subscription_20210713_models.ListWebhooksRequest,
    ) -> msc_open_subscription_20210713_models.ListWebhooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_webhooks_with_options_async(request, runtime)

    def send_verification_message_with_options(
        self,
        request: msc_open_subscription_20210713_models.SendVerificationMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.SendVerificationMessageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationMessage',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.SendVerificationMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_message_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.SendVerificationMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.SendVerificationMessageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationMessage',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.SendVerificationMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_message(
        self,
        request: msc_open_subscription_20210713_models.SendVerificationMessageRequest,
    ) -> msc_open_subscription_20210713_models.SendVerificationMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_message_with_options(request, runtime)

    async def send_verification_message_async(
        self,
        request: msc_open_subscription_20210713_models.SendVerificationMessageRequest,
    ) -> msc_open_subscription_20210713_models.SendVerificationMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_message_with_options_async(request, runtime)

    def update_contact_with_options(
        self,
        request: msc_open_subscription_20210713_models.UpdateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contact_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.UpdateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateContact',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contact(
        self,
        request: msc_open_subscription_20210713_models.UpdateContactRequest,
    ) -> msc_open_subscription_20210713_models.UpdateContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_contact_with_options(request, runtime)

    async def update_contact_async(
        self,
        request: msc_open_subscription_20210713_models.UpdateContactRequest,
    ) -> msc_open_subscription_20210713_models.UpdateContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_contact_with_options_async(request, runtime)

    def update_subscription_item_with_options(
        self,
        tmp_req: msc_open_subscription_20210713_models.UpdateSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse:
        UtilClient.validate_model(tmp_req)
        request = msc_open_subscription_20210713_models.UpdateSubscriptionItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_ids):
            request.contact_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_ids, 'ContactIds', 'json')
        if not UtilClient.is_unset(tmp_req.webhook_ids):
            request.webhook_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.webhook_ids, 'WebhookIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_ids_shrink):
            body['ContactIds'] = request.contact_ids_shrink
        if not UtilClient.is_unset(request.email_status):
            body['EmailStatus'] = request.email_status
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.pmsg_status):
            body['PmsgStatus'] = request.pmsg_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sms_status):
            body['SmsStatus'] = request.sms_status
        if not UtilClient.is_unset(request.tts_status):
            body['TtsStatus'] = request.tts_status
        if not UtilClient.is_unset(request.webhook_ids_shrink):
            body['WebhookIds'] = request.webhook_ids_shrink
        if not UtilClient.is_unset(request.webhook_status):
            body['WebhookStatus'] = request.webhook_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_item_with_options_async(
        self,
        tmp_req: msc_open_subscription_20210713_models.UpdateSubscriptionItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse:
        UtilClient.validate_model(tmp_req)
        request = msc_open_subscription_20210713_models.UpdateSubscriptionItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_ids):
            request.contact_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_ids, 'ContactIds', 'json')
        if not UtilClient.is_unset(tmp_req.webhook_ids):
            request.webhook_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.webhook_ids, 'WebhookIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.contact_ids_shrink):
            body['ContactIds'] = request.contact_ids_shrink
        if not UtilClient.is_unset(request.email_status):
            body['EmailStatus'] = request.email_status
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.pmsg_status):
            body['PmsgStatus'] = request.pmsg_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sms_status):
            body['SmsStatus'] = request.sms_status
        if not UtilClient.is_unset(request.tts_status):
            body['TtsStatus'] = request.tts_status
        if not UtilClient.is_unset(request.webhook_ids_shrink):
            body['WebhookIds'] = request.webhook_ids_shrink
        if not UtilClient.is_unset(request.webhook_status):
            body['WebhookStatus'] = request.webhook_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscriptionItem',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription_item(
        self,
        request: msc_open_subscription_20210713_models.UpdateSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_subscription_item_with_options(request, runtime)

    async def update_subscription_item_async(
        self,
        request: msc_open_subscription_20210713_models.UpdateSubscriptionItemRequest,
    ) -> msc_open_subscription_20210713_models.UpdateSubscriptionItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_subscription_item_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: msc_open_subscription_20210713_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.server_url):
            body['ServerUrl'] = request.server_url
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: msc_open_subscription_20210713_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_open_subscription_20210713_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.server_url):
            body['ServerUrl'] = request.server_url
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2021-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_open_subscription_20210713_models.UpdateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_webhook(
        self,
        request: msc_open_subscription_20210713_models.UpdateWebhookRequest,
    ) -> msc_open_subscription_20210713_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: msc_open_subscription_20210713_models.UpdateWebhookRequest,
    ) -> msc_open_subscription_20210713_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)
