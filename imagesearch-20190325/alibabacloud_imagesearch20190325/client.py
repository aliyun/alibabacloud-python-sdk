# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imagesearch20190325 import models as image_search_20190325_models
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
        self._endpoint = self.get_endpoint('imagesearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image(
        self,
        request: image_search_20190325_models.AddImageRequest,
    ) -> image_search_20190325_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(request, headers, runtime)

    async def add_image_async(
        self,
        request: image_search_20190325_models.AddImageRequest,
    ) -> image_search_20190325_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(request, headers, runtime)

    def add_image_with_options(
        self,
        request: image_search_20190325_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.AddImageResponse(),
            self.do_roarequest_with_form('AddImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/add', 'json', req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: image_search_20190325_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.AddImageResponse(),
            await self.do_roarequest_with_form_async('AddImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/add', 'json', req, runtime)
        )

    def delete_image(
        self,
        request: image_search_20190325_models.DeleteImageRequest,
    ) -> image_search_20190325_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_image_with_options(request, headers, runtime)

    async def delete_image_async(
        self,
        request: image_search_20190325_models.DeleteImageRequest,
    ) -> image_search_20190325_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_image_with_options_async(request, headers, runtime)

    def delete_image_with_options(
        self,
        request: image_search_20190325_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.DeleteImageResponse(),
            self.do_roarequest_with_form('DeleteImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/delete', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: image_search_20190325_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.DeleteImageResponse(),
            await self.do_roarequest_with_form_async('DeleteImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/delete', 'json', req, runtime)
        )

    def search_image(
        self,
        request: image_search_20190325_models.SearchImageRequest,
    ) -> image_search_20190325_models.SearchImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_image_with_options(request, headers, runtime)

    async def search_image_async(
        self,
        request: image_search_20190325_models.SearchImageRequest,
    ) -> image_search_20190325_models.SearchImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_image_with_options_async(request, headers, runtime)

    def search_image_with_options(
        self,
        request: image_search_20190325_models.SearchImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.SearchImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.SearchImageResponse(),
            self.do_roarequest_with_form('SearchImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/search', 'json', req, runtime)
        )

    async def search_image_with_options_async(
        self,
        request: image_search_20190325_models.SearchImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20190325_models.SearchImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            image_search_20190325_models.SearchImageResponse(),
            await self.do_roarequest_with_form_async('SearchImage', '2019-03-25', 'HTTPS', 'POST', 'AK', f'/v2/image/search', 'json', req, runtime)
        )
