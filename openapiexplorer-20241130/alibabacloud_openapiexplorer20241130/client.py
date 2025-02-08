# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openapiexplorer20241130 import models as open_apiexplorer_20241130_models
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
        self._endpoint = self.get_endpoint('openapiexplorer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_error_code_solutions_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary 根据提供的错误码获取对应的解决方案
        
        @description ## 请求说明
        - 本接口支持通过POST或GET方法调用。
        - `Accept-Language`请求头必须设置为`zh-CN`或`en-US`之一，用于指定返回结果的语言类型。
        - 错误码格式需符合特定规则，特别是针对OSS的错误码应遵循正则表达式`[0-9]{4}-[0-9]{8}`。
        - 当前实现中未使用`maxResults`和`nextToken`参数。
        - 如果请求失败，将根据不同的错误情况返回相应的错误代码及描述信息。
        
        @param request: GetErrorCodeSolutionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorCodeSolutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_message):
            query['errorMessage'] = request.error_message
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorCodeSolutions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getErrorCodeSolutions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_error_code_solutions_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary 根据提供的错误码获取对应的解决方案
        
        @description ## 请求说明
        - 本接口支持通过POST或GET方法调用。
        - `Accept-Language`请求头必须设置为`zh-CN`或`en-US`之一，用于指定返回结果的语言类型。
        - 错误码格式需符合特定规则，特别是针对OSS的错误码应遵循正则表达式`[0-9]{4}-[0-9]{8}`。
        - 当前实现中未使用`maxResults`和`nextToken`参数。
        - 如果请求失败，将根据不同的错误情况返回相应的错误代码及描述信息。
        
        @param request: GetErrorCodeSolutionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorCodeSolutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_message):
            query['errorMessage'] = request.error_message
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorCodeSolutions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getErrorCodeSolutions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_error_code_solutions(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary 根据提供的错误码获取对应的解决方案
        
        @description ## 请求说明
        - 本接口支持通过POST或GET方法调用。
        - `Accept-Language`请求头必须设置为`zh-CN`或`en-US`之一，用于指定返回结果的语言类型。
        - 错误码格式需符合特定规则，特别是针对OSS的错误码应遵循正则表达式`[0-9]{4}-[0-9]{8}`。
        - 当前实现中未使用`maxResults`和`nextToken`参数。
        - 如果请求失败，将根据不同的错误情况返回相应的错误代码及描述信息。
        
        @param request: GetErrorCodeSolutionsRequest
        @return: GetErrorCodeSolutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_error_code_solutions_with_options(request, headers, runtime)

    async def get_error_code_solutions_async(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary 根据提供的错误码获取对应的解决方案
        
        @description ## 请求说明
        - 本接口支持通过POST或GET方法调用。
        - `Accept-Language`请求头必须设置为`zh-CN`或`en-US`之一，用于指定返回结果的语言类型。
        - 错误码格式需符合特定规则，特别是针对OSS的错误码应遵循正则表达式`[0-9]{4}-[0-9]{8}`。
        - 当前实现中未使用`maxResults`和`nextToken`参数。
        - 如果请求失败，将根据不同的错误情况返回相应的错误代码及描述信息。
        
        @param request: GetErrorCodeSolutionsRequest
        @return: GetErrorCodeSolutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_error_code_solutions_with_options_async(request, headers, runtime)

    def get_own_request_log_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary 通过API RequestId 查询当前账号调用OpenAPI的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetOwnRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOwnRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getOwnRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
                self.execute(params, req, runtime)
            )

    async def get_own_request_log_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary 通过API RequestId 查询当前账号调用OpenAPI的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetOwnRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOwnRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getOwnRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_own_request_log(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary 通过API RequestId 查询当前账号调用OpenAPI的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetOwnRequestLogRequest
        @return: GetOwnRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_own_request_log_with_options(request, headers, runtime)

    async def get_own_request_log_async(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary 通过API RequestId 查询当前账号调用OpenAPI的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetOwnRequestLogRequest
        @return: GetOwnRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_own_request_log_with_options_async(request, headers, runtime)

    def get_request_log_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary 通过API请求ID查询特定请求的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetRequestLogResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetRequestLogResponse(),
                self.execute(params, req, runtime)
            )

    async def get_request_log_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary 通过API请求ID查询特定请求的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetRequestLogResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                open_apiexplorer_20241130_models.GetRequestLogResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_request_log(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary 通过API请求ID查询特定请求的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetRequestLogRequest
        @return: GetRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_request_log_with_options(request, headers, runtime)

    async def get_request_log_async(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary 通过API请求ID查询特定请求的日志详情，用于故障排查。
        
        @description ## 请求说明
        - 本接口主要用于帮助用户通过提供具体的`apiRequestId`来获取相关API请求的详细日志信息。
        - `apiRequestId`必须是大写形式的UUID，并且应确保该ID确实来自于您之前对某个OpenAPI的实际调用。
        - 如果提供的`apiRequestId`无效或者没有找到对应的日志记录，系统将返回相应的错误提示。
        - 在使用此接口时，请注意检查您的网络环境以及权限设置，以保证能够顺利访问到所需资源。
        
        @param request: GetRequestLogRequest
        @return: GetRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_request_log_with_options_async(request, headers, runtime)
