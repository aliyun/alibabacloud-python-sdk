# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20181029 import models as yundun_dbaudit_20181029_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clear_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ClearInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ClearInstanceStorageResponse(),
            self.do_rpcrequest('ClearInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ClearInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ClearInstanceStorageResponse(),
            await self.do_rpcrequest_async('ClearInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_instance_storage(
        self,
        request: yundun_dbaudit_20181029_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.ClearInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_instance_storage_with_options(request, runtime)

    async def clear_instance_storage_async(
        self,
        request: yundun_dbaudit_20181029_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.ClearInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_instance_storage_with_options_async(request, runtime)

    def config_instance_white_list_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse(),
            self.do_rpcrequest('ConfigInstanceWhiteList', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_white_list_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse(),
            await self.do_rpcrequest_async('ConfigInstanceWhiteList', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_white_list(
        self,
        request: yundun_dbaudit_20181029_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    async def config_instance_white_list_async(
        self,
        request: yundun_dbaudit_20181029_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_dbaudit_20181029_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_white_list_with_options_async(request, runtime)

    def describe_audit_logs_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeAuditLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeAuditLogsResponse(),
            self.do_rpcrequest('DescribeAuditLogs', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_logs_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeAuditLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeAuditLogsResponse(),
            await self.do_rpcrequest_async('DescribeAuditLogs', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_logs(
        self,
        request: yundun_dbaudit_20181029_models.DescribeAuditLogsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeAuditLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_logs_with_options(request, runtime)

    async def describe_audit_logs_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeAuditLogsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeAuditLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_logs_with_options_async(request, runtime)

    def describe_instance_attribue_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttribueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse(),
            self.do_rpcrequest('DescribeInstanceAttribue', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribue_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttribueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAttribue', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribue(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttribueRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribue_with_options(request, runtime)

    async def describe_instance_attribue_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttribueRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttribueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribue_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse(),
            self.do_rpcrequest('DescribeInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse(),
            await self.do_rpcrequest_async('DescribeInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_storage(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_with_options(request, runtime)

    async def describe_instance_storage_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_storage_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_renew_status_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRenewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeRenewStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeRenewStatusResponse(),
            self.do_rpcrequest('DescribeRenewStatus', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_renew_status_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRenewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeRenewStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeRenewStatusResponse(),
            await self.do_rpcrequest_async('DescribeRenewStatus', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renew_status(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRenewStatusRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeRenewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_renew_status_with_options(request, runtime)

    async def describe_renew_status_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeRenewStatusRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeRenewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_renew_status_with_options_async(request, runtime)

    def describe_session_logs_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DescribeSessionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeSessionLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeSessionLogsResponse(),
            self.do_rpcrequest('DescribeSessionLogs', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_session_logs_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeSessionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DescribeSessionLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DescribeSessionLogsResponse(),
            await self.do_rpcrequest_async('DescribeSessionLogs', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_session_logs(
        self,
        request: yundun_dbaudit_20181029_models.DescribeSessionLogsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeSessionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_session_logs_with_options(request, runtime)

    async def describe_session_logs_async(
        self,
        request: yundun_dbaudit_20181029_models.DescribeSessionLogsRequest,
    ) -> yundun_dbaudit_20181029_models.DescribeSessionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_session_logs_with_options_async(request, runtime)

    def disable_instance_public_access_with_options(
        self,
        request: yundun_dbaudit_20181029_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse(),
            self.do_rpcrequest('DisableInstancePublicAccess', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_instance_public_access_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse(),
            await self.do_rpcrequest_async('DisableInstancePublicAccess', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_instance_public_access(
        self,
        request: yundun_dbaudit_20181029_models.DisableInstancePublicAccessRequest,
    ) -> yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    async def disable_instance_public_access_async(
        self,
        request: yundun_dbaudit_20181029_models.DisableInstancePublicAccessRequest,
    ) -> yundun_dbaudit_20181029_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_public_access_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: yundun_dbaudit_20181029_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse(),
            self.do_rpcrequest('EnableInstancePublicAccess', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_instance_public_access_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse(),
            await self.do_rpcrequest_async('EnableInstancePublicAccess', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_public_access(
        self,
        request: yundun_dbaudit_20181029_models.EnableInstancePublicAccessRequest,
    ) -> yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    async def enable_instance_public_access_async(
        self,
        request: yundun_dbaudit_20181029_models.EnableInstancePublicAccessRequest,
    ) -> yundun_dbaudit_20181029_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_public_access_with_options_async(request, runtime)

    def generate_upload_auth_with_options(
        self,
        request: yundun_dbaudit_20181029_models.GenerateUploadAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.GenerateUploadAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.GenerateUploadAuthResponse(),
            self.do_rpcrequest('GenerateUploadAuth', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_upload_auth_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.GenerateUploadAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.GenerateUploadAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.GenerateUploadAuthResponse(),
            await self.do_rpcrequest_async('GenerateUploadAuth', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_upload_auth(
        self,
        request: yundun_dbaudit_20181029_models.GenerateUploadAuthRequest,
    ) -> yundun_dbaudit_20181029_models.GenerateUploadAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_auth_with_options(request, runtime)

    async def generate_upload_auth_async(
        self,
        request: yundun_dbaudit_20181029_models.GenerateUploadAuthRequest,
    ) -> yundun_dbaudit_20181029_models.GenerateUploadAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_auth_with_options_async(request, runtime)

    def grant_service_role_with_options(
        self,
        request: yundun_dbaudit_20181029_models.GrantServiceRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.GrantServiceRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.GrantServiceRoleResponse(),
            self.do_rpcrequest('GrantServiceRole', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_service_role_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.GrantServiceRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.GrantServiceRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.GrantServiceRoleResponse(),
            await self.do_rpcrequest_async('GrantServiceRole', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_service_role(
        self,
        request: yundun_dbaudit_20181029_models.GrantServiceRoleRequest,
    ) -> yundun_dbaudit_20181029_models.GrantServiceRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_service_role_with_options(request, runtime)

    async def grant_service_role_async(
        self,
        request: yundun_dbaudit_20181029_models.GrantServiceRoleRequest,
    ) -> yundun_dbaudit_20181029_models.GrantServiceRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_service_role_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: yundun_dbaudit_20181029_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20181029_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_dbaudit_20181029_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20181029_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: yundun_dbaudit_20181029_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_dbaudit_20181029_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse(),
            self.do_rpcrequest('ModifyInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse(),
            await self.do_rpcrequest_async('ModifyInstanceStorage', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_storage(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_storage_with_options(request, runtime)

    async def modify_instance_storage_async(
        self,
        request: yundun_dbaudit_20181029_models.ModifyInstanceStorageRequest,
    ) -> yundun_dbaudit_20181029_models.ModifyInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_storage_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_dbaudit_20181029_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.MoveResourceGroupResponse(),
            await self.do_rpcrequest_async('MoveResourceGroup', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: yundun_dbaudit_20181029_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20181029_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_dbaudit_20181029_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20181029_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def refund_instance_with_options(
        self,
        request: yundun_dbaudit_20181029_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.RefundInstanceResponse(),
            self.do_rpcrequest('RefundInstance', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_instance_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.RefundInstanceResponse(),
            await self.do_rpcrequest_async('RefundInstance', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_instance(
        self,
        request: yundun_dbaudit_20181029_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20181029_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    async def refund_instance_async(
        self,
        request: yundun_dbaudit_20181029_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20181029_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_dbaudit_20181029_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.StartInstanceResponse(),
            await self.do_rpcrequest_async('StartInstance', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: yundun_dbaudit_20181029_models.StartInstanceRequest,
    ) -> yundun_dbaudit_20181029_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: yundun_dbaudit_20181029_models.StartInstanceRequest,
    ) -> yundun_dbaudit_20181029_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_dbaudit_20181029_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: yundun_dbaudit_20181029_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_dbaudit_20181029_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_dbaudit_20181029_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20181029_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20181029_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20181029_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2018-10-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: yundun_dbaudit_20181029_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_dbaudit_20181029_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20181029_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
