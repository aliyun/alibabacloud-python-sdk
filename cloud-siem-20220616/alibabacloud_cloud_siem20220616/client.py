# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloud_siem20220616 import models as cloud_siem_20220616_models
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
        self._endpoint = self.get_endpoint('cloud-siem', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_data_source_with_options(
        self,
        request: cloud_siem_20220616_models.AddDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not UtilClient.is_unset(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not UtilClient.is_unset(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_source_with_options_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not UtilClient.is_unset(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not UtilClient.is_unset(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_source(
        self,
        request: cloud_siem_20220616_models.AddDataSourceRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    async def add_data_source_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_source_with_options_async(request, runtime)

    def add_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_source_log_with_options_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_source_log(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_log_with_options(request, runtime)

    async def add_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_source_log_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: cloud_siem_20220616_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.added_user_id):
            body['AddedUserId'] = request.added_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_with_options_async(
        self,
        request: cloud_siem_20220616_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.added_user_id):
            body['AddedUserId'] = request.added_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user(
        self,
        request: cloud_siem_20220616_models.AddUserRequest,
    ) -> cloud_siem_20220616_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: cloud_siem_20220616_models.AddUserRequest,
    ) -> cloud_siem_20220616_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def add_user_source_log_config_with_options(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deleted):
            body['Deleted'] = request.deleted
        if not UtilClient.is_unset(request.dis_play_line):
            body['DisPlayLine'] = request.dis_play_line
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_log_info):
            body['SourceLogInfo'] = request.source_log_info
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserSourceLogConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddUserSourceLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_source_log_config_with_options_async(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deleted):
            body['Deleted'] = request.deleted
        if not UtilClient.is_unset(request.dis_play_line):
            body['DisPlayLine'] = request.dis_play_line
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_log_info):
            body['SourceLogInfo'] = request.source_log_info
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserSourceLogConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.AddUserSourceLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_source_log_config(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_source_log_config_with_options(request, runtime)

    async def add_user_source_log_config_async(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_source_log_config_with_options_async(request, runtime)

    def batch_job_check_with_options(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobCheck',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_job_check_with_options_async(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobCheck',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_job_check(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_job_check_with_options(request, runtime)

    async def batch_job_check_async(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_job_check_with_options_async(request, runtime)

    def batch_job_submit_with_options(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_config):
            body['JsonConfig'] = request.json_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobSubmit',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_job_submit_with_options_async(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_config):
            body['JsonConfig'] = request.json_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobSubmit',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_job_submit(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_job_submit_with_options(request, runtime)

    async def batch_job_submit_async(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_job_submit_with_options_async(request, runtime)

    def close_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.CloseDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_delivery_with_options_async(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.CloseDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_delivery(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_delivery_with_options(request, runtime)

    async def close_delivery_async(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_delivery_with_options_async(request, runtime)

    def delete_automate_response_config_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_automate_response_config_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_automate_response_config(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_automate_response_config_with_options(request, runtime)

    async def delete_automate_response_config_async(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_automate_response_config_with_options_async(request, runtime)

    def delete_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.bind_id):
            body['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bind_account_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.bind_id):
            body['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bind_account(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bind_account_with_options(request, runtime)

    async def delete_bind_account_async(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bind_account_with_options_async(request, runtime)

    def delete_customize_rule_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customize_rule_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteCustomizeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customize_rule(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_customize_rule_with_options(request, runtime)

    async def delete_customize_rule_async(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_customize_rule_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_log_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source_log(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_log_with_options(request, runtime)

    async def delete_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_log_with_options_async(request, runtime)

    def delete_quick_query_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quick_query_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteQuickQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quick_query(
        self,
        request: cloud_siem_20220616_models.DeleteQuickQueryRequest,
    ) -> cloud_siem_20220616_models.DeleteQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quick_query_with_options(request, runtime)

    async def delete_quick_query_async(
        self,
        request: cloud_siem_20220616_models.DeleteQuickQueryRequest,
    ) -> cloud_siem_20220616_models.DeleteQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quick_query_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.added_user_id):
            body['AddedUserId'] = request.added_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.added_user_id):
            body['AddedUserId'] = request.added_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: cloud_siem_20220616_models.DeleteUserRequest,
    ) -> cloud_siem_20220616_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: cloud_siem_20220616_models.DeleteUserRequest,
    ) -> cloud_siem_20220616_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_white_rule_list_with_options_async(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_white_rule_list(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_white_rule_list_with_options(request, runtime)

    async def delete_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_white_rule_list_with_options_async(request, runtime)

    def describe_aggregate_function_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAggregateFunction',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAggregateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aggregate_function_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAggregateFunction',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAggregateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aggregate_function(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_aggregate_function_with_options(request, runtime)

    async def describe_aggregate_function_async(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_aggregate_function_with_options_async(request, runtime)

    def describe_alert_scene_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertScene',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_scene_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertScene',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_scene(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_scene_with_options(request, runtime)

    async def describe_alert_scene_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_scene_with_options_async(request, runtime)

    def describe_alert_scene_by_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSceneByEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSceneByEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_scene_by_event_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSceneByEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSceneByEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_scene_by_event(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_scene_by_event_with_options(request, runtime)

    async def describe_alert_scene_by_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_scene_by_event_with_options_async(request, runtime)

    def describe_alert_source_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_source_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_source(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_options(request, runtime)

    async def describe_alert_source_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_source_with_options_async(request, runtime)

    def describe_alert_source_with_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSourceWithEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_source_with_event_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSourceWithEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_source_with_event(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_event_with_options(request, runtime)

    async def describe_alert_source_with_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_source_with_event_with_options_async(request, runtime)

    def describe_alert_type_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_type_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_type(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_type_with_options(request, runtime)

    async def describe_alert_type_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_type_with_options_async(request, runtime)

    def describe_alerts_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlerts',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlerts',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_options(request, runtime)

    async def describe_alerts_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_options_async(request, runtime)

    def describe_alerts_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_count_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_count(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_count_with_options(request, runtime)

    async def describe_alerts_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_count_with_options_async(request, runtime)

    def describe_alerts_with_entity_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsWithEntity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsWithEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_entity_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsWithEntity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsWithEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_with_entity(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_entity_with_options(request, runtime)

    async def describe_alerts_with_entity_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_entity_with_options_async(request, runtime)

    def describe_alerts_with_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsWithEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsWithEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_event_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsWithEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsWithEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_with_event(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_event_with_options(request, runtime)

    async def describe_alerts_with_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_event_with_options_async(request, runtime)

    def describe_attack_time_line_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAttackTimeLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAttackTimeLineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAttackTimeLine',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAttackTimeLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_time_line_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAttackTimeLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAttackTimeLineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAttackTimeLine',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAttackTimeLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_time_line(
        self,
        request: cloud_siem_20220616_models.DescribeAttackTimeLineRequest,
    ) -> cloud_siem_20220616_models.DescribeAttackTimeLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_time_line_with_options(request, runtime)

    async def describe_attack_time_line_async(
        self,
        request: cloud_siem_20220616_models.DescribeAttackTimeLineRequest,
    ) -> cloud_siem_20220616_models.DescribeAttackTimeLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_time_line_with_options_async(request, runtime)

    def describe_auth_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAuth',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAuth',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_with_options(request, runtime)

    async def describe_auth_async(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auth_with_options_async(request, runtime)

    def describe_automate_response_config_counter_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_automate_response_config_counter_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_automate_response_config_counter(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_counter_with_options(request, runtime)

    async def describe_automate_response_config_counter_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_counter_with_options_async(request, runtime)

    def describe_automate_response_config_feature_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigFeature',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_automate_response_config_feature_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigFeature',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_automate_response_config_feature(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_feature_with_options(request, runtime)

    async def describe_automate_response_config_feature_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_feature_with_options_async(request, runtime)

    def describe_automate_response_config_play_books_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigPlayBooks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_automate_response_config_play_books_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigPlayBooks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_automate_response_config_play_books(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_play_books_with_options(request, runtime)

    async def describe_automate_response_config_play_books_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_play_books_with_options_async(request, runtime)

    def describe_cloud_siem_assets_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_type):
            body['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssets',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_assets_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_type):
            body['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssets',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_assets(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_with_options(request, runtime)

    async def describe_cloud_siem_assets_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_assets_with_options_async(request, runtime)

    def describe_cloud_siem_assets_counter_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssetsCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_assets_counter_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssetsCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_assets_counter(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_counter_with_options(request, runtime)

    async def describe_cloud_siem_assets_counter_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_assets_counter_with_options_async(request, runtime)

    def describe_cloud_siem_event_detail_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEventDetail',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_event_detail_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEventDetail',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_event_detail(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_event_detail_with_options(request, runtime)

    async def describe_cloud_siem_event_detail_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_event_detail_with_options_async(request, runtime)

    def describe_cloud_siem_events_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.thread_level):
            body['ThreadLevel'] = request.thread_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEvents',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_events_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.thread_level):
            body['ThreadLevel'] = request.thread_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEvents',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_events(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_events_with_options(request, runtime)

    async def describe_cloud_siem_events_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_events_with_options_async(request, runtime)

    def describe_cs_imported_prod_status_by_user_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_prod):
            body['SourceLogProd'] = request.source_log_prod
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCsImportedProdStatusByUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cs_imported_prod_status_by_user_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_prod):
            body['SourceLogProd'] = request.source_log_prod
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCsImportedProdStatusByUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cs_imported_prod_status_by_user(
        self,
        request: cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserRequest,
    ) -> cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cs_imported_prod_status_by_user_with_options(request, runtime)

    async def describe_cs_imported_prod_status_by_user_async(
        self,
        request: cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserRequest,
    ) -> cloud_siem_20220616_models.DescribeCsImportedProdStatusByUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cs_imported_prod_status_by_user_with_options_async(request, runtime)

    def describe_customize_rule_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_with_options(request, runtime)

    async def describe_customize_rule_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_with_options_async(request, runtime)

    def describe_customize_rule_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_count_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_count(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_count_with_options(request, runtime)

    async def describe_customize_rule_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_count_with_options_async(request, runtime)

    def describe_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_test_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_test(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_with_options(request, runtime)

    async def describe_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_test_with_options_async(request, runtime)

    def describe_customize_rule_test_histogram_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTestHistogram',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_test_histogram_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTestHistogram',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_test_histogram(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_histogram_with_options(request, runtime)

    async def describe_customize_rule_test_histogram_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_test_histogram_with_options_async(request, runtime)

    def describe_data_source_instance_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceInstance',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDataSourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_instance_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceInstance',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDataSourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_instance(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_instance_with_options(request, runtime)

    async def describe_data_source_instance_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_source_instance_with_options_async(request, runtime)

    def describe_data_source_parameters_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceParameters',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDataSourceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_parameters_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceParameters',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDataSourceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_parameters(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_parameters_with_options(request, runtime)

    async def describe_data_source_parameters_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_source_parameters_with_options_async(request, runtime)

    def describe_dispose_and_playbook_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeAndPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispose_and_playbook_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeAndPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispose_and_playbook(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_and_playbook_with_options(request, runtime)

    async def describe_dispose_and_playbook_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispose_and_playbook_with_options_async(request, runtime)

    def describe_dispose_strategy_playbook_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeStrategyPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispose_strategy_playbook_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeStrategyPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispose_strategy_playbook(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_strategy_playbook_with_options(request, runtime)

    async def describe_dispose_strategy_playbook_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispose_strategy_playbook_with_options_async(request, runtime)

    def describe_entity_info_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEntityInfo',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEntityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_entity_info_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEntityInfo',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEntityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_entity_info(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_entity_info_with_options(request, runtime)

    async def describe_entity_info_async(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_entity_info_with_options_async(request, runtime)

    def describe_event_count_by_threat_level_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventCountByThreatLevel',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_count_by_threat_level_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventCountByThreatLevel',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_count_by_threat_level(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_count_by_threat_level_with_options(request, runtime)

    async def describe_event_count_by_threat_level_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_count_by_threat_level_with_options_async(request, runtime)

    def describe_event_dispose_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventDispose',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventDisposeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_dispose_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventDispose',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventDisposeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_dispose(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_dispose_with_options(request, runtime)

    async def describe_event_dispose_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_dispose_with_options_async(request, runtime)

    def describe_imported_log_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedLogCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeImportedLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imported_log_count_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedLogCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeImportedLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imported_log_count(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_imported_log_count_with_options(request, runtime)

    async def describe_imported_log_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_imported_log_count_with_options_async(request, runtime)

    def describe_job_status_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeJobStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_status_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeJobStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_status(
        self,
        request: cloud_siem_20220616_models.DescribeJobStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_status_with_options(request, runtime)

    async def describe_job_status_async(
        self,
        request: cloud_siem_20220616_models.DescribeJobStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_status_with_options_async(request, runtime)

    def describe_log_fields_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogFields',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_fields_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogFields',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_fields(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_fields_with_options(request, runtime)

    async def describe_log_fields_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_fields_with_options_async(request, runtime)

    def describe_log_source_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_source_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_source(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_source_with_options(request, runtime)

    async def describe_log_source_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_source_with_options_async(request, runtime)

    def describe_log_store_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogStoreResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogStore',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogStoreResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogStore',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store(
        self,
        request: cloud_siem_20220616_models.DescribeLogStoreRequest,
    ) -> cloud_siem_20220616_models.DescribeLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_with_options(request, runtime)

    async def describe_log_store_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogStoreRequest,
    ) -> cloud_siem_20220616_models.DescribeLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_with_options_async(request, runtime)

    def describe_log_type_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_type_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_type(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_type_with_options(request, runtime)

    async def describe_log_type_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_type_with_options_async(request, runtime)

    def describe_operators_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOperators',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeOperatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operators_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOperators',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeOperatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operators(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_operators_with_options(request, runtime)

    async def describe_operators_async(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_operators_with_options_async(request, runtime)

    def describe_prod_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProdCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeProdCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prod_count_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProdCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeProdCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prod_count(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_prod_count_with_options(request, runtime)

    async def describe_prod_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_prod_count_with_options_async(request, runtime)

    def describe_scope_users_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScopeUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeScopeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scope_users_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScopeUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeScopeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scope_users(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scope_users_with_options(request, runtime)

    async def describe_scope_users_async(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scope_users_with_options_async(request, runtime)

    def describe_service_status_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_status_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_status(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_status_with_options(request, runtime)

    async def describe_service_status_async(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_status_with_options_async(request, runtime)

    def describe_storage_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_with_options(request, runtime)

    async def describe_storage_async(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_with_options_async(request, runtime)

    def describe_user_buy_status_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserBuyStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeUserBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_buy_status_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserBuyStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeUserBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_buy_status(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_buy_status_with_options(request, runtime)

    async def describe_user_buy_status_async(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_buy_status_with_options_async(request, runtime)

    def describe_waf_scope_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWafScope',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeWafScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_scope_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWafScope',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeWafScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_scope(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_scope_with_options(request, runtime)

    async def describe_waf_scope_async(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_scope_with_options_async(request, runtime)

    def describe_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_white_rule_list_with_options_async(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_white_rule_list(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_white_rule_list_with_options(request, runtime)

    async def describe_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_white_rule_list_with_options_async(request, runtime)

    def do_quick_field_with_options(
        self,
        request: cloud_siem_20220616_models.DoQuickFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DoQuickFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.index):
            body['Index'] = request.index
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            body['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoQuickField',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoQuickFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_quick_field_with_options_async(
        self,
        request: cloud_siem_20220616_models.DoQuickFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DoQuickFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.index):
            body['Index'] = request.index
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            body['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoQuickField',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoQuickFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_quick_field(
        self,
        request: cloud_siem_20220616_models.DoQuickFieldRequest,
    ) -> cloud_siem_20220616_models.DoQuickFieldResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_quick_field_with_options(request, runtime)

    async def do_quick_field_async(
        self,
        request: cloud_siem_20220616_models.DoQuickFieldRequest,
    ) -> cloud_siem_20220616_models.DoQuickFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_quick_field_with_options_async(request, runtime)

    def do_self_delegate_with_options(
        self,
        request: cloud_siem_20220616_models.DoSelfDelegateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DoSelfDelegateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.delegate_or_not):
            body['DelegateOrNot'] = request.delegate_or_not
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoSelfDelegate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoSelfDelegateResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_self_delegate_with_options_async(
        self,
        request: cloud_siem_20220616_models.DoSelfDelegateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DoSelfDelegateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.delegate_or_not):
            body['DelegateOrNot'] = request.delegate_or_not
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoSelfDelegate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoSelfDelegateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_self_delegate(
        self,
        request: cloud_siem_20220616_models.DoSelfDelegateRequest,
    ) -> cloud_siem_20220616_models.DoSelfDelegateResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_self_delegate_with_options(request, runtime)

    async def do_self_delegate_async(
        self,
        request: cloud_siem_20220616_models.DoSelfDelegateRequest,
    ) -> cloud_siem_20220616_models.DoSelfDelegateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_self_delegate_with_options_async(request, runtime)

    def enable_access_for_cloud_siem_with_options(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAccessForCloudSiem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.EnableAccessForCloudSiemResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_access_for_cloud_siem_with_options_async(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAccessForCloudSiem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.EnableAccessForCloudSiemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_access_for_cloud_siem(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_access_for_cloud_siem_with_options(request, runtime)

    async def enable_access_for_cloud_siem_async(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_access_for_cloud_siem_with_options_async(request, runtime)

    def enable_service_for_cloud_siem_with_options(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableServiceForCloudSiem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.EnableServiceForCloudSiemResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_for_cloud_siem_with_options_async(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableServiceForCloudSiem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.EnableServiceForCloudSiemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service_for_cloud_siem(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_service_for_cloud_siem_with_options(request, runtime)

    async def enable_service_for_cloud_siem_async(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_service_for_cloud_siem_with_options_async(request, runtime)

    def get_capacity_with_options(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_capacity_with_options_async(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_capacity(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    async def get_capacity_async(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_capacity_with_options_async(request, runtime)

    def get_histograms_with_options(
        self,
        request: cloud_siem_20220616_models.GetHistogramsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetHistogramsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetHistogramsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_histograms_with_options_async(
        self,
        request: cloud_siem_20220616_models.GetHistogramsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetHistogramsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetHistogramsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_histograms(
        self,
        request: cloud_siem_20220616_models.GetHistogramsRequest,
    ) -> cloud_siem_20220616_models.GetHistogramsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_histograms_with_options(request, runtime)

    async def get_histograms_async(
        self,
        request: cloud_siem_20220616_models.GetHistogramsRequest,
    ) -> cloud_siem_20220616_models.GetHistogramsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_histograms_with_options_async(request, runtime)

    def get_logs_with_options(
        self,
        request: cloud_siem_20220616_models.GetLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse_or_not):
            body['ReverseOrNot'] = request.reverse_or_not
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.total):
            body['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_logs_with_options_async(
        self,
        request: cloud_siem_20220616_models.GetLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse_or_not):
            body['ReverseOrNot'] = request.reverse_or_not
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.total):
            body['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_logs(
        self,
        request: cloud_siem_20220616_models.GetLogsRequest,
    ) -> cloud_siem_20220616_models.GetLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_logs_with_options(request, runtime)

    async def get_logs_async(
        self,
        request: cloud_siem_20220616_models.GetLogsRequest,
    ) -> cloud_siem_20220616_models.GetLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_logs_with_options_async(request, runtime)

    def get_quick_query_with_options(
        self,
        request: cloud_siem_20220616_models.GetQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quick_query_with_options_async(
        self,
        request: cloud_siem_20220616_models.GetQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetQuickQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quick_query(
        self,
        request: cloud_siem_20220616_models.GetQuickQueryRequest,
    ) -> cloud_siem_20220616_models.GetQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quick_query_with_options(request, runtime)

    async def get_quick_query_async(
        self,
        request: cloud_siem_20220616_models.GetQuickQueryRequest,
    ) -> cloud_siem_20220616_models.GetQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quick_query_with_options_async(request, runtime)

    def get_storage_with_options(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_with_options_async(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_storage_with_options(request, runtime)

    async def get_storage_async(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_storage_with_options_async(request, runtime)

    def list_account_access_id_with_options(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAccountAccessId',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAccountAccessIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_access_id_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAccountAccessId',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAccountAccessIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_access_id(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_account_access_id_with_options(request, runtime)

    async def list_account_access_id_async(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_account_access_id_with_options_async(request, runtime)

    def list_accounts_by_log_with_options(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAccountsByLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAccountsByLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_by_log_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAccountsByLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAccountsByLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_by_log(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_by_log_with_options(request, runtime)

    async def list_accounts_by_log_async(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_by_log_with_options_async(request, runtime)

    def list_all_prods_with_options(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAllProds',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAllProdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_prods_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAllProds',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAllProdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_prods(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_prods_with_options(request, runtime)

    async def list_all_prods_async(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_prods_with_options_async(request, runtime)

    def list_automate_response_configs_with_options(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutomateResponseConfigs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAutomateResponseConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_automate_response_configs_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutomateResponseConfigs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAutomateResponseConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_automate_response_configs(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_automate_response_configs_with_options(request, runtime)

    async def list_automate_response_configs_async(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_automate_response_configs_with_options_async(request, runtime)

    def list_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_account_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_account(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bind_account_with_options(request, runtime)

    async def list_bind_account_async(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bind_account_with_options_async(request, runtime)

    def list_bind_data_sources_with_options(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindDataSources',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListBindDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_data_sources_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindDataSources',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListBindDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_data_sources(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bind_data_sources_with_options(request, runtime)

    async def list_bind_data_sources_async(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bind_data_sources_with_options_async(request, runtime)

    def list_cloud_siem_customize_rules_with_options(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemCustomizeRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_siem_customize_rules_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemCustomizeRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_siem_customize_rules(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_customize_rules_with_options(request, runtime)

    async def list_cloud_siem_customize_rules_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_siem_customize_rules_with_options_async(request, runtime)

    def list_cloud_siem_predefined_rules_with_options(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemPredefinedRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_siem_predefined_rules_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemPredefinedRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_siem_predefined_rules(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_predefined_rules_with_options(request, runtime)

    async def list_cloud_siem_predefined_rules_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_siem_predefined_rules_with_options_async(request, runtime)

    def list_customize_rule_test_result_with_options(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomizeRuleTestResult',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_customize_rule_test_result_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomizeRuleTestResult',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_customize_rule_test_result(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_customize_rule_test_result_with_options(request, runtime)

    async def list_customize_rule_test_result_async(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_customize_rule_test_result_with_options_async(request, runtime)

    def list_data_source_logs_with_options(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDataSourceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_logs_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDataSourceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_logs(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_logs_with_options(request, runtime)

    async def list_data_source_logs_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_logs_with_options_async(request, runtime)

    def list_data_source_types_with_options(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceTypes',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDataSourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_types_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceTypes',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDataSourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_types(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_types_with_options(request, runtime)

    async def list_data_source_types_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_types_with_options_async(request, runtime)

    def list_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_with_options(request, runtime)

    async def list_delivery_async(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delivery_with_options_async(request, runtime)

    def list_dispose_strategy_with_options(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.effective_status):
            body['EffectiveStatus'] = request.effective_status
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_types):
            body['PlaybookTypes'] = request.playbook_types
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDisposeStrategy',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDisposeStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dispose_strategy_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.effective_status):
            body['EffectiveStatus'] = request.effective_status
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_types):
            body['PlaybookTypes'] = request.playbook_types
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDisposeStrategy',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDisposeStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dispose_strategy(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dispose_strategy_with_options(request, runtime)

    async def list_dispose_strategy_async(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dispose_strategy_with_options_async(request, runtime)

    def list_imported_logs_by_prod_with_options(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImportedLogsByProd',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListImportedLogsByProdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_imported_logs_by_prod_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImportedLogsByProd',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListImportedLogsByProdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_imported_logs_by_prod(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_imported_logs_by_prod_with_options(request, runtime)

    async def list_imported_logs_by_prod_async(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_imported_logs_by_prod_with_options_async(request, runtime)

    def list_operation_with_options(
        self,
        request: cloud_siem_20220616_models.ListOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListOperationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOperation',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListOperationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOperation',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation(
        self,
        request: cloud_siem_20220616_models.ListOperationRequest,
    ) -> cloud_siem_20220616_models.ListOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_with_options(request, runtime)

    async def list_operation_async(
        self,
        request: cloud_siem_20220616_models.ListOperationRequest,
    ) -> cloud_siem_20220616_models.ListOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_with_options_async(request, runtime)

    def list_project_log_stores_with_options(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectLogStores',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListProjectLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_log_stores_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectLogStores',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListProjectLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_log_stores(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_log_stores_with_options(request, runtime)

    async def list_project_log_stores_async(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_log_stores_with_options_async(request, runtime)

    def list_quick_query_with_options(
        self,
        request: cloud_siem_20220616_models.ListQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quick_query_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListQuickQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quick_query(
        self,
        request: cloud_siem_20220616_models.ListQuickQueryRequest,
    ) -> cloud_siem_20220616_models.ListQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quick_query_with_options(request, runtime)

    async def list_quick_query_async(
        self,
        request: cloud_siem_20220616_models.ListQuickQueryRequest,
    ) -> cloud_siem_20220616_models.ListQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quick_query_with_options_async(request, runtime)

    def list_rd_users_with_options(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRdUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListRdUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rd_users_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRdUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListRdUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rd_users(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rd_users_with_options(request, runtime)

    async def list_rd_users_async(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rd_users_with_options_async(request, runtime)

    def list_user_prod_logs_with_options(
        self,
        request: cloud_siem_20220616_models.ListUserProdLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListUserProdLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserProdLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListUserProdLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_prod_logs_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListUserProdLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListUserProdLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserProdLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListUserProdLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_prod_logs(
        self,
        request: cloud_siem_20220616_models.ListUserProdLogsRequest,
    ) -> cloud_siem_20220616_models.ListUserProdLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_prod_logs_with_options(request, runtime)

    async def list_user_prod_logs_async(
        self,
        request: cloud_siem_20220616_models.ListUserProdLogsRequest,
    ) -> cloud_siem_20220616_models.ListUserProdLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_prod_logs_with_options_async(request, runtime)

    def list_users_by_prod_with_options(
        self,
        request: cloud_siem_20220616_models.ListUsersByProdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListUsersByProdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsersByProd',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListUsersByProdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_by_prod_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListUsersByProdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListUsersByProdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsersByProd',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListUsersByProdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_by_prod(
        self,
        request: cloud_siem_20220616_models.ListUsersByProdRequest,
    ) -> cloud_siem_20220616_models.ListUsersByProdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_by_prod_with_options(request, runtime)

    async def list_users_by_prod_async(
        self,
        request: cloud_siem_20220616_models.ListUsersByProdRequest,
    ) -> cloud_siem_20220616_models.ListUsersByProdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_by_prod_with_options_async(request, runtime)

    def modify_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.bind_id):
            body['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_bind_account_with_options_async(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.bind_id):
            body['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBindAccount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_bind_account(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bind_account_with_options(request, runtime)

    async def modify_bind_account_async(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bind_account_with_options_async(request, runtime)

    def modify_data_source_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not UtilClient.is_unset(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not UtilClient.is_unset(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not UtilClient.is_unset(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not UtilClient.is_unset(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_with_options(request, runtime)

    async def modify_data_source_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_with_options_async(request, runtime)

    def modify_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_log_with_options_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not UtilClient.is_unset(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSourceLog',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ModifyDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source_log(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_log_with_options(request, runtime)

    async def modify_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_log_with_options_async(request, runtime)

    def open_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.OpenDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_delivery_with_options_async(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.OpenDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_delivery(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_delivery_with_options(request, runtime)

    async def open_delivery_async(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_delivery_with_options_async(request, runtime)

    def post_automate_response_config_with_options(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_config):
            body['ActionConfig'] = request.action_config
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.execution_condition):
            body['ExecutionCondition'] = request.execution_condition
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_automate_response_config_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_config):
            body['ActionConfig'] = request.action_config
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.execution_condition):
            body['ExecutionCondition'] = request.execution_condition
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostAutomateResponseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_automate_response_config(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_automate_response_config_with_options(request, runtime)

    async def post_automate_response_config_async(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_automate_response_config_with_options_async(request, runtime)

    def post_customize_rule_with_options(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not UtilClient.is_unset(request.event_transfer_ext):
            body['EventTransferExt'] = request.event_transfer_ext
        if not UtilClient.is_unset(request.event_transfer_switch):
            body['EventTransferSwitch'] = request.event_transfer_switch
        if not UtilClient.is_unset(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_source_mds):
            body['LogSourceMds'] = request.log_source_mds
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.log_type_mds):
            body['LogTypeMds'] = request.log_type_mds
        if not UtilClient.is_unset(request.query_cycle):
            body['QueryCycle'] = request.query_cycle
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_condition):
            body['RuleCondition'] = request.rule_condition
        if not UtilClient.is_unset(request.rule_desc):
            body['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_group):
            body['RuleGroup'] = request.rule_group
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_threshold):
            body['RuleThreshold'] = request.rule_threshold
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_customize_rule_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not UtilClient.is_unset(request.event_transfer_ext):
            body['EventTransferExt'] = request.event_transfer_ext
        if not UtilClient.is_unset(request.event_transfer_switch):
            body['EventTransferSwitch'] = request.event_transfer_switch
        if not UtilClient.is_unset(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_source_mds):
            body['LogSourceMds'] = request.log_source_mds
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.log_type_mds):
            body['LogTypeMds'] = request.log_type_mds
        if not UtilClient.is_unset(request.query_cycle):
            body['QueryCycle'] = request.query_cycle
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_condition):
            body['RuleCondition'] = request.rule_condition
        if not UtilClient.is_unset(request.rule_desc):
            body['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_group):
            body['RuleGroup'] = request.rule_group
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_threshold):
            body['RuleThreshold'] = request.rule_threshold
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_customize_rule(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_with_options(request, runtime)

    async def post_customize_rule_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_customize_rule_with_options_async(request, runtime)

    def post_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.simulated_data):
            body['SimulatedData'] = request.simulated_data
        if not UtilClient.is_unset(request.test_type):
            body['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_customize_rule_test_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.simulated_data):
            body['SimulatedData'] = request.simulated_data
        if not UtilClient.is_unset(request.test_type):
            body['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_customize_rule_test(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_test_with_options(request, runtime)

    async def post_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_customize_rule_test_with_options_async(request, runtime)

    def post_event_dispose_and_whiterule_list_with_options(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_dispose):
            body['EventDispose'] = request.event_dispose
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.receiver_info):
            body['ReceiverInfo'] = request.receiver_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventDisposeAndWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_event_dispose_and_whiterule_list_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_dispose):
            body['EventDispose'] = request.event_dispose
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.receiver_info):
            body['ReceiverInfo'] = request.receiver_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventDisposeAndWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_event_dispose_and_whiterule_list(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_event_dispose_and_whiterule_list_with_options(request, runtime)

    async def post_event_dispose_and_whiterule_list_async(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_event_dispose_and_whiterule_list_with_options_async(request, runtime)

    def post_event_whiterule_list_with_options(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.whiterule_list):
            body['WhiteruleList'] = request.whiterule_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_event_whiterule_list_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.whiterule_list):
            body['WhiteruleList'] = request.whiterule_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventWhiteruleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_event_whiterule_list(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_event_whiterule_list_with_options(request, runtime)

    async def post_event_whiterule_list_async(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_event_whiterule_list_with_options_async(request, runtime)

    def post_finish_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostFinishCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_finish_customize_rule_test_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostFinishCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_finish_customize_rule_test(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_finish_customize_rule_test_with_options(request, runtime)

    async def post_finish_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_finish_customize_rule_test_with_options_async(request, runtime)

    def post_rule_status_change_with_options(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostRuleStatusChange',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostRuleStatusChangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_rule_status_change_with_options_async(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostRuleStatusChange',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostRuleStatusChangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_rule_status_change(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.post_rule_status_change_with_options(request, runtime)

    async def post_rule_status_change_async(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_rule_status_change_with_options_async(request, runtime)

    def restore_capacity_with_options(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.RestoreCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_capacity_with_options_async(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.RestoreCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_capacity(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_capacity_with_options(request, runtime)

    async def restore_capacity_async(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_capacity_with_options_async(request, runtime)

    def save_quick_query_with_options(
        self,
        request: cloud_siem_20220616_models.SaveQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SaveQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SaveQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_quick_query_with_options_async(
        self,
        request: cloud_siem_20220616_models.SaveQuickQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SaveQuickQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SaveQuickQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_quick_query(
        self,
        request: cloud_siem_20220616_models.SaveQuickQueryRequest,
    ) -> cloud_siem_20220616_models.SaveQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_quick_query_with_options(request, runtime)

    async def save_quick_query_async(
        self,
        request: cloud_siem_20220616_models.SaveQuickQueryRequest,
    ) -> cloud_siem_20220616_models.SaveQuickQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_quick_query_with_options_async(request, runtime)

    def set_storage_with_options(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_storage_with_options_async(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SetStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_storage(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_storage_with_options(request, runtime)

    async def set_storage_async(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_storage_with_options_async(request, runtime)

    def show_quick_analysis_with_options(
        self,
        request: cloud_siem_20220616_models.ShowQuickAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ShowQuickAnalysisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ShowQuickAnalysis',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ShowQuickAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def show_quick_analysis_with_options_async(
        self,
        request: cloud_siem_20220616_models.ShowQuickAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ShowQuickAnalysisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ShowQuickAnalysis',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ShowQuickAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def show_quick_analysis(
        self,
        request: cloud_siem_20220616_models.ShowQuickAnalysisRequest,
    ) -> cloud_siem_20220616_models.ShowQuickAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.show_quick_analysis_with_options(request, runtime)

    async def show_quick_analysis_async(
        self,
        request: cloud_siem_20220616_models.ShowQuickAnalysisRequest,
    ) -> cloud_siem_20220616_models.ShowQuickAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.show_quick_analysis_with_options_async(request, runtime)

    def submit_import_log_tasks_with_options(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accounts):
            body['Accounts'] = request.accounts
        if not UtilClient.is_unset(request.auto_imported):
            body['AutoImported'] = request.auto_imported
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImportLogTasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SubmitImportLogTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_import_log_tasks_with_options_async(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accounts):
            body['Accounts'] = request.accounts
        if not UtilClient.is_unset(request.auto_imported):
            body['AutoImported'] = request.auto_imported
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImportLogTasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SubmitImportLogTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_import_log_tasks(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_import_log_tasks_with_options(request, runtime)

    async def submit_import_log_tasks_async(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_import_log_tasks_with_options_async(request, runtime)

    def submit_jobs_with_options(
        self,
        request: cloud_siem_20220616_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_param):
            body['JsonParam'] = request.json_param
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SubmitJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_jobs_with_options_async(
        self,
        request: cloud_siem_20220616_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_param):
            body['JsonParam'] = request.json_param
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SubmitJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_jobs(
        self,
        request: cloud_siem_20220616_models.SubmitJobsRequest,
    ) -> cloud_siem_20220616_models.SubmitJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_jobs_with_options(request, runtime)

    async def submit_jobs_async(
        self,
        request: cloud_siem_20220616_models.SubmitJobsRequest,
    ) -> cloud_siem_20220616_models.SubmitJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_jobs_with_options_async(request, runtime)

    def update_automate_response_config_status_with_options(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutomateResponseConfigStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_automate_response_config_status_with_options_async(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutomateResponseConfigStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_automate_response_config_status(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_automate_response_config_status_with_options(request, runtime)

    async def update_automate_response_config_status_async(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_automate_response_config_status_with_options_async(request, runtime)

    def update_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_rule_id):
            body['WhiteRuleId'] = request.white_rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_white_rule_list_with_options_async(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_rule_id):
            body['WhiteRuleId'] = request.white_rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_white_rule_list(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_white_rule_list_with_options(request, runtime)

    async def update_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_white_rule_list_with_options_async(request, runtime)
