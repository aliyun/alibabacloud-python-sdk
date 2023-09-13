# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkcard20210520 import models as linkcard_20210520_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkcard', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_card_to_directional_group_with_options(
        self,
        tmp_req: linkcard_20210520_models.AddCardToDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddCardToDirectionalGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddCardToDirectionalGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.iccid_list):
            request.iccid_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.iccid_list, 'IccidList', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_type):
            query['AddType'] = request.add_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iccid_list_shrink):
            query['IccidList'] = request.iccid_list_shrink
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCardToDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddCardToDirectionalGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_card_to_directional_group_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.AddCardToDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddCardToDirectionalGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddCardToDirectionalGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.iccid_list):
            request.iccid_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.iccid_list, 'IccidList', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_type):
            query['AddType'] = request.add_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iccid_list_shrink):
            query['IccidList'] = request.iccid_list_shrink
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCardToDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddCardToDirectionalGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_card_to_directional_group(
        self,
        request: linkcard_20210520_models.AddCardToDirectionalGroupRequest,
    ) -> linkcard_20210520_models.AddCardToDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_card_to_directional_group_with_options(request, runtime)

    async def add_card_to_directional_group_async(
        self,
        request: linkcard_20210520_models.AddCardToDirectionalGroupRequest,
    ) -> linkcard_20210520_models.AddCardToDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_card_to_directional_group_with_options_async(request, runtime)

    def add_directional_address_with_options(
        self,
        request: linkcard_20210520_models.AddDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.url_insecurity_force):
            query['UrlInsecurityForce'] = request.url_insecurity_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_directional_address_with_options_async(
        self,
        request: linkcard_20210520_models.AddDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.url_insecurity_force):
            query['UrlInsecurityForce'] = request.url_insecurity_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_directional_address(
        self,
        request: linkcard_20210520_models.AddDirectionalAddressRequest,
    ) -> linkcard_20210520_models.AddDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_directional_address_with_options(request, runtime)

    async def add_directional_address_async(
        self,
        request: linkcard_20210520_models.AddDirectionalAddressRequest,
    ) -> linkcard_20210520_models.AddDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_directional_address_with_options_async(request, runtime)

    def add_directional_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.AddDirectionalCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddDirectionalCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_list):
            request.order_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_list, 'OrderList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.file_uri):
            query['FileUri'] = request.file_uri
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order_list_shrink):
            query['OrderList'] = request.order_list_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.upload_method):
            query['UploadMethod'] = request.upload_method
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_directional_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.AddDirectionalCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddDirectionalCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_list):
            request.order_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_list, 'OrderList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.file_uri):
            query['FileUri'] = request.file_uri
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order_list_shrink):
            query['OrderList'] = request.order_list_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.upload_method):
            query['UploadMethod'] = request.upload_method
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_directional_card(
        self,
        request: linkcard_20210520_models.AddDirectionalCardRequest,
    ) -> linkcard_20210520_models.AddDirectionalCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_directional_card_with_options(request, runtime)

    async def add_directional_card_async(
        self,
        request: linkcard_20210520_models.AddDirectionalCardRequest,
    ) -> linkcard_20210520_models.AddDirectionalCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_directional_card_with_options_async(request, runtime)

    def add_directional_group_with_options(
        self,
        request: linkcard_20210520_models.AddDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_directional_group_with_options_async(
        self,
        request: linkcard_20210520_models.AddDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddDirectionalGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddDirectionalGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_directional_group(
        self,
        request: linkcard_20210520_models.AddDirectionalGroupRequest,
    ) -> linkcard_20210520_models.AddDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_directional_group_with_options(request, runtime)

    async def add_directional_group_async(
        self,
        request: linkcard_20210520_models.AddDirectionalGroupRequest,
    ) -> linkcard_20210520_models.AddDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_directional_group_with_options_async(request, runtime)

    def add_tags_to_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.AddTagsToCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddTagsToCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddTagsToCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_name_list):
            request.tag_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_name_list, 'TagNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.tag_name_list_shrink):
            query['TagNameList'] = request.tag_name_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsToCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddTagsToCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_to_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.AddTagsToCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.AddTagsToCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.AddTagsToCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_name_list):
            request.tag_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_name_list, 'TagNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.tag_name_list_shrink):
            query['TagNameList'] = request.tag_name_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsToCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.AddTagsToCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags_to_card(
        self,
        request: linkcard_20210520_models.AddTagsToCardRequest,
    ) -> linkcard_20210520_models.AddTagsToCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_card_with_options(request, runtime)

    async def add_tags_to_card_async(
        self,
        request: linkcard_20210520_models.AddTagsToCardRequest,
    ) -> linkcard_20210520_models.AddTagsToCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_to_card_with_options_async(request, runtime)

    def batch_add_directional_address_with_options(
        self,
        request: linkcard_20210520_models.BatchAddDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.BatchAddDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.list_address):
            query['ListAddress'] = request.list_address
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.BatchAddDirectionalAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_directional_address_with_options_async(
        self,
        request: linkcard_20210520_models.BatchAddDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.BatchAddDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.list_address):
            query['ListAddress'] = request.list_address
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.BatchAddDirectionalAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_directional_address(
        self,
        request: linkcard_20210520_models.BatchAddDirectionalAddressRequest,
    ) -> linkcard_20210520_models.BatchAddDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_directional_address_with_options(request, runtime)

    async def batch_add_directional_address_async(
        self,
        request: linkcard_20210520_models.BatchAddDirectionalAddressRequest,
    ) -> linkcard_20210520_models.BatchAddDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_directional_address_with_options_async(request, runtime)

    def delete_directional_address_with_options(
        self,
        request: linkcard_20210520_models.DeleteDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.DeleteDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.DeleteDirectionalAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directional_address_with_options_async(
        self,
        request: linkcard_20210520_models.DeleteDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.DeleteDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.msg_notify):
            query['MsgNotify'] = request.msg_notify
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.DeleteDirectionalAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directional_address(
        self,
        request: linkcard_20210520_models.DeleteDirectionalAddressRequest,
    ) -> linkcard_20210520_models.DeleteDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directional_address_with_options(request, runtime)

    async def delete_directional_address_async(
        self,
        request: linkcard_20210520_models.DeleteDirectionalAddressRequest,
    ) -> linkcard_20210520_models.DeleteDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directional_address_with_options_async(request, runtime)

    def delete_directional_group_with_options(
        self,
        request: linkcard_20210520_models.DeleteDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.DeleteDirectionalGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.DeleteDirectionalGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directional_group_with_options_async(
        self,
        request: linkcard_20210520_models.DeleteDirectionalGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.DeleteDirectionalGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectionalGroup',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.DeleteDirectionalGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directional_group(
        self,
        request: linkcard_20210520_models.DeleteDirectionalGroupRequest,
    ) -> linkcard_20210520_models.DeleteDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directional_group_with_options(request, runtime)

    async def delete_directional_group_async(
        self,
        request: linkcard_20210520_models.DeleteDirectionalGroupRequest,
    ) -> linkcard_20210520_models.DeleteDirectionalGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directional_group_with_options_async(request, runtime)

    def force_activation_with_options(
        self,
        request: linkcard_20210520_models.ForceActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ForceActivationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_type):
            query['DateType'] = request.date_type
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForceActivation',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ForceActivationResponse(),
            self.call_api(params, req, runtime)
        )

    async def force_activation_with_options_async(
        self,
        request: linkcard_20210520_models.ForceActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ForceActivationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_type):
            query['DateType'] = request.date_type
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForceActivation',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ForceActivationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def force_activation(
        self,
        request: linkcard_20210520_models.ForceActivationRequest,
    ) -> linkcard_20210520_models.ForceActivationResponse:
        runtime = util_models.RuntimeOptions()
        return self.force_activation_with_options(request, runtime)

    async def force_activation_async(
        self,
        request: linkcard_20210520_models.ForceActivationRequest,
    ) -> linkcard_20210520_models.ForceActivationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.force_activation_with_options_async(request, runtime)

    def get_card_detail_with_options(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destroy_card):
            query['DestroyCard'] = request.destroy_card
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.show_psim):
            query['ShowPsim'] = request.show_psim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_detail_with_options_async(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destroy_card):
            query['DestroyCard'] = request.destroy_card
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.show_psim):
            query['ShowPsim'] = request.show_psim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_detail(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_detail_with_options(request, runtime)

    async def get_card_detail_async(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_detail_with_options_async(request, runtime)

    def get_card_flow_info_with_options(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_list):
            query['DateList'] = request.date_list
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardFlowInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_flow_info_with_options_async(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_list):
            query['DateList'] = request.date_list
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardFlowInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_flow_info(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_flow_info_with_options(request, runtime)

    async def get_card_flow_info_async(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_flow_info_with_options_async(request, runtime)

    def get_card_latest_flow_with_options(
        self,
        request: linkcard_20210520_models.GetCardLatestFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardLatestFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardLatestFlow',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardLatestFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_latest_flow_with_options_async(
        self,
        request: linkcard_20210520_models.GetCardLatestFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardLatestFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardLatestFlow',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardLatestFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_latest_flow(
        self,
        request: linkcard_20210520_models.GetCardLatestFlowRequest,
    ) -> linkcard_20210520_models.GetCardLatestFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_latest_flow_with_options(request, runtime)

    async def get_card_latest_flow_async(
        self,
        request: linkcard_20210520_models.GetCardLatestFlowRequest,
    ) -> linkcard_20210520_models.GetCardLatestFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_latest_flow_with_options_async(request, runtime)

    def get_card_real_status_with_options(
        self,
        tmp_req: linkcard_20210520_models.GetCardRealStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardRealStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.GetCardRealStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serial_no):
            request.serial_no_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serial_no, 'SerialNo', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.msisdn):
            query['Msisdn'] = request.msisdn
        if not UtilClient.is_unset(request.serial_no_shrink):
            query['SerialNo'] = request.serial_no_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardRealStatus',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardRealStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_real_status_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.GetCardRealStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardRealStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.GetCardRealStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serial_no):
            request.serial_no_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serial_no, 'SerialNo', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.msisdn):
            query['Msisdn'] = request.msisdn
        if not UtilClient.is_unset(request.serial_no_shrink):
            query['SerialNo'] = request.serial_no_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardRealStatus',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardRealStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_real_status(
        self,
        request: linkcard_20210520_models.GetCardRealStatusRequest,
    ) -> linkcard_20210520_models.GetCardRealStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_real_status_with_options(request, runtime)

    async def get_card_real_status_async(
        self,
        request: linkcard_20210520_models.GetCardRealStatusRequest,
    ) -> linkcard_20210520_models.GetCardRealStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_real_status_with_options_async(request, runtime)

    def get_card_status_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardStatusStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCardStatusStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardStatusStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_status_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardStatusStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCardStatusStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardStatusStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_status_statistics(self) -> linkcard_20210520_models.GetCardStatusStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_status_statistics_with_options(runtime)

    async def get_card_status_statistics_async(self) -> linkcard_20210520_models.GetCardStatusStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_status_statistics_with_options_async(runtime)

    def get_credential_pool_statistics_with_options(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialPoolStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCredentialPoolStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_pool_statistics_with_options_async(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialPoolStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCredentialPoolStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential_pool_statistics(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_credential_pool_statistics_with_options(request, runtime)

    async def get_credential_pool_statistics_async(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_credential_pool_statistics_with_options_async(request, runtime)

    def get_operate_result_with_options(
        self,
        request: linkcard_20210520_models.GetOperateResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetOperateResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product):
            query['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.res_id):
            query['ResId'] = request.res_id
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperateResult',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetOperateResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operate_result_with_options_async(
        self,
        request: linkcard_20210520_models.GetOperateResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetOperateResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product):
            query['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.res_id):
            query['ResId'] = request.res_id
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperateResult',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetOperateResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operate_result(
        self,
        request: linkcard_20210520_models.GetOperateResultRequest,
    ) -> linkcard_20210520_models.GetOperateResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_operate_result_with_options(request, runtime)

    async def get_operate_result_async(
        self,
        request: linkcard_20210520_models.GetOperateResultRequest,
    ) -> linkcard_20210520_models.GetOperateResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_operate_result_with_options_async(request, runtime)

    def get_real_name_status_with_options(
        self,
        tmp_req: linkcard_20210520_models.GetRealNameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetRealNameStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.GetRealNameStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_msisdns):
            request.list_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_msisdns, 'ListMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.list_msisdns_shrink):
            query['ListMsisdns'] = request.list_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealNameStatus',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetRealNameStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_name_status_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.GetRealNameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetRealNameStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.GetRealNameStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_msisdns):
            request.list_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_msisdns, 'ListMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.list_msisdns_shrink):
            query['ListMsisdns'] = request.list_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealNameStatus',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetRealNameStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_name_status(
        self,
        request: linkcard_20210520_models.GetRealNameStatusRequest,
    ) -> linkcard_20210520_models.GetRealNameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_real_name_status_with_options(request, runtime)

    async def get_real_name_status_async(
        self,
        request: linkcard_20210520_models.GetRealNameStatusRequest,
    ) -> linkcard_20210520_models.GetRealNameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_real_name_status_with_options_async(request, runtime)

    def get_sim_card_state_distribution_with_options(
        self,
        request: linkcard_20210520_models.GetSimCardStateDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetSimCardStateDistributionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimCardStateDistribution',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetSimCardStateDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sim_card_state_distribution_with_options_async(
        self,
        request: linkcard_20210520_models.GetSimCardStateDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetSimCardStateDistributionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimCardStateDistribution',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetSimCardStateDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sim_card_state_distribution(
        self,
        request: linkcard_20210520_models.GetSimCardStateDistributionRequest,
    ) -> linkcard_20210520_models.GetSimCardStateDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sim_card_state_distribution_with_options(request, runtime)

    async def get_sim_card_state_distribution_async(
        self,
        request: linkcard_20210520_models.GetSimCardStateDistributionRequest,
    ) -> linkcard_20210520_models.GetSimCardStateDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sim_card_state_distribution_with_options_async(request, runtime)

    def list_card_info_with_options(
        self,
        request: linkcard_20210520_models.ListCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListCardInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_time_end):
            query['ActiveTimeEnd'] = request.active_time_end
        if not UtilClient.is_unset(request.active_time_start):
            query['ActiveTimeStart'] = request.active_time_start
        if not UtilClient.is_unset(request.ali_fee):
            query['AliFee'] = request.ali_fee
        if not UtilClient.is_unset(request.aliyun_order_id):
            query['AliyunOrderId'] = request.aliyun_order_id
        if not UtilClient.is_unset(request.apn_name):
            query['ApnName'] = request.apn_name
        if not UtilClient.is_unset(request.certify_type):
            query['CertifyType'] = request.certify_type
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not UtilClient.is_unset(request.data_level):
            query['DataLevel'] = request.data_level
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directional_group_id):
            query['DirectionalGroupId'] = request.directional_group_id
        if not UtilClient.is_unset(request.expire_time_end):
            query['ExpireTimeEnd'] = request.expire_time_end
        if not UtilClient.is_unset(request.expire_time_start):
            query['ExpireTimeStart'] = request.expire_time_start
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.imsi):
            query['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.is_auto_recharge):
            query['IsAutoRecharge'] = request.is_auto_recharge
        if not UtilClient.is_unset(request.max_flow):
            query['MaxFlow'] = request.max_flow
        if not UtilClient.is_unset(request.max_rest_flow_percentage):
            query['MaxRestFlowPercentage'] = request.max_rest_flow_percentage
        if not UtilClient.is_unset(request.min_flow):
            query['MinFlow'] = request.min_flow
        if not UtilClient.is_unset(request.msisdn):
            query['Msisdn'] = request.msisdn
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.notify_id):
            query['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.os_status):
            query['OsStatus'] = request.os_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pool_id):
            query['PoolId'] = request.pool_id
        if not UtilClient.is_unset(request.sim_type):
            query['SimType'] = request.sim_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListCardInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_card_info_with_options_async(
        self,
        request: linkcard_20210520_models.ListCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListCardInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_time_end):
            query['ActiveTimeEnd'] = request.active_time_end
        if not UtilClient.is_unset(request.active_time_start):
            query['ActiveTimeStart'] = request.active_time_start
        if not UtilClient.is_unset(request.ali_fee):
            query['AliFee'] = request.ali_fee
        if not UtilClient.is_unset(request.aliyun_order_id):
            query['AliyunOrderId'] = request.aliyun_order_id
        if not UtilClient.is_unset(request.apn_name):
            query['ApnName'] = request.apn_name
        if not UtilClient.is_unset(request.certify_type):
            query['CertifyType'] = request.certify_type
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not UtilClient.is_unset(request.data_level):
            query['DataLevel'] = request.data_level
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directional_group_id):
            query['DirectionalGroupId'] = request.directional_group_id
        if not UtilClient.is_unset(request.expire_time_end):
            query['ExpireTimeEnd'] = request.expire_time_end
        if not UtilClient.is_unset(request.expire_time_start):
            query['ExpireTimeStart'] = request.expire_time_start
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.imsi):
            query['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.is_auto_recharge):
            query['IsAutoRecharge'] = request.is_auto_recharge
        if not UtilClient.is_unset(request.max_flow):
            query['MaxFlow'] = request.max_flow
        if not UtilClient.is_unset(request.max_rest_flow_percentage):
            query['MaxRestFlowPercentage'] = request.max_rest_flow_percentage
        if not UtilClient.is_unset(request.min_flow):
            query['MinFlow'] = request.min_flow
        if not UtilClient.is_unset(request.msisdn):
            query['Msisdn'] = request.msisdn
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.notify_id):
            query['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.os_status):
            query['OsStatus'] = request.os_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pool_id):
            query['PoolId'] = request.pool_id
        if not UtilClient.is_unset(request.sim_type):
            query['SimType'] = request.sim_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListCardInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_card_info(
        self,
        request: linkcard_20210520_models.ListCardInfoRequest,
    ) -> linkcard_20210520_models.ListCardInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_card_info_with_options(request, runtime)

    async def list_card_info_async(
        self,
        request: linkcard_20210520_models.ListCardInfoRequest,
    ) -> linkcard_20210520_models.ListCardInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_card_info_with_options_async(request, runtime)

    def list_directional_address_with_options(
        self,
        request: linkcard_20210520_models.ListDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListDirectionalAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directional_address_with_options_async(
        self,
        request: linkcard_20210520_models.ListDirectionalAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListDirectionalAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectionalAddress',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListDirectionalAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directional_address(
        self,
        request: linkcard_20210520_models.ListDirectionalAddressRequest,
    ) -> linkcard_20210520_models.ListDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directional_address_with_options(request, runtime)

    async def list_directional_address_async(
        self,
        request: linkcard_20210520_models.ListDirectionalAddressRequest,
    ) -> linkcard_20210520_models.ListDirectionalAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directional_address_with_options_async(request, runtime)

    def list_directional_detail_with_options(
        self,
        request: linkcard_20210520_models.ListDirectionalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListDirectionalDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectionalDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListDirectionalDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directional_detail_with_options_async(
        self,
        request: linkcard_20210520_models.ListDirectionalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListDirectionalDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectionalDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListDirectionalDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directional_detail(
        self,
        request: linkcard_20210520_models.ListDirectionalDetailRequest,
    ) -> linkcard_20210520_models.ListDirectionalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directional_detail_with_options(request, runtime)

    async def list_directional_detail_async(
        self,
        request: linkcard_20210520_models.ListDirectionalDetailRequest,
    ) -> linkcard_20210520_models.ListDirectionalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directional_detail_with_options_async(request, runtime)

    def list_order_with_options(
        self,
        request: linkcard_20210520_models.ListOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrder',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_order_with_options_async(
        self,
        request: linkcard_20210520_models.ListOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ListOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrder',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_order(
        self,
        request: linkcard_20210520_models.ListOrderRequest,
    ) -> linkcard_20210520_models.ListOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_order_with_options(request, runtime)

    async def list_order_async(
        self,
        request: linkcard_20210520_models.ListOrderRequest,
    ) -> linkcard_20210520_models.ListOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_order_with_options_async(request, runtime)

    def rebind_resume_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.RebindResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.RebindResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RebindResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebind_resume_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.RebindResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.RebindResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RebindResumeSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebind_resume_single_card(
        self,
        request: linkcard_20210520_models.RebindResumeSingleCardRequest,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebind_resume_single_card_with_options(request, runtime)

    async def rebind_resume_single_card_async(
        self,
        request: linkcard_20210520_models.RebindResumeSingleCardRequest,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebind_resume_single_card_with_options_async(request, runtime)

    def renew_with_options(
        self,
        request: linkcard_20210520_models.RenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RenewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_num):
            query['BuyNum'] = request.buy_num
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.offer_code):
            query['OfferCode'] = request.offer_code
        if not UtilClient.is_unset(request.recharge_type):
            query['RechargeType'] = request.recharge_type
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.api_revision):
            body['ApiRevision'] = request.api_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Renew',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_with_options_async(
        self,
        request: linkcard_20210520_models.RenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RenewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_num):
            query['BuyNum'] = request.buy_num
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.offer_code):
            query['OfferCode'] = request.offer_code
        if not UtilClient.is_unset(request.recharge_type):
            query['RechargeType'] = request.recharge_type
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.api_revision):
            body['ApiRevision'] = request.api_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Renew',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew(
        self,
        request: linkcard_20210520_models.RenewRequest,
    ) -> linkcard_20210520_models.RenewResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_with_options(request, runtime)

    async def renew_async(
        self,
        request: linkcard_20210520_models.RenewRequest,
    ) -> linkcard_20210520_models.RenewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_with_options_async(request, runtime)

    def resume_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.ResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.ResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.ResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.ResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ResumeSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_single_card(
        self,
        request: linkcard_20210520_models.ResumeSingleCardRequest,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_single_card_with_options(request, runtime)

    async def resume_single_card_async(
        self,
        request: linkcard_20210520_models.ResumeSingleCardRequest,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_single_card_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        tmp_req: linkcard_20210520_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.msisdns):
            request.msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.msisdns, 'Msisdns', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.message_send_time):
            body['MessageSendTime'] = request.message_send_time
        if not UtilClient.is_unset(request.message_template_id):
            body['MessageTemplateId'] = request.message_template_id
        if not UtilClient.is_unset(request.message_variable_param):
            body['MessageVariableParam'] = request.message_variable_param
        if not UtilClient.is_unset(request.msisdns_shrink):
            body['Msisdns'] = request.msisdns_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.msisdns):
            request.msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.msisdns, 'Msisdns', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.message_send_time):
            body['MessageSendTime'] = request.message_send_time
        if not UtilClient.is_unset(request.message_template_id):
            body['MessageTemplateId'] = request.message_template_id
        if not UtilClient.is_unset(request.message_variable_param):
            body['MessageVariableParam'] = request.message_variable_param
        if not UtilClient.is_unset(request.msisdns_shrink):
            body['Msisdns'] = request.msisdns_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: linkcard_20210520_models.SendMessageRequest,
    ) -> linkcard_20210520_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: linkcard_20210520_models.SendMessageRequest,
    ) -> linkcard_20210520_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def set_card_stop_rule_with_options(
        self,
        request: linkcard_20210520_models.SetCardStopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.SetCardStopRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_restore):
            query['AutoRestore'] = request.auto_restore
        if not UtilClient.is_unset(request.flow_limit):
            query['FlowLimit'] = request.flow_limit
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCardStopRule',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.SetCardStopRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_card_stop_rule_with_options_async(
        self,
        request: linkcard_20210520_models.SetCardStopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.SetCardStopRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_restore):
            query['AutoRestore'] = request.auto_restore
        if not UtilClient.is_unset(request.flow_limit):
            query['FlowLimit'] = request.flow_limit
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCardStopRule',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.SetCardStopRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_card_stop_rule(
        self,
        request: linkcard_20210520_models.SetCardStopRuleRequest,
    ) -> linkcard_20210520_models.SetCardStopRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_card_stop_rule_with_options(request, runtime)

    async def set_card_stop_rule_async(
        self,
        request: linkcard_20210520_models.SetCardStopRuleRequest,
    ) -> linkcard_20210520_models.SetCardStopRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_card_stop_rule_with_options_async(request, runtime)

    def stop_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.StopSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.StopSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.StopSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.StopSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.StopSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.StopSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_single_card(
        self,
        request: linkcard_20210520_models.StopSingleCardRequest,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_single_card_with_options(request, runtime)

    async def stop_single_card_async(
        self,
        request: linkcard_20210520_models.StopSingleCardRequest,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_single_card_with_options_async(request, runtime)

    def update_auto_recharge_switch_with_options(
        self,
        request: linkcard_20210520_models.UpdateAutoRechargeSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.UpdateAutoRechargeSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoRechargeSwitch',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.UpdateAutoRechargeSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_recharge_switch_with_options_async(
        self,
        request: linkcard_20210520_models.UpdateAutoRechargeSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.UpdateAutoRechargeSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoRechargeSwitch',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.UpdateAutoRechargeSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_recharge_switch(
        self,
        request: linkcard_20210520_models.UpdateAutoRechargeSwitchRequest,
    ) -> linkcard_20210520_models.UpdateAutoRechargeSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_recharge_switch_with_options(request, runtime)

    async def update_auto_recharge_switch_async(
        self,
        request: linkcard_20210520_models.UpdateAutoRechargeSwitchRequest,
    ) -> linkcard_20210520_models.UpdateAutoRechargeSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_recharge_switch_with_options_async(request, runtime)

    def verify_iot_card_with_options(
        self,
        request: linkcard_20210520_models.VerifyIotCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.VerifyIotCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyIotCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.VerifyIotCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_iot_card_with_options_async(
        self,
        request: linkcard_20210520_models.VerifyIotCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.VerifyIotCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyIotCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.VerifyIotCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_iot_card(
        self,
        request: linkcard_20210520_models.VerifyIotCardRequest,
    ) -> linkcard_20210520_models.VerifyIotCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_iot_card_with_options(request, runtime)

    async def verify_iot_card_async(
        self,
        request: linkcard_20210520_models.VerifyIotCardRequest,
    ) -> linkcard_20210520_models.VerifyIotCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_iot_card_with_options_async(request, runtime)
