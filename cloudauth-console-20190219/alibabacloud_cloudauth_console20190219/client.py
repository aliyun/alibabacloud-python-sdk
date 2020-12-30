# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth_console20190219 import models as cloudauth_console_20190219_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth-console', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_project_with_options(
        self,
        request: cloudauth_console_20190219_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.CreateProjectResponse().from_map(
            self.do_rpcrequest('CreateProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: cloudauth_console_20190219_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.CreateProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: cloudauth_console_20190219_models.CreateProjectRequest,
    ) -> cloudauth_console_20190219_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: cloudauth_console_20190219_models.CreateProjectRequest,
    ) -> cloudauth_console_20190219_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_slr_role_with_options(
        self,
        request: cloudauth_console_20190219_models.CreateSlrRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.CreateSlrRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.CreateSlrRoleResponse().from_map(
            self.do_rpcrequest('CreateSlrRole', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_slr_role_with_options_async(
        self,
        request: cloudauth_console_20190219_models.CreateSlrRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.CreateSlrRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.CreateSlrRoleResponse().from_map(
            await self.do_rpcrequest_async('CreateSlrRole', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_slr_role(
        self,
        request: cloudauth_console_20190219_models.CreateSlrRoleRequest,
    ) -> cloudauth_console_20190219_models.CreateSlrRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_slr_role_with_options(request, runtime)

    async def create_slr_role_async(
        self,
        request: cloudauth_console_20190219_models.CreateSlrRoleRequest,
    ) -> cloudauth_console_20190219_models.CreateSlrRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_slr_role_with_options_async(request, runtime)

    def delete_mns_serve_with_options(
        self,
        request: cloudauth_console_20190219_models.DeleteMnsServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteMnsServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteMnsServeResponse().from_map(
            self.do_rpcrequest('DeleteMnsServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mns_serve_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DeleteMnsServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteMnsServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteMnsServeResponse().from_map(
            await self.do_rpcrequest_async('DeleteMnsServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mns_serve(
        self,
        request: cloudauth_console_20190219_models.DeleteMnsServeRequest,
    ) -> cloudauth_console_20190219_models.DeleteMnsServeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mns_serve_with_options(request, runtime)

    async def delete_mns_serve_async(
        self,
        request: cloudauth_console_20190219_models.DeleteMnsServeRequest,
    ) -> cloudauth_console_20190219_models.DeleteMnsServeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mns_serve_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: cloudauth_console_20190219_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteUserGroupResponse().from_map(
            self.do_rpcrequest('DeleteUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_group(
        self,
        request: cloudauth_console_20190219_models.DeleteUserGroupRequest,
    ) -> cloudauth_console_20190219_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: cloudauth_console_20190219_models.DeleteUserGroupRequest,
    ) -> cloudauth_console_20190219_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def delete_user_info_with_options(
        self,
        request: cloudauth_console_20190219_models.DeleteUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteUserInfoResponse().from_map(
            self.do_rpcrequest('DeleteUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_info_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DeleteUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DeleteUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DeleteUserInfoResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_info(
        self,
        request: cloudauth_console_20190219_models.DeleteUserInfoRequest,
    ) -> cloudauth_console_20190219_models.DeleteUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_info_with_options(request, runtime)

    async def delete_user_info_async(
        self,
        request: cloudauth_console_20190219_models.DeleteUserInfoRequest,
    ) -> cloudauth_console_20190219_models.DeleteUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_info_with_options_async(request, runtime)

    def describe_all_end_point_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeAllEndPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeAllEndPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeAllEndPointResponse().from_map(
            self.do_rpcrequest('DescribeAllEndPoint', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_end_point_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeAllEndPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeAllEndPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeAllEndPointResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllEndPoint', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_end_point(
        self,
        request: cloudauth_console_20190219_models.DescribeAllEndPointRequest,
    ) -> cloudauth_console_20190219_models.DescribeAllEndPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_end_point_with_options(request, runtime)

    async def describe_all_end_point_async(
        self,
        request: cloudauth_console_20190219_models.DescribeAllEndPointRequest,
    ) -> cloudauth_console_20190219_models.DescribeAllEndPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_end_point_with_options_async(request, runtime)

    def describe_bind_user_id_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeBindUserIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeBindUserIdListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeBindUserIdListResponse().from_map(
            self.do_rpcrequest('DescribeBindUserIdList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bind_user_id_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeBindUserIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeBindUserIdListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeBindUserIdListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBindUserIdList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bind_user_id_list(
        self,
        request: cloudauth_console_20190219_models.DescribeBindUserIdListRequest,
    ) -> cloudauth_console_20190219_models.DescribeBindUserIdListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bind_user_id_list_with_options(request, runtime)

    async def describe_bind_user_id_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeBindUserIdListRequest,
    ) -> cloudauth_console_20190219_models.DescribeBindUserIdListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bind_user_id_list_with_options_async(request, runtime)

    def describe_certificate_type_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeCertificateTypeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeCertificateTypeListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeCertificateTypeListResponse().from_map(
            self.do_rpcrequest('DescribeCertificateTypeList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_certificate_type_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeCertificateTypeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeCertificateTypeListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeCertificateTypeListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertificateTypeList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certificate_type_list(
        self,
        request: cloudauth_console_20190219_models.DescribeCertificateTypeListRequest,
    ) -> cloudauth_console_20190219_models.DescribeCertificateTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_type_list_with_options(request, runtime)

    async def describe_certificate_type_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeCertificateTypeListRequest,
    ) -> cloudauth_console_20190219_models.DescribeCertificateTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_type_list_with_options_async(request, runtime)

    def describe_device_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeDeviceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeDeviceListResponse().from_map(
            self.do_rpcrequest('DescribeDeviceList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeDeviceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeDeviceListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_list(
        self,
        request: cloudauth_console_20190219_models.DescribeDeviceListRequest,
    ) -> cloudauth_console_20190219_models.DescribeDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_list_with_options(request, runtime)

    async def describe_device_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeDeviceListRequest,
    ) -> cloudauth_console_20190219_models.DescribeDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_list_with_options_async(request, runtime)

    def describe_excel_analysis_result_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeExcelAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse().from_map(
            self.do_rpcrequest('DescribeExcelAnalysisResult', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_excel_analysis_result_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeExcelAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeExcelAnalysisResult', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_excel_analysis_result(
        self,
        request: cloudauth_console_20190219_models.DescribeExcelAnalysisResultRequest,
    ) -> cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_excel_analysis_result_with_options(request, runtime)

    async def describe_excel_analysis_result_async(
        self,
        request: cloudauth_console_20190219_models.DescribeExcelAnalysisResultRequest,
    ) -> cloudauth_console_20190219_models.DescribeExcelAnalysisResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_excel_analysis_result_with_options_async(request, runtime)

    def describe_identify_record_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeIdentifyRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse().from_map(
            self.do_rpcrequest('DescribeIdentifyRecordList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_identify_record_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeIdentifyRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse().from_map(
            await self.do_rpcrequest_async('DescribeIdentifyRecordList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_identify_record_list(
        self,
        request: cloudauth_console_20190219_models.DescribeIdentifyRecordListRequest,
    ) -> cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_identify_record_list_with_options(request, runtime)

    async def describe_identify_record_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeIdentifyRecordListRequest,
    ) -> cloudauth_console_20190219_models.DescribeIdentifyRecordListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_identify_record_list_with_options_async(request, runtime)

    def describe_mns_oauth_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeMnsOauthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeMnsOauthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeMnsOauthResponse().from_map(
            self.do_rpcrequest('DescribeMnsOauth', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mns_oauth_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeMnsOauthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeMnsOauthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeMnsOauthResponse().from_map(
            await self.do_rpcrequest_async('DescribeMnsOauth', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mns_oauth(
        self,
        request: cloudauth_console_20190219_models.DescribeMnsOauthRequest,
    ) -> cloudauth_console_20190219_models.DescribeMnsOauthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mns_oauth_with_options(request, runtime)

    async def describe_mns_oauth_async(
        self,
        request: cloudauth_console_20190219_models.DescribeMnsOauthRequest,
    ) -> cloudauth_console_20190219_models.DescribeMnsOauthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mns_oauth_with_options_async(request, runtime)

    def describe_oss_oauth_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeOssOauthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeOssOauthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeOssOauthResponse().from_map(
            self.do_rpcrequest('DescribeOssOauth', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_oauth_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeOssOauthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeOssOauthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeOssOauthResponse().from_map(
            await self.do_rpcrequest_async('DescribeOssOauth', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_oauth(
        self,
        request: cloudauth_console_20190219_models.DescribeOssOauthRequest,
    ) -> cloudauth_console_20190219_models.DescribeOssOauthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_oauth_with_options(request, runtime)

    async def describe_oss_oauth_async(
        self,
        request: cloudauth_console_20190219_models.DescribeOssOauthRequest,
    ) -> cloudauth_console_20190219_models.DescribeOssOauthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_oauth_with_options_async(request, runtime)

    def describe_signed_url_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeSignedUrlResponse().from_map(
            self.do_rpcrequest('DescribeSignedUrl', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_signed_url_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeSignedUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeSignedUrl', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_signed_url(
        self,
        request: cloudauth_console_20190219_models.DescribeSignedUrlRequest,
    ) -> cloudauth_console_20190219_models.DescribeSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_signed_url_with_options(request, runtime)

    async def describe_signed_url_async(
        self,
        request: cloudauth_console_20190219_models.DescribeSignedUrlRequest,
    ) -> cloudauth_console_20190219_models.DescribeSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_signed_url_with_options_async(request, runtime)

    def describe_topic_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeTopicResponse().from_map(
            self.do_rpcrequest('DescribeTopic', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_topic_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeTopicResponse().from_map(
            await self.do_rpcrequest_async('DescribeTopic', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_topic(
        self,
        request: cloudauth_console_20190219_models.DescribeTopicRequest,
    ) -> cloudauth_console_20190219_models.DescribeTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_topic_with_options(request, runtime)

    async def describe_topic_async(
        self,
        request: cloudauth_console_20190219_models.DescribeTopicRequest,
    ) -> cloudauth_console_20190219_models.DescribeTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_topic_with_options_async(request, runtime)

    def describe_upload_pre_sign_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeUploadPreSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUploadPreSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUploadPreSignResponse().from_map(
            self.do_rpcrequest('DescribeUploadPreSign', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_upload_pre_sign_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUploadPreSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUploadPreSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUploadPreSignResponse().from_map(
            await self.do_rpcrequest_async('DescribeUploadPreSign', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upload_pre_sign(
        self,
        request: cloudauth_console_20190219_models.DescribeUploadPreSignRequest,
    ) -> cloudauth_console_20190219_models.DescribeUploadPreSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_pre_sign_with_options(request, runtime)

    async def describe_upload_pre_sign_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUploadPreSignRequest,
    ) -> cloudauth_console_20190219_models.DescribeUploadPreSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_pre_sign_with_options_async(request, runtime)

    def describe_user_group_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeUserGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUserGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUserGroupListResponse().from_map(
            self.do_rpcrequest('DescribeUserGroupList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_group_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUserGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUserGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUserGroupListResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserGroupList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_group_list(
        self,
        request: cloudauth_console_20190219_models.DescribeUserGroupListRequest,
    ) -> cloudauth_console_20190219_models.DescribeUserGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_group_list_with_options(request, runtime)

    async def describe_user_group_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUserGroupListRequest,
    ) -> cloudauth_console_20190219_models.DescribeUserGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_group_list_with_options_async(request, runtime)

    def describe_user_info_list_with_options(
        self,
        request: cloudauth_console_20190219_models.DescribeUserInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUserInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUserInfoListResponse().from_map(
            self.do_rpcrequest('DescribeUserInfoList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_info_list_with_options_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUserInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.DescribeUserInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.DescribeUserInfoListResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserInfoList', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_info_list(
        self,
        request: cloudauth_console_20190219_models.DescribeUserInfoListRequest,
    ) -> cloudauth_console_20190219_models.DescribeUserInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_list_with_options(request, runtime)

    async def describe_user_info_list_async(
        self,
        request: cloudauth_console_20190219_models.DescribeUserInfoListRequest,
    ) -> cloudauth_console_20190219_models.DescribeUserInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_info_list_with_options_async(request, runtime)

    def get_account_project_with_options(
        self,
        request: cloudauth_console_20190219_models.GetAccountProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.GetAccountProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.GetAccountProjectResponse().from_map(
            self.do_rpcrequest('GetAccountProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_project_with_options_async(
        self,
        request: cloudauth_console_20190219_models.GetAccountProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.GetAccountProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.GetAccountProjectResponse().from_map(
            await self.do_rpcrequest_async('GetAccountProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_project(
        self,
        request: cloudauth_console_20190219_models.GetAccountProjectRequest,
    ) -> cloudauth_console_20190219_models.GetAccountProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_project_with_options(request, runtime)

    async def get_account_project_async(
        self,
        request: cloudauth_console_20190219_models.GetAccountProjectRequest,
    ) -> cloudauth_console_20190219_models.GetAccountProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_project_with_options_async(request, runtime)

    def save_mns_serve_with_options(
        self,
        request: cloudauth_console_20190219_models.SaveMnsServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveMnsServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveMnsServeResponse().from_map(
            self.do_rpcrequest('SaveMnsServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_mns_serve_with_options_async(
        self,
        request: cloudauth_console_20190219_models.SaveMnsServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveMnsServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveMnsServeResponse().from_map(
            await self.do_rpcrequest_async('SaveMnsServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_mns_serve(
        self,
        request: cloudauth_console_20190219_models.SaveMnsServeRequest,
    ) -> cloudauth_console_20190219_models.SaveMnsServeResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_mns_serve_with_options(request, runtime)

    async def save_mns_serve_async(
        self,
        request: cloudauth_console_20190219_models.SaveMnsServeRequest,
    ) -> cloudauth_console_20190219_models.SaveMnsServeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_mns_serve_with_options_async(request, runtime)

    def save_oss_serve_with_options(
        self,
        request: cloudauth_console_20190219_models.SaveOssServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveOssServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveOssServeResponse().from_map(
            self.do_rpcrequest('SaveOssServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_oss_serve_with_options_async(
        self,
        request: cloudauth_console_20190219_models.SaveOssServeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveOssServeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveOssServeResponse().from_map(
            await self.do_rpcrequest_async('SaveOssServe', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_oss_serve(
        self,
        request: cloudauth_console_20190219_models.SaveOssServeRequest,
    ) -> cloudauth_console_20190219_models.SaveOssServeResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_oss_serve_with_options(request, runtime)

    async def save_oss_serve_async(
        self,
        request: cloudauth_console_20190219_models.SaveOssServeRequest,
    ) -> cloudauth_console_20190219_models.SaveOssServeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_oss_serve_with_options_async(request, runtime)

    def save_user_group_with_options(
        self,
        request: cloudauth_console_20190219_models.SaveUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveUserGroupResponse().from_map(
            self.do_rpcrequest('SaveUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_user_group_with_options_async(
        self,
        request: cloudauth_console_20190219_models.SaveUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveUserGroupResponse().from_map(
            await self.do_rpcrequest_async('SaveUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_user_group(
        self,
        request: cloudauth_console_20190219_models.SaveUserGroupRequest,
    ) -> cloudauth_console_20190219_models.SaveUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_user_group_with_options(request, runtime)

    async def save_user_group_async(
        self,
        request: cloudauth_console_20190219_models.SaveUserGroupRequest,
    ) -> cloudauth_console_20190219_models.SaveUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_user_group_with_options_async(request, runtime)

    def save_user_info_with_options(
        self,
        request: cloudauth_console_20190219_models.SaveUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveUserInfoResponse().from_map(
            self.do_rpcrequest('SaveUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_user_info_with_options_async(
        self,
        request: cloudauth_console_20190219_models.SaveUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.SaveUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.SaveUserInfoResponse().from_map(
            await self.do_rpcrequest_async('SaveUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_user_info(
        self,
        request: cloudauth_console_20190219_models.SaveUserInfoRequest,
    ) -> cloudauth_console_20190219_models.SaveUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_user_info_with_options(request, runtime)

    async def save_user_info_async(
        self,
        request: cloudauth_console_20190219_models.SaveUserInfoRequest,
    ) -> cloudauth_console_20190219_models.SaveUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_user_info_with_options_async(request, runtime)

    def unbind_device_with_options(
        self,
        request: cloudauth_console_20190219_models.UnbindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UnbindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UnbindDeviceResponse().from_map(
            self.do_rpcrequest('UnbindDevice', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_device_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UnbindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UnbindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UnbindDeviceResponse().from_map(
            await self.do_rpcrequest_async('UnbindDevice', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_device(
        self,
        request: cloudauth_console_20190219_models.UnbindDeviceRequest,
    ) -> cloudauth_console_20190219_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_device_with_options(request, runtime)

    async def unbind_device_async(
        self,
        request: cloudauth_console_20190219_models.UnbindDeviceRequest,
    ) -> cloudauth_console_20190219_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_device_with_options_async(request, runtime)

    def update_device_control_info_with_options(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceControlInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse().from_map(
            self.do_rpcrequest('UpdateDeviceControlInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_control_info_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceControlInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse().from_map(
            await self.do_rpcrequest_async('UpdateDeviceControlInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_control_info(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceControlInfoRequest,
    ) -> cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_control_info_with_options(request, runtime)

    async def update_device_control_info_async(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceControlInfoRequest,
    ) -> cloudauth_console_20190219_models.UpdateDeviceControlInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_control_info_with_options_async(request, runtime)

    def update_device_name_with_options(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateDeviceNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateDeviceNameResponse().from_map(
            self.do_rpcrequest('UpdateDeviceName', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_name_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateDeviceNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateDeviceNameResponse().from_map(
            await self.do_rpcrequest_async('UpdateDeviceName', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_name(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceNameRequest,
    ) -> cloudauth_console_20190219_models.UpdateDeviceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_name_with_options(request, runtime)

    async def update_device_name_async(
        self,
        request: cloudauth_console_20190219_models.UpdateDeviceNameRequest,
    ) -> cloudauth_console_20190219_models.UpdateDeviceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_name_with_options_async(request, runtime)

    def update_project_name_with_options(
        self,
        request: cloudauth_console_20190219_models.UpdateProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateProjectNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateProjectNameResponse().from_map(
            self.do_rpcrequest('UpdateProjectName', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_name_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UpdateProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateProjectNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateProjectNameResponse().from_map(
            await self.do_rpcrequest_async('UpdateProjectName', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project_name(
        self,
        request: cloudauth_console_20190219_models.UpdateProjectNameRequest,
    ) -> cloudauth_console_20190219_models.UpdateProjectNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_name_with_options(request, runtime)

    async def update_project_name_async(
        self,
        request: cloudauth_console_20190219_models.UpdateProjectNameRequest,
    ) -> cloudauth_console_20190219_models.UpdateProjectNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_name_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: cloudauth_console_20190219_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateUserGroupResponse().from_map(
            self.do_rpcrequest('UpdateUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateUserGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateUserGroup', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user_group(
        self,
        request: cloudauth_console_20190219_models.UpdateUserGroupRequest,
    ) -> cloudauth_console_20190219_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: cloudauth_console_20190219_models.UpdateUserGroupRequest,
    ) -> cloudauth_console_20190219_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_user_info_with_options(
        self,
        request: cloudauth_console_20190219_models.UpdateUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateUserInfoResponse().from_map(
            self.do_rpcrequest('UpdateUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_info_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UpdateUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UpdateUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UpdateUserInfoResponse().from_map(
            await self.do_rpcrequest_async('UpdateUserInfo', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user_info(
        self,
        request: cloudauth_console_20190219_models.UpdateUserInfoRequest,
    ) -> cloudauth_console_20190219_models.UpdateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_info_with_options(request, runtime)

    async def update_user_info_async(
        self,
        request: cloudauth_console_20190219_models.UpdateUserInfoRequest,
    ) -> cloudauth_console_20190219_models.UpdateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_info_with_options_async(request, runtime)

    def upload_identify_record_with_options(
        self,
        request: cloudauth_console_20190219_models.UploadIdentifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UploadIdentifyRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UploadIdentifyRecordResponse().from_map(
            self.do_rpcrequest('UploadIdentifyRecord', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_identify_record_with_options_async(
        self,
        request: cloudauth_console_20190219_models.UploadIdentifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.UploadIdentifyRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.UploadIdentifyRecordResponse().from_map(
            await self.do_rpcrequest_async('UploadIdentifyRecord', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_identify_record(
        self,
        request: cloudauth_console_20190219_models.UploadIdentifyRecordRequest,
    ) -> cloudauth_console_20190219_models.UploadIdentifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_identify_record_with_options(request, runtime)

    async def upload_identify_record_async(
        self,
        request: cloudauth_console_20190219_models.UploadIdentifyRecordRequest,
    ) -> cloudauth_console_20190219_models.UploadIdentifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_identify_record_with_options_async(request, runtime)

    def verify_account_project_with_options(
        self,
        request: cloudauth_console_20190219_models.VerifyAccountProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.VerifyAccountProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.VerifyAccountProjectResponse().from_map(
            self.do_rpcrequest('VerifyAccountProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_account_project_with_options_async(
        self,
        request: cloudauth_console_20190219_models.VerifyAccountProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190219_models.VerifyAccountProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190219_models.VerifyAccountProjectResponse().from_map(
            await self.do_rpcrequest_async('VerifyAccountProject', '2019-02-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_account_project(
        self,
        request: cloudauth_console_20190219_models.VerifyAccountProjectRequest,
    ) -> cloudauth_console_20190219_models.VerifyAccountProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_account_project_with_options(request, runtime)

    async def verify_account_project_async(
        self,
        request: cloudauth_console_20190219_models.VerifyAccountProjectRequest,
    ) -> cloudauth_console_20190219_models.VerifyAccountProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_account_project_with_options_async(request, runtime)
