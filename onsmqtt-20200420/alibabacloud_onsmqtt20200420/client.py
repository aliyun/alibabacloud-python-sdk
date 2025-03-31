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
        """
        @summary Activate CA Certificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to reactivate only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: ActiveCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def active_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        """
        @summary Activate CA Certificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to reactivate only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: ActiveCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def active_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        """
        @summary Activate CA Certificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to reactivate only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: ActiveCaCertificateRequest
        @return: ActiveCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.active_ca_certificate_with_options(request, runtime)

    async def active_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ActiveCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveCaCertificateResponse:
        """
        @summary Activate CA Certificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to reactivate only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: ActiveCaCertificateRequest
        @return: ActiveCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.active_ca_certificate_with_options_async(request, runtime)

    def active_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        """
        @summary Reactivates a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client based on the registered CA certificate. If the CA certificate matches the device certificate, the client passes the authentication and the system automatically registers the device certificate with the ApsaraMQ for MQTT broker. After a device certificate is registered with an ApsaraMQ for MQTT broker, the certificate is automatically activated. If your device certificate is changed to the inactivated state, you can call this operation to reactivate the device certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ActiveDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def active_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        """
        @summary Reactivates a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client based on the registered CA certificate. If the CA certificate matches the device certificate, the client passes the authentication and the system automatically registers the device certificate with the ApsaraMQ for MQTT broker. After a device certificate is registered with an ApsaraMQ for MQTT broker, the certificate is automatically activated. If your device certificate is changed to the inactivated state, you can call this operation to reactivate the device certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ActiveDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ActiveDeviceCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def active_device_certificate(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        """
        @summary Reactivates a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client based on the registered CA certificate. If the CA certificate matches the device certificate, the client passes the authentication and the system automatically registers the device certificate with the ApsaraMQ for MQTT broker. After a device certificate is registered with an ApsaraMQ for MQTT broker, the certificate is automatically activated. If your device certificate is changed to the inactivated state, you can call this operation to reactivate the device certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ActiveDeviceCertificateRequest
        @return: ActiveDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.active_device_certificate_with_options(request, runtime)

    async def active_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ActiveDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ActiveDeviceCertificateResponse:
        """
        @summary Reactivates a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client based on the registered CA certificate. If the CA certificate matches the device certificate, the client passes the authentication and the system automatically registers the device certificate with the ApsaraMQ for MQTT broker. After a device certificate is registered with an ApsaraMQ for MQTT broker, the certificate is automatically activated. If your device certificate is changed to the inactivated state, you can call this operation to reactivate the device certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ActiveDeviceCertificateRequest
        @return: ActiveDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.active_device_certificate_with_options_async(request, runtime)

    def add_custom_auth_connect_black_with_options(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse:
        """
        @summary Adds a device to the connection blacklist to disable connections from the device.
        
        @param request: AddCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse(),
                self.execute(params, req, runtime)
            )

    async def add_custom_auth_connect_black_with_options_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse:
        """
        @summary Adds a device to the connection blacklist to disable connections from the device.
        
        @param request: AddCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_custom_auth_connect_black(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse:
        """
        @summary Adds a device to the connection blacklist to disable connections from the device.
        
        @param request: AddCustomAuthConnectBlackRequest
        @return: AddCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_auth_connect_black_with_options(request, runtime)

    async def add_custom_auth_connect_black_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthConnectBlackResponse:
        """
        @summary Adds a device to the connection blacklist to disable connections from the device.
        
        @param request: AddCustomAuthConnectBlackRequest
        @return: AddCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_auth_connect_black_with_options_async(request, runtime)

    def add_custom_auth_identity_with_options(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthIdentityResponse:
        """
        @summary Adds the information about identity authentication. The identity can be accurate to a client.
        
        @param request: AddCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret):
            body['Secret'] = request.secret
        if not UtilClient.is_unset(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthIdentityResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthIdentityResponse(),
                self.execute(params, req, runtime)
            )

    async def add_custom_auth_identity_with_options_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthIdentityResponse:
        """
        @summary Adds the information about identity authentication. The identity can be accurate to a client.
        
        @param request: AddCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret):
            body['Secret'] = request.secret
        if not UtilClient.is_unset(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthIdentityResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthIdentityResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_custom_auth_identity(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthIdentityResponse:
        """
        @summary Adds the information about identity authentication. The identity can be accurate to a client.
        
        @param request: AddCustomAuthIdentityRequest
        @return: AddCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_auth_identity_with_options(request, runtime)

    async def add_custom_auth_identity_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthIdentityResponse:
        """
        @summary Adds the information about identity authentication. The identity can be accurate to a client.
        
        @param request: AddCustomAuthIdentityRequest
        @return: AddCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_auth_identity_with_options_async(request, runtime)

    def add_custom_auth_permission_with_options(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthPermissionResponse:
        """
        @summary Grants permissions on topics. You must create a parent topic in the console before you call this API operation.
        
        @param request: AddCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effect):
            body['Effect'] = request.effect
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def add_custom_auth_permission_with_options_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.AddCustomAuthPermissionResponse:
        """
        @summary Grants permissions on topics. You must create a parent topic in the console before you call this API operation.
        
        @param request: AddCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effect):
            body['Effect'] = request.effect
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.AddCustomAuthPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_custom_auth_permission(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthPermissionResponse:
        """
        @summary Grants permissions on topics. You must create a parent topic in the console before you call this API operation.
        
        @param request: AddCustomAuthPermissionRequest
        @return: AddCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_auth_permission_with_options(request, runtime)

    async def add_custom_auth_permission_async(
        self,
        request: ons_mqtt_20200420_models.AddCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.AddCustomAuthPermissionResponse:
        """
        @summary Grants permissions on topics. You must create a parent topic in the console before you call this API operation.
        
        @param request: AddCustomAuthPermissionRequest
        @return: AddCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_auth_permission_with_options_async(request, runtime)

    def apply_token_with_options(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        @summary Applies for a token from ApsaraMQ for MQTT. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ApplyTokenResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ApplyTokenResponse(),
                self.execute(params, req, runtime)
            )

    async def apply_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        @summary Applies for a token from ApsaraMQ for MQTT. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ApplyTokenResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ApplyTokenResponse(),
                await self.execute_async(params, req, runtime)
            )

    def apply_token(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        """
        @summary Applies for a token from ApsaraMQ for MQTT. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Applies for a token from ApsaraMQ for MQTT. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **ApplyToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the status of multiple ApsaraMQ for MQTT clients by client ID.
        
        @description    You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_query_session_by_client_ids_with_options_async(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        @summary Queries the status of multiple ApsaraMQ for MQTT clients by client ID.
        
        @description    You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_query_session_by_client_ids(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        """
        @summary Queries the status of multiple ApsaraMQ for MQTT clients by client ID.
        
        @description    You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the status of multiple ApsaraMQ for MQTT clients by client ID.
        
        @description    You can call the **BatchQuerySessionByClientIds** operation up to 100 times per second. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        You can call the **BatchQuerySessionByClientIds** operation to query the status of up to 10 ApsaraMQ for MQTT clients in a single query.
        Each successful call to the **BatchQuerySessionByClientIds** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: BatchQuerySessionByClientIdsRequest
        @return: BatchQuerySessionByClientIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_query_session_by_client_ids_with_options_async(request, runtime)

    def close_connection_with_options(
        self,
        request: ons_mqtt_20200420_models.CloseConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CloseConnectionResponse:
        """
        @summary Proactively closes an online connection. After you call this API operation, the device may reconnect to the broker based on the client reconnection mechanism.
        
        @description This API is still in the testing phase and is only available for Professional Edition instances in the Shanghai region. Legacy instances are not supported at this time.
        
        @param request: CloseConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseConnectionResponse
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
            action='CloseConnection',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CloseConnectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CloseConnectionResponse(),
                self.execute(params, req, runtime)
            )

    async def close_connection_with_options_async(
        self,
        request: ons_mqtt_20200420_models.CloseConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CloseConnectionResponse:
        """
        @summary Proactively closes an online connection. After you call this API operation, the device may reconnect to the broker based on the client reconnection mechanism.
        
        @description This API is still in the testing phase and is only available for Professional Edition instances in the Shanghai region. Legacy instances are not supported at this time.
        
        @param request: CloseConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseConnectionResponse
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
            action='CloseConnection',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CloseConnectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CloseConnectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def close_connection(
        self,
        request: ons_mqtt_20200420_models.CloseConnectionRequest,
    ) -> ons_mqtt_20200420_models.CloseConnectionResponse:
        """
        @summary Proactively closes an online connection. After you call this API operation, the device may reconnect to the broker based on the client reconnection mechanism.
        
        @description This API is still in the testing phase and is only available for Professional Edition instances in the Shanghai region. Legacy instances are not supported at this time.
        
        @param request: CloseConnectionRequest
        @return: CloseConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_connection_with_options(request, runtime)

    async def close_connection_async(
        self,
        request: ons_mqtt_20200420_models.CloseConnectionRequest,
    ) -> ons_mqtt_20200420_models.CloseConnectionResponse:
        """
        @summary Proactively closes an online connection. After you call this API operation, the device may reconnect to the broker based on the client reconnection mechanism.
        
        @description This API is still in the testing phase and is only available for Professional Edition instances in the Shanghai region. Legacy instances are not supported at this time.
        
        @param request: CloseConnectionRequest
        @return: CloseConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_connection_with_options_async(request, runtime)

    def create_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        @summary Creates a group ID. Before you connect producers and consumers to an ApsaraMQ for MQTT broker to send and receive messages, you must specify a unique ID for each client for identification. A client ID is in the format of \\<GroupID>@@@\\<DeviceID>. In the preceding format, DeviceID is the custom ID that you specify for the client, and GroupID is the ID of the group that you create on the ApsaraMQ for MQTT broker in advance.
        
        @description Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CreateGroupIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CreateGroupIdResponse(),
                self.execute(params, req, runtime)
            )

    async def create_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        @summary Creates a group ID. Before you connect producers and consumers to an ApsaraMQ for MQTT broker to send and receive messages, you must specify a unique ID for each client for identification. A client ID is in the format of \\<GroupID>@@@\\<DeviceID>. In the preceding format, DeviceID is the custom ID that you specify for the client, and GroupID is the ID of the group that you create on the ApsaraMQ for MQTT broker in advance.
        
        @description Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CreateGroupIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.CreateGroupIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_group_id(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        """
        @summary Creates a group ID. Before you connect producers and consumers to an ApsaraMQ for MQTT broker to send and receive messages, you must specify a unique ID for each client for identification. A client ID is in the format of \\<GroupID>@@@\\<DeviceID>. In the preceding format, DeviceID is the custom ID that you specify for the client, and GroupID is the ID of the group that you create on the ApsaraMQ for MQTT broker in advance.
        
        @description Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Creates a group ID. Before you connect producers and consumers to an ApsaraMQ for MQTT broker to send and receive messages, you must specify a unique ID for each client for identification. A client ID is in the format of \\<GroupID>@@@\\<DeviceID>. In the preceding format, DeviceID is the custom ID that you specify for the client, and GroupID is the ID of the group that you create on the ApsaraMQ for MQTT broker in advance.
        
        @description Each successful call to the *CreateGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        """
        @summary Deletes a certificate authority (CA) certificate from an ApsaraMQ for MQTT broker. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. Before you can use a CA certificate, you must register the certificate with an ApsaraMQ for MQTT broker. If you no longer require a CA certificate, you can call this operation to delete the certificate from the ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to delete only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        If you delete a specific CA certificate from an ApsaraMQ for MQTT broker, all device certificates that are issued by the CA certificate and are registered with the ApsaraMQ for MQTT broker are automatically deleted.
        
        @param request: DeleteCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        """
        @summary Deletes a certificate authority (CA) certificate from an ApsaraMQ for MQTT broker. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. Before you can use a CA certificate, you must register the certificate with an ApsaraMQ for MQTT broker. If you no longer require a CA certificate, you can call this operation to delete the certificate from the ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to delete only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        If you delete a specific CA certificate from an ApsaraMQ for MQTT broker, all device certificates that are issued by the CA certificate and are registered with the ApsaraMQ for MQTT broker are automatically deleted.
        
        @param request: DeleteCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        """
        @summary Deletes a certificate authority (CA) certificate from an ApsaraMQ for MQTT broker. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. Before you can use a CA certificate, you must register the certificate with an ApsaraMQ for MQTT broker. If you no longer require a CA certificate, you can call this operation to delete the certificate from the ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to delete only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        If you delete a specific CA certificate from an ApsaraMQ for MQTT broker, all device certificates that are issued by the CA certificate and are registered with the ApsaraMQ for MQTT broker are automatically deleted.
        
        @param request: DeleteCaCertificateRequest
        @return: DeleteCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ca_certificate_with_options(request, runtime)

    async def delete_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteCaCertificateResponse:
        """
        @summary Deletes a certificate authority (CA) certificate from an ApsaraMQ for MQTT broker. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. Before you can use a CA certificate, you must register the certificate with an ApsaraMQ for MQTT broker. If you no longer require a CA certificate, you can call this operation to delete the certificate from the ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to delete only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        If you delete a specific CA certificate from an ApsaraMQ for MQTT broker, all device certificates that are issued by the CA certificate and are registered with the ApsaraMQ for MQTT broker are automatically deleted.
        
        @param request: DeleteCaCertificateRequest
        @return: DeleteCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ca_certificate_with_options_async(request, runtime)

    def delete_custom_auth_connect_black_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse:
        """
        @summary Deletes a connection blacklist.
        
        @param request: DeleteCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_custom_auth_connect_black_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse:
        """
        @summary Deletes a connection blacklist.
        
        @param request: DeleteCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_custom_auth_connect_black(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse:
        """
        @summary Deletes a connection blacklist.
        
        @param request: DeleteCustomAuthConnectBlackRequest
        @return: DeleteCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_auth_connect_black_with_options(request, runtime)

    async def delete_custom_auth_connect_black_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthConnectBlackResponse:
        """
        @summary Deletes a connection blacklist.
        
        @param request: DeleteCustomAuthConnectBlackRequest
        @return: DeleteCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_auth_connect_black_with_options_async(request, runtime)

    def delete_custom_auth_identity_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse:
        """
        @summary Deletes an identity for custom authorization.
        
        @param request: DeleteCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_custom_auth_identity_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse:
        """
        @summary Deletes an identity for custom authorization.
        
        @param request: DeleteCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_custom_auth_identity(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse:
        """
        @summary Deletes an identity for custom authorization.
        
        @param request: DeleteCustomAuthIdentityRequest
        @return: DeleteCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_auth_identity_with_options(request, runtime)

    async def delete_custom_auth_identity_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthIdentityResponse:
        """
        @summary Deletes an identity for custom authorization.
        
        @param request: DeleteCustomAuthIdentityRequest
        @return: DeleteCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_auth_identity_with_options_async(request, runtime)

    def delete_custom_auth_permission_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse:
        """
        @summary Deletes permissions on a topic.
        
        @param request: DeleteCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_custom_auth_permission_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse:
        """
        @summary Deletes permissions on a topic.
        
        @param request: DeleteCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_custom_auth_permission(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse:
        """
        @summary Deletes permissions on a topic.
        
        @param request: DeleteCustomAuthPermissionRequest
        @return: DeleteCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_auth_permission_with_options(request, runtime)

    async def delete_custom_auth_permission_async(
        self,
        request: ons_mqtt_20200420_models.DeleteCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.DeleteCustomAuthPermissionResponse:
        """
        @summary Deletes permissions on a topic.
        
        @param request: DeleteCustomAuthPermissionRequest
        @return: DeleteCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_auth_permission_with_options_async(request, runtime)

    def delete_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        """
        @summary Deletes the registration information about a specific device certificate from an ApsaraMQ for MQTT broker. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client. If you no longer require a device certificate, you can call this operation to delete the registration information about the certificate from an ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: DeleteDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        """
        @summary Deletes the registration information about a specific device certificate from an ApsaraMQ for MQTT broker. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client. If you no longer require a device certificate, you can call this operation to delete the registration information about the certificate from an ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: DeleteDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteDeviceCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_device_certificate(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        """
        @summary Deletes the registration information about a specific device certificate from an ApsaraMQ for MQTT broker. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client. If you no longer require a device certificate, you can call this operation to delete the registration information about the certificate from an ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: DeleteDeviceCertificateRequest
        @return: DeleteDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_device_certificate_with_options(request, runtime)

    async def delete_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.DeleteDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.DeleteDeviceCertificateResponse:
        """
        @summary Deletes the registration information about a specific device certificate from an ApsaraMQ for MQTT broker. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client. If you no longer require a device certificate, you can call this operation to delete the registration information about the certificate from an ApsaraMQ for MQTT broker.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: DeleteDeviceCertificateRequest
        @return: DeleteDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_certificate_with_options_async(request, runtime)

    def delete_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        @summary Deletes a group from an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteGroupIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteGroupIdResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        @summary Deletes a group from an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteGroupIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DeleteGroupIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_group_id(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        """
        @summary Deletes a group from an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Deletes a group from an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *DeleteGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: DeleteGroupIdRequest
        @return: DeleteGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_id_with_options_async(request, runtime)

    def disaster_downgrade_with_options(
        self,
        request: ons_mqtt_20200420_models.DisasterDowngradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DisasterDowngradeResponse:
        """
        @summary Downgrades the virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call the operation, you must submit a ticket.
        
        @param request: DisasterDowngradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisasterDowngradeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.downgrade_instance_id):
            body['DowngradeInstanceId'] = request.downgrade_instance_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisasterDowngrade',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterDowngradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterDowngradeResponse(),
                self.execute(params, req, runtime)
            )

    async def disaster_downgrade_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DisasterDowngradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DisasterDowngradeResponse:
        """
        @summary Downgrades the virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call the operation, you must submit a ticket.
        
        @param request: DisasterDowngradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisasterDowngradeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.downgrade_instance_id):
            body['DowngradeInstanceId'] = request.downgrade_instance_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisasterDowngrade',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterDowngradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterDowngradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disaster_downgrade(
        self,
        request: ons_mqtt_20200420_models.DisasterDowngradeRequest,
    ) -> ons_mqtt_20200420_models.DisasterDowngradeResponse:
        """
        @summary Downgrades the virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call the operation, you must submit a ticket.
        
        @param request: DisasterDowngradeRequest
        @return: DisasterDowngradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disaster_downgrade_with_options(request, runtime)

    async def disaster_downgrade_async(
        self,
        request: ons_mqtt_20200420_models.DisasterDowngradeRequest,
    ) -> ons_mqtt_20200420_models.DisasterDowngradeResponse:
        """
        @summary Downgrades the virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call the operation, you must submit a ticket.
        
        @param request: DisasterDowngradeRequest
        @return: DisasterDowngradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disaster_downgrade_with_options_async(request, runtime)

    def disaster_recovery_with_options(
        self,
        request: ons_mqtt_20200420_models.DisasterRecoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DisasterRecoveryResponse:
        """
        @summary Recovers the public virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call this operation, you must submit a ticket.
        
        @param request: DisasterRecoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisasterRecoveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.recovery_instance_id):
            body['RecoveryInstanceId'] = request.recovery_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisasterRecovery',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterRecoveryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterRecoveryResponse(),
                self.execute(params, req, runtime)
            )

    async def disaster_recovery_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DisasterRecoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DisasterRecoveryResponse:
        """
        @summary Recovers the public virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call this operation, you must submit a ticket.
        
        @param request: DisasterRecoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisasterRecoveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.recovery_instance_id):
            body['RecoveryInstanceId'] = request.recovery_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisasterRecovery',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterRecoveryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.DisasterRecoveryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disaster_recovery(
        self,
        request: ons_mqtt_20200420_models.DisasterRecoveryRequest,
    ) -> ons_mqtt_20200420_models.DisasterRecoveryResponse:
        """
        @summary Recovers the public virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call this operation, you must submit a ticket.
        
        @param request: DisasterRecoveryRequest
        @return: DisasterRecoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disaster_recovery_with_options(request, runtime)

    async def disaster_recovery_async(
        self,
        request: ons_mqtt_20200420_models.DisasterRecoveryRequest,
    ) -> ons_mqtt_20200420_models.DisasterRecoveryResponse:
        """
        @summary Recovers the public virtual IP address (VIP) access of a specific instance during the disaster recovery of multiple instances. Only Enterprise Platinum Edition instances support this operation. To call this operation, you must submit a ticket.
        
        @param request: DisasterRecoveryRequest
        @return: DisasterRecoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disaster_recovery_with_options_async(request, runtime)

    def get_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        """
        @summary Queries the details of a certificate authority (CA) certificate, such as the content and status of the certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        """
        @summary Queries the details of a certificate authority (CA) certificate, such as the content and status of the certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        """
        @summary Queries the details of a certificate authority (CA) certificate, such as the content and status of the certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetCaCertificateRequest
        @return: GetCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ca_certificate_with_options(request, runtime)

    async def get_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.GetCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetCaCertificateResponse:
        """
        @summary Queries the details of a certificate authority (CA) certificate, such as the content and status of the certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetCaCertificateRequest
        @return: GetCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_certificate_with_options_async(request, runtime)

    def get_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        """
        @summary Queries the details of a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def get_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        """
        @summary Queries the details of a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_device_certificate(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        """
        @summary Queries the details of a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetDeviceCertificateRequest
        @return: GetDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_certificate_with_options(request, runtime)

    async def get_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCertificateResponse:
        """
        @summary Queries the details of a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetDeviceCertificateRequest
        @return: GetDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_certificate_with_options_async(request, runtime)

    def get_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        @summary Queries the access credential of a device. If unique-certificate-per-device authentication is used as the authentication method on an ApsaraMQ for MQTT broker, an access credential that you apply for in advance is required for authentication when you connect your device to the broker. The connection can be established only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
                self.execute(params, req, runtime)
            )

    async def get_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        @summary Queries the access credential of a device. If unique-certificate-per-device authentication is used as the authentication method on an ApsaraMQ for MQTT broker, an access credential that you apply for in advance is required for authentication when you connect your device to the broker. The connection can be established only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_device_credential(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        """
        @summary Queries the access credential of a device. If unique-certificate-per-device authentication is used as the authentication method on an ApsaraMQ for MQTT broker, an access credential that you apply for in advance is required for authentication when you connect your device to the broker. The connection can be established only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the access credential of a device. If unique-certificate-per-device authentication is used as the authentication method on an ApsaraMQ for MQTT broker, an access credential that you apply for in advance is required for authentication when you connect your device to the broker. The connection can be established only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **GetDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        """
        @summary Obtains the registration code of a specific certificate authority (CA) certificate. When you register a CA certificate with an ApsaraMQ for MQTT broker, you must upload the validation certificate of the CA certificate to verify whether you have the private key of the CA certificate. The validation certificate of a CA certificate must be generated by using the registration code of the CA certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetRegisterCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisterCodeResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetRegisterCodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetRegisterCodeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_register_code_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        """
        @summary Obtains the registration code of a specific certificate authority (CA) certificate. When you register a CA certificate with an ApsaraMQ for MQTT broker, you must upload the validation certificate of the CA certificate to verify whether you have the private key of the CA certificate. The validation certificate of a CA certificate must be generated by using the registration code of the CA certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetRegisterCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisterCodeResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetRegisterCodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.GetRegisterCodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_register_code(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        """
        @summary Obtains the registration code of a specific certificate authority (CA) certificate. When you register a CA certificate with an ApsaraMQ for MQTT broker, you must upload the validation certificate of the CA certificate to verify whether you have the private key of the CA certificate. The validation certificate of a CA certificate must be generated by using the registration code of the CA certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetRegisterCodeRequest
        @return: GetRegisterCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_register_code_with_options(request, runtime)

    async def get_register_code_async(
        self,
        request: ons_mqtt_20200420_models.GetRegisterCodeRequest,
    ) -> ons_mqtt_20200420_models.GetRegisterCodeResponse:
        """
        @summary Obtains the registration code of a specific certificate authority (CA) certificate. When you register a CA certificate with an ApsaraMQ for MQTT broker, you must upload the validation certificate of the CA certificate to verify whether you have the private key of the CA certificate. The validation certificate of a CA certificate must be generated by using the registration code of the CA certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: GetRegisterCodeRequest
        @return: GetRegisterCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_register_code_with_options_async(request, runtime)

    def inactivate_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        """
        @summary Deregister a certificate authority (CA) certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. If you no longer require a CA certificate, you can call this operation to deregister the certificate. If you want to continue using a deregistered CA certificate, you can call the ActiveCaCertificate operation to reactivate the certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to deregister only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: InactivateCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InactivateCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def inactivate_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        """
        @summary Deregister a certificate authority (CA) certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. If you no longer require a CA certificate, you can call this operation to deregister the certificate. If you want to continue using a deregistered CA certificate, you can call the ActiveCaCertificate operation to reactivate the certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to deregister only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: InactivateCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InactivateCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inactivate_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        """
        @summary Deregister a certificate authority (CA) certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. If you no longer require a CA certificate, you can call this operation to deregister the certificate. If you want to continue using a deregistered CA certificate, you can call the ActiveCaCertificate operation to reactivate the certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to deregister only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: InactivateCaCertificateRequest
        @return: InactivateCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inactivate_ca_certificate_with_options(request, runtime)

    async def inactivate_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.InactivateCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateCaCertificateResponse:
        """
        @summary Deregister a certificate authority (CA) certificate. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates. If you no longer require a CA certificate, you can call this operation to deregister the certificate. If you want to continue using a deregistered CA certificate, you can call the ActiveCaCertificate operation to reactivate the certificate.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        You can call this operation to deregister only CA certificates that are registered with ApsaraMQ for MQTT brokers. You can call the [ListCaCertificate](https://help.aliyun.com/document_detail/2604958.html) operation to query CA certificates that are registered with an ApsaraMQ for MQTT instance.
        
        @param request: InactivateCaCertificateRequest
        @return: InactivateCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inactivate_ca_certificate_with_options_async(request, runtime)

    def inactivate_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        """
        @summary Deregisters a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: InactivateDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InactivateDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def inactivate_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        """
        @summary Deregisters a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: InactivateDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InactivateDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.InactivateDeviceCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inactivate_device_certificate(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        """
        @summary Deregisters a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: InactivateDeviceCertificateRequest
        @return: InactivateDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inactivate_device_certificate_with_options(request, runtime)

    async def inactivate_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.InactivateDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.InactivateDeviceCertificateResponse:
        """
        @summary Deregisters a device certificate. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: InactivateDeviceCertificateRequest
        @return: InactivateDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inactivate_device_certificate_with_options_async(request, runtime)

    def list_ca_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        """
        @summary Queries all certificate authority (CA) certificates that are registered with an ApsaraMQ for MQTT instance. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def list_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        """
        @summary Queries all certificate authority (CA) certificates that are registered with an ApsaraMQ for MQTT instance. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        """
        @summary Queries all certificate authority (CA) certificates that are registered with an ApsaraMQ for MQTT instance. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListCaCertificateRequest
        @return: ListCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ca_certificate_with_options(request, runtime)

    async def list_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ListCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListCaCertificateResponse:
        """
        @summary Queries all certificate authority (CA) certificates that are registered with an ApsaraMQ for MQTT instance. ApsaraMQ for MQTT allows you to use X.509 certificates for authentication. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, you can use the device certificate to implement authentication. CA certificates are used to issue device certificates to clients and validate the device certificates.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListCaCertificateRequest
        @return: ListCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ca_certificate_with_options_async(request, runtime)

    def list_device_certificate_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        """
        @summary Queries all device certificates that are registered with an ApsaraMQ for MQTT instance. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def list_device_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        """
        @summary Queries all device certificates that are registered with an ApsaraMQ for MQTT instance. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_device_certificate(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        """
        @summary Queries all device certificates that are registered with an ApsaraMQ for MQTT instance. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateRequest
        @return: ListDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_certificate_with_options(request, runtime)

    async def list_device_certificate_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateResponse:
        """
        @summary Queries all device certificates that are registered with an ApsaraMQ for MQTT instance. Device certificates are digital certificates issued to clients by certificate authority (CA) root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateRequest
        @return: ListDeviceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_certificate_with_options_async(request, runtime)

    def list_device_certificate_by_ca_sn_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        """
        @summary Queries all device certificates that are issued by a certificate authority (CA) certificate and registered with ApsaraMQ for MQTT brokers. Device certificates are digital certificates issued to clients by CA root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateByCaSnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCertificateByCaSnResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
                self.execute(params, req, runtime)
            )

    async def list_device_certificate_by_ca_sn_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        """
        @summary Queries all device certificates that are issued by a certificate authority (CA) certificate and registered with ApsaraMQ for MQTT brokers. Device certificates are digital certificates issued to clients by CA root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateByCaSnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCertificateByCaSnResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_device_certificate_by_ca_sn(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        """
        @summary Queries all device certificates that are issued by a certificate authority (CA) certificate and registered with ApsaraMQ for MQTT brokers. Device certificates are digital certificates issued to clients by CA root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateByCaSnRequest
        @return: ListDeviceCertificateByCaSnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_certificate_by_ca_sn_with_options(request, runtime)

    async def list_device_certificate_by_ca_sn_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCertificateByCaSnRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCertificateByCaSnResponse:
        """
        @summary Queries all device certificates that are issued by a certificate authority (CA) certificate and registered with ApsaraMQ for MQTT brokers. Device certificates are digital certificates issued to clients by CA root certificates. When you connect an ApsaraMQ for MQTT client to an ApsaraMQ for MQTT broker, the broker uses the device certificate to authenticate the client. If the client passes the authentication, the client and the broker can communicate with each other based on the encrypted private key in the device certificate. If the client fails the authentication, access requests from the client are denied by the client.
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: ListDeviceCertificateByCaSnRequest
        @return: ListDeviceCertificateByCaSnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_certificate_by_ca_sn_with_options_async(request, runtime)

    def list_device_credential_client_id_with_options(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        """
        @summary Queries clients that have applied for access credentials in unique-certificate-per-device authentication mode in an ApsaraMQ for MQTT instance.
        
        @param request: ListDeviceCredentialClientIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCredentialClientIdResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
                self.execute(params, req, runtime)
            )

    async def list_device_credential_client_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        """
        @summary Queries clients that have applied for access credentials in unique-certificate-per-device authentication mode in an ApsaraMQ for MQTT instance.
        
        @param request: ListDeviceCredentialClientIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceCredentialClientIdResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_device_credential_client_id(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        """
        @summary Queries clients that have applied for access credentials in unique-certificate-per-device authentication mode in an ApsaraMQ for MQTT instance.
        
        @param request: ListDeviceCredentialClientIdRequest
        @return: ListDeviceCredentialClientIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_credential_client_id_with_options(request, runtime)

    async def list_device_credential_client_id_async(
        self,
        request: ons_mqtt_20200420_models.ListDeviceCredentialClientIdRequest,
    ) -> ons_mqtt_20200420_models.ListDeviceCredentialClientIdResponse:
        """
        @summary Queries clients that have applied for access credentials in unique-certificate-per-device authentication mode in an ApsaraMQ for MQTT instance.
        
        @param request: ListDeviceCredentialClientIdRequest
        @return: ListDeviceCredentialClientIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_credential_client_id_with_options_async(request, runtime)

    def list_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        @summary Queries all groups on an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: ListGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListGroupIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListGroupIdResponse(),
                self.execute(params, req, runtime)
            )

    async def list_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        @summary Queries all groups on an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: ListGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListGroupIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListGroupIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_group_id(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        """
        @summary Queries all groups on an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries all groups on an ApsaraMQ for MQTT instance.
        
        @description Each successful call to the *ListGroupId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: ListGroupIdRequest
        @return: ListGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_group_id_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: ons_mqtt_20200420_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_instances_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_instances(
        self,
        request: ons_mqtt_20200420_models.ListInstancesRequest,
    ) -> ons_mqtt_20200420_models.ListInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: ons_mqtt_20200420_models.ListInstancesRequest,
    ) -> ons_mqtt_20200420_models.ListInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ons_mqtt_20200420_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListTagResourcesResponse:
        """
        @summary 查询标签
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListTagResourcesResponse:
        """
        @summary 查询标签
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: ons_mqtt_20200420_models.ListTagResourcesRequest,
    ) -> ons_mqtt_20200420_models.ListTagResourcesResponse:
        """
        @summary 查询标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ons_mqtt_20200420_models.ListTagResourcesRequest,
    ) -> ons_mqtt_20200420_models.ListTagResourcesResponse:
        """
        @summary 查询标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def query_custom_auth_connect_black_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse:
        """
        @summary Queries a client ID in a connection blacklist.
        
        @param request: QueryCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse(),
                self.execute(params, req, runtime)
            )

    async def query_custom_auth_connect_black_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthConnectBlackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse:
        """
        @summary Queries a client ID in a connection blacklist.
        
        @param request: QueryCustomAuthConnectBlackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthConnectBlackResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthConnectBlack',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_custom_auth_connect_black(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse:
        """
        @summary Queries a client ID in a connection blacklist.
        
        @param request: QueryCustomAuthConnectBlackRequest
        @return: QueryCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_custom_auth_connect_black_with_options(request, runtime)

    async def query_custom_auth_connect_black_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthConnectBlackRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthConnectBlackResponse:
        """
        @summary Queries a client ID in a connection blacklist.
        
        @param request: QueryCustomAuthConnectBlackRequest
        @return: QueryCustomAuthConnectBlackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_custom_auth_connect_black_with_options_async(request, runtime)

    def query_custom_auth_identity_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse:
        """
        @summary Queries the information about custom identity authentication.
        
        @param request: QueryCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse(),
                self.execute(params, req, runtime)
            )

    async def query_custom_auth_identity_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse:
        """
        @summary Queries the information about custom identity authentication.
        
        @param request: QueryCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_custom_auth_identity(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse:
        """
        @summary Queries the information about custom identity authentication.
        
        @param request: QueryCustomAuthIdentityRequest
        @return: QueryCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_custom_auth_identity_with_options(request, runtime)

    async def query_custom_auth_identity_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthIdentityResponse:
        """
        @summary Queries the information about custom identity authentication.
        
        @param request: QueryCustomAuthIdentityRequest
        @return: QueryCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_custom_auth_identity_with_options_async(request, runtime)

    def query_custom_auth_permission_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse:
        """
        @summary Queries the authorization information about a topic.
        
        @param request: QueryCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def query_custom_auth_permission_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse:
        """
        @summary Queries the authorization information about a topic.
        
        @param request: QueryCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_custom_auth_permission(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse:
        """
        @summary Queries the authorization information about a topic.
        
        @param request: QueryCustomAuthPermissionRequest
        @return: QueryCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_custom_auth_permission_with_options(request, runtime)

    async def query_custom_auth_permission_async(
        self,
        request: ons_mqtt_20200420_models.QueryCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.QueryCustomAuthPermissionResponse:
        """
        @summary Queries the authorization information about a topic.
        
        @param request: QueryCustomAuthPermissionRequest
        @return: QueryCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_custom_auth_permission_with_options_async(request, runtime)

    def query_mqtt_trace_device_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        @summary Queries the trace of a device that corresponds to an ApsaraMQ for MQTT client by page. When the status of a device is abnormal, you can call this operation to query the connection history of the device. This helps you efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_mqtt_trace_device_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        @summary Queries the trace of a device that corresponds to an ApsaraMQ for MQTT client by page. When the status of a device is abnormal, you can call this operation to query the connection history of the device. This helps you efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_mqtt_trace_device(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceDeviceRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse:
        """
        @summary Queries the trace of a device that corresponds to an ApsaraMQ for MQTT client by page. When the status of a device is abnormal, you can call this operation to query the connection history of the device. This helps you efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the trace of a device that corresponds to an ApsaraMQ for MQTT client by page. When the status of a device is abnormal, you can call this operation to query the connection history of the device. This helps you efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceDevice** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries messages on a device within a specific period of time. If a message is not sent or received as expected, you can call this operation to query the messaging status of the message to efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
                self.execute(params, req, runtime)
            )

    async def query_mqtt_trace_message_of_client_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        @summary Queries messages on a device within a specific period of time. If a message is not sent or received as expected, you can call this operation to query the messaging status of the message to efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_mqtt_trace_message_of_client(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse:
        """
        @summary Queries messages on a device within a specific period of time. If a message is not sent or received as expected, you can call this operation to query the messaging status of the message to efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries messages on a device within a specific period of time. If a message is not sent or received as expected, you can call this operation to query the messaging status of the message to efficiently troubleshoot issues.
        
        @description    Each successful call to the **QueryMqttTraceMessageOfClient** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the trace of a message. If a message is not sent or received as expected, you can call this operation to view the message details to troubleshoot the issue. For example, you can query the time when the message is published and the client that publishes the message.
        
        @description    Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
                self.execute(params, req, runtime)
            )

    async def query_mqtt_trace_message_publish_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        @summary Queries the trace of a message. If a message is not sent or received as expected, you can call this operation to view the message details to troubleshoot the issue. For example, you can query the time when the message is published and the client that publishes the message.
        
        @description    Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_mqtt_trace_message_publish(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessagePublishRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse:
        """
        @summary Queries the trace of a message. If a message is not sent or received as expected, you can call this operation to view the message details to troubleshoot the issue. For example, you can query the time when the message is published and the client that publishes the message.
        
        @description    Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the trace of a message. If a message is not sent or received as expected, you can call this operation to view the message details to troubleshoot the issue. For example, you can query the time when the message is published and the client that publishes the message.
        
        @description    Each successful call to the **QueryMqttTraceMessagePublish** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the delivery trace of a message. If a message is not sent or received as expected, you can call this operation to view the details about the message. For example, you can query the clients that subscribe to the message and the time when the message is delivered. This operation helps you locate the problem and identify the cause of the problem.
        
        @description    Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
                self.execute(params, req, runtime)
            )

    async def query_mqtt_trace_message_subscribe_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        @summary Queries the delivery trace of a message. If a message is not sent or received as expected, you can call this operation to view the details about the message. For example, you can query the clients that subscribe to the message and the time when the message is delivered. This operation helps you locate the problem and identify the cause of the problem.
        
        @description    Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_mqtt_trace_message_subscribe(
        self,
        request: ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeRequest,
    ) -> ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse:
        """
        @summary Queries the delivery trace of a message. If a message is not sent or received as expected, you can call this operation to view the details about the message. For example, you can query the clients that subscribe to the message and the time when the message is delivered. This operation helps you locate the problem and identify the cause of the problem.
        
        @description    Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the delivery trace of a message. If a message is not sent or received as expected, you can call this operation to view the details about the message. For example, you can query the clients that subscribe to the message and the time when the message is delivered. This operation helps you locate the problem and identify the cause of the problem.
        
        @description    Each successful call to the **QueryMqttTraceMessageSubscribe** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        
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
        @summary Queries the running status of an ApsaraMQ for MQTT client. You can troubleshoot issues based on the queried results. You can enter the ID of an ApsaraMQ for MQTT client to check the connection status and IP address of the device.
        
        @description    You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
                self.execute(params, req, runtime)
            )

    async def query_session_by_client_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        @summary Queries the running status of an ApsaraMQ for MQTT client. You can troubleshoot issues based on the queried results. You can enter the ID of an ApsaraMQ for MQTT client to check the connection status and IP address of the device.
        
        @description    You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_session_by_client_id(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        """
        @summary Queries the running status of an ApsaraMQ for MQTT client. You can troubleshoot issues based on the queried results. You can enter the ID of an ApsaraMQ for MQTT client to check the connection status and IP address of the device.
        
        @description    You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the running status of an ApsaraMQ for MQTT client. You can troubleshoot issues based on the queried results. You can enter the ID of an ApsaraMQ for MQTT client to check the connection status and IP address of the device.
        
        @description    You can call this operation up to 500 times per second.**** For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **QuerySessionByClientId** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the status of a token. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker. A token is a temporary credential and is valid only within a specific period of time. You can call this operation to query whether a token expires.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryTokenResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryTokenResponse(),
                self.execute(params, req, runtime)
            )

    async def query_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        @summary Queries the status of a token. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker. A token is a temporary credential and is valid only within a specific period of time. You can call this operation to query whether a token expires.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryTokenResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.QueryTokenResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_token(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        """
        @summary Queries the status of a token. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker. A token is a temporary credential and is valid only within a specific period of time. You can call this operation to query whether a token expires.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Queries the status of a token. If token-based authentication is used for permission authentication on an ApsaraMQ for MQTT broker, a token that is issued by the broker is required for authentication each time a client is connected to the broker. A token is a temporary credential and is valid only within a specific period of time. You can call this operation to query whether a token expires.
        
        @description    You can call this operation up to 100 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **QueryToken** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Updates the access credential of a device.
        
        @description ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        >  Each successful call to the *RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
                self.execute(params, req, runtime)
            )

    async def refresh_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        @summary Updates the access credential of a device.
        
        @description ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        >  Each successful call to the *RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
                await self.execute_async(params, req, runtime)
            )

    def refresh_device_credential(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        """
        @summary Updates the access credential of a device.
        
        @description ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        >  Each successful call to the *RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Updates the access credential of a device.
        
        @description ## [](#)Limits
        You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        >  Each successful call to the *RefreshDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        """
        @summary RegisterCaCertificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: RegisterCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
                self.execute(params, req, runtime)
            )

    async def register_ca_certificate_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        """
        @summary RegisterCaCertificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: RegisterCaCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCaCertificateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterCaCertificateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def register_ca_certificate(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        """
        @summary RegisterCaCertificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: RegisterCaCertificateRequest
        @return: RegisterCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_ca_certificate_with_options(request, runtime)

    async def register_ca_certificate_async(
        self,
        request: ons_mqtt_20200420_models.RegisterCaCertificateRequest,
    ) -> ons_mqtt_20200420_models.RegisterCaCertificateResponse:
        """
        @summary RegisterCaCertificate
        
        @description    Only ApsaraMQ for MQTT Enterprise Platinum Edition instances support this operation.
        You can call this operation up to 500 times per second per Alibaba Cloud account. If you want to increase the limit, join the DingTalk group (ID: 35228338) to contact ApsaraMQ for MQTT technical support.
        
        @param request: RegisterCaCertificateRequest
        @return: RegisterCaCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_ca_certificate_with_options_async(request, runtime)

    def register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        @summary Registers an access credential for a device. In unique-certificate-per-device authentication mode, an application server applies a unique access credential for each device from the corresponding ApsaraMQ for MQTT broker. The access credential of a device consists of the client ID, AccessKey ID, and AccessKey secret of the device. When you connect a device to ApsaraMQ for MQTT, you must configure Username and Password based on the access credential of the device for authentication. You can activate the device and transfer data between the device and ApsaraMQ for MQTT only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
                self.execute(params, req, runtime)
            )

    async def register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        @summary Registers an access credential for a device. In unique-certificate-per-device authentication mode, an application server applies a unique access credential for each device from the corresponding ApsaraMQ for MQTT broker. The access credential of a device consists of the client ID, AccessKey ID, and AccessKey secret of the device. When you connect a device to ApsaraMQ for MQTT, you must configure Username and Password based on the access credential of the device for authentication. You can activate the device and transfer data between the device and ApsaraMQ for MQTT only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
                await self.execute_async(params, req, runtime)
            )

    def register_device_credential(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        """
        @summary Registers an access credential for a device. In unique-certificate-per-device authentication mode, an application server applies a unique access credential for each device from the corresponding ApsaraMQ for MQTT broker. The access credential of a device consists of the client ID, AccessKey ID, and AccessKey secret of the device. When you connect a device to ApsaraMQ for MQTT, you must configure Username and Password based on the access credential of the device for authentication. You can activate the device and transfer data between the device and ApsaraMQ for MQTT only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Registers an access credential for a device. In unique-certificate-per-device authentication mode, an application server applies a unique access credential for each device from the corresponding ApsaraMQ for MQTT broker. The access credential of a device consists of the client ID, AccessKey ID, and AccessKey secret of the device. When you connect a device to ApsaraMQ for MQTT, you must configure Username and Password based on the access credential of the device for authentication. You can activate the device and transfer data between the device and ApsaraMQ for MQTT only after the authentication is passed.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **RegisterDeviceCredential** operation increases the messaging transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Revokes a token.
        
        @description    You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RevokeTokenResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RevokeTokenResponse(),
                self.execute(params, req, runtime)
            )

    async def revoke_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        @summary Revokes a token.
        
        @description    You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RevokeTokenResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.RevokeTokenResponse(),
                await self.execute_async(params, req, runtime)
            )

    def revoke_token(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        """
        @summary Revokes a token.
        
        @description    You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Revokes a token.
        
        @description    You can call this operation up to 5 times per second per account. If you want to increase the limit, join the DingTalk group 35228338 to contact ApsaraMQ for MQTT technical support.
        Each successful call to the **RevokeToken** operation increases the messaging transactions per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Sends a single message from an application on a cloud server to ApsaraMQ for MQTT.
        
        @description    The **SendMessage** operation is called by an application on a cloud server. This operation is complementary to the operation that is called to send a message from an ApsaraMQ for MQTT client. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](https://help.aliyun.com/document_detail/179160.html).
        Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT broker to forward messages to ApsaraMQ for RocketMQ, use [an SDK to send the messages](https://help.aliyun.com/document_detail/174527.html). The **SendMessage** operation supports up to 1,000 queries per second (QPS). For more information, see [QPS limits](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **SendMessage** operation is calculated as a message transaction per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SendMessageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SendMessageResponse(),
                self.execute(params, req, runtime)
            )

    async def send_message_with_options_async(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        @summary Sends a single message from an application on a cloud server to ApsaraMQ for MQTT.
        
        @description    The **SendMessage** operation is called by an application on a cloud server. This operation is complementary to the operation that is called to send a message from an ApsaraMQ for MQTT client. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](https://help.aliyun.com/document_detail/179160.html).
        Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT broker to forward messages to ApsaraMQ for RocketMQ, use [an SDK to send the messages](https://help.aliyun.com/document_detail/174527.html). The **SendMessage** operation supports up to 1,000 queries per second (QPS). For more information, see [QPS limits](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **SendMessage** operation is calculated as a message transaction per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SendMessageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SendMessageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def send_message(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        """
        @summary Sends a single message from an application on a cloud server to ApsaraMQ for MQTT.
        
        @description    The **SendMessage** operation is called by an application on a cloud server. This operation is complementary to the operation that is called to send a message from an ApsaraMQ for MQTT client. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](https://help.aliyun.com/document_detail/179160.html).
        Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT broker to forward messages to ApsaraMQ for RocketMQ, use [an SDK to send the messages](https://help.aliyun.com/document_detail/174527.html). The **SendMessage** operation supports up to 1,000 queries per second (QPS). For more information, see [QPS limits](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **SendMessage** operation is calculated as a message transaction per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Sends a single message from an application on a cloud server to ApsaraMQ for MQTT.
        
        @description    The **SendMessage** operation is called by an application on a cloud server. This operation is complementary to the operation that is called to send a message from an ApsaraMQ for MQTT client. For information about the differences between the scenarios of sending messages from applications on cloud servers and the scenarios of sending messages from ApsaraMQ for MQTT clients, see [Developer guide](https://help.aliyun.com/document_detail/179160.html).
        Messages that are sent by calling the **SendMessage** operation cannot be forwarded to ApsaraMQ for RocketMQ. If you want to use an ApsaraMQ for MQTT broker to forward messages to ApsaraMQ for RocketMQ, use [an SDK to send the messages](https://help.aliyun.com/document_detail/174527.html). The **SendMessage** operation supports up to 1,000 queries per second (QPS). For more information, see [QPS limits](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **SendMessage** operation is calculated as a message transaction per second (TPS). This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: SendMessageRequest
        @return: SendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def set_sni_config_with_options(
        self,
        request: ons_mqtt_20200420_models.SetSniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SetSniConfigResponse:
        """
        @summary Configures a multi-domain certificate.
        
        @param request: SetSniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSniConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_certificate):
            query['DefaultCertificate'] = request.default_certificate
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sni_config):
            query['SniConfig'] = request.sni_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSniConfig',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SetSniConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SetSniConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def set_sni_config_with_options_async(
        self,
        request: ons_mqtt_20200420_models.SetSniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SetSniConfigResponse:
        """
        @summary Configures a multi-domain certificate.
        
        @param request: SetSniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSniConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_certificate):
            query['DefaultCertificate'] = request.default_certificate
        if not UtilClient.is_unset(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not UtilClient.is_unset(request.sni_config):
            query['SniConfig'] = request.sni_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSniConfig',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SetSniConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.SetSniConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_sni_config(
        self,
        request: ons_mqtt_20200420_models.SetSniConfigRequest,
    ) -> ons_mqtt_20200420_models.SetSniConfigResponse:
        """
        @summary Configures a multi-domain certificate.
        
        @param request: SetSniConfigRequest
        @return: SetSniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_sni_config_with_options(request, runtime)

    async def set_sni_config_async(
        self,
        request: ons_mqtt_20200420_models.SetSniConfigRequest,
    ) -> ons_mqtt_20200420_models.SetSniConfigResponse:
        """
        @summary Configures a multi-domain certificate.
        
        @param request: SetSniConfigRequest
        @return: SetSniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_sni_config_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ons_mqtt_20200420_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.TagResourcesResponse:
        """
        @summary 新增tag
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: ons_mqtt_20200420_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.TagResourcesResponse:
        """
        @summary 新增tag
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: ons_mqtt_20200420_models.TagResourcesRequest,
    ) -> ons_mqtt_20200420_models.TagResourcesResponse:
        """
        @summary 新增tag
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ons_mqtt_20200420_models.TagResourcesRequest,
    ) -> ons_mqtt_20200420_models.TagResourcesResponse:
        """
        @summary 新增tag
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        @summary Deregisters the access credential of a device. After the access credential of a device is deregistered, you can no longer use the access credential to authenticate the device on the ApsaraMQ for MQTT broker.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
                self.execute(params, req, runtime)
            )

    async def un_register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        @summary Deregisters the access credential of a device. After the access credential of a device is deregistered, you can no longer use the access credential to authenticate the device on the ApsaraMQ for MQTT broker.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
                await self.execute_async(params, req, runtime)
            )

    def un_register_device_credential(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        """
        @summary Deregisters the access credential of a device. After the access credential of a device is deregistered, you can no longer use the access credential to authenticate the device on the ApsaraMQ for MQTT broker.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
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
        @summary Deregisters the access credential of a device. After the access credential of a device is deregistered, you can no longer use the access credential to authenticate the device on the ApsaraMQ for MQTT broker.
        
        @description    You can call this operation up to 500 times per second per account. If the limit is exceeded, throttling is triggered. This may affect your business. We recommend that you take note of this limit when you call this operation. For more information, see [Limits on QPS](https://help.aliyun.com/document_detail/163047.html).
        Each successful call to the **UnRegisterDeviceCredential** operation increases the number of transactions per second (TPS) by one. This affects the billing of your instance. For more information, see [Billing rules](https://help.aliyun.com/document_detail/52819.html).
        
        @param request: UnRegisterDeviceCredentialRequest
        @return: UnRegisterDeviceCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_register_device_credential_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ons_mqtt_20200420_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UntagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UntagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: ons_mqtt_20200420_models.UntagResourcesRequest,
    ) -> ons_mqtt_20200420_models.UntagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ons_mqtt_20200420_models.UntagResourcesRequest,
    ) -> ons_mqtt_20200420_models.UntagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_auth_identity_with_options(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse:
        """
        @summary Updates the information about custom identity authentication.
        
        @param request: UpdateCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret):
            body['Secret'] = request.secret
        if not UtilClient.is_unset(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse(),
                self.execute(params, req, runtime)
            )

    async def update_custom_auth_identity_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse:
        """
        @summary Updates the information about custom identity authentication.
        
        @param request: UpdateCustomAuthIdentityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAuthIdentityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret):
            body['Secret'] = request.secret
        if not UtilClient.is_unset(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomAuthIdentity',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_custom_auth_identity(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse:
        """
        @summary Updates the information about custom identity authentication.
        
        @param request: UpdateCustomAuthIdentityRequest
        @return: UpdateCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_auth_identity_with_options(request, runtime)

    async def update_custom_auth_identity_async(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthIdentityRequest,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthIdentityResponse:
        """
        @summary Updates the information about custom identity authentication.
        
        @param request: UpdateCustomAuthIdentityRequest
        @return: UpdateCustomAuthIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_auth_identity_with_options_async(request, runtime)

    def update_custom_auth_permission_with_options(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse:
        """
        @summary Updates the permissions on a topic.
        
        @param request: UpdateCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effect):
            body['Effect'] = request.effect
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def update_custom_auth_permission_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse:
        """
        @summary Updates the permissions on a topic.
        
        @param request: UpdateCustomAuthPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAuthPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effect):
            body['Effect'] = request.effect
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomAuthPermission',
            version='2020-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_custom_auth_permission(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse:
        """
        @summary Updates the permissions on a topic.
        
        @param request: UpdateCustomAuthPermissionRequest
        @return: UpdateCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_auth_permission_with_options(request, runtime)

    async def update_custom_auth_permission_async(
        self,
        request: ons_mqtt_20200420_models.UpdateCustomAuthPermissionRequest,
    ) -> ons_mqtt_20200420_models.UpdateCustomAuthPermissionResponse:
        """
        @summary Updates the permissions on a topic.
        
        @param request: UpdateCustomAuthPermissionRequest
        @return: UpdateCustomAuthPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_auth_permission_with_options_async(request, runtime)
