# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alicloudproc20240104 import models as alicloudproc_20240104_models
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
        self._endpoint = self.get_endpoint('alicloudproc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_sourcing_project_with_options(
        self,
        tmp_req: alicloudproc_20240104_models.CreateSourcingProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alicloudproc_20240104_models.CreateSourcingProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = alicloudproc_20240104_models.CreateSourcingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.company):
            request.company_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company, 'Company', 'json')
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        if not UtilClient.is_unset(tmp_req.subjects):
            request.subjects_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subjects, 'Subjects', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_no):
            query['BizNo'] = request.biz_no
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.company_shrink):
            query['Company'] = request.company_shrink
        if not UtilClient.is_unset(request.contact_shrink):
            query['Contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.sub_biz_type):
            query['SubBizType'] = request.sub_biz_type
        if not UtilClient.is_unset(request.subjects_shrink):
            query['Subjects'] = request.subjects_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSourcingProject',
            version='2024-01-04',
            protocol='HTTPS',
            pathname=f'/srm/lite/sourcing/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alicloudproc_20240104_models.CreateSourcingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sourcing_project_with_options_async(
        self,
        tmp_req: alicloudproc_20240104_models.CreateSourcingProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alicloudproc_20240104_models.CreateSourcingProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = alicloudproc_20240104_models.CreateSourcingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.company):
            request.company_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company, 'Company', 'json')
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        if not UtilClient.is_unset(tmp_req.subjects):
            request.subjects_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subjects, 'Subjects', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_no):
            query['BizNo'] = request.biz_no
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.company_shrink):
            query['Company'] = request.company_shrink
        if not UtilClient.is_unset(request.contact_shrink):
            query['Contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.sub_biz_type):
            query['SubBizType'] = request.sub_biz_type
        if not UtilClient.is_unset(request.subjects_shrink):
            query['Subjects'] = request.subjects_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSourcingProject',
            version='2024-01-04',
            protocol='HTTPS',
            pathname=f'/srm/lite/sourcing/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alicloudproc_20240104_models.CreateSourcingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sourcing_project(
        self,
        request: alicloudproc_20240104_models.CreateSourcingProjectRequest,
    ) -> alicloudproc_20240104_models.CreateSourcingProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sourcing_project_with_options(request, headers, runtime)

    async def create_sourcing_project_async(
        self,
        request: alicloudproc_20240104_models.CreateSourcingProjectRequest,
    ) -> alicloudproc_20240104_models.CreateSourcingProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sourcing_project_with_options_async(request, headers, runtime)

    def update_sourcing_project_with_options(
        self,
        request: alicloudproc_20240104_models.UpdateSourcingProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alicloudproc_20240104_models.UpdateSourcingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.update_time):
            query['UpdateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSourcingProject',
            version='2024-01-04',
            protocol='HTTPS',
            pathname=f'/srm/lite/sourcing/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alicloudproc_20240104_models.UpdateSourcingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sourcing_project_with_options_async(
        self,
        request: alicloudproc_20240104_models.UpdateSourcingProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alicloudproc_20240104_models.UpdateSourcingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.update_time):
            query['UpdateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSourcingProject',
            version='2024-01-04',
            protocol='HTTPS',
            pathname=f'/srm/lite/sourcing/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alicloudproc_20240104_models.UpdateSourcingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sourcing_project(
        self,
        request: alicloudproc_20240104_models.UpdateSourcingProjectRequest,
    ) -> alicloudproc_20240104_models.UpdateSourcingProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sourcing_project_with_options(request, headers, runtime)

    async def update_sourcing_project_async(
        self,
        request: alicloudproc_20240104_models.UpdateSourcingProjectRequest,
    ) -> alicloudproc_20240104_models.UpdateSourcingProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sourcing_project_with_options_async(request, headers, runtime)
