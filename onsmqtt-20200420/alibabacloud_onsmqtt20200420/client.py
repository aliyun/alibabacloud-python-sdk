# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_onsmqtt20200420 import models as ons_mqtt_20200420_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('onsmqtt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_ca_certificate_with_options(request, runtime)

    async def active_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_ca_certificate_with_options_async(request, runtime)

    def active_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_device_certificate(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_device_certificate_with_options(request, runtime)

    async def active_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_device_certificate_with_options_async(request, runtime)

    def apply_token_with_options(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ApplyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actions):
            query['Actions'] = request.actions
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ApplyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ApplyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actions):
            query['Actions'] = request.actions
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ApplyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_token(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ApplyTokenRequest
        @return: ApplyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_token_with_options(request, runtime)

    async def apply_token_async(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ApplyTokenRequest
        @return: ApplyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_token_with_options_async(request, runtime)

    def batch_query_session_by_client_ids_with_options(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        *   Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: BatchQuerySessionByClientIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchQuerySessionByClientIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQuerySessionByClientIds',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_session_by_client_ids_with_options_async(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        *   Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: BatchQuerySessionByClientIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchQuerySessionByClientIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQuerySessionByClientIds',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_session_by_client_ids(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        *   Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: BatchQuerySessionByClientIdsRequest
        @return: BatchQuerySessionByClientIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_query_session_by_client_ids_with_options(request, runtime)

    async def batch_query_session_by_client_ids_async(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        *   Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: BatchQuerySessionByClientIdsRequest
        @return: BatchQuerySessionByClientIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_query_session_by_client_ids_with_options_async(request, runtime)

    def create_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: CreateGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.CreateGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: CreateGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.CreateGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_id(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: CreateGroupIdRequest
        @return: CreateGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_id_with_options(request, runtime)

    async def create_group_id_async(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: CreateGroupIdRequest
        @return: CreateGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_id_with_options_async(request, runtime)

    def delete_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ca_certificate_with_options(request, runtime)

    async def delete_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ca_certificate_with_options_async(request, runtime)

    def delete_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_certificate(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_certificate_with_options(request, runtime)

    async def delete_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_certificate_with_options_async(request, runtime)

    def delete_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: DeleteGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: DeleteGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_id(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: DeleteGroupIdRequest
        @return: DeleteGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_id_with_options(request, runtime)

    async def delete_group_id_async(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: DeleteGroupIdRequest
        @return: DeleteGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_id_with_options_async(request, runtime)

    def get_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ca_certificate_with_options(request, runtime)

    async def get_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_certificate_with_options_async(request, runtime)

    def get_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_certificate(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_certificate_with_options(request, runtime)

    async def get_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_certificate_with_options_async(request, runtime)

    def get_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: GetDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: GetDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_credential(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: GetDeviceCredentialRequest
        @return: GetDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_credential_with_options(request, runtime)

    async def get_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: GetDeviceCredentialRequest
        @return: GetDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_credential_with_options_async(request, runtime)

    def get_register_code_with_options(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisterCode',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetRegisterCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_register_code_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegisterCode',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetRegisterCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_register_code(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_register_code_with_options(request, runtime)

    async def get_register_code_async(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_register_code_with_options_async(request, runtime)

    def inactivate_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InactivateCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def inactivate_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InactivateCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inactivate_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.inactivate_ca_certificate_with_options(request, runtime)

    async def inactivate_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inactivate_ca_certificate_with_options_async(request, runtime)

    def inactivate_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InactivateDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def inactivate_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not UtilClient.is_unset(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InactivateDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inactivate_device_certificate(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.inactivate_device_certificate_with_options(request, runtime)

    async def inactivate_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inactivate_device_certificate_with_options_async(request, runtime)

    def list_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ca_certificate_with_options(request, runtime)

    async def list_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ca_certificate_with_options_async(request, runtime)

    def list_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_certificate(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_certificate_with_options(request, runtime)

    async def list_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_certificate_with_options_async(request, runtime)

    def list_device_certificate_by_ca_sn_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCertificateByCaSn',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_certificate_by_ca_sn_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCertificateByCaSn',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_certificate_by_ca_sn(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_certificate_by_ca_sn_with_options(request, runtime)

    async def list_device_certificate_by_ca_sn_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_certificate_by_ca_sn_with_options_async(request, runtime)

    def list_device_credential_client_id_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCredentialClientId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_credential_client_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceCredentialClientId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_credential_client_id(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_credential_client_id_with_options(request, runtime)

    async def list_device_credential_client_id_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_credential_client_id_with_options_async(request, runtime)

    def list_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ListGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ListGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_id(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ListGroupIdRequest
        @return: ListGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_group_id_with_options(request, runtime)

    async def list_group_id_async(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: ListGroupIdRequest
        @return: ListGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_group_id_with_options_async(request, runtime)

    def query_mqtt_trace_device_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceDevice',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_device_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceDevice',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_device(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceDeviceRequest
        @return: QueryMqttTraceDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_device_with_options(request, runtime)

    async def query_mqtt_trace_device_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceDeviceRequest
        @return: QueryMqttTraceDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mqtt_trace_device_with_options_async(request, runtime)

    def query_mqtt_trace_message_of_client_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageOfClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessageOfClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessageOfClient',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_of_client_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageOfClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessageOfClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessageOfClient',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_of_client(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageOfClientRequest
        @return: QueryMqttTraceMessageOfClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_of_client_with_options(request, runtime)

    async def query_mqtt_trace_message_of_client_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageOfClientRequest
        @return: QueryMqttTraceMessageOfClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mqtt_trace_message_of_client_with_options_async(request, runtime)

    def query_mqtt_trace_message_publish_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessagePublishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessagePublishResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessagePublish',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_publish_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessagePublishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessagePublishResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessagePublish',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_publish(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessagePublishRequest
        @return: QueryMqttTraceMessagePublishResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_publish_with_options(request, runtime)

    async def query_mqtt_trace_message_publish_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessagePublishRequest
        @return: QueryMqttTraceMessagePublishResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mqtt_trace_message_publish_with_options_async(request, runtime)

    def query_mqtt_trace_message_subscribe_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessageSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessageSubscribe',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_subscribe_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMqttTraceMessageSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMqttTraceMessageSubscribe',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_subscribe(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageSubscribeRequest
        @return: QueryMqttTraceMessageSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_subscribe_with_options(request, runtime)

    async def query_mqtt_trace_message_subscribe_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        *   You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        
        @param request: QueryMqttTraceMessageSubscribeRequest
        @return: QueryMqttTraceMessageSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mqtt_trace_message_subscribe_with_options_async(request, runtime)

    def query_session_by_client_id_with_options(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QuerySessionByClientIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionByClientIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionByClientId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_by_client_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QuerySessionByClientIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionByClientIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionByClientId',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_by_client_id(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QuerySessionByClientIdRequest
        @return: QuerySessionByClientIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_session_by_client_id_with_options(request, runtime)

    async def query_session_by_client_id_async(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QuerySessionByClientIdRequest
        @return: QuerySessionByClientIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_session_by_client_id_with_options_async(request, runtime)

    def query_token_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QueryTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QueryTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_token(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QueryTokenRequest
        @return: QueryTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_token_with_options(request, runtime)

    async def query_token_async(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: QueryTokenRequest
        @return: QueryTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_token_with_options_async(request, runtime)

    def refresh_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        >  Each successful call to the **RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RefreshDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        >  Each successful call to the **RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RefreshDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_device_credential(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        >  Each successful call to the **RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RefreshDeviceCredentialRequest
        @return: RefreshDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_credential_with_options(request, runtime)

    async def refresh_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        >  Each successful call to the **RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RefreshDeviceCredentialRequest
        @return: RefreshDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_device_credential_with_options_async(request, runtime)

    def register_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_content):
            query['CaContent'] = request.ca_content
        if not UtilClient.is_unset(request.ca_name):
            query['CaName'] = request.ca_name
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.verification_content):
            query['VerificationContent'] = request.verification_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_content):
            query['CaContent'] = request.ca_content
        if not UtilClient.is_unset(request.ca_name):
            query['CaName'] = request.ca_name
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.verification_content):
            query['VerificationContent'] = request.verification_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCaCertificate',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_ca_certificate_with_options(request, runtime)

    async def register_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_ca_certificate_with_options_async(request, runtime)

    def register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RegisterDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RegisterDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device_credential(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RegisterDeviceCredentialRequest
        @return: RegisterDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_device_credential_with_options(request, runtime)

    async def register_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RegisterDeviceCredentialRequest
        @return: RegisterDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_device_credential_with_options_async(request, runtime)

    def revoke_token_with_options(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RevokeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RevokeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RevokeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RevokeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_token(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RevokeTokenRequest
        @return: RevokeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_token_with_options(request, runtime)

    async def revoke_token_async(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        *   Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: RevokeTokenRequest
        @return: RevokeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_token_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        The **SendMessage** operation is called by applications on cloud servers. It is complementary to the operation that is called by ApsaraMQ for MQTT clients to send messages. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](~~179160~~).
        *   Before you call the **SendMessage** operation, make sure that the kernel version of your ApsaraMQ for MQTT instance is 3.3.0 or later. You can obtain the information about the kernel version on the [Instance Details](https://mqtt.console.aliyun.com) page that corresponds to the instance in the **ApsaraMQ for MQTT console**.
        *   Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT to forward messages to ApsaraMQ for RocketMQ, send the messages by using an SDK. For more information, see [Export data from ApsaraMQ for MQTT to other Alibaba Cloud services](~~174527~~). You can call the **SendMessage** operation up to 1,000 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **SendMessage** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For information about the billing details, see [Billing rules](~~52819~~).
        
        @param request: SendMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_topic):
            query['MqttTopic'] = request.mqtt_topic
        if not UtilClient.is_unset(request.payload):
            query['Payload'] = request.payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        The **SendMessage** operation is called by applications on cloud servers. It is complementary to the operation that is called by ApsaraMQ for MQTT clients to send messages. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](~~179160~~).
        *   Before you call the **SendMessage** operation, make sure that the kernel version of your ApsaraMQ for MQTT instance is 3.3.0 or later. You can obtain the information about the kernel version on the [Instance Details](https://mqtt.console.aliyun.com) page that corresponds to the instance in the **ApsaraMQ for MQTT console**.
        *   Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT to forward messages to ApsaraMQ for RocketMQ, send the messages by using an SDK. For more information, see [Export data from ApsaraMQ for MQTT to other Alibaba Cloud services](~~174527~~). You can call the **SendMessage** operation up to 1,000 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **SendMessage** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For information about the billing details, see [Billing rules](~~52819~~).
        
        @param request: SendMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_topic):
            query['MqttTopic'] = request.mqtt_topic
        if not UtilClient.is_unset(request.payload):
            query['Payload'] = request.payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        The **SendMessage** operation is called by applications on cloud servers. It is complementary to the operation that is called by ApsaraMQ for MQTT clients to send messages. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](~~179160~~).
        *   Before you call the **SendMessage** operation, make sure that the kernel version of your ApsaraMQ for MQTT instance is 3.3.0 or later. You can obtain the information about the kernel version on the [Instance Details](https://mqtt.console.aliyun.com) page that corresponds to the instance in the **ApsaraMQ for MQTT console**.
        *   Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT to forward messages to ApsaraMQ for RocketMQ, send the messages by using an SDK. For more information, see [Export data from ApsaraMQ for MQTT to other Alibaba Cloud services](~~174527~~). You can call the **SendMessage** operation up to 1,000 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **SendMessage** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For information about the billing details, see [Billing rules](~~52819~~).
        
        @param request: SendMessageRequest
        @return: SendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        The **SendMessage** operation is called by applications on cloud servers. It is complementary to the operation that is called by ApsaraMQ for MQTT clients to send messages. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](~~179160~~).
        *   Before you call the **SendMessage** operation, make sure that the kernel version of your ApsaraMQ for MQTT instance is 3.3.0 or later. You can obtain the information about the kernel version on the [Instance Details](https://mqtt.console.aliyun.com) page that corresponds to the instance in the **ApsaraMQ for MQTT console**.
        *   Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT to forward messages to ApsaraMQ for RocketMQ, send the messages by using an SDK. For more information, see [Export data from ApsaraMQ for MQTT to other Alibaba Cloud services](~~174527~~). You can call the **SendMessage** operation up to 1,000 times per second. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **SendMessage** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For information about the billing details, see [Billing rules](~~52819~~).
        
        @param request: SendMessageRequest
        @return: SendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def un_register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: UnRegisterDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnRegisterDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnRegisterDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: UnRegisterDeviceCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnRegisterDeviceCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnRegisterDeviceCredential',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_register_device_credential(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: UnRegisterDeviceCredentialRequest
        @return: UnRegisterDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_register_device_credential_with_options(request, runtime)

    async def un_register_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](~~163047~~).
        *   Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](~~52819~~).
        
        @param request: UnRegisterDeviceCredentialRequest
        @return: UnRegisterDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_register_device_credential_with_options_async(request, runtime)
