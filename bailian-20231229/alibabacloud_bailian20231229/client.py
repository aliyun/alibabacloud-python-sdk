# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailian20231229 import models as bailian_20231229_models
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
        self._endpoint = self.get_endpoint('bailian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_file_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not UtilClient.is_unset(request.parser):
            body['Parser'] = request.parser
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_file_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not UtilClient.is_unset(request.parser):
            body['Parser'] = request.parser
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_file(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @return: AddFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_file_with_options(workspace_id, request, headers, runtime)

    async def add_file_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @return: AddFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_file_with_options_async(workspace_id, request, headers, runtime)

    def apply_file_upload_lease_with_options(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFileUploadLeaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            body['Md5'] = request.md_5
        if not UtilClient.is_unset(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyFileUploadLease',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ApplyFileUploadLeaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_file_upload_lease_with_options_async(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFileUploadLeaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            body['Md5'] = request.md_5
        if not UtilClient.is_unset(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyFileUploadLease',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ApplyFileUploadLeaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_file_upload_lease(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @return: ApplyFileUploadLeaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_file_upload_lease_with_options(category_id, workspace_id, request, headers, runtime)

    async def apply_file_upload_lease_async(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @return: ApplyFileUploadLeaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_file_upload_lease_with_options_async(category_id, workspace_id, request, headers, runtime)

    def describe_file_with_options(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DescribeFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_with_options_async(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DescribeFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file(
        self,
        workspace_id: str,
        file_id: str,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @return: DescribeFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_file_with_options(workspace_id, file_id, headers, runtime)

    async def describe_file_async(
        self,
        workspace_id: str,
        file_id: str,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @return: DescribeFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_file_with_options_async(workspace_id, file_id, headers, runtime)
