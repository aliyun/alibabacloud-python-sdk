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
        """
        @summary Adds a data source to a cloud account that is added to the threat analysis feature.
        
        @param request: AddDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataSourceResponse
        """
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
        """
        @summary Adds a data source to a cloud account that is added to the threat analysis feature.
        
        @param request: AddDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataSourceResponse
        """
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
        """
        @summary Adds a data source to a cloud account that is added to the threat analysis feature.
        
        @param request: AddDataSourceRequest
        @return: AddDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    async def add_data_source_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceResponse:
        """
        @summary Adds a data source to a cloud account that is added to the threat analysis feature.
        
        @param request: AddDataSourceRequest
        @return: AddDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_data_source_with_options_async(request, runtime)

    def add_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        """
        @summary Adds logs of a cloud account to the threat analysis feature.
        
        @param request: AddDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataSourceLogResponse
        """
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
        """
        @summary Adds logs of a cloud account to the threat analysis feature.
        
        @param request: AddDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataSourceLogResponse
        """
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
        """
        @summary Adds logs of a cloud account to the threat analysis feature.
        
        @param request: AddDataSourceLogRequest
        @return: AddDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_log_with_options(request, runtime)

    async def add_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.AddDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.AddDataSourceLogResponse:
        """
        @summary Adds logs of a cloud account to the threat analysis feature.
        
        @param request: AddDataSourceLogRequest
        @return: AddDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_data_source_log_with_options_async(request, runtime)

    def add_user_source_log_config_with_options(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        """
        @summary Adds the logs of a cloud service within a cloud account to the threat analysis feature for alert and event anslysis.
        
        @param request: AddUserSourceLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserSourceLogConfigResponse
        """
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
        """
        @summary Adds the logs of a cloud service within a cloud account to the threat analysis feature for alert and event anslysis.
        
        @param request: AddUserSourceLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserSourceLogConfigResponse
        """
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
        """
        @summary Adds the logs of a cloud service within a cloud account to the threat analysis feature for alert and event anslysis.
        
        @param request: AddUserSourceLogConfigRequest
        @return: AddUserSourceLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_source_log_config_with_options(request, runtime)

    async def add_user_source_log_config_async(
        self,
        request: cloud_siem_20220616_models.AddUserSourceLogConfigRequest,
    ) -> cloud_siem_20220616_models.AddUserSourceLogConfigResponse:
        """
        @summary Adds the logs of a cloud service within a cloud account to the threat analysis feature for alert and event anslysis.
        
        @param request: AddUserSourceLogConfigRequest
        @return: AddUserSourceLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_source_log_config_with_options_async(request, runtime)

    def bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BindAccountResponse:
        """
        @summary Adds a third-party cloud account that is displayed on the Multi-cloud assets tab of the Feature Settings page to the threat analysis feature.
        
        @param request: BindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindAccount',
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
            cloud_siem_20220616_models.BindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_with_options_async(
        self,
        request: cloud_siem_20220616_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BindAccountResponse:
        """
        @summary Adds a third-party cloud account that is displayed on the Multi-cloud assets tab of the Feature Settings page to the threat analysis feature.
        
        @param request: BindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_id):
            body['AccessId'] = request.access_id
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindAccount',
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
            cloud_siem_20220616_models.BindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account(
        self,
        request: cloud_siem_20220616_models.BindAccountRequest,
    ) -> cloud_siem_20220616_models.BindAccountResponse:
        """
        @summary Adds a third-party cloud account that is displayed on the Multi-cloud assets tab of the Feature Settings page to the threat analysis feature.
        
        @param request: BindAccountRequest
        @return: BindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_account_with_options(request, runtime)

    async def bind_account_async(
        self,
        request: cloud_siem_20220616_models.BindAccountRequest,
    ) -> cloud_siem_20220616_models.BindAccountResponse:
        """
        @summary Adds a third-party cloud account that is displayed on the Multi-cloud assets tab of the Feature Settings page to the threat analysis feature.
        
        @param request: BindAccountRequest
        @return: BindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_account_with_options_async(request, runtime)

    def close_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        """
        @summary Disables the log delivery feature for a cloud service.
        
        @param request: CloseDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Disables the log delivery feature for a cloud service.
        
        @param request: CloseDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Disables the log delivery feature for a cloud service.
        
        @param request: CloseDeliveryRequest
        @return: CloseDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_delivery_with_options(request, runtime)

    async def close_delivery_async(
        self,
        request: cloud_siem_20220616_models.CloseDeliveryRequest,
    ) -> cloud_siem_20220616_models.CloseDeliveryResponse:
        """
        @summary Disables the log delivery feature for a cloud service.
        
        @param request: CloseDeliveryRequest
        @return: CloseDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_delivery_with_options_async(request, runtime)

    def delete_automate_response_config_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        """
        @summary Deletes the automated response rule with a specified ID.
        
        @param request: DeleteAutomateResponseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutomateResponseConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes the automated response rule with a specified ID.
        
        @param request: DeleteAutomateResponseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutomateResponseConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes the automated response rule with a specified ID.
        
        @param request: DeleteAutomateResponseConfigRequest
        @return: DeleteAutomateResponseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_automate_response_config_with_options(request, runtime)

    async def delete_automate_response_config_async(
        self,
        request: cloud_siem_20220616_models.DeleteAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse:
        """
        @summary Deletes the automated response rule with a specified ID.
        
        @param request: DeleteAutomateResponseConfigRequest
        @return: DeleteAutomateResponseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_automate_response_config_with_options_async(request, runtime)

    def delete_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        """
        @summary Removes a third-party cloud account that is added to the threat analysis feature by using its AccessKey ID. You can add another cloud account based on your business requirements.
        
        @param request: DeleteBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindAccountResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Removes a third-party cloud account that is added to the threat analysis feature by using its AccessKey ID. You can add another cloud account based on your business requirements.
        
        @param request: DeleteBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindAccountResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Removes a third-party cloud account that is added to the threat analysis feature by using its AccessKey ID. You can add another cloud account based on your business requirements.
        
        @param request: DeleteBindAccountRequest
        @return: DeleteBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_bind_account_with_options(request, runtime)

    async def delete_bind_account_async(
        self,
        request: cloud_siem_20220616_models.DeleteBindAccountRequest,
    ) -> cloud_siem_20220616_models.DeleteBindAccountResponse:
        """
        @summary Removes a third-party cloud account that is added to the threat analysis feature by using its AccessKey ID. You can add another cloud account based on your business requirements.
        
        @param request: DeleteBindAccountRequest
        @return: DeleteBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_bind_account_with_options_async(request, runtime)

    def delete_customize_rule_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        """
        @summary Deletes a rule by rule ID.
        
        @param request: DeleteCustomizeRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes a rule by rule ID.
        
        @param request: DeleteCustomizeRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes a rule by rule ID.
        
        @param request: DeleteCustomizeRuleRequest
        @return: DeleteCustomizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_customize_rule_with_options(request, runtime)

    async def delete_customize_rule_async(
        self,
        request: cloud_siem_20220616_models.DeleteCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.DeleteCustomizeRuleResponse:
        """
        @summary Deletes a rule by rule ID.
        
        @param request: DeleteCustomizeRuleRequest
        @return: DeleteCustomizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_customize_rule_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        """
        @summary Removes a data source that is no longer required.
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
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
        """
        @summary Removes a data source that is no longer required.
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
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
        """
        @summary Removes a data source that is no longer required.
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceResponse:
        """
        @summary Removes a data source that is no longer required.
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        """
        @summary Removes a log.
        
        @param request: DeleteDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceLogResponse
        """
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
        """
        @summary Removes a log.
        
        @param request: DeleteDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceLogResponse
        """
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
        """
        @summary Removes a log.
        
        @param request: DeleteDataSourceLogRequest
        @return: DeleteDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_log_with_options(request, runtime)

    async def delete_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.DeleteDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.DeleteDataSourceLogResponse:
        """
        @summary Removes a log.
        
        @param request: DeleteDataSourceLogRequest
        @return: DeleteDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_log_with_options_async(request, runtime)

    def delete_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        """
        @summary Deletes an alert whitelist rule with a specified ID.
        
        @param request: DeleteWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWhiteRuleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes an alert whitelist rule with a specified ID.
        
        @param request: DeleteWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWhiteRuleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Deletes an alert whitelist rule with a specified ID.
        
        @param request: DeleteWhiteRuleListRequest
        @return: DeleteWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_white_rule_list_with_options(request, runtime)

    async def delete_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.DeleteWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DeleteWhiteRuleListResponse:
        """
        @summary Deletes an alert whitelist rule with a specified ID.
        
        @param request: DeleteWhiteRuleListRequest
        @return: DeleteWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_white_rule_list_with_options_async(request, runtime)

    def describe_aggregate_function_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        """
        @summary Queries the aggregate functions that are supported for a custom rule.
        
        @param request: DescribeAggregateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAggregateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the aggregate functions that are supported for a custom rule.
        
        @param request: DescribeAggregateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAggregateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the aggregate functions that are supported for a custom rule.
        
        @param request: DescribeAggregateFunctionRequest
        @return: DescribeAggregateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_aggregate_function_with_options(request, runtime)

    async def describe_aggregate_function_async(
        self,
        request: cloud_siem_20220616_models.DescribeAggregateFunctionRequest,
    ) -> cloud_siem_20220616_models.DescribeAggregateFunctionResponse:
        """
        @summary Queries the aggregate functions that are supported for a custom rule.
        
        @param request: DescribeAggregateFunctionRequest
        @return: DescribeAggregateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_aggregate_function_with_options_async(request, runtime)

    def describe_alert_scene_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        """
        @summary Queries the scenarios in which an alert needs to be added to the whitelist.
        
        @param request: DescribeAlertSceneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the scenarios in which an alert needs to be added to the whitelist.
        
        @param request: DescribeAlertSceneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the scenarios in which an alert needs to be added to the whitelist.
        
        @param request: DescribeAlertSceneRequest
        @return: DescribeAlertSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_scene_with_options(request, runtime)

    async def describe_alert_scene_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneResponse:
        """
        @summary Queries the scenarios in which an alert needs to be added to the whitelist.
        
        @param request: DescribeAlertSceneRequest
        @return: DescribeAlertSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_scene_with_options_async(request, runtime)

    def describe_alert_scene_by_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        """
        @summary Queries the scenarios and objects that can be added to an alert whitelist rule.
        
        @param request: DescribeAlertSceneByEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSceneByEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the scenarios and objects that can be added to an alert whitelist rule.
        
        @param request: DescribeAlertSceneByEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSceneByEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the scenarios and objects that can be added to an alert whitelist rule.
        
        @param request: DescribeAlertSceneByEventRequest
        @return: DescribeAlertSceneByEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_scene_by_event_with_options(request, runtime)

    async def describe_alert_scene_by_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSceneByEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSceneByEventResponse:
        """
        @summary Queries the scenarios and objects that can be added to an alert whitelist rule.
        
        @param request: DescribeAlertSceneByEventRequest
        @return: DescribeAlertSceneByEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_scene_by_event_with_options_async(request, runtime)

    def describe_alert_source_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        """
        @summary Queries alert data sources.
        
        @param request: DescribeAlertSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries alert data sources.
        
        @param request: DescribeAlertSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries alert data sources.
        
        @param request: DescribeAlertSourceRequest
        @return: DescribeAlertSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_options(request, runtime)

    async def describe_alert_source_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceResponse:
        """
        @summary Queries alert data sources.
        
        @param request: DescribeAlertSourceRequest
        @return: DescribeAlertSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_source_with_options_async(request, runtime)

    def describe_alert_source_with_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        """
        @summary Queries the data sources of the alert that is associated with an event.
        
        @param request: DescribeAlertSourceWithEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSourceWithEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the data sources of the alert that is associated with an event.
        
        @param request: DescribeAlertSourceWithEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertSourceWithEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the data sources of the alert that is associated with an event.
        
        @param request: DescribeAlertSourceWithEventRequest
        @return: DescribeAlertSourceWithEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_event_with_options(request, runtime)

    async def describe_alert_source_with_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertSourceWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse:
        """
        @summary Queries the data sources of the alert that is associated with an event.
        
        @param request: DescribeAlertSourceWithEventRequest
        @return: DescribeAlertSourceWithEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_source_with_event_with_options_async(request, runtime)

    def describe_alert_type_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        """
        @summary Queries the threat types that you can select when you create a custom rule.
        
        @param request: DescribeAlertTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
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
        """
        @summary Queries the threat types that you can select when you create a custom rule.
        
        @param request: DescribeAlertTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
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
        """
        @summary Queries the threat types that you can select when you create a custom rule.
        
        @param request: DescribeAlertTypeRequest
        @return: DescribeAlertTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_type_with_options(request, runtime)

    async def describe_alert_type_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertTypeResponse:
        """
        @summary Queries the threat types that you can select when you create a custom rule.
        
        @param request: DescribeAlertTypeRequest
        @return: DescribeAlertTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_type_with_options_async(request, runtime)

    def describe_alerts_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        """
        @summary Queries alerts within your account.
        
        @param request: DescribeAlertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.label_type):
            body['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries alerts within your account.
        
        @param request: DescribeAlertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not UtilClient.is_unset(request.label_type):
            body['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries alerts within your account.
        
        @param request: DescribeAlertsRequest
        @return: DescribeAlertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_options(request, runtime)

    async def describe_alerts_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsResponse:
        """
        @summary Queries alerts within your account.
        
        @param request: DescribeAlertsRequest
        @return: DescribeAlertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_options_async(request, runtime)

    def describe_alerts_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        """
        @summary Queries the number of alerts of different severities.
        
        @param request: DescribeAlertsCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_type):
            body['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of alerts of different severities.
        
        @param request: DescribeAlertsCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_type):
            body['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of alerts of different severities.
        
        @param request: DescribeAlertsCountRequest
        @return: DescribeAlertsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_count_with_options(request, runtime)

    async def describe_alerts_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsCountRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsCountResponse:
        """
        @summary Queries the number of alerts of different severities.
        
        @param request: DescribeAlertsCountRequest
        @return: DescribeAlertsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_count_with_options_async(request, runtime)

    def describe_alerts_with_entity_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        """
        @summary Queries the alerts that are associated with an entity.
        
        @param request: DescribeAlertsWithEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsWithEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
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
        """
        @summary Queries the alerts that are associated with an entity.
        
        @param request: DescribeAlertsWithEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsWithEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
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
        """
        @summary Queries the alerts that are associated with an entity.
        
        @param request: DescribeAlertsWithEntityRequest
        @return: DescribeAlertsWithEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_entity_with_options(request, runtime)

    async def describe_alerts_with_entity_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEntityRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEntityResponse:
        """
        @summary Queries the alerts that are associated with an entity.
        
        @param request: DescribeAlertsWithEntityRequest
        @return: DescribeAlertsWithEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_entity_with_options_async(request, runtime)

    def describe_alerts_with_event_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        """
        @summary Queries the alerts that are associated with an event.
        
        @param request: DescribeAlertsWithEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsWithEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the alerts that are associated with an event.
        
        @param request: DescribeAlertsWithEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertsWithEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the alerts that are associated with an event.
        
        @param request: DescribeAlertsWithEventRequest
        @return: DescribeAlertsWithEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_with_event_with_options(request, runtime)

    async def describe_alerts_with_event_async(
        self,
        request: cloud_siem_20220616_models.DescribeAlertsWithEventRequest,
    ) -> cloud_siem_20220616_models.DescribeAlertsWithEventResponse:
        """
        @summary Queries the alerts that are associated with an event.
        
        @param request: DescribeAlertsWithEventRequest
        @return: DescribeAlertsWithEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerts_with_event_with_options_async(request, runtime)

    def describe_auth_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        """
        @summary Checks whether the security information and event management (SIEM) system is granted the required permissions to access other cloud resources within your Alibaba Cloud account and whether the AliyunServiceRoleForSasCloudSiem service-linked role is created.
        
        @param request: DescribeAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuthResponse
        """
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
        """
        @summary Checks whether the security information and event management (SIEM) system is granted the required permissions to access other cloud resources within your Alibaba Cloud account and whether the AliyunServiceRoleForSasCloudSiem service-linked role is created.
        
        @param request: DescribeAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuthResponse
        """
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
        """
        @summary Checks whether the security information and event management (SIEM) system is granted the required permissions to access other cloud resources within your Alibaba Cloud account and whether the AliyunServiceRoleForSasCloudSiem service-linked role is created.
        
        @param request: DescribeAuthRequest
        @return: DescribeAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_with_options(request, runtime)

    async def describe_auth_async(
        self,
        request: cloud_siem_20220616_models.DescribeAuthRequest,
    ) -> cloud_siem_20220616_models.DescribeAuthResponse:
        """
        @summary Checks whether the security information and event management (SIEM) system is granted the required permissions to access other cloud resources within your Alibaba Cloud account and whether the AliyunServiceRoleForSasCloudSiem service-linked role is created.
        
        @param request: DescribeAuthRequest
        @return: DescribeAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auth_with_options_async(request, runtime)

    def describe_automate_response_config_counter_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        """
        @summary Queries the number of automated response rules.
        
        @param request: DescribeAutomateResponseConfigCounterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigCounterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of automated response rules.
        
        @param request: DescribeAutomateResponseConfigCounterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigCounterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of automated response rules.
        
        @param request: DescribeAutomateResponseConfigCounterRequest
        @return: DescribeAutomateResponseConfigCounterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_counter_with_options(request, runtime)

    async def describe_automate_response_config_counter_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse:
        """
        @summary Queries the number of automated response rules.
        
        @param request: DescribeAutomateResponseConfigCounterRequest
        @return: DescribeAutomateResponseConfigCounterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_counter_with_options_async(request, runtime)

    def describe_automate_response_config_feature_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        """
        @summary Queries the configurable fields and operators of an automated response rule.
        
        @param request: DescribeAutomateResponseConfigFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the configurable fields and operators of an automated response rule.
        
        @param request: DescribeAutomateResponseConfigFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the configurable fields and operators of an automated response rule.
        
        @param request: DescribeAutomateResponseConfigFeatureRequest
        @return: DescribeAutomateResponseConfigFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_feature_with_options(request, runtime)

    async def describe_automate_response_config_feature_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse:
        """
        @summary Queries the configurable fields and operators of an automated response rule.
        
        @param request: DescribeAutomateResponseConfigFeatureRequest
        @return: DescribeAutomateResponseConfigFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_feature_with_options_async(request, runtime)

    def describe_automate_response_config_play_books_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        """
        @summary Queries user-defined playbooks.
        
        @param request: DescribeAutomateResponseConfigPlayBooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigPlayBooksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries user-defined playbooks.
        
        @param request: DescribeAutomateResponseConfigPlayBooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutomateResponseConfigPlayBooksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries user-defined playbooks.
        
        @param request: DescribeAutomateResponseConfigPlayBooksRequest
        @return: DescribeAutomateResponseConfigPlayBooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_play_books_with_options(request, runtime)

    async def describe_automate_response_config_play_books_async(
        self,
        request: cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksRequest,
    ) -> cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse:
        """
        @summary Queries user-defined playbooks.
        
        @param request: DescribeAutomateResponseConfigPlayBooksRequest
        @return: DescribeAutomateResponseConfigPlayBooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_automate_response_config_play_books_with_options_async(request, runtime)

    def describe_cloud_siem_assets_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        """
        @summary Queries the assets that are associated with an event.
        
        @param request: DescribeCloudSiemAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemAssetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.asset_type):
            body['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.asset_uuid):
            body['AssetUuid'] = request.asset_uuid
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the assets that are associated with an event.
        
        @param request: DescribeCloudSiemAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemAssetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.asset_type):
            body['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.asset_uuid):
            body['AssetUuid'] = request.asset_uuid
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the assets that are associated with an event.
        
        @param request: DescribeCloudSiemAssetsRequest
        @return: DescribeCloudSiemAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_with_options(request, runtime)

    async def describe_cloud_siem_assets_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse:
        """
        @summary Queries the assets that are associated with an event.
        
        @param request: DescribeCloudSiemAssetsRequest
        @return: DescribeCloudSiemAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_assets_with_options_async(request, runtime)

    def describe_cloud_siem_assets_counter_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        """
        @summary Queries the number of assets that are associated with an event by asset type.
        
        @param request: DescribeCloudSiemAssetsCounterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemAssetsCounterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of assets that are associated with an event by asset type.
        
        @param request: DescribeCloudSiemAssetsCounterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemAssetsCounterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of assets that are associated with an event by asset type.
        
        @param request: DescribeCloudSiemAssetsCounterRequest
        @return: DescribeCloudSiemAssetsCounterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_counter_with_options(request, runtime)

    async def describe_cloud_siem_assets_counter_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse:
        """
        @summary Queries the number of assets that are associated with an event by asset type.
        
        @param request: DescribeCloudSiemAssetsCounterRequest
        @return: DescribeCloudSiemAssetsCounterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_assets_counter_with_options_async(request, runtime)

    def describe_cloud_siem_event_detail_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        """
        @summary Queries the details of an event.
        
        @param request: DescribeCloudSiemEventDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemEventDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of an event.
        
        @param request: DescribeCloudSiemEventDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemEventDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of an event.
        
        @param request: DescribeCloudSiemEventDetailRequest
        @return: DescribeCloudSiemEventDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_event_detail_with_options(request, runtime)

    async def describe_cloud_siem_event_detail_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventDetailRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse:
        """
        @summary Queries the details of an event.
        
        @param request: DescribeCloudSiemEventDetailRequest
        @return: DescribeCloudSiemEventDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_event_detail_with_options_async(request, runtime)

    def describe_cloud_siem_events_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        """
        @summary Queries events in SIEM.
        
        @param request: DescribeCloudSiemEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemEventsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries events in SIEM.
        
        @param request: DescribeCloudSiemEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudSiemEventsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries events in SIEM.
        
        @param request: DescribeCloudSiemEventsRequest
        @return: DescribeCloudSiemEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_events_with_options(request, runtime)

    async def describe_cloud_siem_events_async(
        self,
        request: cloud_siem_20220616_models.DescribeCloudSiemEventsRequest,
    ) -> cloud_siem_20220616_models.DescribeCloudSiemEventsResponse:
        """
        @summary Queries events in SIEM.
        
        @param request: DescribeCloudSiemEventsRequest
        @return: DescribeCloudSiemEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_siem_events_with_options_async(request, runtime)

    def describe_customize_rule_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        """
        @summary Queries the number of custom rules.
        
        @param request: DescribeCustomizeRuleCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of custom rules.
        
        @param request: DescribeCustomizeRuleCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of custom rules.
        
        @param request: DescribeCustomizeRuleCountRequest
        @return: DescribeCustomizeRuleCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_count_with_options(request, runtime)

    async def describe_customize_rule_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleCountRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse:
        """
        @summary Queries the number of custom rules.
        
        @param request: DescribeCustomizeRuleCountRequest
        @return: DescribeCustomizeRuleCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_count_with_options_async(request, runtime)

    def describe_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        """
        @summary Queries the historical simulation data that is used in a simulation test scenario.
        
        @param request: DescribeCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the historical simulation data that is used in a simulation test scenario.
        
        @param request: DescribeCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the historical simulation data that is used in a simulation test scenario.
        
        @param request: DescribeCustomizeRuleTestRequest
        @return: DescribeCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_with_options(request, runtime)

    async def describe_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse:
        """
        @summary Queries the historical simulation data that is used in a simulation test scenario.
        
        @param request: DescribeCustomizeRuleTestRequest
        @return: DescribeCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_test_with_options_async(request, runtime)

    def describe_customize_rule_test_histogram_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        """
        @summary Queries the chart that displays the test results of business data for a custom rule.
        
        @param request: DescribeCustomizeRuleTestHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleTestHistogramResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the chart that displays the test results of business data for a custom rule.
        
        @param request: DescribeCustomizeRuleTestHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomizeRuleTestHistogramResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the chart that displays the test results of business data for a custom rule.
        
        @param request: DescribeCustomizeRuleTestHistogramRequest
        @return: DescribeCustomizeRuleTestHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_histogram_with_options(request, runtime)

    async def describe_customize_rule_test_histogram_async(
        self,
        request: cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramRequest,
    ) -> cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse:
        """
        @summary Queries the chart that displays the test results of business data for a custom rule.
        
        @param request: DescribeCustomizeRuleTestHistogramRequest
        @return: DescribeCustomizeRuleTestHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_customize_rule_test_histogram_with_options_async(request, runtime)

    def describe_data_source_instance_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        """
        @summary Queries the details of a data source.
        
        @param request: DescribeDataSourceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSourceInstanceResponse
        """
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
        """
        @summary Queries the details of a data source.
        
        @param request: DescribeDataSourceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSourceInstanceResponse
        """
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
        """
        @summary Queries the details of a data source.
        
        @param request: DescribeDataSourceInstanceRequest
        @return: DescribeDataSourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_instance_with_options(request, runtime)

    async def describe_data_source_instance_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceInstanceRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceInstanceResponse:
        """
        @summary Queries the details of a data source.
        
        @param request: DescribeDataSourceInstanceRequest
        @return: DescribeDataSourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_source_instance_with_options_async(request, runtime)

    def describe_data_source_parameters_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        """
        @summary Queries the parameters of a data source.
        
        @param request: DescribeDataSourceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSourceParametersResponse
        """
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
        """
        @summary Queries the parameters of a data source.
        
        @param request: DescribeDataSourceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSourceParametersResponse
        """
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
        """
        @summary Queries the parameters of a data source.
        
        @param request: DescribeDataSourceParametersRequest
        @return: DescribeDataSourceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_parameters_with_options(request, runtime)

    async def describe_data_source_parameters_async(
        self,
        request: cloud_siem_20220616_models.DescribeDataSourceParametersRequest,
    ) -> cloud_siem_20220616_models.DescribeDataSourceParametersResponse:
        """
        @summary Queries the parameters of a data source.
        
        @param request: DescribeDataSourceParametersRequest
        @return: DescribeDataSourceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_source_parameters_with_options_async(request, runtime)

    def describe_dispose_and_playbook_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        """
        @summary Queries the list of entities and playbooks that need to be handled.
        
        @param request: DescribeDisposeAndPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisposeAndPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of entities and playbooks that need to be handled.
        
        @param request: DescribeDisposeAndPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisposeAndPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of entities and playbooks that need to be handled.
        
        @param request: DescribeDisposeAndPlaybookRequest
        @return: DescribeDisposeAndPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_and_playbook_with_options(request, runtime)

    async def describe_dispose_and_playbook_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeAndPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse:
        """
        @summary Queries the list of entities and playbooks that need to be handled.
        
        @param request: DescribeDisposeAndPlaybookRequest
        @return: DescribeDisposeAndPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispose_and_playbook_with_options_async(request, runtime)

    def describe_dispose_strategy_playbook_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        """
        @summary Queries the list of playbooks that are used by a handling policy.
        
        @param request: DescribeDisposeStrategyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisposeStrategyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of playbooks that are used by a handling policy.
        
        @param request: DescribeDisposeStrategyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisposeStrategyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of playbooks that are used by a handling policy.
        
        @param request: DescribeDisposeStrategyPlaybookRequest
        @return: DescribeDisposeStrategyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_strategy_playbook_with_options(request, runtime)

    async def describe_dispose_strategy_playbook_async(
        self,
        request: cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookRequest,
    ) -> cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse:
        """
        @summary Queries the list of playbooks that are used by a handling policy.
        
        @param request: DescribeDisposeStrategyPlaybookRequest
        @return: DescribeDisposeStrategyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispose_strategy_playbook_with_options_async(request, runtime)

    def describe_entity_info_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        """
        @summary Queries the details of an entity.
        
        @param request: DescribeEntityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEntityInfoResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of an entity.
        
        @param request: DescribeEntityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEntityInfoResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of an entity.
        
        @param request: DescribeEntityInfoRequest
        @return: DescribeEntityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_entity_info_with_options(request, runtime)

    async def describe_entity_info_async(
        self,
        request: cloud_siem_20220616_models.DescribeEntityInfoRequest,
    ) -> cloud_siem_20220616_models.DescribeEntityInfoResponse:
        """
        @summary Queries the details of an entity.
        
        @param request: DescribeEntityInfoRequest
        @return: DescribeEntityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_entity_info_with_options_async(request, runtime)

    def describe_event_count_by_threat_level_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        """
        @summary Queries the number of events by type.
        
        @param request: DescribeEventCountByThreatLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventCountByThreatLevelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
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
        """
        @summary Queries the number of events by type.
        
        @param request: DescribeEventCountByThreatLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventCountByThreatLevelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
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
        """
        @summary Queries the number of events by type.
        
        @param request: DescribeEventCountByThreatLevelRequest
        @return: DescribeEventCountByThreatLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_count_by_threat_level_with_options(request, runtime)

    async def describe_event_count_by_threat_level_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventCountByThreatLevelRequest,
    ) -> cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse:
        """
        @summary Queries the number of events by type.
        
        @param request: DescribeEventCountByThreatLevelRequest
        @return: DescribeEventCountByThreatLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_count_by_threat_level_with_options_async(request, runtime)

    def describe_event_dispose_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        """
        @summary Queries the handling policies of a historical event.
        
        @param request: DescribeEventDisposeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventDisposeResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the handling policies of a historical event.
        
        @param request: DescribeEventDisposeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventDisposeResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the handling policies of a historical event.
        
        @param request: DescribeEventDisposeRequest
        @return: DescribeEventDisposeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_dispose_with_options(request, runtime)

    async def describe_event_dispose_async(
        self,
        request: cloud_siem_20220616_models.DescribeEventDisposeRequest,
    ) -> cloud_siem_20220616_models.DescribeEventDisposeResponse:
        """
        @summary Queries the handling policies of a historical event.
        
        @param request: DescribeEventDisposeRequest
        @return: DescribeEventDisposeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_dispose_with_options_async(request, runtime)

    def describe_imported_log_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        """
        @summary Queries the number of logs that are added to the threat analysis feature.
        
        @param request: DescribeImportedLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportedLogCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of logs that are added to the threat analysis feature.
        
        @param request: DescribeImportedLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportedLogCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of logs that are added to the threat analysis feature.
        
        @param request: DescribeImportedLogCountRequest
        @return: DescribeImportedLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_imported_log_count_with_options(request, runtime)

    async def describe_imported_log_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeImportedLogCountRequest,
    ) -> cloud_siem_20220616_models.DescribeImportedLogCountResponse:
        """
        @summary Queries the number of logs that are added to the threat analysis feature.
        
        @param request: DescribeImportedLogCountRequest
        @return: DescribeImportedLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_imported_log_count_with_options_async(request, runtime)

    def describe_log_fields_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        """
        @summary Queries the fields that can be configured for a custom rule.
        
        @param request: DescribeLogFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogFieldsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the fields that can be configured for a custom rule.
        
        @param request: DescribeLogFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogFieldsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the fields that can be configured for a custom rule.
        
        @param request: DescribeLogFieldsRequest
        @return: DescribeLogFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_fields_with_options(request, runtime)

    async def describe_log_fields_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogFieldsRequest,
    ) -> cloud_siem_20220616_models.DescribeLogFieldsResponse:
        """
        @summary Queries the fields that can be configured for a custom rule.
        
        @param request: DescribeLogFieldsRequest
        @return: DescribeLogFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_fields_with_options_async(request, runtime)

    def describe_log_source_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        """
        @summary Queries the log sources that can be configured for a custom rule.
        
        @param request: DescribeLogSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the log sources that can be configured for a custom rule.
        
        @param request: DescribeLogSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the log sources that can be configured for a custom rule.
        
        @param request: DescribeLogSourceRequest
        @return: DescribeLogSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_source_with_options(request, runtime)

    async def describe_log_source_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogSourceRequest,
    ) -> cloud_siem_20220616_models.DescribeLogSourceResponse:
        """
        @summary Queries the log sources that can be configured for a custom rule.
        
        @param request: DescribeLogSourceRequest
        @return: DescribeLogSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_source_with_options_async(request, runtime)

    def describe_log_type_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        """
        @summary Queries the log types that can be configured for a custom rule.
        
        @param request: DescribeLogTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the log types that can be configured for a custom rule.
        
        @param request: DescribeLogTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the log types that can be configured for a custom rule.
        
        @param request: DescribeLogTypeRequest
        @return: DescribeLogTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_type_with_options(request, runtime)

    async def describe_log_type_async(
        self,
        request: cloud_siem_20220616_models.DescribeLogTypeRequest,
    ) -> cloud_siem_20220616_models.DescribeLogTypeResponse:
        """
        @summary Queries the log types that can be configured for a custom rule.
        
        @param request: DescribeLogTypeRequest
        @return: DescribeLogTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_type_with_options_async(request, runtime)

    def describe_operators_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        """
        @summary Queries the operator of a custom rule.
        
        @param request: DescribeOperatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOperatorsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the operator of a custom rule.
        
        @param request: DescribeOperatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOperatorsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the operator of a custom rule.
        
        @param request: DescribeOperatorsRequest
        @return: DescribeOperatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operators_with_options(request, runtime)

    async def describe_operators_async(
        self,
        request: cloud_siem_20220616_models.DescribeOperatorsRequest,
    ) -> cloud_siem_20220616_models.DescribeOperatorsResponse:
        """
        @summary Queries the operator of a custom rule.
        
        @param request: DescribeOperatorsRequest
        @return: DescribeOperatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_operators_with_options_async(request, runtime)

    def describe_prod_count_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        """
        @summary Queries the number of services that can be added to the threat analysis feature in Alibaba Cloud, Tenant Cloud, and Huawei Cloud.
        
        @param request: DescribeProdCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProdCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of services that can be added to the threat analysis feature in Alibaba Cloud, Tenant Cloud, and Huawei Cloud.
        
        @param request: DescribeProdCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProdCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the number of services that can be added to the threat analysis feature in Alibaba Cloud, Tenant Cloud, and Huawei Cloud.
        
        @param request: DescribeProdCountRequest
        @return: DescribeProdCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_prod_count_with_options(request, runtime)

    async def describe_prod_count_async(
        self,
        request: cloud_siem_20220616_models.DescribeProdCountRequest,
    ) -> cloud_siem_20220616_models.DescribeProdCountResponse:
        """
        @summary Queries the number of services that can be added to the threat analysis feature in Alibaba Cloud, Tenant Cloud, and Huawei Cloud.
        
        @param request: DescribeProdCountRequest
        @return: DescribeProdCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_prod_count_with_options_async(request, runtime)

    def describe_scope_users_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        """
        @summary Queries the list of users in the playbook scope.
        
        @param request: DescribeScopeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScopeUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of users in the playbook scope.
        
        @param request: DescribeScopeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScopeUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the list of users in the playbook scope.
        
        @param request: DescribeScopeUsersRequest
        @return: DescribeScopeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scope_users_with_options(request, runtime)

    async def describe_scope_users_async(
        self,
        request: cloud_siem_20220616_models.DescribeScopeUsersRequest,
    ) -> cloud_siem_20220616_models.DescribeScopeUsersResponse:
        """
        @summary Queries the list of users in the playbook scope.
        
        @param request: DescribeScopeUsersRequest
        @return: DescribeScopeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scope_users_with_options_async(request, runtime)

    def describe_service_status_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        """
        @summary Checks whether the threat analysis feature is authorized to access a resource directory.
        
        @param request: DescribeServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceStatusResponse
        """
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
        """
        @summary Checks whether the threat analysis feature is authorized to access a resource directory.
        
        @param request: DescribeServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceStatusResponse
        """
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
        """
        @summary Checks whether the threat analysis feature is authorized to access a resource directory.
        
        @param request: DescribeServiceStatusRequest
        @return: DescribeServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_status_with_options(request, runtime)

    async def describe_service_status_async(
        self,
        request: cloud_siem_20220616_models.DescribeServiceStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeServiceStatusResponse:
        """
        @summary Checks whether the threat analysis feature is authorized to access a resource directory.
        
        @param request: DescribeServiceStatusRequest
        @return: DescribeServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_status_with_options_async(request, runtime)

    def describe_storage_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        """
        @summary Queries the status of the Logstores for the threat analysis feature in Simple Log Service on the user side.
        
        @param request: DescribeStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the status of the Logstores for the threat analysis feature in Simple Log Service on the user side.
        
        @param request: DescribeStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the status of the Logstores for the threat analysis feature in Simple Log Service on the user side.
        
        @param request: DescribeStorageRequest
        @return: DescribeStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_with_options(request, runtime)

    async def describe_storage_async(
        self,
        request: cloud_siem_20220616_models.DescribeStorageRequest,
    ) -> cloud_siem_20220616_models.DescribeStorageResponse:
        """
        @summary Queries the status of the Logstores for the threat analysis feature in Simple Log Service on the user side.
        
        @param request: DescribeStorageRequest
        @return: DescribeStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_with_options_async(request, runtime)

    def describe_user_buy_status_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        """
        @summary Checks whether the current Alibaba Cloud account or the management account of a resource directory is used to purchase the threat analysis feature.
        
        @param request: DescribeUserBuyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserBuyStatusResponse
        """
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
        """
        @summary Checks whether the current Alibaba Cloud account or the management account of a resource directory is used to purchase the threat analysis feature.
        
        @param request: DescribeUserBuyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserBuyStatusResponse
        """
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
        """
        @summary Checks whether the current Alibaba Cloud account or the management account of a resource directory is used to purchase the threat analysis feature.
        
        @param request: DescribeUserBuyStatusRequest
        @return: DescribeUserBuyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_buy_status_with_options(request, runtime)

    async def describe_user_buy_status_async(
        self,
        request: cloud_siem_20220616_models.DescribeUserBuyStatusRequest,
    ) -> cloud_siem_20220616_models.DescribeUserBuyStatusResponse:
        """
        @summary Checks whether the current Alibaba Cloud account or the management account of a resource directory is used to purchase the threat analysis feature.
        
        @param request: DescribeUserBuyStatusRequest
        @return: DescribeUserBuyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_buy_status_with_options_async(request, runtime)

    def describe_waf_scope_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        """
        @summary Queries the protected domain names of the WAF instance for a user to which an entity belongs.
        
        @param request: DescribeWafScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafScopeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the protected domain names of the WAF instance for a user to which an entity belongs.
        
        @param request: DescribeWafScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafScopeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the protected domain names of the WAF instance for a user to which an entity belongs.
        
        @param request: DescribeWafScopeRequest
        @return: DescribeWafScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_scope_with_options(request, runtime)

    async def describe_waf_scope_async(
        self,
        request: cloud_siem_20220616_models.DescribeWafScopeRequest,
    ) -> cloud_siem_20220616_models.DescribeWafScopeResponse:
        """
        @summary Queries the protected domain names of the WAF instance for a user to which an entity belongs.
        
        @param request: DescribeWafScopeRequest
        @return: DescribeWafScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_scope_with_options_async(request, runtime)

    def describe_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        """
        @summary Queries a list of whitelist rules for alerts.
        
        @param request: DescribeWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWhiteRuleListResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of whitelist rules for alerts.
        
        @param request: DescribeWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWhiteRuleListResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of whitelist rules for alerts.
        
        @param request: DescribeWhiteRuleListRequest
        @return: DescribeWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_white_rule_list_with_options(request, runtime)

    async def describe_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.DescribeWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.DescribeWhiteRuleListResponse:
        """
        @summary Queries a list of whitelist rules for alerts.
        
        @param request: DescribeWhiteRuleListRequest
        @return: DescribeWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_white_rule_list_with_options_async(request, runtime)

    def enable_access_for_cloud_siem_with_options(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        """
        @summary Creates a service-linked role named AliyunServiceRoleForSasCloudSiem for the threat analysis feature. The feature can assume this role to access cloud services.
        
        @param request: EnableAccessForCloudSiemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAccessForCloudSiemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_submit):
            body['AutoSubmit'] = request.auto_submit
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates a service-linked role named AliyunServiceRoleForSasCloudSiem for the threat analysis feature. The feature can assume this role to access cloud services.
        
        @param request: EnableAccessForCloudSiemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAccessForCloudSiemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_submit):
            body['AutoSubmit'] = request.auto_submit
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates a service-linked role named AliyunServiceRoleForSasCloudSiem for the threat analysis feature. The feature can assume this role to access cloud services.
        
        @param request: EnableAccessForCloudSiemRequest
        @return: EnableAccessForCloudSiemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_access_for_cloud_siem_with_options(request, runtime)

    async def enable_access_for_cloud_siem_async(
        self,
        request: cloud_siem_20220616_models.EnableAccessForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableAccessForCloudSiemResponse:
        """
        @summary Creates a service-linked role named AliyunServiceRoleForSasCloudSiem for the threat analysis feature. The feature can assume this role to access cloud services.
        
        @param request: EnableAccessForCloudSiemRequest
        @return: EnableAccessForCloudSiemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_access_for_cloud_siem_with_options_async(request, runtime)

    def enable_service_for_cloud_siem_with_options(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        """
        @summary Authorizes the threat analysis feature to access a resource directory. This operation must be called by the management account of the resource directory.
        
        @param request: EnableServiceForCloudSiemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServiceForCloudSiemResponse
        """
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
        """
        @summary Authorizes the threat analysis feature to access a resource directory. This operation must be called by the management account of the resource directory.
        
        @param request: EnableServiceForCloudSiemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServiceForCloudSiemResponse
        """
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
        """
        @summary Authorizes the threat analysis feature to access a resource directory. This operation must be called by the management account of the resource directory.
        
        @param request: EnableServiceForCloudSiemRequest
        @return: EnableServiceForCloudSiemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_service_for_cloud_siem_with_options(request, runtime)

    async def enable_service_for_cloud_siem_async(
        self,
        request: cloud_siem_20220616_models.EnableServiceForCloudSiemRequest,
    ) -> cloud_siem_20220616_models.EnableServiceForCloudSiemResponse:
        """
        @summary Authorizes the threat analysis feature to access a resource directory. This operation must be called by the management account of the resource directory.
        
        @param request: EnableServiceForCloudSiemRequest
        @return: EnableServiceForCloudSiemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_service_for_cloud_siem_with_options_async(request, runtime)

    def get_capacity_with_options(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        """
        @summary Queries the storage capacity usage of the threat analysis feature and the purchased storage capacity
        
        @param request: GetCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the storage capacity usage of the threat analysis feature and the purchased storage capacity
        
        @param request: GetCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the storage capacity usage of the threat analysis feature and the purchased storage capacity
        
        @param request: GetCapacityRequest
        @return: GetCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    async def get_capacity_async(
        self,
        request: cloud_siem_20220616_models.GetCapacityRequest,
    ) -> cloud_siem_20220616_models.GetCapacityResponse:
        """
        @summary Queries the storage capacity usage of the threat analysis feature and the purchased storage capacity
        
        @param request: GetCapacityRequest
        @return: GetCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_capacity_with_options_async(request, runtime)

    def get_storage_with_options(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        """
        @summary Queries the storage configurations for the threat analysis feature on the user side.
        
        @param request: GetStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the storage configurations for the threat analysis feature on the user side.
        
        @param request: GetStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the storage configurations for the threat analysis feature on the user side.
        
        @param request: GetStorageRequest
        @return: GetStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_storage_with_options(request, runtime)

    async def get_storage_async(
        self,
        request: cloud_siem_20220616_models.GetStorageRequest,
    ) -> cloud_siem_20220616_models.GetStorageResponse:
        """
        @summary Queries the storage configurations for the threat analysis feature on the user side.
        
        @param request: GetStorageRequest
        @return: GetStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_storage_with_options_async(request, runtime)

    def list_account_access_id_with_options(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        """
        @summary Queries a list of AccessKey IDs of third-party cloud accounts that are added to the threat analysis feature.
        
        @param request: ListAccountAccessIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountAccessIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of AccessKey IDs of third-party cloud accounts that are added to the threat analysis feature.
        
        @param request: ListAccountAccessIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountAccessIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of AccessKey IDs of third-party cloud accounts that are added to the threat analysis feature.
        
        @param request: ListAccountAccessIdRequest
        @return: ListAccountAccessIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_account_access_id_with_options(request, runtime)

    async def list_account_access_id_async(
        self,
        request: cloud_siem_20220616_models.ListAccountAccessIdRequest,
    ) -> cloud_siem_20220616_models.ListAccountAccessIdResponse:
        """
        @summary Queries a list of AccessKey IDs of third-party cloud accounts that are added to the threat analysis feature.
        
        @param request: ListAccountAccessIdRequest
        @return: ListAccountAccessIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_account_access_id_with_options_async(request, runtime)

    def list_accounts_by_log_with_options(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        """
        @summary Query accounts by log.
        
        @param request: ListAccountsByLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsByLogResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Query accounts by log.
        
        @param request: ListAccountsByLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsByLogResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Query accounts by log.
        
        @param request: ListAccountsByLogRequest
        @return: ListAccountsByLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_by_log_with_options(request, runtime)

    async def list_accounts_by_log_async(
        self,
        request: cloud_siem_20220616_models.ListAccountsByLogRequest,
    ) -> cloud_siem_20220616_models.ListAccountsByLogResponse:
        """
        @summary Query accounts by log.
        
        @param request: ListAccountsByLogRequest
        @return: ListAccountsByLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_by_log_with_options_async(request, runtime)

    def list_all_prods_with_options(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        """
        @summary Queries a list of cloud services that can be added to the threat analysis feature.
        
        @param request: ListAllProdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of cloud services that can be added to the threat analysis feature.
        
        @param request: ListAllProdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of cloud services that can be added to the threat analysis feature.
        
        @param request: ListAllProdsRequest
        @return: ListAllProdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_prods_with_options(request, runtime)

    async def list_all_prods_async(
        self,
        request: cloud_siem_20220616_models.ListAllProdsRequest,
    ) -> cloud_siem_20220616_models.ListAllProdsResponse:
        """
        @summary Queries a list of cloud services that can be added to the threat analysis feature.
        
        @param request: ListAllProdsRequest
        @return: ListAllProdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_prods_with_options_async(request, runtime)

    def list_automate_response_configs_with_options(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        """
        @summary Queries automated response rules.
        
        @param request: ListAutomateResponseConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutomateResponseConfigsResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries automated response rules.
        
        @param request: ListAutomateResponseConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutomateResponseConfigsResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries automated response rules.
        
        @param request: ListAutomateResponseConfigsRequest
        @return: ListAutomateResponseConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_automate_response_configs_with_options(request, runtime)

    async def list_automate_response_configs_async(
        self,
        request: cloud_siem_20220616_models.ListAutomateResponseConfigsRequest,
    ) -> cloud_siem_20220616_models.ListAutomateResponseConfigsResponse:
        """
        @summary Queries automated response rules.
        
        @param request: ListAutomateResponseConfigsRequest
        @return: ListAutomateResponseConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_automate_response_configs_with_options_async(request, runtime)

    def list_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        """
        @summary Queries a list of cloud accounts that are added to the threat analysis feature.
        
        @param request: ListBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of cloud accounts that are added to the threat analysis feature.
        
        @param request: ListBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries a list of cloud accounts that are added to the threat analysis feature.
        
        @param request: ListBindAccountRequest
        @return: ListBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bind_account_with_options(request, runtime)

    async def list_bind_account_async(
        self,
        request: cloud_siem_20220616_models.ListBindAccountRequest,
    ) -> cloud_siem_20220616_models.ListBindAccountResponse:
        """
        @summary Queries a list of cloud accounts that are added to the threat analysis feature.
        
        @param request: ListBindAccountRequest
        @return: ListBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bind_account_with_options_async(request, runtime)

    def list_bind_data_sources_with_options(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        """
        @summary Queries a list of data sources that are added to the threat analysis feature.
        
        @param request: ListBindDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindDataSourcesResponse
        """
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
        """
        @summary Queries a list of data sources that are added to the threat analysis feature.
        
        @param request: ListBindDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindDataSourcesResponse
        """
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
        """
        @summary Queries a list of data sources that are added to the threat analysis feature.
        
        @param request: ListBindDataSourcesRequest
        @return: ListBindDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bind_data_sources_with_options(request, runtime)

    async def list_bind_data_sources_async(
        self,
        request: cloud_siem_20220616_models.ListBindDataSourcesRequest,
    ) -> cloud_siem_20220616_models.ListBindDataSourcesResponse:
        """
        @summary Queries a list of data sources that are added to the threat analysis feature.
        
        @param request: ListBindDataSourcesRequest
        @return: ListBindDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bind_data_sources_with_options_async(request, runtime)

    def list_cloud_siem_customize_rules_with_options(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        """
        @summary Queries custom rules.
        
        @param request: ListCloudSiemCustomizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudSiemCustomizeRulesResponse
        """
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
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries custom rules.
        
        @param request: ListCloudSiemCustomizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudSiemCustomizeRulesResponse
        """
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
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries custom rules.
        
        @param request: ListCloudSiemCustomizeRulesRequest
        @return: ListCloudSiemCustomizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_customize_rules_with_options(request, runtime)

    async def list_cloud_siem_customize_rules_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemCustomizeRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse:
        """
        @summary Queries custom rules.
        
        @param request: ListCloudSiemCustomizeRulesRequest
        @return: ListCloudSiemCustomizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_siem_customize_rules_with_options_async(request, runtime)

    def list_cloud_siem_predefined_rules_with_options(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        """
        @summary Queries predefined rules.
        
        @param request: ListCloudSiemPredefinedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudSiemPredefinedRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.att_ck):
            body['AttCk'] = request.att_ck
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries predefined rules.
        
        @param request: ListCloudSiemPredefinedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudSiemPredefinedRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.att_ck):
            body['AttCk'] = request.att_ck
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries predefined rules.
        
        @param request: ListCloudSiemPredefinedRulesRequest
        @return: ListCloudSiemPredefinedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_predefined_rules_with_options(request, runtime)

    async def list_cloud_siem_predefined_rules_async(
        self,
        request: cloud_siem_20220616_models.ListCloudSiemPredefinedRulesRequest,
    ) -> cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse:
        """
        @summary Queries predefined rules.
        
        @param request: ListCloudSiemPredefinedRulesRequest
        @return: ListCloudSiemPredefinedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_siem_predefined_rules_with_options_async(request, runtime)

    def list_customize_rule_test_result_with_options(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        """
        @summary Queries the test results of a custom rule.
        
        @param request: ListCustomizeRuleTestResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomizeRuleTestResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.verify_type):
            body['VerifyType'] = request.verify_type
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
        """
        @summary Queries the test results of a custom rule.
        
        @param request: ListCustomizeRuleTestResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomizeRuleTestResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.verify_type):
            body['VerifyType'] = request.verify_type
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
        """
        @summary Queries the test results of a custom rule.
        
        @param request: ListCustomizeRuleTestResultRequest
        @return: ListCustomizeRuleTestResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_customize_rule_test_result_with_options(request, runtime)

    async def list_customize_rule_test_result_async(
        self,
        request: cloud_siem_20220616_models.ListCustomizeRuleTestResultRequest,
    ) -> cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse:
        """
        @summary Queries the test results of a custom rule.
        
        @param request: ListCustomizeRuleTestResultRequest
        @return: ListCustomizeRuleTestResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_customize_rule_test_result_with_options_async(request, runtime)

    def list_data_source_logs_with_options(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        """
        @summary Queries the logs of a data source.
        
        @param request: ListDataSourceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceLogsResponse
        """
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
        """
        @summary Queries the logs of a data source.
        
        @param request: ListDataSourceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceLogsResponse
        """
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
        """
        @summary Queries the logs of a data source.
        
        @param request: ListDataSourceLogsRequest
        @return: ListDataSourceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_logs_with_options(request, runtime)

    async def list_data_source_logs_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceLogsRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceLogsResponse:
        """
        @summary Queries the logs of a data source.
        
        @param request: ListDataSourceLogsRequest
        @return: ListDataSourceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_logs_with_options_async(request, runtime)

    def list_data_source_types_with_options(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        """
        @summary Queries a list of data source types in third-party cloud services that can be added to the threat analysis feature.
        
        @param request: ListDataSourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTypesResponse
        """
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
        """
        @summary Queries a list of data source types in third-party cloud services that can be added to the threat analysis feature.
        
        @param request: ListDataSourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTypesResponse
        """
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
        """
        @summary Queries a list of data source types in third-party cloud services that can be added to the threat analysis feature.
        
        @param request: ListDataSourceTypesRequest
        @return: ListDataSourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_types_with_options(request, runtime)

    async def list_data_source_types_async(
        self,
        request: cloud_siem_20220616_models.ListDataSourceTypesRequest,
    ) -> cloud_siem_20220616_models.ListDataSourceTypesResponse:
        """
        @summary Queries a list of data source types in third-party cloud services that can be added to the threat analysis feature.
        
        @param request: ListDataSourceTypesRequest
        @return: ListDataSourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_types_with_options_async(request, runtime)

    def list_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        """
        @summary Queries the information about the cloud services that are integrated with the threat analysis feature, the logs of the cloud services, and the delivery of the logs.
        
        @param request: ListDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the information about the cloud services that are integrated with the threat analysis feature, the logs of the cloud services, and the delivery of the logs.
        
        @param request: ListDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the information about the cloud services that are integrated with the threat analysis feature, the logs of the cloud services, and the delivery of the logs.
        
        @param request: ListDeliveryRequest
        @return: ListDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_with_options(request, runtime)

    async def list_delivery_async(
        self,
        request: cloud_siem_20220616_models.ListDeliveryRequest,
    ) -> cloud_siem_20220616_models.ListDeliveryResponse:
        """
        @summary Queries the information about the cloud services that are integrated with the threat analysis feature, the logs of the cloud services, and the delivery of the logs.
        
        @param request: ListDeliveryRequest
        @return: ListDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_delivery_with_options_async(request, runtime)

    def list_dispose_strategy_with_options(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        """
        @summary Queries handling policies.
        
        @param request: ListDisposeStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDisposeStrategyResponse
        """
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
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries handling policies.
        
        @param request: ListDisposeStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDisposeStrategyResponse
        """
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
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries handling policies.
        
        @param request: ListDisposeStrategyRequest
        @return: ListDisposeStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dispose_strategy_with_options(request, runtime)

    async def list_dispose_strategy_async(
        self,
        request: cloud_siem_20220616_models.ListDisposeStrategyRequest,
    ) -> cloud_siem_20220616_models.ListDisposeStrategyResponse:
        """
        @summary Queries handling policies.
        
        @param request: ListDisposeStrategyRequest
        @return: ListDisposeStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dispose_strategy_with_options_async(request, runtime)

    def list_entities_with_options(
        self,
        request: cloud_siem_20220616_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListEntitiesResponse:
        """
        @summary 查询实体列表
        
        @param request: ListEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntitiesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.is_malware_entity):
            body['IsMalwareEntity'] = request.is_malware_entity
        if not UtilClient.is_unset(request.malware_type):
            body['MalwareType'] = request.malware_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEntities',
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
            cloud_siem_20220616_models.ListEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_with_options_async(
        self,
        request: cloud_siem_20220616_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListEntitiesResponse:
        """
        @summary 查询实体列表
        
        @param request: ListEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntitiesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_name):
            body['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.is_malware_entity):
            body['IsMalwareEntity'] = request.is_malware_entity
        if not UtilClient.is_unset(request.malware_type):
            body['MalwareType'] = request.malware_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEntities',
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
            cloud_siem_20220616_models.ListEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities(
        self,
        request: cloud_siem_20220616_models.ListEntitiesRequest,
    ) -> cloud_siem_20220616_models.ListEntitiesResponse:
        """
        @summary 查询实体列表
        
        @param request: ListEntitiesRequest
        @return: ListEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_entities_with_options(request, runtime)

    async def list_entities_async(
        self,
        request: cloud_siem_20220616_models.ListEntitiesRequest,
    ) -> cloud_siem_20220616_models.ListEntitiesResponse:
        """
        @summary 查询实体列表
        
        @param request: ListEntitiesRequest
        @return: ListEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_entities_with_options_async(request, runtime)

    def list_imported_logs_by_prod_with_options(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        """
        @summary Queries the details of the logs in a cloud service that is added to the threat analysis feature.
        
        @param request: ListImportedLogsByProdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImportedLogsByProdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of the logs in a cloud service that is added to the threat analysis feature.
        
        @param request: ListImportedLogsByProdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImportedLogsByProdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not UtilClient.is_unset(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Queries the details of the logs in a cloud service that is added to the threat analysis feature.
        
        @param request: ListImportedLogsByProdRequest
        @return: ListImportedLogsByProdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_imported_logs_by_prod_with_options(request, runtime)

    async def list_imported_logs_by_prod_async(
        self,
        request: cloud_siem_20220616_models.ListImportedLogsByProdRequest,
    ) -> cloud_siem_20220616_models.ListImportedLogsByProdResponse:
        """
        @summary Queries the details of the logs in a cloud service that is added to the threat analysis feature.
        
        @param request: ListImportedLogsByProdRequest
        @return: ListImportedLogsByProdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_imported_logs_by_prod_with_options_async(request, runtime)

    def list_project_log_stores_with_options(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        """
        @summary Queries the dedicated Simple Log Service project and Logstore for a cloud service based on the patterns of the project and Logstore names.
        
        @param request: ListProjectLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectLogStoresResponse
        """
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
        """
        @summary Queries the dedicated Simple Log Service project and Logstore for a cloud service based on the patterns of the project and Logstore names.
        
        @param request: ListProjectLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectLogStoresResponse
        """
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
        """
        @summary Queries the dedicated Simple Log Service project and Logstore for a cloud service based on the patterns of the project and Logstore names.
        
        @param request: ListProjectLogStoresRequest
        @return: ListProjectLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_log_stores_with_options(request, runtime)

    async def list_project_log_stores_async(
        self,
        request: cloud_siem_20220616_models.ListProjectLogStoresRequest,
    ) -> cloud_siem_20220616_models.ListProjectLogStoresResponse:
        """
        @summary Queries the dedicated Simple Log Service project and Logstore for a cloud service based on the patterns of the project and Logstore names.
        
        @param request: ListProjectLogStoresRequest
        @return: ListProjectLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_log_stores_with_options_async(request, runtime)

    def list_rd_users_with_options(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        """
        @summary Queries a list of Alibaba Cloud accounts that are added to the threat analysis feature for centralized management. These accounts can be used to perform operations supported by the threat analysis feature, such as adding logs and handling events.
        
        @param request: ListRdUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRdUsersResponse
        """
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
        """
        @summary Queries a list of Alibaba Cloud accounts that are added to the threat analysis feature for centralized management. These accounts can be used to perform operations supported by the threat analysis feature, such as adding logs and handling events.
        
        @param request: ListRdUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRdUsersResponse
        """
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
        """
        @summary Queries a list of Alibaba Cloud accounts that are added to the threat analysis feature for centralized management. These accounts can be used to perform operations supported by the threat analysis feature, such as adding logs and handling events.
        
        @param request: ListRdUsersRequest
        @return: ListRdUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rd_users_with_options(request, runtime)

    async def list_rd_users_async(
        self,
        request: cloud_siem_20220616_models.ListRdUsersRequest,
    ) -> cloud_siem_20220616_models.ListRdUsersResponse:
        """
        @summary Queries a list of Alibaba Cloud accounts that are added to the threat analysis feature for centralized management. These accounts can be used to perform operations supported by the threat analysis feature, such as adding logs and handling events.
        
        @param request: ListRdUsersRequest
        @return: ListRdUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rd_users_with_options_async(request, runtime)

    def modify_bind_account_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        """
        @summary Modifies a third-party cloud account that is added to the threat analysis feature.
        
        @param request: ModifyBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBindAccountResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Modifies a third-party cloud account that is added to the threat analysis feature.
        
        @param request: ModifyBindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBindAccountResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Modifies a third-party cloud account that is added to the threat analysis feature.
        
        @param request: ModifyBindAccountRequest
        @return: ModifyBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_bind_account_with_options(request, runtime)

    async def modify_bind_account_async(
        self,
        request: cloud_siem_20220616_models.ModifyBindAccountRequest,
    ) -> cloud_siem_20220616_models.ModifyBindAccountResponse:
        """
        @summary Modifies a third-party cloud account that is added to the threat analysis feature.
        
        @param request: ModifyBindAccountRequest
        @return: ModifyBindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_bind_account_with_options_async(request, runtime)

    def modify_data_source_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        """
        @summary Modifies a data source that is added to the threat analysis feature.
        
        @param request: ModifyDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
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
        """
        @summary Modifies a data source that is added to the threat analysis feature.
        
        @param request: ModifyDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
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
        """
        @summary Modifies a data source that is added to the threat analysis feature.
        
        @param request: ModifyDataSourceRequest
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_with_options(request, runtime)

    async def modify_data_source_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceResponse:
        """
        @summary Modifies a data source that is added to the threat analysis feature.
        
        @param request: ModifyDataSourceRequest
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_with_options_async(request, runtime)

    def modify_data_source_log_with_options(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        """
        @summary Modifies the description of the logs that are added to the threat analysis feature for a data source within a cloud account.
        
        @param request: ModifyDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceLogResponse
        """
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
        """
        @summary Modifies the description of the logs that are added to the threat analysis feature for a data source within a cloud account.
        
        @param request: ModifyDataSourceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceLogResponse
        """
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
        """
        @summary Modifies the description of the logs that are added to the threat analysis feature for a data source within a cloud account.
        
        @param request: ModifyDataSourceLogRequest
        @return: ModifyDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_log_with_options(request, runtime)

    async def modify_data_source_log_async(
        self,
        request: cloud_siem_20220616_models.ModifyDataSourceLogRequest,
    ) -> cloud_siem_20220616_models.ModifyDataSourceLogResponse:
        """
        @summary Modifies the description of the logs that are added to the threat analysis feature for a data source within a cloud account.
        
        @param request: ModifyDataSourceLogRequest
        @return: ModifyDataSourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_source_log_with_options_async(request, runtime)

    def open_delivery_with_options(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        """
        @summary Enables the log delivery feature for a cloud service that is integrated with Simple Log Service.
        
        @param request: OpenDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Enables the log delivery feature for a cloud service that is integrated with Simple Log Service.
        
        @param request: OpenDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Enables the log delivery feature for a cloud service that is integrated with Simple Log Service.
        
        @param request: OpenDeliveryRequest
        @return: OpenDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_delivery_with_options(request, runtime)

    async def open_delivery_async(
        self,
        request: cloud_siem_20220616_models.OpenDeliveryRequest,
    ) -> cloud_siem_20220616_models.OpenDeliveryResponse:
        """
        @summary Enables the log delivery feature for a cloud service that is integrated with Simple Log Service.
        
        @param request: OpenDeliveryRequest
        @return: OpenDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_delivery_with_options_async(request, runtime)

    def post_automate_response_config_with_options(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        """
        @summary Creates or updates an automatic response rule.
        
        @param request: PostAutomateResponseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostAutomateResponseConfigResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates an automatic response rule.
        
        @param request: PostAutomateResponseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostAutomateResponseConfigResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates an automatic response rule.
        
        @param request: PostAutomateResponseConfigRequest
        @return: PostAutomateResponseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_automate_response_config_with_options(request, runtime)

    async def post_automate_response_config_async(
        self,
        request: cloud_siem_20220616_models.PostAutomateResponseConfigRequest,
    ) -> cloud_siem_20220616_models.PostAutomateResponseConfigResponse:
        """
        @summary Creates or updates an automatic response rule.
        
        @param request: PostAutomateResponseConfigRequest
        @return: PostAutomateResponseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_automate_response_config_with_options_async(request, runtime)

    def post_customize_rule_with_options(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        """
        @summary Creates or updates a custom rule.
        
        @param request: PostCustomizeRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostCustomizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not UtilClient.is_unset(request.att_ck):
            body['AttCk'] = request.att_ck
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates a custom rule.
        
        @param request: PostCustomizeRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostCustomizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not UtilClient.is_unset(request.att_ck):
            body['AttCk'] = request.att_ck
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates a custom rule.
        
        @param request: PostCustomizeRuleRequest
        @return: PostCustomizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_with_options(request, runtime)

    async def post_customize_rule_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleResponse:
        """
        @summary Creates or updates a custom rule.
        
        @param request: PostCustomizeRuleRequest
        @return: PostCustomizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_customize_rule_with_options_async(request, runtime)

    def post_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        """
        @summary Submits a custom rule for testing.
        
        @param request: PostCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits a custom rule for testing.
        
        @param request: PostCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits a custom rule for testing.
        
        @param request: PostCustomizeRuleTestRequest
        @return: PostCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_test_with_options(request, runtime)

    async def post_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.PostCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostCustomizeRuleTestResponse:
        """
        @summary Submits a custom rule for testing.
        
        @param request: PostCustomizeRuleTestRequest
        @return: PostCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_customize_rule_test_with_options_async(request, runtime)

    def post_event_dispose_and_whiterule_list_with_options(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        """
        @summary Submits event handling information.
        
        @param request: PostEventDisposeAndWhiteruleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostEventDisposeAndWhiteruleListResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
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
        """
        @summary Submits event handling information.
        
        @param request: PostEventDisposeAndWhiteruleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostEventDisposeAndWhiteruleListResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
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
        """
        @summary Submits event handling information.
        
        @param request: PostEventDisposeAndWhiteruleListRequest
        @return: PostEventDisposeAndWhiteruleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_event_dispose_and_whiterule_list_with_options(request, runtime)

    async def post_event_dispose_and_whiterule_list_async(
        self,
        request: cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse:
        """
        @summary Submits event handling information.
        
        @param request: PostEventDisposeAndWhiteruleListRequest
        @return: PostEventDisposeAndWhiteruleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_event_dispose_and_whiterule_list_with_options_async(request, runtime)

    def post_event_whiterule_list_with_options(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        """
        @summary Submits an alert whitelist rule.
        
        @param request: PostEventWhiteruleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostEventWhiteruleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits an alert whitelist rule.
        
        @param request: PostEventWhiteruleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostEventWhiteruleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits an alert whitelist rule.
        
        @param request: PostEventWhiteruleListRequest
        @return: PostEventWhiteruleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_event_whiterule_list_with_options(request, runtime)

    async def post_event_whiterule_list_async(
        self,
        request: cloud_siem_20220616_models.PostEventWhiteruleListRequest,
    ) -> cloud_siem_20220616_models.PostEventWhiteruleListResponse:
        """
        @summary Submits an alert whitelist rule.
        
        @param request: PostEventWhiteruleListRequest
        @return: PostEventWhiteruleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_event_whiterule_list_with_options_async(request, runtime)

    def post_finish_customize_rule_test_with_options(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        """
        @summary Ends the test of a custom rule.
        
        @param request: PostFinishCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostFinishCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Ends the test of a custom rule.
        
        @param request: PostFinishCustomizeRuleTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostFinishCustomizeRuleTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Ends the test of a custom rule.
        
        @param request: PostFinishCustomizeRuleTestRequest
        @return: PostFinishCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_finish_customize_rule_test_with_options(request, runtime)

    async def post_finish_customize_rule_test_async(
        self,
        request: cloud_siem_20220616_models.PostFinishCustomizeRuleTestRequest,
    ) -> cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse:
        """
        @summary Ends the test of a custom rule.
        
        @param request: PostFinishCustomizeRuleTestRequest
        @return: PostFinishCustomizeRuleTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_finish_customize_rule_test_with_options_async(request, runtime)

    def post_rule_status_change_with_options(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        """
        @summary Updates the status of a custom rule.
        
        @param request: PostRuleStatusChangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostRuleStatusChangeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Updates the status of a custom rule.
        
        @param request: PostRuleStatusChangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostRuleStatusChangeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Updates the status of a custom rule.
        
        @param request: PostRuleStatusChangeRequest
        @return: PostRuleStatusChangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_rule_status_change_with_options(request, runtime)

    async def post_rule_status_change_async(
        self,
        request: cloud_siem_20220616_models.PostRuleStatusChangeRequest,
    ) -> cloud_siem_20220616_models.PostRuleStatusChangeResponse:
        """
        @summary Updates the status of a custom rule.
        
        @param request: PostRuleStatusChangeRequest
        @return: PostRuleStatusChangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_rule_status_change_with_options_async(request, runtime)

    def restore_capacity_with_options(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        """
        @summary Releases storage to reduce the storage usage. The release operation is irreversible and may cause data loss. Proceed with caution.
        
        @param request: RestoreCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Releases storage to reduce the storage usage. The release operation is irreversible and may cause data loss. Proceed with caution.
        
        @param request: RestoreCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Releases storage to reduce the storage usage. The release operation is irreversible and may cause data loss. Proceed with caution.
        
        @param request: RestoreCapacityRequest
        @return: RestoreCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_capacity_with_options(request, runtime)

    async def restore_capacity_async(
        self,
        request: cloud_siem_20220616_models.RestoreCapacityRequest,
    ) -> cloud_siem_20220616_models.RestoreCapacityResponse:
        """
        @summary Releases storage to reduce the storage usage. The release operation is irreversible and may cause data loss. Proceed with caution.
        
        @param request: RestoreCapacityRequest
        @return: RestoreCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_capacity_with_options_async(request, runtime)

    def set_storage_with_options(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        """
        @summary Configures the settings of log storage, such as the storage duration and storage region.
        
        @param request: SetStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Configures the settings of log storage, such as the storage duration and storage region.
        
        @param request: SetStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Configures the settings of log storage, such as the storage duration and storage region.
        
        @param request: SetStorageRequest
        @return: SetStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_storage_with_options(request, runtime)

    async def set_storage_async(
        self,
        request: cloud_siem_20220616_models.SetStorageRequest,
    ) -> cloud_siem_20220616_models.SetStorageResponse:
        """
        @summary Configures the settings of log storage, such as the storage duration and storage region.
        
        @param request: SetStorageRequest
        @return: SetStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_storage_with_options_async(request, runtime)

    def submit_import_log_tasks_with_options(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        """
        @summary Submits log collection tasks at a time.
        
        @param request: SubmitImportLogTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImportLogTasksResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits log collection tasks at a time.
        
        @param request: SubmitImportLogTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImportLogTasksResponse
        """
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
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Submits log collection tasks at a time.
        
        @param request: SubmitImportLogTasksRequest
        @return: SubmitImportLogTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_import_log_tasks_with_options(request, runtime)

    async def submit_import_log_tasks_async(
        self,
        request: cloud_siem_20220616_models.SubmitImportLogTasksRequest,
    ) -> cloud_siem_20220616_models.SubmitImportLogTasksResponse:
        """
        @summary Submits log collection tasks at a time.
        
        @param request: SubmitImportLogTasksRequest
        @return: SubmitImportLogTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_import_log_tasks_with_options_async(request, runtime)

    def update_automate_response_config_status_with_options(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        """
        @summary Updates the status of an automatic response rule.
        
        @param request: UpdateAutomateResponseConfigStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutomateResponseConfigStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Updates the status of an automatic response rule.
        
        @param request: UpdateAutomateResponseConfigStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutomateResponseConfigStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Updates the status of an automatic response rule.
        
        @param request: UpdateAutomateResponseConfigStatusRequest
        @return: UpdateAutomateResponseConfigStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_automate_response_config_status_with_options(request, runtime)

    async def update_automate_response_config_status_async(
        self,
        request: cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusRequest,
    ) -> cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse:
        """
        @summary Updates the status of an automatic response rule.
        
        @param request: UpdateAutomateResponseConfigStatusRequest
        @return: UpdateAutomateResponseConfigStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_automate_response_config_status_with_options_async(request, runtime)

    def update_white_rule_list_with_options(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        """
        @summary Creates or updates an alert whitelist rule.
        
        @param request: UpdateWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWhiteRuleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates an alert whitelist rule.
        
        @param request: UpdateWhiteRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWhiteRuleListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
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
        """
        @summary Creates or updates an alert whitelist rule.
        
        @param request: UpdateWhiteRuleListRequest
        @return: UpdateWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_white_rule_list_with_options(request, runtime)

    async def update_white_rule_list_async(
        self,
        request: cloud_siem_20220616_models.UpdateWhiteRuleListRequest,
    ) -> cloud_siem_20220616_models.UpdateWhiteRuleListResponse:
        """
        @summary Creates or updates an alert whitelist rule.
        
        @param request: UpdateWhiteRuleListRequest
        @return: UpdateWhiteRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_white_rule_list_with_options_async(request, runtime)
